from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic import TemplateView

app_name = 'xunzhou_test'
urlpatterns=[
    path('cats', views.cats.as_view(), name='cats'),
    path('cat/<slug:guess>', views.cat.as_view(), name='cat'),
]

