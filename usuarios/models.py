from django.db import models
from django.db.models.fields import CharField

# Create your models here.

#user: caio12
#email: caio@teste.com  
#senha: 12345678

class Usuario(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    senha = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.nome 


