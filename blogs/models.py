from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=30)

class Life(models.Model):
    ID = models.BigAutoField(primary_key=True, editable=False)
    lastEditTime = models.DateTimeField(auto_now_add=True)
    lifeName = models.CharField(max_length=20, verbose_name="lifeName")
    lifeText = models.TextField(verbose_name="lifeContext")
    picture = models.ImageField(verbose_name='picture', null=True, upload_to='img/')

class Study(models.Model):
    title = models.CharField(max_length=30)
    mark = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=30)

