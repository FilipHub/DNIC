from re import template
from unicodedata import name
from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.osPage, name=''),
    path('login', views.loginPage, name='login'),
    path('register', views.registerPage, name='register'),
    path('courses', views.coursesPage, name='courses'),
    path('forum', views.forumPage, name='forum'),
    path('quizz', views.quizzPage, name='quizz'),
    path('os', views.osPage, name='os'),
    path('logout', auth_views.LogoutView.as_view(
        template_name='logout.html'), name='logout'),
]
