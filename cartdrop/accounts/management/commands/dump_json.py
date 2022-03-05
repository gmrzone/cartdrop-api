import os
from importlib.resources import path

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.utils import timezone


class Command(BaseCommand):
    def add_arguments(self, parser) -> None:
        parser.add_argument("app_names", nargs="+", type=str)
        parser.add_argument("-p", "--path", type=str, help="Specify path to json file")

    def handle(self, *args, **options):
        full_path = options["path"]
        if options["path"]:
            path, filename = full_path.rsplit("/", 1)
            for app_name in options["app_names"]:
                if filename[-5:] == ".json":
                    date_now = timezone.now().strftime("%d-%m-%Y")
                    updated_filename = (
                        f"{app_name}_{filename[:-5]}_{date_now}{filename[-5:]}"
                    )
                else:
                    updated_filename = f"{app_name}_{filename}_{date_now}.json"
                output_path = os.path.join(settings.BASE_DIR, path, updated_filename)
                call_command(
                    "dumpdata",
                    app_name,
                    "--natural-foreign",
                    "--natural-primary",
                    exclude=["contenttypes", "auth.Permission"],
                    indent=4,
                    format="json",
                    output=output_path,
                )
        else:
            self.stdout.write(
                self.style.WARNING(
                    "Please specify the path and filename for the output json file using --path or -p"
                )
            )
