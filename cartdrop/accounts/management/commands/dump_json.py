from importlib.resources import path
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings
import os

class Command(BaseCommand):
    def add_arguments(self, parser) -> None:
        parser.add_argument("app_names", nargs="+", type=str)


    def handle(self, *args, **options):
        for i in options["app_names"]:
            call_command("dumpdata", i, "--natural-foreign", "--natural-primary", exclude=["contenttypes", "auth.Permission"], indent=4, format='json', output=os.path.join(settings.BASE_DIR, "/afzal_test_new.json"))