from django.contrib import admin
# Register your models here.
from .models import Post, Solicitacao

class PostAdmin(admin.ModelAdmin):
    list_display = [ 'nome', 'cpf', 'servico', 'tipo', 'aprovado' ]

admin.site.register(Post)
admin.site.register(Solicitacao)
