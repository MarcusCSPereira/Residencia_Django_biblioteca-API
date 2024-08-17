from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Book, Author, Categoria
from .serializers import LivroSerializer, AuthorSerializer, CategoriaSerializer

import json

@api_view(['GET', 'POST'])
def livro_list_create(request):
      if request.method == 'GET':
          livros = Book.objects.all()
          serializers = LivroSerializer(livros, many = True)
          return Response(serializers.data)
      
      elif request.method == 'POST':
        serializer = LivroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
@api_view(['GET', 'PUT', 'DELETE'])
def livro_details(request, pk):
    try:
        livro = Book.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET':
        serializer = LivroSerializer(livro)
        return Response(serializer.data)
      
    if request.method == 'PUT':
      serializer = LivroSerializer(livro, data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
      try:
          livro_para_deletar = Book.objects.get(pk=request.data['pk'])
          livro_para_deletar.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)
      except:
          return Response(status=status.HTTP_204_NO_CONTENT)        


