# Server Status Checker

Um sistema simples para monitoramento de aplicações HTTP/HTTPS, que verifica periodicamente se as aplicações estão online.

## Avisos
- Este projeto foi criado apenas para **fins de estudos** e prática em desenvolvimento.
- Este projeto foi criado para rodar localmente, com apenas um superusuário e uma Setting

## Sumário
- [Funcionalidades](#funcionalidades)
- [Tecnologias utilizadas](#tecnologias-utilizadas)
- [Instalação](#instalação)
- [Como usar](#como-usar)
- [Autor](#autor)

---
## Funcionalidades
  - Cadastro de aplicações para monitoramento
  - Checagem automática utilizando **APScheduler**
  - Registro do tempo de resposta, status code HTTP e erros
  - Histórico de logs para consulta
  - Gerenciamento e visualização via **Django Admin**

---
## Tecnologias utilizadas
  - Python 3.12
  - Django 5.2
  - Python-dotenv 1.1
  - APScheduler 3.11
  - Requests 2.32
  - SQLite3

---
## Instalação
### Clone o repositório
```bash
  git clone https://github.com/Everton-Renan/server-status-checker
  cd server-status-checker
```
### Crie um ambiente virtual e instale as dependências
```bash
  python -m venv venv

  source venv/bin/activate # No Linux/Mac
  venv\Scripts\activate # No Windows

  pip install -r requirements.txt
```

### Aplique as migrações do Django
```bash
  python manage.py migrate
```

### Crie um superusuário para acessar o Django Admin
```bash
  python manage.py createsuperuser
```

### Renomeie o arquivo .env-example para .env e configure o valor da sua SECRET-KEY
```bash
  SECRET-KEY="Sua chave"
```

### Inicie o servidor
```bash
  python manage.py runserver
```

### Como usar
  - Acesse a url http://127.0.0.1:8000/
  - Crie uma Settings (model) definindo o intervalo de checagem (em segundos)
  - Cadastre as aplicações para o monitoramento
  - Consulte os logs gerados automaticamente

## Autor
Desenvolvido por Everton Renan
