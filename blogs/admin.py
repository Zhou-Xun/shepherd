from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Author)
admin.site.register(Life)
admin.site.register(Study)
admin.site.register(Comment)