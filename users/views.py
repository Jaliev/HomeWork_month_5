from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from users.models import VerificationUserCode
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from users.serializers import UserLoginSerializer, UserRegisterSerializer, UserProfileSerializer, UserVerifySerializer
import random, math


'''Метод с использованием CBV - Class Based Views'''

class RegisterAPIView(GenericAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.create_user(**serializer.validated_data)

        digits = [i for i in range(0, 10)]
        random_code = ''
        for i in range(8):
            index = math.floor(random.random() * 10)
            random_code += str(digits[index])

        return Response(
            {
                'verify_code': random_code,
                'data': serializer.data,
            }
        )

class VerifyAPIView(GenericAPIView):
    serializer_class = UserVerifySerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        VerificationUserCode.is_active = True

        return Response({'message': 'Пользователь успешно активирован'})

class LoginAPIView(GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(**serializer.validated_data)

        if not user.is_active:
            return Response({'error': 'Пользователь не активен'})
        else:
            token, created = Token.objects.get_or_create(user=user)

        return Response(
            {
                'token': token.key,
                'username': user.username,
            }
        )

class LogoutAPIView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response({'message': 'Успешный выход из системы!'})

class ProfileViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer


'''Метод с использованием FBV - Function Based Views'''

# @api_view(['POST'])
# def register(request):
#     serializer = UserRegisterSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#
#     user = User.objects.create_user(**serializer.validated_data)
#
#     digits = [i for i in range(0, 10)]
#     random_code = ''
#     for i in range(8):
#         index = math.floor(random.random() * 10)
#         random_code += str(digits[index])
#
#     return Response(
#         {
#             'verify_code': random_code,
#             'data': serializer.data,
#         }
#     )

# @api_view(['POST'])
# def verify(request):
#     serializer = UserVerifySerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     VerificationUserCode.is_active = True
#
#     return Response({'message': 'Пользователь успешно активирован'})

# @api_view(['POST'])
# def login(request):
#     serializer = UserLoginSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#
#     user = authenticate(**serializer.validated_data)
#
#     if not user.is_active:
#         return Response({'error': 'Пользователь не активен'})
#     else:
#         token, created = Token.objects.get_or_create(user=user)
#
#     return Response(
#             {
#                 'token': token.key,
#                 'username': user.username,
#             }
#         )

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def logout(request):
#     request.user.auth_token.delete()
#     return Response({'message': 'Успешный выход из системы!'})

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def profile(request):
#     serializer = UserProfileSerializer(instance=request.user, many=False)
#     return Response(serializer.data)