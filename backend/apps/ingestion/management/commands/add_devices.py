from django.core.management import BaseCommand,CommandError
from apps.readings.models import Device
import json

class Command(BaseCommand):
    help = "Adding devices to database"

    def add_arguments(self, parser):
        parser.add_argument(
            "--file",
            type=str,
            required=True,
            help="add the path of raw data"
        )
    
    def handle(self, *args, **options):
        file_path = options["file"]

        try:
            with open(file_path,"r") as f:
                data = json.load(f)
                self.style.SUCCESS(self.stdout.write(file_path))
        except FileNotFoundError:
            raise CommandError("File not found.")