from django.contrib.auth.models import User
from rest_framework import serializers
from users.models import VerificationUserCode


class UserValidateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)

class UserRegisterSerializer(UserValidateSerializer):
    email = serializers.EmailField(required=False)
    first_name = serializers.CharField(max_length=50, required=False)
    last_name = serializers.CharField(max_length=50, required=False)
    verify_code = serializers.CharField(max_length=8, required=False)

    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError('Имя пользователя уже существует!')
        return username

    def validate_password(self, password):
        if len(password) < 8:
            raise serializers.ValidationError('Пароль должен содержать не менее 8 символов')
        elif password.isdigit():
            raise serializers.ValidationError('Пароль должен содержать буквы')
        elif password.isalpha():
            raise serializers.ValidationError('Пароль должен содержать цифры')
        return password

class UserVerifySerializer(serializers.ModelSerializer):
    class Meta:
        model = VerificationUserCode
        fields = ['verify_code']

class UserLoginSerializer(UserValidateSerializer):
    pass

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'is_active']