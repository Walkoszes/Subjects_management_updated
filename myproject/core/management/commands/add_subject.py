from django.core.management.base import BaseCommand
from core.models import Subject

class Command(BaseCommand):
    help = "Add a new subject"

    def add_arguments(self, parser):
        parser.add_argument("name", type=str, help="Name of the new subject")
        parser.add_argument("description", type=str, help="Description of the subject")
    
    def handle(self, *args, **kwargs):
        name = kwargs["name"]
        description = kwargs["description"]

        if Subject.objects.filter(name=name).exists():
            self.stdout.write(self.style.ERROR("Subject already exists."))
        else:
            subject = Subject.objects.create(name=name, description=description)
            subject.save()
            self.stdout.write(self.style.SUCCESS(f"Subject '{name}' added successfully."))