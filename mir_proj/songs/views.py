from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import api_view
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from django.core.files.storage import default_storage



# Create your views here.
from .serializers import SongSerializer,SegmentSerializer
from rest_framework import viewsets
from .models import Song, Segment
from deep_audio_features.bin.audio_process import process_wave_file
from deep_audio_features.bin.deep_retrieval_query  import search_deep_database
import json  

import os.path,sys
sys.path.insert(0, os.path.join(os.path.dirname(
os.path.realpath(__file__)), "../"))



class SongViewSet(viewsets.ModelViewSet):
     serializer_class = SongSerializer
     queryset = Song.objects.all()

class FileUploadView(APIView):
    parser_classes = [MultiPartParser,]

    def post(self, request, format=None):

          file_obj = request.data['file']
          print(request.data)
          if file_obj:
               filename = str(file_obj)
               audio = 'audio/' + filename
               print(audio)
               with default_storage.open('audio/' + filename, 'wb+') as destination:
                    print(destination)
                    for chunk in file_obj.chunks():
                         destination.write(chunk)
               
               db = '/home/george/Documents/Thesis/MIR-mobile-app/mir_proj/deep_audio_features/db'
               segment_output = '/home/george/Documents/Thesis/MIR-mobile-app/mir_proj/audio/wav/'
             
               new_path = process_wave_file(audio,segment_output)
               song_list  = search_deep_database(db,new_path)

               ret = json.dumps(song_list)
               
               return Response(song_list,status=200)
          else:
               return Response({"message":"File is missing"},status=200)

          
                    # serializer = SegmentSerializer(data=request.data)
          # if serializer.is_valid():
          #     serializer.save()
          #     return Response(serializer.data, status= status.HTTP_201_CREATED)
          # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     

    def get(self,request):
        segments = Segment.objects.all()
        serializer = SegmentSerializer(segments,many=True)
        return Response(serializer.data)



   
# #class based views

# class SongList(APIView):

#     def get(self,request):
#         songs = Song.objects.all()
#         serializer = SongSerializer(songs,many=True)
#         return Response(serializer.data)

#     def post(self,request):
#         serializer = SongSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status= status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class SongDetails(APIView):

#     def get_object(self,id):
#         try:
#             return Song.objects.get(id=id)
    
#         except Song.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def get(self,request,id):
#         song = self.get_object(id)
#         serializer = SongSerializer(song)
#         return Response(serializer.data)

#     def put(self,request,id):
#         song = self.get_object(id)
#         serializer = SongSerializer(song,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self,request,id):
#         song = self.get_object(id)
#         song.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# #function based vies 

# @api_view(['GET','POST'])
# def song_list(request):
#     if request.method == 'GET':
#         songs = Song.objects.all()
#         serializer = SongSerializer(songs,many=True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = SongSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status= status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT','DELETE'])
# def song_details(request,pk):
#     try:
#         song = Song.objects.get(pk=pk)
    
#     except Song.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = SongSerializer(song)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = SongSerializer(song,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         song.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
