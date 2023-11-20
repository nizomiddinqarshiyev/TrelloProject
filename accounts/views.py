from django.contrib.auth.views import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework.views import APIView

from .serializers import UserSerializer

User = get_user_model()


class RegisterAPIView(APIView):

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password2 == password1:
            if User.objects.filter(username=username).exists():
                return Response({'success': False, 'error': 'Username already exists!'}, status=400)
            if User.objects.filter(email=email).exists():
                return Response({'success': False, 'error': 'Email already exists!'}, status=400)
            else:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    username=username,
                    password=password1
                )
                user_serializer = UserSerializer(user)
                return Response({'success': True, 'data': user_serializer.data})
        else:
            return Response({'success': False, 'error': 'Passwords are not same!'})


class UserInfoAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        user_serializer = UserSerializer(user)
        return Response({'success': True, 'data': user_serializer.data})
