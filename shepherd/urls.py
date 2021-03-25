"""shepherd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', TemplateView.as_view(template_name='main/main.html')),
    path('note/', include('note.urls')),
    path('xunzhou/', include('xunzhou.urls', namespace='xunzhou')),
    path('blogs/', include('blogs.urls', namespace='blogs')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#
# path('hello/', views.hello),
# path('funky', views.funky),
# path('danger', views.danger),
# path('rest/<int:guess>', views.rest),
# path('remain/<slug:guess>', views.RestMainView.as_view()),
# path('bounce', views.bounce),
# path('game/<slug:guess>', views.GameView.as_view()),
# path('simple', views.simple),
# path('loop', views.loop),