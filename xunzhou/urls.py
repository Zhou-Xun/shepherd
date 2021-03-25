from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic import TemplateView

app_name = 'xunzhou'
urlpatterns=[
    path('', TemplateView.as_view(template_name='xunzhou/loginV2.html')),
    path('open', views.OpenView.as_view(), name='open'),
    path('apereo', views.ApereoView.as_view(), name='apereo'),
    path('manual', views.ManualProtect.as_view(), name='manual'),
    path('protect', views.ProtectView.as_view(), name='protect'),
    path('loginV2', views.loginV2.as_view(), name='loginV2'),
    path('cats', views.cats.as_view(), name='cats'),
    path('cat/<slug:guess>', views.cat.as_view(), name='cat'),
    path('login', views.login.as_view(), name='login'),

]

