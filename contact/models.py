from django.db import models
from django.utils import timezone


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50, unique=True, primary_key=True)
    email = models.EmailField(max_length=122)
    password = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    description = models.TextField()
    datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

