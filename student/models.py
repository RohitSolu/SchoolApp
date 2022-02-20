from django.db import models
import datetime

CLS_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("10", "10"),
    ("11", "11"),
    ("12", "12"),
)
GRADE_CHOICES = (
    ("1", "A+"),
    ("2", "A"),
    ("3", "B+"),
    ("4", "B"),
    ("5", "C+"),
    ("6", "C"),
    ("7", "D+"),
    ("8", "D"),
    
)
CHAR_CHOICES = (
    ("1", "Outstanding"),
    ("2", "Very Good"),
    ("3", "Good"),
    ("4", "Average"),
       
)

class Student(models.Model):
    name = models.CharField(max_length=255)
    fathers_name = models.CharField(max_length=255)
    mothers_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    cls = models.CharField(max_length=10, choices = CLS_CHOICES, default=10)
    grade = models.CharField(max_length=10, choices=GRADE_CHOICES, default='A+')
    date_of_birth = models.DateField(default=datetime.date.today)
    date_of_exam = models.DateField(default=datetime.date.today)
    date_of_issue = models.DateField(default=datetime.date.today)
    character_of_student = models.CharField(max_length=50, choices=CHAR_CHOICES, default='good')
    issuer = models.CharField(max_length=255)

    class Meta:
      verbose_name_plural = "students"


    def __str__(self):
        return self.name

    
class Subject(models.Model):
    name = models.CharField(max_length=255, default=' ')
    cls = models.CharField(max_length=10, choices = CLS_CHOICES, default=10)
    subject_code = models.CharField(max_length=10)
    subjects = models.CharField(max_length=255)
    credit_hour = models.FloatField(max_length=10)
    grade_point = models.FloatField(max_length=10)
    grade = models.CharField(max_length=10, choices=GRADE_CHOICES, default='A+')
    final_grade = models.CharField(max_length=10, choices=GRADE_CHOICES, default='A+')
    remarks = models.CharField(max_length=40)
    total_gpa = models.CharField(max_length=10, default="3.5")
    

    def __str__(self):
        return self.subjects