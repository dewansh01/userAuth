from rest_framework import generics,authentication,permissions
from authApp.serializers import (UserSerializer,AuthTokenSerializers)
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

class createUserView(generics.CreateAPIView):
    """
        create a new user in the system
    """
    serializer_class = UserSerializer

class createTokenView(ObtainAuthToken):
    """
        create a new user in the system
    """
    serializer_class = AuthTokenSerializers
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ManageUserView(generics.RetrieveUpdateAPIView):
    """
        Manage the authenticated user
    """
    serializer_class=UserSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user