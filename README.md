# Sistema de Cadastro de Alunos, Cursos, Produtos e API de Usuários (EA 1, EA 2 e EA 3)

Projeto Django desenvolvido para as atividades **EA 1**, **EA 2** e **EA 3** (Arquitetura de Sistemas), implementando:
- **EA 1:** Cadastro de **alunos** e **cursos** com relacionamento **muitos-para-muitos (N:N)** via Django Admin e listagem pública.
- **EA 2:** Cadastro de **produtos** com **ModelForm (`ProdutoForm`)** e view `produto_new` funcionando sem Django Admin.
- **EA 3:** API REST com **Django Rest Framework (DRF)** expondo `/api/usuarios/` em JSON, além da documentação teórica em `docs/ea3_respostas.md`.

---

## Mapa do Projeto

```text
E.A1/
├── manage.py                         # Utilitário de linha de comando do Django
├── requirements.txt                  # Dependências Python (Django 6.1.3 e DRF 3.18.3)
├── .gitignore                        # Arquivos ignorados pelo Git (venv, db.sqlite3, __pycache__)
├── README.md                         # Documentação e guia de execução do projeto
│
├── docs/                             # Documentos e arquivos da EA 3
│   ├── usuarios.json                 # JSON equivalente à tabela de usuários (Carlos e João)
│   └── ea3_respostas.md              # Respostas sobre SQL vs NoSQL, JSON e fluxo JWT
│
├── escola/                           # Pacote principal de configuração do projeto
│   ├── __init__.py
│   ├── asgi.py                       # Ponto de entrada ASGI
│   ├── wsgi.py                       # Ponto de entrada WSGI
│   ├── settings.py                   # Configurações (INSTALLED_APPS com rest_framework e cadastro, pt-br, America/Maceio)
│   └── urls.py                       # Roteamento raiz (/admin/ e inclusão de cadastro.urls)
│
└── cadastro/                         # App responsável pelos cadastros e API
    ├── __init__.py
    ├── admin.py                      # Registro de AlunoAdmin, CursoAdmin e UsuarioAdmin
    ├── apps.py                       # Configuração do app (CadastroConfig)
    ├── forms.py                      # ProdutoForm (ModelForm para Produto)
    ├── models.py                     # Models Curso, Aluno (ManyToMany), Produto e Usuario
    ├── serializers.py                # UsuarioSerializer (ModelSerializer do DRF)
    ├── views.py                      # Views HTML e view DRF listar_usuarios_api
    ├── urls.py                       # Rotas /alunos/, /cursos/, /produtos/, /produtos/novo/ e /api/usuarios/
    ├── tests.py                      # Arquivo de testes do app
    ├── migrations/
    │   ├── __init__.py
    │   ├── 0001_initial.py           # Migração inicial (Curso e Aluno)
    │   ├── 0002_produto.py           # Migração da EA 2 (Produto)
    │   └── 0003_usuario.py           # Migração da EA 3 (Usuario)
    └── templates/
        ├── base.html                 # Template base com bloco {% block content %} e barra de navegação
        └── cadastro/
            ├── alunos.html           # Listagem de alunos e seus respectivos cursos
            ├── cursos.html           # Listagem de cursos e seus respectivos alunos
            ├── produtos.html         # Listagem de produtos cadastrados
            └── produto_form.html     # Formulário de cadastro de produto (com {% csrf_token %})
```

---

## Rotas Disponíveis

| Rota | View / Destino | Formato | Descrição |
| :--- | :--- | :--- | :--- |
| `/alunos/` | `cadastro.views.listar_alunos` | HTML | Lista todos os alunos e os cursos matriculados. |
| `/cursos/` | `cadastro.views.listar_cursos` | HTML | Lista todos os cursos e os alunos matriculados. |
| `/produtos/` | `cadastro.views.listar_produtos` | HTML | Lista todos os produtos cadastrados. |
| `/produtos/novo/` | `cadastro.views.produto_new` | HTML | Exibe e processa o `ProdutoForm` (sem Django Admin). |
| `/api/usuarios/` | `cadastro.views.listar_usuarios_api` | JSON (DRF) | Retorna os usuários cadastrados (`Carlos` e `João`) em JSON. |
| `/admin/` | `admin.site.urls` | HTML | Painel administrativo do Django. |

---

## Configurações Principais (`escola/settings.py`)

- **Apps instalados:** `'rest_framework'` e `'cadastro'` em `INSTALLED_APPS`
- **Idioma:** `LANGUAGE_CODE = 'pt-br'`
- **Fuso horário:** `TIME_ZONE = 'America/Maceio'`
- **Banco de dados:** SQLite (`db.sqlite3`)

---

## Como Executar Localmente

### 1. Clonar o repositório e entrar na pasta

```bash
git clone https://github.com/gabrieltrabalhos478-art/E.A1-Arquitetura-de-Sistemas.git
cd E.A1-Arquitetura-de-Sistemas
```

### 2. Criar e ativar o ambiente virtual (`venv`)

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Linux / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Aplicar as migrações e validar o projeto

```bash
python manage.py check
python manage.py migrate
```

### 5. Iniciar o servidor de desenvolvimento

```bash
python manage.py runserver
```

Acesse no navegador:
- Alunos: `http://127.0.0.1:8000/alunos/`
- Cursos: `http://127.0.0.1:8000/cursos/`
- Produtos: `http://127.0.0.1:8000/produtos/`
- Cadastrar Produto: `http://127.0.0.1:8000/produtos/novo/`
- API Usuários (JSON): `http://127.0.0.1:8000/api/usuarios/`
- Admin: `http://127.0.0.1:8000/admin/`
