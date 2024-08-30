from django.core.management.base import BaseCommand
from core.models import Student, Class

class Command(BaseCommand):
    help = "Add a new student"

    def add_arguments(self, parser):
        parser.add_argument("first_name", type=str, help="First name of the student")
        parser.add_argument("last_name", type=str, help="Last name of the student")
        parser.add_argument("class_name", type=str, help="Class name in which is student")
    
    def handle(self, *args, **kwargs):
        first_name = kwargs["first_name"]
        last_name = kwargs["last_name"]
        class_name = kwargs["class_name"]

        try:
            student_class = Class.objects.get(name=class_name)
            students_class = Student.objects.create(first_name=first_name, last_name=last_name, student_class=student_class)
            students_class.save()
            self.stdout.write(self.style.SUCCESS(f"Student '{first_name} {last_name}' added successfully to the class {student_class}."))
        except:
            self.stdout.write(self.style.ERROR("Class does not exist."))