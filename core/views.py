from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse
from core.models import Categoria, Author, Book
from core.serializers import CategoriaSerializer, AuthorSerializer, LivroSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    name = 'categoria'
    
class AuthorViewSet(viewsets.ModelViewSet):
  queryset = Author.objects.all()
  serializer_class = AuthorSerializer
  name = 'author'

class BookViewSet(viewsets.ModelViewSet):
  queryset = Book.objects.all()
  serializer_class = LivroSerializer
  name = 'book'
