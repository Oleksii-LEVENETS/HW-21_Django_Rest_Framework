from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.template.defaultfilters import pluralize

from faker import Faker


class Command(BaseCommand):
    help = "Creating fake Users"  # noqa: A003

    def add_arguments(self, parser):
        parser.add_argument(
            "count_of_users",
            type=int,
            choices=range(1, 6),
            help="Enter an integer from 1 to 5 incl. -- the count of fake users.",
        )

    def handle(self, *args, **options):
        fake = Faker()
        list_users = []
        for _ in range(options["count_of_users"]):
            name = fake.name()
            first_name = name.split(" ")[0]
            last_name = name.split(" ")[-1]
            username = first_name.lower() + last_name.lower()
            email = username + "@" + last_name.lower() + ".com"
            password = "QWE!@#qwe123"
            list_users.append(
                User(
                    username=username,
                    password=make_password(password),
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                )
            )

        # User.objects.bulk_create(list_users)
        for user in list_users:
            User.objects.create_user(
                username=user.username,
                password=user.password,
                email=user.email,
                first_name=user.first_name,
                last_name=user.last_name,
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully created {options['count_of_users']} user{pluralize(options['count_of_users'])}!"
            )
        )
