# 🏆 Álbum de Figurinhas IA

<p align="center">

  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/FastAPI-API-green?style=for-the-badge&logo=fastapi&logoColor=white">
  <img src="https://img.shields.io/badge/JavaScript-Frontend-yellow?style=for-the-badge&logo=javascript&logoColor=black">
  <img src="https://img.shields.io/badge/HTML5-Frontend-orange?style=for-the-badge&logo=html5&logoColor=white">
  <img src="https://img.shields.io/badge/CSS3-Design-blue?style=for-the-badge&logo=css3&logoColor=white">

</p>

<p align="center">

  <strong>Um álbum digital interativo com temática de Inteligência Artificial, programação, tecnologia e desenvolvimento.</strong>

</p>

---

## 📖 Sobre o projeto

O **Álbum de Figurinhas IA** é uma aplicação web desenvolvida durante a **Imersão Alura**, com o objetivo de unir programação, tecnologia e uma experiência visual interativa.

O projeto apresenta uma coleção de **31 figurinhas**, reunindo personalidades importantes das áreas de:

- 🤖 Inteligência Artificial
- 🐍 Python
- 🗄️ Banco de Dados
- 💻 Sistemas Operacionais
- 🇧🇷 Tecnologia e programação no Brasil
- 👨‍💻 Programação

A aplicação possui um álbum digital com capa, páginas duplas, navegação entre páginas e fechamento automático ao chegar ao final da coleção.

---

# 🎯 Objetivos

O projeto foi desenvolvido com os seguintes objetivos:

- Praticar desenvolvimento de aplicações web.
- Integrar frontend e backend.
- Criar uma API REST utilizando FastAPI.
- Trabalhar com JavaScript para manipulação dinâmica da interface.
- Utilizar HTML5 e CSS3 para construção da interface.
- Trabalhar com arquivos e imagens no backend.
- Aprender conceitos de organização de projetos.
- Utilizar Git e GitHub para versionamento.
- Criar um projeto completo para portfólio.

---

# ✨ Funcionalidades

## 📕 Álbum digital

- Capa do álbum.
- Animação de abertura.
- Animação de fechamento.
- Navegação entre páginas.
- Visualização de duas páginas simultaneamente.
- Indicador da página atual.
- Botão **Anterior**.
- Botão **Próxima**.
- Botão **Fechar álbum** na última abertura.
- Retorno automático para a capa.

## 🖼️ Figurinhas

O álbum possui atualmente **31 figurinhas**.

### 🤖 Inteligência Artificial

| Nº | Nome |
|---:|---|
| 01 | Alan Turing |
| 02 | John McCarthy |
| 03 | Sam Altman |
| 04 | Geoffrey Hinton |
| 05 | Yann LeCun |

### 🐍 Python

| Nº | Nome |
|---:|---|
| 06 | Guido van Rossum |
| 07 | Tim Peters |
| 08 | Raymond Hettinger |
| 09 | Travis Oliphant |
| 10 | Wes McKinney |

### 🗄️ Banco de Dados

| Nº | Nome |
|---:|---|
| 11 | Edgar F. Codd |
| 12 | Larry Ellison |
| 13 | Michael Widenius |
| 14 | Salvatore Sanfilippo |
| 15 | Eliot Horowitz |

### 💻 Sistemas Operacionais

| Nº | Nome |
|---:|---|
| 16 | Linus Torvalds |
| 17 | Dennis Ritchie |
| 18 | Richard Stallman |
| 19 | Bill Gates |
| 20 | Steve Jobs |

### 🇧🇷 Brasil

| Nº | Nome |
|---:|---|
| 21 | Paulo Silveira |
| 22 | Guilherme Silveira |
| 23 | Gustavo Guanabara |
| 24 | Maurício Aniche |
| 25 | Andre David |
| 26 | Guilherme Lima |
| 27 | Gi Space Coding |
| 28 | Vinicius Neves |
| 29 | Rafaela Ballerini |
| 30 | Luiz Asevedo |
| 31 | Luiz |

---

# 🛠️ Tecnologias utilizadas

## Backend

- Python
- FastAPI
- Uvicorn
- Pydantic
- Python Multipart
- CORS
- API REST

## Frontend

- HTML5
- CSS3
- JavaScript
- Fetch API
- Manipulação do DOM
- CSS Transitions
- CSS Transformations

## Ferramentas

- Visual Studio Code
- Git
- GitHub
- PowerShell
- Navegador Google Chrome

---

# 🏗️ Arquitetura do projeto

O projeto está dividido em duas partes principais:

