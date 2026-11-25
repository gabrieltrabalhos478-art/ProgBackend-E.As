# Sistema de Cadastro de Alunos e Cursos (EA 1)

Projeto Django simples para cadastro de **alunos** e **cursos** com relacionamento muitos-para-muitos (um aluno pode estar matriculado em vários cursos e um curso pode ter vários alunos).

## Estrutura principal

- `escola/`: configurações do projeto Django (`settings.py`, `urls.py`).
- `cadastro/`: app com os models `Aluno` e `Curso`, painel admin, views e templates.
  - `/alunos/`: lista todos os alunos e os cursos matriculados.
  - `/cursos/`: lista todos os cursos e os alunos matriculados.
  - `/admin/`: painel administrativo do Django.

## Como executar o projeto localmente

### 1. Criar e ativar o ambiente virtual (`venv`)

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

### 2. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 3. Aplicar as migrações do banco de dados

```bash
python manage.py migrate
```

### 4. (Opcional) Criar um superusuário para acessar o Admin

```bash
python manage.py createsuperuser
```

### 5. Iniciar o servidor de desenvolvimento

```bash
python manage.py runserver
```

Acesse no navegador:
- Alunos: `http://127.0.0.1:8000/alunos/`
- Cursos: `http://127.0.0.1:8000/cursos/`
- Admin: `http://127.0.0.1:8000/admin/`
