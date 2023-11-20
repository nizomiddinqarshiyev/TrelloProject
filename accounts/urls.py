from django.urls import path

from accounts.views import RegisterAPIView, UserInfoAPIView

urlpatterns = [
    path('register', RegisterAPIView.as_view(), name='register'),
    path('user-info', UserInfoAPIView.as_view(), name='user_info')
]
