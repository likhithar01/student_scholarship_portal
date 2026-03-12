from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    CATEGORY_CHOICES = [
        ('General','General'),
        ('OBC','OBC'),
        ('SC','SC'),
        ('ST','ST')
    ]

    COURSE_CHOICES = [
        ('Engineering','Engineering'),
        ('Medicine','Medicine'),
        ('Arts','Arts'),
        ('Science','Science')
    ]

    user = models.OneToOneField(User,on_delete=models.CASCADE)

    income = models.IntegerField(default=0)

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='General'
    )

    course = models.CharField(
        max_length=50,
        choices=COURSE_CHOICES,
        default='Engineering'
    )

    def __str__(self):
        return self.user.username