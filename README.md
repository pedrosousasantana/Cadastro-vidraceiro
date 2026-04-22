# 🪟 Vidraçaria — CRUD com Flask

Sistema de gerenciamento de vidros com cadastro, listagem, edição e exclusão.

## Tecnologias

- Python 3.10+
- Flask 3.x
- HTML5 + CSS3 (sem dependências externas de JS)

## Como rodar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/vidracaria.git
cd vidracaria
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Rode a aplicação

```bash
python app.py
```

Acesse: <http://localhost:5000>

## Funcionalidades

|Rota           |Método    |Descrição             |
|---------------|----------|----------------------|
|`/`            |GET       |Lista todos os vidros |
|`/criar`       |GET / POST|Formulário de cadastro|
|`/editar/<id>` |GET / POST|Formulário de edição  |
|`/deletar/<id>`|POST      |Remove um vidro       |

## Estrutura do projeto

```
vidracaria/
├── app.py               # Rotas e lógica Flask
├── requirements.txt     # Dependências
├── README.md
└── templates/
    ├── base.html        # Layout base
    ├── index.html       # Listagem
    └── form.html        # Cadastro / Edição
```

## Observações

- Os dados ficam em memória (lista Python). Para persistência, integre com SQLite usando Flask-SQLAlchemy.
- A `secret_key` deve ser trocada por uma variável de ambiente em produção.