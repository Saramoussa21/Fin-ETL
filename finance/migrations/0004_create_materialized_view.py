from django.db import migrations, connection

# Function to execute raw SQL for creating the materialized view
def create_materialized_view(apps, schema_editor):
    with connection.cursor() as cursor:
        cursor.execute("""
            CREATE MATERIALIZED VIEW client_summary_view AS
            SELECT 
                c.client_id,
                COUNT(t.transaction_id) AS total_transactions,
                SUM(CASE WHEN t.transaction_type = 'buy' THEN t.amount ELSE 0 END) AS total_amount_spent,
                SUM(CASE WHEN t.transaction_type = 'sell' THEN t.amount ELSE 0 END) AS total_amount_gained
            FROM 
                clients c
            LEFT JOIN 
                transactions t
            ON 
                c.client_id = t.client_id
            GROUP BY 
                c.client_id;
        """)

class Migration(migrations.Migration):
    dependencies = [
        ('finance', '0003_transaction_transaction_date_idx_alter_client_table_and_more'),
    ]

    operations = [
        migrations.RunPython(create_materialized_view),
    ]
