from django.contrib import admin
from .models import Aluno, Curso


# Configuração de exibição dos alunos no painel admin
@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')
    search_fields = ('nome', 'sobrenome', 'email')


# Configuração de exibição dos cursos no painel admin
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    search_fields = ('titulo',)
