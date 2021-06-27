from django.contrib import admin
from .models import Categoria, registro_usuario

# Register your models here.

admin.site.register(Categoria)
admin.site.register(registro_usuario)