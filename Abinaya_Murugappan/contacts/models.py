from django.db import models
import datetime

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    created_time = models.DateTimeField("time published")
    notes = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name
