# apps/users/serializers.py

from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate  # Import authenticate
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'profile_picture']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'phone_number']

    def create(self, validated_data):
        # Create the user using the create_user method
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            phone_number=validated_data.get('phone_number', '')
        )
        return user

class CustomAuthTokenSerializer(serializers.Serializer):
    username = serializers.CharField(
        label=_("Username or Email"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        username_or_email = attrs.get('username')
        password = attrs.get('password')

        # Allow login with email
        user = None
        if '@' in username_or_email:
            try:
                user_obj = User.objects.get(email=username_or_email)
                username = user_obj.username
            except User.DoesNotExist:
                raise serializers.ValidationError(
                    _("Unable to log in with provided credentials.")
                )
        else:
            username = username_or_email

        user = authenticate(request=self.context.get('request'), username=username, password=password)

        if not user:
            raise serializers.ValidationError(
                _("Unable to log in with provided credentials.")
            )

        attrs['user'] = user
        return attrs
