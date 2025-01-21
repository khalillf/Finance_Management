# apps/users/views.py

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import login, get_user_model
from .serializers import UserSerializer, RegisterSerializer, CustomAuthTokenSerializer

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]  # Explicitly allow any

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            # Save the user to the database
            user = serializer.save()
            print(f"User ID: {user.id}, Username: {user.username}")  # Debugging

            # Ensure the user is saved before creating the token
            if user.id:
                # Create or get the token
                token, created = Token.objects.get_or_create(user=user)
                print(f"Token: {token.key}, Created: {created}")  # Debugging

                # Log the user in after registration
                login(request, user)

                # Prepare the response data
                response_data = {
                    'user': UserSerializer(user).data,
                    'token': token.key  # Include the token in the response
                }

                # Return the custom response
                return Response(response_data, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    'error': 'User was not saved to the database.'
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(f"Error: {e}")  # Debugging
            return Response({
                'error': str(e),
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CustomObtainAuthToken(generics.GenericAPIView):
    serializer_class = CustomAuthTokenSerializer
    permission_classes = [permissions.AllowAny]  # Ensure login is public

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        # Get or create token
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key
        }, status=status.HTTP_200_OK)

class UserProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class LogoutView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            # Delete the token to force a login
            request.user.auth_token.delete()
            return Response(status=status.HTTP_200_OK)
        except (AttributeError, Token.DoesNotExist):
            return Response(status=status.HTTP_400_BAD_REQUEST)
