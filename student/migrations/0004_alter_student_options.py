# Generated by Django 4.0.2 on 2022-02-15 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_alter_student_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name_plural': 'students'},
        ),
    ]