from django.contrib import admin
from .models import Client, Transaction

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'name', 'email', 'country', 'account_balance')
    search_fields = ('name', 'email', 'country')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'client', 'transaction_type', 'transaction_date', 'amount', 'currency')
    list_filter = ('transaction_type', 'currency')
