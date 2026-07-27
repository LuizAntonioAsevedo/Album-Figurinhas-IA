from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from pathlib import Path
import shutil


app = FastAPI(
    title="Álbum de Figurinhas IA",
    description="API para gerenciamento do Álbum de Figurinhas IA.",
    version="1.0.0"
)


# ============================================================
# CORS
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5500",
        "http://127.0.0.1:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# CONFIGURAÇÃO DAS IMAGENS
# ============================================================

PASTA_FIGURINHAS = Path("figurinhas")

PASTA_FIGURINHAS.mkdir(
    exist_ok=True
)


# ============================================================
# MODELO DE DADOS
# ============================================================

class Figurinha(BaseModel):
    nome: str
    categoria: str


# ============================================================
# BANCO DE DADOS TEMPORÁRIO
# ============================================================

figurinhas = [
    {"id": 1, "nome": "Alan Turing", "categoria": "IA"},
    {"id": 2, "nome": "John McCarthy", "categoria": "IA"},
    {"id": 3, "nome": "Sam Altman", "categoria": "IA"},
    {"id": 4, "nome": "Geoffrey Hinton", "categoria": "IA"},
    {"id": 5, "nome": "Yann LeCun", "categoria": "IA"},

    {"id": 6, "nome": "Guido van Rossum", "categoria": "Python"},
    {"id": 7, "nome": "Tim Peters", "categoria": "Python"},
    {"id": 8, "nome": "Raymond Hettinger", "categoria": "Python"},
    {"id": 9, "nome": "Travis Oliphant", "categoria": "Python"},
    {"id": 10, "nome": "Wes McKinney", "categoria": "Python"},

    {"id": 11, "nome": "Edgar F. Codd", "categoria": "Banco de Dados"},
    {"id": 12, "nome": "Larry Ellison", "categoria": "Banco de Dados"},
    {"id": 13, "nome": "Michael Widenius", "categoria": "Banco de Dados"},
    {"id": 14, "nome": "Salvatore Sanfilippo", "categoria": "Banco de Dados"},
    {"id": 15, "nome": "Eliot Horowitz", "categoria": "Banco de Dados"},

    {"id": 16, "nome": "Linus Torvalds", "categoria": "Sistemas Operacionais"},
    {"id": 17, "nome": "Dennis Ritchie", "categoria": "Sistemas Operacionais"},
    {"id": 18, "nome": "Richard Stallman", "categoria": "Sistemas Operacionais"},
    {"id": 19, "nome": "Bill Gates", "categoria": "Sistemas Operacionais"},
    {"id": 20, "nome": "Steve Jobs", "categoria": "Sistemas Operacionais"},

    {"id": 21, "nome": "Paulo Silveira", "categoria": "Brasil"},
    {"id": 22, "nome": "Guilherme Silveira", "categoria": "Brasil"},
    {"id": 23, "nome": "Gustavo Guanabara", "categoria": "Brasil"},
    {"id": 24, "nome": "Maurício Aniche", "categoria": "Brasil"},
    {"id": 25, "nome": "Andre David", "categoria": "Brasil"},
    {"id": 26, "nome": "Guilherme Lima", "categoria": "Brasil"},
    {"id": 27, "nome": "Gi Space Coding", "categoria": "Brasil"},
    {"id": 28, "nome": "Vinicius Neves", "categoria": "Brasil"},
    {"id": 29, "nome": "Rafaela Ballerini", "categoria": "Brasil"},
    {"id": 30, "nome": "Luiz Asevedo", "categoria": "Brasil"},
    {"id": 31, "nome": "Luiz Asevedo", "categoria": "Brasil"}
]


# ============================================================
# PÁGINA INICIAL
# ============================================================

@app.get(
    "/",
    summary="Página inicial",
    tags=["Home"]
)
def home():
    return {
        "mensagem": "Bem-vindo ao Álbum de Figurinhas IA!"
    }


# ============================================================
# LISTAR FIGURINHAS
# ============================================================

@app.get(
    "/figurinhas",
    summary="Listar figurinhas",
    tags=["Figurinhas"]
)
def listar_figurinhas():
    return figurinhas


# ============================================================
# BUSCAR FIGURINHA POR ID
# ============================================================

@app.get(
    "/figurinhas/{id}",
    summary="Buscar figurinha por ID",
    tags=["Figurinhas"]
)
def buscar_figurinha(id: int):

    for figurinha in figurinhas:

        if figurinha["id"] == id:
            return figurinha

    raise HTTPException(
        status_code=404,
        detail="Figurinha não encontrada."
    )


# ============================================================
# CADASTRAR NOVA FIGURINHA
# ============================================================

@app.post(
    "/figurinhas",
    summary="Cadastrar nova figurinha",
    tags=["Figurinhas"]
)
def cadastrar_figurinha(figurinha: Figurinha):

    novo_id = max(
        item["id"]
        for item in figurinhas
    ) + 1

    nova_figurinha = {
        "id": novo_id,
        "nome": figurinha.nome,
        "categoria": figurinha.categoria
    }

    figurinhas.append(
        nova_figurinha
    )

    return nova_figurinha


# ============================================================
# ENVIAR IMAGEM DA FIGURINHA
# ============================================================

@app.post(
    "/figurinhas/{id}/imagem",
    summary="Enviar imagem da figurinha",
    tags=["Imagens"]
)
def enviar_imagem(
    id: int,
    arquivo: UploadFile = File(...)
):

    figurinha = None

    for item in figurinhas:

        if item["id"] == id:
            figurinha = item
            break

    if figurinha is None:

        raise HTTPException(
            status_code=404,
            detail="Figurinha não encontrada."
        )


    extensoes_permitidas = {
        ".jpg",
        ".jpeg",
        ".png",
        ".webp"
    }


    nome_original = Path(
        arquivo.filename
    ).name


    extensao = Path(
        nome_original
    ).suffix.lower()


    if extensao not in extensoes_permitidas:

        raise HTTPException(
            status_code=400,
            detail="Formato de imagem não permitido."
        )


    prefixo_id = f"{id:02d}-"


    if nome_original.startswith(prefixo_id):

        nome_arquivo = nome_original

    else:

        nome_arquivo = (
            f"{prefixo_id}"
            f"{nome_original}"
        )


    caminho = (
        PASTA_FIGURINHAS /
        nome_arquivo
    )


    with caminho.open("wb") as destino:

        shutil.copyfileobj(
            arquivo.file,
            destino
        )


    return {
        "mensagem": "Imagem enviada com sucesso.",
        "id": id,
        "arquivo": nome_arquivo
    }


# ============================================================
# EXIBIR IMAGEM DA FIGURINHA
# ============================================================

@app.get(
    "/figurinhas/{id}/imagem",
    summary="Exibir imagem da figurinha",
    tags=["Imagens"]
)
def imagem_figurinha(id: int):

    arquivos = list(
        PASTA_FIGURINHAS.glob(
            f"{id:02d}-*"
        )
    )


    if not arquivos:

        raise HTTPException(
            status_code=404,
            detail="Imagem da figurinha não encontrada."
        )


    return FileResponse(
        arquivos[0]
    )