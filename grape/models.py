from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=30)
    role = models.CharField(max_length=10)
    password = models.CharField(max_length=30)
    is_active = models.BooleanField(default=False)
