from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('create-account/', views.create_account, name="create_account"),
    path('login/', views.login, name="login"),
    path("profiles/", views.profiles, name="profiles"),
    path("profile/<int:pk>", views.profile, name="profile"),
    path("about/", views.about, name="about"),
]