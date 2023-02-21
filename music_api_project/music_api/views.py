from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status
from .serializers import SongModelSerializer
from .models import SongModel

@api_view(['GET', 'POST'])
def song_list(request):
    if request.method == 'GET':     
        song = SongModel.objects.all()
        serializer = SongModelSerializer(song, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    elif request.method =='POST':
        serializer = SongModelSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)



@api_view(['GET', 'PUT', 'DELETE'])
def song_detail(request, pk):
    song = get_object_or_404(SongModel, pk = pk)
    
    if request.method == 'GET':
        serializer = SongModelSerializer(song)
        return Response(serializer.data, status = status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = SongModelSerializer(song, data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_200_OK)




# Create your views here.
