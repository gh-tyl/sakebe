from django.contrib.auth.models import User, Group
from rest_framework import generics, permissions, status, viewsets
from rest_framework.response import Response
from django.db import transaction

from .models import *
from .serializers import *

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

# # ユーザ情報取得のView(GET)
# class ScreamListView(generics.RetrieveAPIView):
#     permission_classes = (permissions.IsAuthenticated,)
#     queryset = MyUser.objects.all()
#     serializer_class = UserSerializer

#     def get(self, request, format=None):
#         return Response(data={
#             'username': request.user.username,
#             'email': request.user.email,
#             },
#             status=status.HTTP_200_OK)

class ScreamView(generics.CreateAPIView):
    queryset = Scream.objects.all()
    serializer_class = ScreamSerializer
    # @transaction.atomic
    def post(self, request, format=None):
        data = {
            "content": request.data["content"],
            "color": request.data["color"],
            "expression_points": request.data["expression_points"],
            "decibel": request.data["decibel"],
        }
        serializer = ScreamSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)