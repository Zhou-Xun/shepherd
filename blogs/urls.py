from django.urls import path
from . import  views
from django.views.generic import TemplateView
app_name = 'blogs'

urlpatterns = [
    path('', views.BlogListView.as_view(), name='all_blogs'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blog'),
    path('lives', views.LifeListView.as_view(), name='lives'),
    path('life/<int:pk>', views.LifeDetailView.as_view(), name='life'),
    path('lives/create/', views.LifeCreate.as_view(), name='lives_create'),
    path('lives/<int:pk>/update/', views.LifeUpdate.as_view(), name='lives_update'),
    path('lives/<int:pk>/delete/', views.LifeDelete.as_view(), name='lives_delete'),
    path('studies', views.StudyListView.as_view(), name='studies'),
    path('study/<int:pk>', views.StudyDetailView.as_view(), name='study'),
    path('studies/create/', views.LifeCreate.as_view(), name='studies_create'),
    path('studies/<int:pk>/update/', views.LifeUpdate.as_view(), name='studies_update'),
    path('studies/<int:pk>/delete/', views.LifeDelete.as_view(), name='studies_delete'),
]
