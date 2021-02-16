from django.db import models

# Create your models here.
class learning_diary(models.Model):
    title = models.CharField(max_length=30)
    field  = models.CharField(max_length=30)
