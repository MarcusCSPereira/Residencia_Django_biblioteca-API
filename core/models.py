from django.db import models

class Categoria(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
      
class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    
    def __str__(self):
        return self.name
      
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    publicado_em = models.DateField()

    def __str__(self):
        return self.title
      
