# Generated by Django 5.1.2 on 2025-01-10 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_trainer_alter_attendance_student_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
