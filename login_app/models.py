from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class User(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=20)
    career = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    number = models.IntegerField(default=0)
    password = models.CharField(max_length=20, null=False, blank=False)
    location = models.CharField(max_length=20)

    def __str__(self):
        return self.username