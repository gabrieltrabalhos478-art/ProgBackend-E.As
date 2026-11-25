# Sistema de Cadastro de Alunos e Cursos (EA 1)

Projeto Django desenvolvido para a atividade **EA 1** (Arquitetura de Sistemas), implementando um sistema simples de cadastro de **alunos** e **cursos** com relacionamento **muitos-para-muitos (N:N)** — um aluno pode estar matriculado em vários cursos e um curso pode ter vários alunos.

---

## Mapa do Projeto

```text
E.A1/
├── manage.py                         # Utilitário de linha de comando do Django
├── requirements.txt                  # Lista de dependências Python (Django 6.1.3)
├── .gitignore                        # Arquivos ignorados pelo Git (venv, db.sqlite3, __pycache__)
├── README.md                         # Documentação e guia de execução do projeto
│
├── escola/                           # Pacote principal de configuração do projeto
│   ├── __init__.py
│   ├── asgi.py                       # Ponto de entrada ASGI
│   ├── wsgi.py                       # Ponto de entrada WSGI
│   ├── settings.py                   # Configurações (INSTALLED_APPS, pt-br, America/Maceio, SQLite)
│   └── urls.py                       # Roteamento raiz (/admin/ e inclusão de cadastro.urls)
│
└── cadastro/                         # App responsável pelo domínio de Alunos e Cursos
    ├── __init__.py
    ├── admin.py                      # Registro e configuração de AlunoAdmin e CursoAdmin
    ├── apps.py                       # Configuração do app (CadastroConfig)
    ├── models.py                     # Models Curso e Aluno (ManyToManyField)
    ├── views.py                      # Views listar_alunos e listar_cursos
    ├── urls.py                       # Rotas /alunos/ e /cursos/
    ├── tests.py                      # Arquivo de testes do app
    ├── migrations/
    │   ├── __init__.py
    │   └── 0001_initial.py           # Migração inicial criando tabelas Curso e Aluno
    └── templates/
        └── cadastro/
            ├── base.html             # Layout base com barra de navegação e estilos
            ├── alunos.html           # Listagem de alunos e seus respectivos cursos
            └── cursos.html           # Listagem de cursos e seus respectivos alunos
```

---

## Arquitetura e Fluxo de Requisição

O projeto segue o padrão **MVT (Model-View-Template)** do Django:

```text
Navegador (/alunos/ ou /cursos/)
   │
   ▼
escola/urls.py ──► cadastro/urls.py
                      │
                      ▼
               cadastro/views.py (listar_alunos / listar_cursos)
                      │  (consulta com prefetch_related)
                      ▼
               cadastro/models.py (Aluno / Curso no SQLite)
                      │
                      ▼
               cadastro/templates/cadastro/*.html (herdam de base.html)
```

---

## Modelagem de Dados (`cadastro/models.py`)

```mermaid
erDiagram
    ALUNO {
        int id PK
        string nome
        string sobrenome
        string email UK
    }
    CURSO {
        int id PK
        string titulo
        text descricao
    }
    ALUNO }o--o{ CURSO : "cursos (related_name='alunos')"
```

- **`Curso`**: `titulo` (`CharField`, máx. 150 caracteres) e `descricao` (`TextField`).
- **`Aluno`**: `nome` (`CharField`, máx. 100), `sobrenome` (`CharField`, máx. 100), `email` (`EmailField`, único) e `cursos` (`ManyToManyField(Curso, related_name='alunos', blank=True)`).

---

## Rotas Disponíveis

| Rota | View / Destino | Nome da URL | Descrição |
| :--- | :--- | :--- | :--- |
| `/alunos/` | `cadastro.views.listar_alunos` | `listar_alunos` | Lista todos os alunos e os cursos matriculados (`aluno.cursos.all`). |
| `/cursos/` | `cadastro.views.listar_cursos` | `listar_cursos` | Lista todos os cursos e os alunos matriculados (`curso.alunos.all`). |
| `/admin/` | `admin.site.urls` | — | Painel administrativo com `AlunoAdmin` e `CursoAdmin` (busca e listagem). |

---

## Configurações Principais (`escola/settings.py`)

- **App registrado:** `'cadastro'` em `INSTALLED_APPS`
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

### 5. (Opcional) Criar superusuário para cadastrar dados no Admin

```bash
python manage.py createsuperuser
```

### 6. Iniciar o servidor de desenvolvimento

```bash
python manage.py runserver
```

Acesse no navegador:
- Alunos: `http://127.0.0.1:8000/alunos/`
- Cursos: `http://127.0.0.1:8000/cursos/`
- Admin: `http://127.0.0.1:8000/admin/`
