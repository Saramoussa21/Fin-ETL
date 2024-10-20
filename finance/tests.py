from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from finance.models import Client, Transaction
from django.contrib.auth.models import User

class TransactionAPITestCase(TestCase):
    def setUp(self):
        # Set up initial data for the test
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

        # Create a test client and transactions
        self.test_client = Client.objects.create(
            client_id=1,
            name='John Doe',
            email='john.doe@example.com',
            date_of_birth='1990-01-01',
            country='USA',
            account_balance=5000.0
        )

        Transaction.objects.create(
            transaction_id=1,
            client=self.test_client,
            transaction_type='buy',
            transaction_date='2023-01-01',
            amount=1000.0,
            currency='USD'
        )

    def test_get_transactions(self):
        # Test getting transactions for a specific client
        response = self.client.get('/api/transactions/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_transactions_invalid_client(self):
        # Test getting transactions for a non-existing client
        response = self.client.get('/api/transactions/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_transactions_with_date_range(self):
        # Test getting transactions with a date range
        response = self.client.get('/api/transactions/1/?start_date=2023-01-01&end_date=2023-12-31')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

