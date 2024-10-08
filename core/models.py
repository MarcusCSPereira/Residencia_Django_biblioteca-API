from django.db import models


class Categoria(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey("Author", related_name="books", on_delete=models.CASCADE)
    categoria = models.ForeignKey(
        "Categoria", related_name="books", on_delete=models.CASCADE
    )
    publicado_em = models.DateField()

    def __str__(self):
        return self.title
