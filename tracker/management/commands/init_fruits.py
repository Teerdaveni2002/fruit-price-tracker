from django.core.management.base import BaseCommand
from tracker.models import Fruit


class Command(BaseCommand):
    help = 'Initialize the database with 5 fruits'

    def handle(self, *args, **options):
        fruits_data = [
            {'name': 'Apple', 'base_price': 100.00},
            {'name': 'Banana', 'base_price': 50.00},
            {'name': 'Orange', 'base_price': 80.00},
            {'name': 'Mango', 'base_price': 120.00},
            {'name': 'Grapes', 'base_price': 150.00},
        ]
        
        created_count = 0
        updated_count = 0
        
        for fruit_data in fruits_data:
            fruit, created = Fruit.objects.get_or_create(
                name=fruit_data['name'],
                defaults={
                    'base_price': fruit_data['base_price'],
                    'current_price': fruit_data['base_price'],
                    'search_count': 0
                }
            )
            
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f"Created fruit: {fruit.name} at ₹{fruit.base_price}")
                )
            else:
                updated_count += 1
                self.stdout.write(
                    self.style.WARNING(f"Fruit already exists: {fruit.name}")
                )
        
        self.stdout.write(
            self.style.SUCCESS(
                f"\nSummary: {created_count} fruits created, {updated_count} already existed"
            )
        )
