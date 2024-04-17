from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from user.serializers import UserSerializer


class RegisterView(CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()
