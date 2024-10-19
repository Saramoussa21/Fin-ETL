from django.core.management.base import BaseCommand
from finance.models import Client, Transaction
import pandas as pd
import os

class Command(BaseCommand):
    help = 'Extract, Transform, and Load data from CSV and XLSX files'

    def handle(self, *args, **kwargs):
        data_directory = './data'

        # Extract 
        clients_file = os.path.join(data_directory, 'clients.csv')
        transactions_file = os.path.join(data_directory, 'transactions.xlsx')

        if not os.path.exists(clients_file) or not os.path.exists(transactions_file):
            self.stdout.write(self.style.ERROR('Data files not found in data directory'))
            return

        # Load Clients Data
        clients_df = pd.read_csv(clients_file)

        # --- Transform  ---

        # Remove duplicate emails
        clients_df.drop_duplicates(subset=['email'], inplace=True)

        # Replace domain of email from 'example.com' to 'gmail.com'
        clients_df['email'] = clients_df['email'].str.replace('example.com', 'gmail.com')

        # Standardize account balance (ensure it is always a float)
        clients_df['account_balance'] = clients_df['account_balance'].astype(float)

        # --- Load Clients Data to Postgres Database ---
        for _, row in clients_df.iterrows():
            Client.objects.update_or_create(
                client_id=row['client_id'],
                defaults={
                    'name': row['name'],
                    'email': row['email'],
                    'date_of_birth': row['date_of_birth'],
                    'country': row['country'],
                    'account_balance': row['account_balance']
                }
            )

        # Load Transactions Data
        transactions_df = pd.read_excel(transactions_file)

        # --- Transform Transactions Data ---

        # Remove transactions with amount = 0
        transactions_df = transactions_df[transactions_df['amount'] != 0]

        # Ensure transaction_date is in correct format (e.g., YYYY-MM-DD)
        transactions_df['transaction_date'] = pd.to_datetime(transactions_df['transaction_date']).dt.strftime('%Y-%m-%d')

        # --- Load Transactions Data to Database ---
        for _, row in transactions_df.iterrows():
            Transaction.objects.update_or_create(
                transaction_id=row['transaction_id'],
                defaults={
                    'client_id': row['client_id'],
                    'transaction_type': row['transaction_type'],
                    'transaction_date': row['transaction_date'],
                    'amount': row['amount'],
                    'currency': row['currency']
                }
            )

        self.stdout.write(self.style.SUCCESS('ETL process completed successfully'))
