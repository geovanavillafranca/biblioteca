from django.contrib import admin

from usuarios.models import Usuario

# Register your models here.


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    # só podera ler esses campos
    readonly_fields = ('nome', 'email', 'senha')

