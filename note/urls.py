from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic import TemplateView

app_name = 'note'
urlpatterns=[
    path('game/<slug:guess>', views.GameView.as_view()),
    path('reverse', TemplateView.as_view(template_name='note/reverse.html')),
    path('first', views.FirstView.as_view(), name='first-view'),
    path('second', views.SecondView.as_view(), name='second-view'),
    path('detail', views.detail, name='detail'),
]

