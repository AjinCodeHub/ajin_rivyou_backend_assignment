import csv
from pathlib import Path

from django.core.management.base import BaseCommand
from products.models import Product


class Command(BaseCommand):
    help = "Import products from CSV"

    def handle(self, *args, **kwargs):

        csv_file = Path("products_data.csv")

        if not csv_file.exists():
            self.stdout.write(
                self.style.ERROR("products_data.csv not found!")
            )
            return

        imported = 0

        with open(csv_file, "r", encoding="utf-8") as file:

            reader = csv.DictReader(file)

            for row in reader:

                tags = []

                if row["tags"]:
                    tags = [
                        tag.strip()
                        for tag in row["tags"].split(",")
                    ]

                Product.objects.create(
                    product_name=row["product_name"],
                    product_description=row["product_description"],
                    category=row["category"],
                    tags=tags,
                )

                imported += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"{imported} products imported successfully!"
            )
        )