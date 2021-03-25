from rest_framework import serializers
from .models import Song,Segment

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id','title' ,'artist', 'album', 'released_date')

class SegmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Segment
        fields = ('id','title' ,'segment')

        