```text
ALBUM-FIGURINHAS-IA
│
├── Backend
│   │
│   ├── figurinhas/
│   │   ├── 01-alan-turing.jpg
│   │   ├── 02-john-mccarthy.jpg
│   │   ├── ...
│   │   ├── 30-luiz-asevedo.jpg
│   │   └── 31-Luiz.jpg
│   │
│   ├── main.py
│   ├── requirements.txt
│   └── .gitignore
│
├── Frontend
│   │
│   ├── index.html
│   ├── app.js
│   └── style.css
│
├── .gitignore
├── LICENSE
└── README.md

🔌 API

O backend foi desenvolvido utilizando FastAPI.

Página inicial

GET /

Retorna:

{
  "mensagem": "Bem-vindo ao Álbum de Figurinhas IA!"
}

Listar figurinhas

GET /figurinhas

Retorna a coleção de figurinhas cadastradas.

Buscar figurinha

GET /figurinhas/{id}

Exemplo:

GET /figurinhas/1

Exibir imagem

GET /figurinhas/{id}/imagem

Exemplo:

GET /figurinhas/1/imagem

Cadastrar figurinha

POST /figurinhas

Enviar imagem

POST /figurinhas/{id}/imagem

🚀 Como executar o projeto

1. Clonar o repositório

git clone https://github.com/LuizAntonioAsevedo/Album-Figurinhas-IA.git

Entrar na pasta:

cd Album-Figurinhas-IA

🐍 Backend

Entrar na pasta:

cd Backend

Criar o ambiente virtual:

python -m venv .venv

Ativar o ambiente virtual no Windows:

.venv\Scripts\Activate.ps1

Instalar as dependências:

pip install -r requirements.txt

Iniciar o servidor:

python -m uvicorn main:app --reload --port 8001

O backend ficará disponível em:

http://127.0.0.1:8001

📚 Documentação da API

O FastAPI disponibiliza automaticamente a documentação interativa.

Acesse:

http://127.0.0.1:8001/docs

A documentação permite testar diretamente os endpoints da API.

🌐 Frontend

Abra um segundo terminal.

Entre na pasta:

cd Frontend

Execute:

python -m http.server 5500

A aplicação ficará disponível em:

http://localhost:5500

🔄 Funcionamento

O fluxo básico da aplicação é:

                  ┌───────────────────┐
                  │      USUÁRIO      │
                  └─────────┬─────────┘
                            │
                            ▼
                  ┌───────────────────┐
                  │     FRONTEND      │
                  │ HTML + CSS + JS   │
                  └─────────┬─────────┘
                            │
                            │ HTTP
                            ▼
                  ┌───────────────────┐
                  │      FASTAPI      │
                  │      BACKEND      │
                  └─────────┬─────────┘
                            │
                            ▼
                  ┌───────────────────┐
                  │    FIGURINHAS     │
                  │     /figurinhas   │
                  └───────────────────┘

🎬 Experiência do álbum

A aplicação possui uma navegação baseada em páginas duplas:

┌─────────────────┬─────────────────┐
│                 │                 │
│    Página 1     │    Página 2     │
│                 │                 │
└─────────────────┴─────────────────┘

              ↓ Próxima

┌─────────────────┬─────────────────┐
│                 │                 │
│    Página 3     │    Página 4     │
│                 │                 │
└─────────────────┴─────────────────┘

              ↓ Próxima

                 ...

              ↓

┌─────────────────┬─────────────────┐
│    Página 7     │    Página 8     │
│                 │                 │
│                 │   ÚLTIMA        │
└─────────────────┴─────────────────┘

              ↓

          Fechar álbum

Ao chegar à última abertura, o botão muda automaticamente para:

Fechar álbum

Após o fechamento, o usuário retorna à capa.

# 📸 Demonstração

## 📕 Capa do álbum

<p align="center">
  <img src="assets/capa.png" alt="Capa do Álbum de Figurinhas IA" width="800">
</p>

---

## 📖 Álbum aberto

<p align="center">
  <img src="assets/album-aberto.png" alt="Álbum de Figurinhas IA aberto" width="800">
</p>

---

## 🖼️ Coleção de figurinhas

<p align="center">
  <img src="assets/colecao.png" alt="Coleção de Figurinhas IA" width="800">
</p>

📌 Status do projeto

Versão 1.0 — Concluída ✅
 Backend FastAPI
 API REST
 Frontend HTML
 CSS
 JavaScript
 Cadastro das figurinhas
 Carregamento das imagens
 Álbum digital
 Navegação entre páginas
 Página dupla
 Fechamento automático
 Retorno para a capa
 Git
 GitHub
 Primeiro commit
 Versionamento da versão 1.0

🔮 Próximas melhorias

O projeto continuará evoluindo.

Possíveis próximas etapas:

 Adicionar screenshots ao README
 Criar GIF demonstrativo
 Melhorar responsividade para celulares
 Criar sistema de coleção de figurinhas
 Identificar figurinhas já visualizadas
 Adicionar busca por nome
 Adicionar filtro por categoria
 Criar banco de dados real
 Implementar cadastro persistente
 Criar sistema de autenticação
 Publicar a aplicação online
 Criar Release oficial no GitHub

🎓 Aprendizados

Durante o desenvolvimento deste projeto foram praticados conceitos de:

Desenvolvimento de API REST.
FastAPI.
Python.
Pydantic.
Uvicorn.
CORS.
HTML.
CSS.
JavaScript.
Fetch API.
Manipulação do DOM.
Animações CSS.
Integração frontend/backend.
Organização de projetos.
Git.
GitHub.
Versionamento de código.

👨‍💻 Autor
Luiz Antonio Asevedo

Projeto desenvolvido como parte da jornada de aprendizado em programação, inteligência artificial e desenvolvimento de aplicações.

📍 São Paulo — SP

📄 Licença

Este projeto está disponibilizado sob a licença definida no arquivo:

LICENSE



