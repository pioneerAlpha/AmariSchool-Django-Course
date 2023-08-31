# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from .models import List
# from .serializers import ListSerializer

from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import mixins
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.authentication import  TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

# # Create your views here.

# @csrf_exempt
# def total_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         lists = List.objects.all()
#         serializer = ListSerializer(lists, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = ListSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def list_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         list = List.objects.get(pk=pk)
#     except List.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = ListSerializer(list)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         print(request.body)
#         data = JSONParser().parse(request)
#         serializer = ListSerializer(list, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         list.delete()
#         return HttpResponse(status=204)


# @api_view(['GET', 'POST'])
# def total_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = List.objects.all()
#         serializer = ListSerializer(snippets, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = ListSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['GET', 'PUT', 'DELETE'])
# def list_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = List.objects.get(pk=pk)
#     except List.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ListSerializer(snippet)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = ListSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class ListList(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         snippets = List.objects.all()
#         serializer = ListSerializer(snippets, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = ListSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class ListDetail(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return List.objects.get(pk=pk)
#         except List.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = ListSerializer(snippet)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = ListSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class ListList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = List.objects.all()
#     serializer_class = ListSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
# class ListDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = List.objects.all()
#     serializer_class = ListSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# class ListList(generics.ListCreateAPIView):
#     queryset = List.objects.all()
#     serializer_class = ListSerializer


# class ListDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = List.objects.all()
#     serializer_class = ListSerializer

# class ListCombinedViewSet(viewsets.ViewSet):
#     """
#     A ViewSet for viewing and editing List instances.
#     """
#     serializer_class = ListSerializer
#     queryset = List.objects.all()

#     def list(self, request):
#         serializer = ListSerializer(self.queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         instance = get_object_or_404(self.queryset, pk=pk)
#         serializer = ListSerializer(instance)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def update(self, request, pk=None):
#         instance = get_object_or_404(self.queryset, pk=pk)
#         serializer = self.serializer_class(instance, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, pk=None):
#         instance = get_object_or_404(self.queryset, pk=pk)
#         instance.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class ListCombinedViewSet(viewsets.ReadOnlyModelViewSet):
    
#     queryset=List.objects.all()
#     serializer_class=ListSerializer
#     # authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]

    
# class LoginView(APIView):
    
#     def post(self, request):
#         username=request.data.get('username')
#         password=request.data.get('password')
        
#         if username is None or password is None:
#             return Response({'error': 'Please provide all credentials'}, status=status.HTTP_400_BAD_REQUEST)
        
#         user=authenticate(username=username, password=password)
        
#         if user:
#             token, created= Token.objects.get_or_create(user=user)
#             return Response({'token':token.key},status=status.HTTP_200_OK)
#         else:
#             return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    
class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    # throttle_scope = 'album'
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields  = ['album_name', 'artist']
    ordering_fields= ['album_name', 'artist']