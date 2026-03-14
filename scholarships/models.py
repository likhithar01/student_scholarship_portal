from django.db import models
from django.contrib.auth.models import User

class Scholarship(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    eligibility = models.CharField(max_length=200)
    deadline = models.DateField()

    def __str__(self):
        return self.title


class Application(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE)
    applied_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.scholarship.title}"