from django.db import models
from django.contrib.auth.models import User


class Subject(models.Model):
    subject_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.subject_name
    

class SubjectTeacher(models.Model):
    subject = models.OneToOneField(Subject, on_delete=models.CASCADE, related_name='subject')
    teacher = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher')

    def __str__(self):
        return f'{self.subject.subject_name} - {self.teacher.first_name} {self.teacher.last_name}'


class Homework(models.Model):
    STATUS_CHOICES = (
    ('New', 'New'),
    ('Pending', 'Pending'),
    ('Reviewed', 'Reviewed')
    )
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='homework_subject')
    file = models.FileField()
    submission_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICES, default='New', max_length=10)
    viewed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.student.first_name} {self.student.last_name} - {self.subject.subject_name}'
    

class HomeworkReview(models.Model):
    homework = models.OneToOneField(Homework, on_delete=models.CASCADE)
    review = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.homework.student.id}{self.homework.student.first_name}'