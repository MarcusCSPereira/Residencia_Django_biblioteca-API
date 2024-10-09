from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from core.models import Categoria, Author, Book
from core.serializers import CategoriaSerializer, AuthorSerializer, LivroSerializer
from core.filters import BookFilter, AuthorFilter


class APIRootView(generics.GenericAPIView):
    name = "api-root"

    def get(self, request, *args, **kwargs):
        return Response(
            {
                "categorias": reverse(CategoriaList.name, request=request),
                "authors": reverse(AuthorList.name, request=request),
                "books": reverse(BookList.name, request=request),
            }
        )


class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    search_fields = ("^name",)
    ordering_fields = ("name",)
    name = "categoria-list"


class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    name = "categoria-detail"


class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filterset_class = AuthorFilter
    name = "author-list"


class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    name = "author-detail"


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = LivroSerializer
    filterset_class = BookFilter
    search_fields = ("^title",)  # Aqui é importante a virgula
    ordering_fields = ("title", "author", "categoria", "publicado_em")
    name = "book-list"


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = LivroSerializer
    name = "book-detail"
