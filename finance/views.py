from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Transaction, Client
from .serializers import TransactionSerializer
from django.utils.dateparse import parse_date
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.permissions import IsAuthenticated
from django_ratelimit.decorators import ratelimit
from django.utils.decorators import method_decorator

class ClientTransactionsView(APIView):
    permission_classes = [IsAuthenticated]
    
    @method_decorator(ratelimit(key='user', rate='5/m', method='GET', block=True))
    def get(self, request, client_id):
        try:
            client = Client.objects.get(client_id=client_id)
        except Client.DoesNotExist:
            raise NotFound({"error": "Client not found."})

        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        if start_date:
            start_date = parse_date(start_date)
            if not start_date:
                raise ValidationError({"error": "Invalid start date format. Use YYYY-MM-DD."})

        if end_date:
            end_date = parse_date(end_date)
            if not end_date:
                raise ValidationError({"error": "Invalid end date format. Use YYYY-MM-DD."})

        # Corrected the filter
        transactions = Transaction.objects.filter(client__client_id=client_id)

        if start_date:
            transactions = transactions.filter(transaction_date__gte=start_date)
        if end_date:
            transactions = transactions.filter(transaction_date__lte=end_date)

        if not transactions.exists():
            raise NotFound({"error": "No transactions found for this client in the specified date range."})

        serializer = TransactionSerializer(transactions, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
