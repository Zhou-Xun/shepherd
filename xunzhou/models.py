from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    age  = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name

class user(models.Model):
    UserName=models.CharField('UserName',primary_key=True,max_length=20)
    UserPasswd=models.CharField('UserPasswd',max_length=20)
    photo = models.ImageField(verbose_name='picture', null=True, upload_to='img/', blank=True)

    def __str__(self):
        return self.UserName
