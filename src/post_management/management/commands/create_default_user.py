from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create default user if there is no user in the database."

    def handle(self, **options):
        if not User.objects.exists():
            user = User.objects.create_superuser(
                username="djangoadmin",
                email="user@example.com"
            )
            user.set_password("djangoadmin")
            user.save()

            self.stdout.write(self.style.SUCCESS("Successfully created a superuser"))
        else:
            self.stdout.write(self.style.SUCCESS("Superuser already exists"))
