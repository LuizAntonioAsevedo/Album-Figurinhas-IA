from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse

app = FastAPI(
    title="Álbum de Figurinhas IA",
    description="API para gerenciamento do Álbum de Figurinhas IA.",
    version="1.0.0"
)

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
    {"id": 30, "nome": "Você", "categoria": "Brasil"}
]

PASTA_FIGURINHAS = Path(__file__).parent / "figurinhas"

IMAGENS = {
    1: "01-alan-turing.jpg"
}


@app.get(
    "/",
    summary="Página inicial",
    tags=["Home"]
)
def home():
    return {
        "mensagem": "Bem-vindo ao Álbum de Figurinhas IA!"
    }


@app.get(
    "/figurinhas",
    summary="Listar figurinhas",
    tags=["Figurinhas"]
)
def listar_figurinhas():
    return figurinhas


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


@app.get(
    "/figurinhas/{id}/imagem",
    summary="Exibir imagem da figurinha",
    tags=["Figurinhas"]
)
def imagem_figurinha(id: int):

    if id not in IMAGENS:
        raise HTTPException(
            status_code=404,
            detail="Imagem não encontrada."
        )

    caminho_imagem = PASTA_FIGURINHAS / IMAGENS[id]

    if not caminho_imagem.exists():
        raise HTTPException(
            status_code=404,
            detail="Arquivo de imagem não encontrado."
        )

    return FileResponse(caminho_imagem)