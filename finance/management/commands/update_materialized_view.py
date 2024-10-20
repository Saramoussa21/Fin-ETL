from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Update materialized view for client transactions summary'

    def handle(self, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute("REFRESH MATERIALIZED VIEW client_summary_view;")
        self.stdout.write(self.style.SUCCESS('Materialized view updated successfully'))
