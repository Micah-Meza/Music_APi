from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status
from .serializers import SongModelSerializer
from .models import SongModel

@api_view(['GET',])
def song_list(request):
         
    song = SongModel.objects.all()
    serializer = SongModelSerializer(song, many = True)
    return Response(serializer.data)
         
         






# Create your views here.
