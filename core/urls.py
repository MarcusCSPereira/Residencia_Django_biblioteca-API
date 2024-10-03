from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.APIRootView.as_view(), name='api-root'),
    path("books/", views.BookList.as_view(), name=views.BookList.name),
    path("books/<int:pk>/", views.BookDetail.as_view(), name=views.BookDetail.name),
    path("authors/", views.AuthorList.as_view(), name=views.AuthorList.name),
    path("authors/<int:pk>/", views.AuthorDetail.as_view(), name=views.AuthorDetail.name),
    path("categorias/", views.CategoriaList.as_view(), name=views.CategoriaList.name),
    path("categorias/<int:pk>/", views.CategoriaDetail.as_view(), name=views.CategoriaDetail.name),
]
