from django.urls import path

from .import views as poll_views  # means take views from the same level

urlpatterns = [
    path('/', poll_views.home, name='pollapp'),
    path('/create/', poll_views.create, name='create'),
    path('/vote/<int:poll_id>', poll_views.vote, name='vote'),
    path('/results/<int:poll_id>', poll_views.results, name='results'),

]
