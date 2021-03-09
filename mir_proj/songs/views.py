from django.shortcuts import render

# Create your views here.
from .serializers import SongSerializer
from rest_framework import viewsets
from .models import Song

class SongView(viewsets.ModelViewSet):
    serializer_class = SongSerializer
    queryset = Song.objects.all()
