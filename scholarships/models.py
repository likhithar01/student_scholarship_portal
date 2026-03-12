from django.db import models
from django.contrib.auth.models import User


class Scholarship(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    amount = models.IntegerField()

    eligibility = models.CharField(max_length=200)

    deadline = models.DateField()

    def __str__(self):
        return self.title


class Application(models.Model):

    STATUS = [
        ('Pending','Pending'),
        ('Approved','Approved'),
        ('Rejected','Rejected')
    ]

    user = models.ForeignKey(User,on_delete=models.CASCADE)

    scholarship = models.ForeignKey(Scholarship,on_delete=models.CASCADE)

    document = models.FileField(upload_to='documents/')

    status = models.CharField(max_length=20,choices=STATUS,default='Pending')

    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username