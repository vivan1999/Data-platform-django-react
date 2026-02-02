from django.core.management import BaseCommand,CommandError
from apps.readings.models import Device, NetworkReading
import json
from django.db import transaction
from datetime import datetime
from django.utils.dateparse import parse_datetime

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
        except FileNotFoundError:
            raise CommandError("File not found.")
        readings = data.get("readings",[])
        if not readings:
            self.style.ERROR(self.stdout.write("No readings found"))
            return
        created_devices = 0
        created_readings = 0
        with transaction.atomic():
            for item in readings:
                device_id = item["device_id"]
                device, device_created = Device.objects.get_or_create(device_id = device_id,defaults={
                    "type": item.get("device_type","smart_meter"),
                    "location": item.get("location",None)
                })
                if device_created:
                    created_devices +=1
                    self.style.SUCCESS(self.stdout.write(f"created device : {device}"))
                else:
                    self.style.SUCCESS(self.stdout.write(f"Already present device : {device.name}"))
                datetime_reading = parse_datetime(item.get("timestamp",datetime.now()))
                try:
                    NetworkReading.objects.create(device= device, timestamp = datetime_reading, metric_name = item["metric_name"], metric_value = item["metric_value"],raw_payload = item.get("raw_payload",{}))
                    created_readings+=1
                except ValueError:
                    self.style.ERROR(self.stdout.write(f"Value Error in adding a reading: {item}"))
            self.style.SUCCESS(self.stdout.write(f"Total devices created : {created_devices}, Total readings added : {created_readings}"))

        
                        