# Generated by Django 5.1 on 2024-08-30 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_class_student_teacher_schedule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='student_class',
        ),
        migrations.RemoveField(
            model_name='student',
            name='student_class',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='subject',
        ),
        migrations.DeleteModel(
            name='Class',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]
