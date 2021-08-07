from django.core.management.base import BaseCommand

from ...utils import create_super_user


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
        if options["createsuperuser"]:
            message = create_super_user(
                "admin", "admin@admin.com", "7894561235", "cartdropadmin"
            )
            self.stdout.write(self.style.SUCCESS(message))
