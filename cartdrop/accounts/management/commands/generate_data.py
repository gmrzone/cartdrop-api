from django.core.management.base import BaseCommand
from django.core.management import call_command
from ...utils import create_super_user, create_normal_user


class Command(BaseCommand):
    def add_arguments(self, parser) -> None:
        parser.add_argument(
            "--createadmin",
            action="store_true",
            dest="createsuperuser",
            default=False,
            help="Create admin account",
        )

    def handle(self, *args, **options):
        # makemigration and migrate
        call_command("makemigrations")
        call_command("migrate")
        # If --createadmin arguement is passed then create a super user else
        # Create a normal user so that we do not get error when loading data
        # which contain foreign key for user
        if options["createsuperuser"]:
            message = create_super_user(
                "admin", "admin@admin.com", "7894561235", "cartdropadmin"
            )
        else:
            message = create_normal_user(
                "cartdrop_user", "user@cartdrop.com", "8956412365", "password123"
            )
        self.stdout.write(self.style.SUCCESS(message))

        # Load data for core and product app
        call_command("loaddata", "json_data/core_latest.json")
        self.stdout.write(self.style.SUCCESS("Sucessfully loaded data for core app"))
        call_command("loaddata", "json_data/product_latest.json")
        self.stdout.write(self.style.SUCCESS("Sucessfully loaded data for Product app"))
