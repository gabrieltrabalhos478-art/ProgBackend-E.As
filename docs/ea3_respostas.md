# Respostas Teóricas — EA 3

## a) Diferença entre bancos SQL e NoSQL (vantagens e desvantagens)

Os bancos **SQL (Relacionais)**, como PostgreSQL, MySQL e SQLite, organizam os dados em **tabelas** com linhas e colunas fixas, usando chaves primárias e estrangeiras para relacionar informações (como `Aluno` e `Curso` neste projeto).

Já os bancos **NoSQL (Não Relacionais)**, como MongoDB e Redis, armazenam dados em formatos flexíveis, como **documentos JSON**, chave-valor ou grafos, sem exigir uma estrutura fixa de colunas para todos os registros.

### Bancos SQL
- **Vantagens:**
  - Estrutura bem definida e padronizada (esquema rígido evita dados inconsistentes).
  - Suporte forte a relacionamentos complexos e transações seguras (**ACID**).
  - Linguagem SQL padrão e muito madura para consultas.
- **Desvantagens:**
  - Menos flexível quando a estrutura dos dados muda com frequência.
  - Escalar horizontalmente (dividir em vários servidores) costuma ser mais trabalhoso.

### Bancos NoSQL
- **Vantagens:**
  - Esquema flexível: cada documento pode ter campos diferentes sem precisar alterar toda a tabela.
  - Alta velocidade para grandes volumes de leitura/escrita e fácil escalabilidade horizontal.
  - Trabalha muito bem com dados no formato JSON, próximo do que APIs REST usam.
- **Desvantagens:**
  - Relacionamentos entre dados (como *joins*) são mais limitados.
  - Menor padronização entre ferramentas (cada banco NoSQL tem sua própria forma de consulta).

---

## b) JSON equivalente à tabela de usuários

```json
[
  {
    "id": 1,
    "nome": "Carlos",
    "email": "carlos@email.com"
  },
  {
    "id": 2,
    "nome": "João",
    "email": "joao@email.com"
  }
]
```

---

## c) Fluxo de autenticação JWT (JSON Web Token)

O **JWT** é um padrão usado em APIs para identificar o usuário sem que o servidor precise guardar sessões na memória ou no banco a cada requisição (*stateless*).

Um token JWT tem três partes separadas por ponto (`header.payload.signature`):
- **Header:** informa o tipo do token (`JWT`) e o algoritmo de assinatura.
- **Payload:** carrega dados públicos do usuário (como `user_id`, `nome` e tempo de expiração).
- **Signature:** assinatura digital criada com uma chave secreta do servidor para garantir que ninguém alterou o token.

### Passo a passo do fluxo

1. **Login:** O cliente (front-end ou aplicativo) envia usuário e senha para a rota de login (ex.: `POST /api/login/`).
2. **Validação e geração do token:** O servidor confere as credenciais no banco. Se estiverem corretas, gera um **JWT** assinado com a chave secreta e devolve para o cliente.
3. **Armazenamento:** O cliente guarda esse token (por exemplo, na memória ou em cookie seguro).
4. **Requisições autenticadas:** Nas próximas chamadas para rotas protegidas (ex.: `GET /api/usuarios/`), o cliente envia o token no cabeçalho HTTP:
   `Authorization: Bearer <seu_token_jwt>`
5. **Verificação no servidor:** O servidor verifica a assinatura e a validade do token usando a chave secreta. Se for válido, libera o acesso e já sabe quem é o usuário pelo conteúdo do `payload`, sem precisar consultar tabela de sessão.
