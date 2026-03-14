from django.db import models

class Scholarship(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.IntegerField()
    deadline = models.DateField()

    def __str__(self):
        return self.title