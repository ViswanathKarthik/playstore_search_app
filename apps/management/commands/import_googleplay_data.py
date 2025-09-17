import csv
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from apps.models import App, Review


class Command(BaseCommand):
    help = "Import apps and reviews from Google Play CSV files"

    def add_arguments(self, parser):
        parser.add_argument("--apps", type=str, help="Path to googleplaystore.csv")
        parser.add_argument("--reviews", type=str, help="Path to googleplaystore_user_reviews.csv")

    def handle(self, *args, **options):
        apps_path = options["apps"]
        reviews_path = options["reviews"]

        if apps_path:
            self.stdout.write(self.style.NOTICE("Importing apps..."))
            with open(apps_path, encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    App.objects.get_or_create(
                        name=row.get("App", "").strip(),
                        defaults={
                            "category": row.get("Category"),
                            "rating": float(row.get("Rating") or 0),
                            "installs": row.get("Installs"),
                            "size": row.get("Size"),
                            "price": row.get("Price"),
                        },
                    )
            self.stdout.write(self.style.SUCCESS("Apps import complete."))

        if reviews_path:
            self.stdout.write(self.style.NOTICE("Importing reviews..."))

            # ensure a demo user exists for review ownership
            user, _ = User.objects.get_or_create(username="demo_user")

            with open(reviews_path, encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    app_name = row.get("App", "").strip()
                    content = row.get("Translated_Review") or ""
                    if not app_name or not content:
                        continue

                    try:
                        app = App.objects.get(name=app_name)
                    except App.DoesNotExist:
                        continue

                    Review.objects.create(
                        app=app,
                        user=user,
                        content=content,
                        approved=True,  # original CSV reviews auto-approved
                    )

            self.stdout.write(self.style.SUCCESS("Reviews import complete."))
