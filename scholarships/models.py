from django.db import models
from django.contrib.auth.models import User


class Scholarship(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    eligibility = models.CharField(max_length=200)
    min_marks = models.IntegerField(default=0)
    max_income = models.IntegerField(default=1000000)
    deadline = models.DateField()

    def __str__(self):
        return self.title


class Application(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    marks = models.IntegerField()
    income = models.IntegerField()
    document = models.FileField(upload_to='documents/')

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    applied_on = models.DateTimeField(auto_now_add=True)