from django.core.management.base import BaseCommand
from core.models import Class

class Command(BaseCommand):
    help = "Add a new class"

    def add_arguments(self, parser):
        parser.add_argument("name", type=str, help="Name of the class")
        parser.add_argument("year", type=int, help="Year of the class")
    
    def handle(self, *args, **kwargs):
        name = kwargs["name"]
        year = kwargs["year"]

        if Class.objects.filter(name=name).exists():
            self.stdout.write(self.style.ERROR("Class already exists."))
        else:
            classs = Class.objects.create(name=name, year=year)
            classs.save()
            self.stdout.write(self.style.SUCCESS(f"Class '{name}' added successfully."))
