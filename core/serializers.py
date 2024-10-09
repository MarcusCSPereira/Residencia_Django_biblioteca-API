from rest_framework import serializers
from .models import Book, Author, Categoria


class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)

    books = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="book-detail",
    )

    class Meta:
        model = Categoria
        fields = ["url", "id", "name", "books"]


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    birth_date = serializers.DateField()

    books = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="book-detail",
    )

    class Meta:
        model = Author
        fields = ["url", "id", "name", "birth_date", "books"]


class LivroSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)

    # Para envio dos dados (criação e atualização)
    categoria = serializers.SlugRelatedField(
        queryset=Categoria.objects.all(), slug_field="name"
    )
    author = serializers.HyperlinkedRelatedField(
        view_name="author-detail", queryset=Author.objects.all()
    )

    # Para exibição apenas do campo 'name' nas respostas
    author_name = serializers.CharField(source="author.name", read_only=True)

    publicado_em = serializers.DateField()

    class Meta:
        model = Book
        fields = [
            "url",
            "id",
            "title",
            "author",
            "author_name",
            "categoria",
            "publicado_em",
        ]
