from django.core.management.base import BaseCommand
from core.models import Schedule, Subject, Class, Teacher

class Command(BaseCommand):
    help = "Add a new schedule"

    def add_arguments(self, parser):
        parser.add_argument("day_of_week", type=str, help="Day of the week(ex. Mon, Wed...))")
        parser.add_argument("start_time", type=str, help="Start time (hours:minutes)")
        parser.add_argument("end_time", type=str, help="End time (hours:minutes)")
        parser.add_argument("subject_name", type=str, help="Subject")
        parser.add_argument("class_name", type=str, help="Class name")
        parser.add_argument("teacher_id", type=int, help="ID of the teacher")
    
    def handle(self, *args, **kwargs):
        day_of_week = kwargs["day_of_week"]
        start_time = kwargs["start_time"]
        end_time = kwargs["end_time"]
        subject_name = kwargs["subject_name"]
        class_name = kwargs["class_name"]
        teacher_id = kwargs["teacher_id"]

        try:
            subject = Subject.objects.get(name=subject_name)
            classs = Class.objects.get(name=class_name)
            teacher = Teacher.objects.get(id=teacher_id)
            schedule = Schedule.objects.create(day_of_week=day_of_week, start_time=start_time, end_time=end_time, subject=subject, student_class=classs, teacher=teacher)
            schedule.save()
            self.stdout.write(self.style.SUCCESS("Schedule entry added successfully."))
        except:
            self.stdout.write(self.style.ERROR("Error. Your input was incorrect or doesn't exist."))
