import json

from app import settings as api_settings
from app.utils import success_response
from rest_framework import generics
from rest_framework import status

from .controllers.authenticate_controller import AuthenticateController
from .serializer import AuthenticateSerializer
from .serializer import UserSerializer


class AuthenticateView(generics.GenericAPIView):

    serializer_class = AuthenticateSerializer
    permission_classes = api_settings.CONSUMER_PERMISSIONS

    def post(self, request):
        """Authenticate the current user."""
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            data = request.data
        return AuthenticateController(request, data, self.serializer_class).process()


class MeView(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = api_settings.CONSUMER_PERMISSIONS

    def get(self, request):
        """Get current authenticated user."""
        return success_response(
            self.serializer_class(request.user).data, status.HTTP_200_OK
        )
