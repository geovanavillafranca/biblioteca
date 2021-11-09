from django.urls import path
from . import  views

urlpatterns = [
  # url estatica, nao muda
  path('home/', views.home, name = 'home'),
  # url dinamica, vai mudar dependendo do livro, que seria seu id
  path('ver_livro/<int:id>', views.ver_livros, name='ver_livros')
]
