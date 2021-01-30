from django.contrib.auth.hashers import make_password
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.serializers import UserCurrentSerializer, UserRegSerializer


class UserRegViewSet(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegSerializer

    def perform_create(self, serializer):
        password = make_password(self.request.data['password'])
        serializer.save(password=password)


class UserCurrentViewSet(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserCurrentSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
