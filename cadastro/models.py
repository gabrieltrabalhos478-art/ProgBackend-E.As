from django.db import models


# Model que representa um curso disponível na escola
class Curso(models.Model):
    titulo = models.CharField(max_length=150)
    descricao = models.TextField()

    def __str__(self):
        # Mostra o título do curso no painel administrativo e no shell
        return self.titulo


# Model que representa um aluno cadastrado
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    # Relação muitos-para-muitos: um aluno pode estar em vários cursos,
    # e um curso pode ter vários alunos (acessível via curso.alunos.all())
    cursos = models.ManyToManyField(Curso, related_name='alunos', blank=True)

    def __str__(self):
        # Mostra o nome completo do aluno
        return f"{self.nome} {self.sobrenome}"
