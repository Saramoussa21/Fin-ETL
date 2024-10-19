import pandas as pd
import random
import os

from faker import Faker


data_directory = '/home/azureuser/FinETL/data'
if not os.path.exists(data_directory):
    os.makedirs(data_directory)

fake = Faker()

clients = []
for client_id in range(1, 1001):
    clients.append({
        'client_id': client_id,
        'name': fake.name(),
        'email': fake.email(),
        'date_of_birth': fake.date_of_birth(minimum_age=18, maximum_age=80).strftime('%Y-%m-%d'),
        'country': fake.country(),
        'account_balance': round(random.uniform(1000, 50000), 2)
    })

clients_df = pd.DataFrame(clients)
clients_df.to_csv(f'{data_directory}/clients.csv', index=False)

transactions = []
for transaction_id in range(1, 5001):
    transactions.append({
        'transaction_id': transaction_id,
        'client_id': random.randint(1, 100),
        'transaction_type': random.choice(['buy', 'sell']),
        'transaction_date': fake.date_between(start_date='-2y', end_date='today').strftime('%Y-%m-%d'),
        'amount': round(random.uniform(50, 5000), 2) * (1 if random.choice(['buy', 'sell']) == 'buy' else -1),
        'currency': random.choice(['USD', 'EUR', 'CAD', 'GBP'])
    })

transactions_df = pd.DataFrame(transactions)
transactions_df.to_excel(f'{data_directory}/transactions.xlsx', index=False)
