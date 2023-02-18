from rest_framework import serializers
from .models import SongModel

class SongModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongModel
        fields = ['id', 'title', 'artist', 'album', 'release_date', 'genre']
