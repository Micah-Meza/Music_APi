from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status
from .serializers import SongModelSerializer
from .models import SongModel

@api_view(['GET',])
def song_list(request):

    if request.method == 'GET':
         song = SongModel.objects.all()
         
         






# Create your views here.
