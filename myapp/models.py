from django.db import models

class Student(models.Model):
    firstname = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    student_id = models.IntegerField(unique=True)
    course = models.CharField(max_length=20)

    def __str__(self):
        return f'Student ID: {self.student_id} - {self.firstname} {self.surname} - Course: {self.course}'