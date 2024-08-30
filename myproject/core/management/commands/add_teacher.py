from django.core.management.base import BaseCommand
from core.models import Teacher, Subject

class Command(BaseCommand):
    help = "Add a new teacher"

    def add_arguments(self, parser):
        parser.add_argument("first_name", type=str, help="First name of the teacher")
        parser.add_argument("last_name", type=str, help="Last name of the teacher")
        parser.add_argument("name", type=str, help="Name of the subject the teacher teaches")
    
    def handle(self, *args, **kwargs):
        first_name = kwargs["first_name"]
        last_name = kwargs["last_name"]
        name = kwargs["name"]

        try:
            subject = Subject.objects.get(name=name)
            teacher = Teacher.objects.create(first_name=first_name, last_name=last_name, subject=subject)
            teacher.save()
            self.stdout.write(self.style.SUCCESS(f"Teacher '{first_name} {last_name}' added successfully."))
        except:
            self.stdout.write(self.style.ERROR("Subject does not exist."))
