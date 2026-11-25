from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import ProdutoForm
from .models import Aluno, Curso, Produto, Usuario
from .serializers import UsuarioSerializer


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


# View para listar os produtos cadastrados (sem precisar do Django Admin)
def listar_produtos(request):
    produtos = Produto.objects.all().order_by('-id')
    return render(request, 'cadastro/produtos.html', {'produtos': produtos})


# View para cadastrar um novo produto usando ProdutoForm
def produto_new(request):
    if request.method == 'POST':
        # Preenche o formulário com os dados enviados pelo usuário
        form = ProdutoForm(request.POST)
        if form.is_valid():
            # Salva no banco e redireciona para a listagem de produtos
            form.save()
            return redirect('listar_produtos')
    else:
        # Em requisições GET, exibe o formulário vazio
        form = ProdutoForm()

    return render(request, 'cadastro/produto_form.html', {'form': form})


# View da API REST (DRF) que retorna todos os usuários em formato JSON (EA 3)
@api_view(['GET'])
def listar_usuarios_api(request):
    usuarios = Usuario.objects.all().order_by('id')
    serializer = UsuarioSerializer(usuarios, many=True)
    return Response(serializer.data)
