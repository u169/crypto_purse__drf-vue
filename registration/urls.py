from django.urls import path
from oauth2_provider import views as oauth2_views

from . import views

urlpatterns = [
    path('reg/', views.UserRegister.as_view()),
]
