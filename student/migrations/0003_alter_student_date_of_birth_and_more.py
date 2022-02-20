# Generated by Django 4.0.2 on 2022-02-15 10:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_student_date_of_issue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_exam',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_issue',
            field=models.DateField(default=datetime.date.today),
        ),
    ]