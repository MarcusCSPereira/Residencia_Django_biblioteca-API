from rest_framework import serializers
from .models import Book, Author, Categoria

class CategoriaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    
    def create(self, validated_data):
        return Categoria.objects.create(**validated_data)
      
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
      
class AuthorSerializer(serializers.Serializer):
  id = serializers.IntegerField(read_only=True)
  name = serializers.CharField(max_length=100)
  birth_date = serializers.DateField()
  
  def create(self, validated_data):
      return Author.objects.create(**validated_data)
    
  def update(self, instance, validated_data):
      instance.name = validated_data.get('name', instance.name)
      instance.birth_date = validated_data.get('birth_date', instance.birth_date)
      instance.save()
      return instance
    
class LivroSerializer(serializers.Serializer):
  id = serializers.IntegerField(read_only=True)
  title = serializers.CharField(max_length=100)
  author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
  categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all())
  publicado_em = serializers.DateField()
  
  def create(self, validated_data):
      return Book.objects.create(**validated_data)
    
  def update(self, instance, validated_data):
    instance.title = validated_data.get('title', instance.title)
    instance.author = validated_data.get('author', instance.author)
    instance.categoria = validated_data.get('categoria', instance.categoria)
    instance.publicado_em = validated_data.get('publicado_em', instance.publicado_em)
    instance.save()
    return instance