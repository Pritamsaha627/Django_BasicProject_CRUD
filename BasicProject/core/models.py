from django.db import models

# Create your models here.
class Record(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    message = models.CharField(max_length=50)

