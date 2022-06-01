
"""Pjugadores URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from app_jugadores import views

urlpatterns = [

    path('', views.index, name='Home'),
    path('jugadores', views.jugadores, name='Jugadores'),
    # path('courses', views.courses, name='jugadores-list'),
    path('clubes', views.club, name='Club'),
    path('liga', views.liga, name='Liga'),
    path('formHTML', views.form_hmtl),
    # path('jugadores-django-forms', views.course_forms_django, name='CourseDjangoForms'),
    # path('profesor-django-forms', views.profesor_forms_django, name='ProfesorDjangoForms'),
    # path('profesor/<int:pk>/update', views.update_profesor, name='UpdateProfesor'),
    # path('profesor/<int:pk>/delete', views.delete_profesor, name='DeleteProfesor'),
    # path('homework-django-forms', views.homework_forms_django, name='HomeworkDjangoForms'),
    # path('search', views.search, name='Search'),


    # Dajngo documentation -->  https://docs.djangoproject.com/en/4.0/topics/class-based-views/generic-editing/
    # Confirmo la url de la documentación es correcta, deben hacer scroll hasta esta parte:
    #
    # from django.urls import path
    # from myapp.views import AuthorCreateView, AuthorDeleteView, AuthorUpdateView

    # urlpatterns = [
    #     # ...
    #     path('author/add/', AuthorCreateView.as_view(), name='author-add'),
    #     path('author/<int:pk>/', AuthorUpdateView.as_view(), name='author-update'),
    #     path('author/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author-delete'),
    # ]
    #
    # Acá se ve la forma clara cómo Django realiza de forma stándar los nombres para urls, views y name del path.

    path('jugadores', views.JugadoresListView.as_view(), name='jugadores-list'),
    path('jugadores/add/', views.JugadoresCreateView.as_view(), name='jugadores-add'),
    path('jugadores/<int:pk>/detail', views.JugadoresDetailView.as_view(), name='jugadores-detail'),
    path('jugadores/<int:pk>/update', views.JugadoresUpdateView.as_view(), name='jugadores-update'),
    path('jugadores/<int:pk>/delete', views.JugadoresDeleteView.as_view(), name='jugadores-delete'),

    path('clubes', views.ClubListView.as_view(), name='clubes-list'),
    path('clubes/add/', views.ClubCreateView.as_view(), name='clubes-add'),
    path('clubes/<int:pk>/detail', views.ClubDetailView.as_view(), name='clubes-detail'),
    path('clubes/<int:pk>/update', views.ClubUpdateView.as_view(), name='clubes-update'),
    path('clubes/<int:pk>/delete', views.ClubDeleteView.as_view(), name='clubes-delete'),

    path('liga', views.LigaListView.as_view(), name='ligas-list'),
    path('ligas/add/', views.LigaCreateView.as_view(), name='ligas-add'),
    path('ligas/<int:pk>/detail', views.LigaDetailView.as_view(), name='ligas-detail'),
    path('ligas/<int:pk>/update', views.LigaUpdateView.as_view(), name='ligas-update'),
    path('ligas/<int:pk>/delete', views.LigaDeleteView.as_view(), name='ligas-delete'),
    ]