from django.db import models
from django.contrib.auth.models import User


class Scholarship(models.Model):
    CATEGORY_CHOICES = [
        ('Engineering', 'Engineering'),
        ('Medical', 'Medical'),
        ('Arts', 'Arts'),
        ('Internship', 'Internship'),
        ('Government', 'Government'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    eligibility = models.CharField(max_length=200, default="General")
    amount = models.IntegerField(default=0)
    deadline = models.DateField()

    # ✅ NEW FIELD
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Engineering')

    def __str__(self):
        return self.title


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE)
    marks = models.IntegerField()
    income = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.scholarship.title}"