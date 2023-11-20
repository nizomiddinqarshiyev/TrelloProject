from django.urls import path, include
from rest_framework import routers

from main.views import BoardViewSet, CardViewSet, TaskViewSet

router = routers.DefaultRouter()
router.register('board', BoardViewSet, basename='board')
router.register('card', CardViewSet, basename='card')
router.register('task', TaskViewSet, basename='task')


urlpatterns = [
    path('', include(router.urls))
]
