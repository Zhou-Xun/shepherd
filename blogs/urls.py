from django.urls import path
from . import  views
from django.views.generic import TemplateView
app_name = 'blogs'

urlpatterns = [
    path('', views.BlogListView.as_view(), name='all_blogs'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blog'),
    path('lives', views.LifeListView.as_view(), name='lives'),
    path('life/<int:pk>', views.LifeDetailView.as_view(), name='life'),
    path('studies', views.StudyListView.as_view(), name='studis'),
    path('study/<int:pk>', views.StudyDetailView.as_view(), name='study'),
]
