from rest_framework import generics
from authApp.serializers import (UserSerializer,AuthTokenSerializers)
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

class createUserView(generics.CreateAPIView):
    """
        create a new user in the system
    """
    serializer_class = UserSerializer

class createTokenView(generics.CreateAPIView):
    """
        create a new user in the system
    """
    serializer_class = AuthTokenSerializers
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES