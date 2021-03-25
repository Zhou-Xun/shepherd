from django.db import models
from xunzhou.models import user

class Blog(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=30)
    user = models.ForeignKey('xunzhou.user', on_delete=models.SET_NULL, null=True)

class Life(models.Model):
    ID = models.BigAutoField(primary_key=True, editable=False)
    lastEditTime = models.DateTimeField(auto_now_add=True)
    lifeName = models.CharField(max_length=20, verbose_name="lifeName")
    lifeText = models.TextField(verbose_name="lifeContext")
    picture = models.FileField(verbose_name='picture', null=True, upload_to='img/', blank=True)

    def __str__(self):
        return self.lifeName

class Study(models.Model):
    title = models.CharField(max_length=30)
    mark = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    note = models.FileField(null=True, upload_to='notes/%Y/%m/%d/', blank=True)
    picture = models.ImageField(verbose_name='picture', null=True, upload_to='img/', blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

