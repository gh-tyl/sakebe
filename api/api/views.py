from datetime import datetime
from django.contrib.auth.models import User, Group
from rest_framework import generics, permissions, status, viewsets
from rest_framework.response import Response
from django.db import connection, transaction

from .models import *
from .serializers import *
from .function import audio, letter_classification
import boto3
s3 = boto3.resource('s3', verify=False)

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

class ScreamUploadView(generics.CreateAPIView):    
    queryset = Scream.objects.all()
    serializer_class = ScreamUploadSerializer
    # @transaction.atomic
    def post(self, request, format=None):
        print(request.data)
        print(len(request.data["audio_path"]))
        print(type(request.data["audio_path"]))
        # bucket = s3.Bucket("/media/audio/sample.wav")
        print("----")
        print(request.data["audio_path"])
        print("----")
        file_path = audio.convert_webm_to_wav(request.data["audio_path"]+'.webm')
        volume = audio.get_voice_volumn(file_path)
        print(volume)
        text = audio.wav_to_letter(file_path)
        print(text)
        text_label = letter_classification(text)
        print(text_label)
        # audio.wav_to_letter(data['audio_path'])
        # audio.wav_to_letter("s3://media/audio/sample.wav")
        data = {
            "content": text,
            "color": text_label,
            # "expression_points": ,
            "decibel": volume,
            # "audio_path": request.data["audio_path"],
            # "audio_path": bucket,
            # "audio_path": "https://mf-app-s3.s3.ap-northeast-1.amazonaws.com/media/audio/sample.wav",
            # "image_path": request.data["image_path"],
        }
        serializer = ScreamUploadSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ScreamUploadView(generics.CreateAPIView):
#     queryset = Scream.objects.all()
#     serializer_class = ScreamUploadSerializer
#     # @transaction.atomic
#     def post(self, request, format=None):
#         data = {
#             "audio_path": request.data["audio_path"],
#             # "image_path": request.data["image_path"],
#         }
#         serializer = ScreamUploadSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(request.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ScreamRegisterView(generics.CreateAPIView):
    queryset = Scream.objects.all()
    serializer_class = ScreamRegisterSerializer
    # @transaction.atomic
    def post(self, request, format=None):
        data = {
            "content": request.data["content"],
            "color": request.data["color"],
            "expression_points": request.data["expression_points"],
            "decibel": request.data["decibel"],
        }
        serializer = ScreamRegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)