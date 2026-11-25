from django.shortcuts import render
from .models import Aluno, Curso


# View para listar todos os alunos e os cursos em que estão matriculados
def listar_alunos(request):
    # prefetch_related otimiza a consulta dos cursos de cada aluno
    alunos = Aluno.objects.prefetch_related('cursos').all()
    return render(request, 'cadastro/alunos.html', {'alunos': alunos})


# View para listar todos os cursos e os alunos matriculados em cada um
def listar_cursos(request):
    # prefetch_related otimiza a consulta dos alunos de cada curso
    cursos = Curso.objects.prefetch_related('alunos').all()
    return render(request, 'cadastro/cursos.html', {'cursos': cursos})
