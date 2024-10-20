from django.contrib import admin
from .models import Client, Transaction
from django.core.management import call_command
from django.contrib import messages

# Admin for Client Model
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'name', 'email', 'country', 'account_balance')
    search_fields = ('name', 'email')
    list_filter = ('country',)
    actions = ['run_etl_process']

    def run_etl_process(self, request, queryset):
        try:
            call_command('etl')  # Assuming you have an ETL management command named `etl`
            self.message_user(request, "ETL process has been executed successfully.", level=messages.SUCCESS)
        except Exception as e:
            self.message_user(request, f"ETL process failed: {str(e)}", level=messages.ERROR)

    run_etl_process.short_description = 'Run ETL Process'

# Admin for Transaction Model
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'client', 'transaction_type', 'transaction_date', 'amount', 'currency')
    search_fields = ('client__name', 'currency')
    list_filter = ('transaction_type', 'currency')
    actions = ['refresh_materialized_view']

    def refresh_materialized_view(self, request, queryset):
        try:
            call_command('update_materialized_view')  # This will run the command you created
            self.message_user(request, "Materialized view has been updated successfully.", level=messages.SUCCESS)
        except Exception as e:
            self.message_user(request, f"Materialized view update failed: {str(e)}", level=messages.ERROR)

    refresh_materialized_view.short_description = 'Update Materialized View'
