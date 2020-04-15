from django.urls import path

from .import views  # means take views from the same level

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:project_id>', views.detail, name='detail'),

]
