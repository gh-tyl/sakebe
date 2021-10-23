from datetime import datetime
from django.contrib.auth.models import User, Group
from rest_framework import generics, permissions, status, viewsets
from rest_framework.response import Response
from django.db import connection, transaction

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

# Scream情報取得のView(GET)
class ScreamListView(generics.ListAPIView):
    # queryset = Scream.objects.all()
    serializer_class = ScreamListSerializer
    def get_queryset(self):
        def dictfetchall(cursor):
            "Return all rows from a cursor as a dict"
            columns = [col[0] for col in cursor.description]
            return [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]
        current_date = datetime.today().date()
        with connection.cursor() as cursor:
            cursor.execute(
                f'''
                SELECT *
                FROM scream 
                WHERE scream.created_at >= '{current_date}' 
                ORDER BY scream.created_at
                '''
            )
            data = dictfetchall(cursor)
        # return data['results']
        return data

class ScreamRegisterView(generics.CreateAPIView):
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