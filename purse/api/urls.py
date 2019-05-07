from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'coins', views.CoinViewSet, basename='coins')


urlpatterns = [
    path('login/', views.index, name='index'),
    path('purses/', views.PurseList.as_view()),
    path('', include(router.urls)),
]
