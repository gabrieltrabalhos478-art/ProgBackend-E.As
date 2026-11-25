from django.urls import path
from . import views

# Rotas do app cadastro
urlpatterns = [
    path('alunos/', views.listar_alunos, name='listar_alunos'),
    path('cursos/', views.listar_cursos, name='listar_cursos'),
]
