# Gerenciamento de Usuários e Obras de Dostoiévski

Este projeto implementa uma aplicação web SPA (**Single Page Application**) para gerenciar usuários e exibir perfis das obras literárias de Dostoiévski, com perfis filosóficos, psicológicos e religiosos.

---

## 📋 Requisitos Atendidos

1. **Back-end (API)**:
   - Implementação em Python com Flask.
   - Banco de Dados SQLite com tabela de usuários.
   - Rotas documentadas e funcionalidade de CRUD.
   - Documentação Swagger disponível.

---

## 🛠️ Instalação e Configuração

### **1. API (Back-end)**

#### Requisitos
- Python 3.9+
- Virtualenv ou Pipenv (opcional para criar ambiente isolado)

#### Passos
1. Clone o repositório da API:
   ```bash
   git clone https://github.com/usuario/projeto-api.git
   cd projeto-api

###  Estrutura do Código
    API:
    ├── app.py: Arquivo principal contendo as rotas da aplicação.
    ├── models.py: Modelos da tabela de usuários e conexão com o SQLite.
    ├── config.py: Configurações da aplicação.
    └── requirements.txt: Dependências do projeto.

### Instalar Dependências
    pip install Flask Flask-SQLAlchemy

### No terminal Bash, execute:
    Usar o Script de Ativação no Bash
    source **activate
    Isso ativará o ambiente virtual no Bash.
    O (venv) no início da linha indica que o ambiente virtual foi ativado.

### Verifique os Arquivos
    ls
    **Certifique-se de que os arquivos do projeto (app.py, models.py, etc.) estão no diretório.

### Rodar o Projeto
    Inicie o servidor Flask:
    **python app.py
    Se tudo estiver configurado corretamente, você verá uma mensagem como:

    