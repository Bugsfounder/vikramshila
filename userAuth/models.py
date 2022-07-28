from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    phoneNumber = models.CharField(max_length=10)
    profilePic = models.ImageField(upload_to="user/profilePic", default="defaultUser.png")
    datetime = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.name
