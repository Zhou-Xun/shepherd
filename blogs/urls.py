from django.urls import path
from . import  views
from django.views.generic import TemplateView
app_name = 'blogs'

urlpatterns = [
    path('', views.BlogListView.as_view(), name='all'),
    path('types/<int:pk>', views.TypeListView.as_view(), name='types'),
    # path('lives', views.LifeListView.as_view(), name='lives'),
    # path('life/<int:pk>', views.LifeDetailView.as_view(), name='life'),
    # path('lives/create/', views.LifeCreate.as_view(), name='lives_create'),
    # path('lives/<int:pk>/update/', views.LifeUpdate.as_view(), name='lives_update'),
    # path('lives/<int:pk>/delete/', views.LifeDelete.as_view(), name='lives_delete'),
    # path('study/<int:pk>', views.StudyDetailView.as_view(), name='study'),
    # path('studies/create/', views.StudyCreate.as_view(), name='studies_create'),
    # path('studies/<int:pk>/update/', views.StudyUpdate.as_view(), name='studies_update'),
    # path('studies/<int:pk>/delete/', views.StudyDelete.as_view(), name='studies_delete'),
]
