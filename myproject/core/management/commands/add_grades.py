from django.core.management.base import BaseCommand
from core.models import Grade, Student, Subject

class Command(BaseCommand):
    help = "Add a new grade for a student"

    def add_arguments(self, parser):
        parser.add_argument("student_id", type=int, help="ID of the student")
        parser.add_argument("subject_name", type=str, help="Subject")
        parser.add_argument("grade", type=int, help="Grade")

    def handle(self, *args, **kwargs):
        student_id = kwargs["student_id"]
        subject_name = kwargs["subject_name"]
        grady = kwargs["grade"]

        try:
            student = Student.objects.get(id=student_id)
            subject = Subject.objects.get(name=subject_name)
            grade = Grade.objects.create(student=student, subject=subject, grade=grady)
            grade.save()
            self.stdout.write(self.style.SUCCESS(f"Grade added successfully for student {student}."))
        except:
            self.stdout.write(self.style.ERROR(f"Error. Something went wrong."))