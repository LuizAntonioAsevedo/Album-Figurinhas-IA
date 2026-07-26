from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse

app = FastAPI(
    title="Álbum de Figurinhas IA",
    description="API para gerenciamento do Álbum de Figurinhas IA.",
    version="1.0.0"
)

figurinhas = [
    {"id": 1, "nome": "Alan Turing", "categoria": "IA", "imagem": "01-alan-turing.jpg"},
    {"id": 2, "nome": "John McCarthy", "categoria": "IA", "imagem": "02-john-mccarthy.jpg"},
    {"id": 3, "nome": "Sam Altman", "categoria": "IA", "imagem": "03-sam-altman.jpg"},
    {"id": 4, "nome": "Geoffrey Hinton", "categoria": "IA", "imagem": "04-geoffrey-hinton.jpg"},
    {"id": 5, "nome": "Yann LeCun", "categoria": "IA", "imagem": "05-yann-lecun.jpg"},

    {"id": 6, "nome": "Guido van Rossum", "categoria": "Python", "imagem": "06-guido-van-rossum.jpg"},
    {"id": 7, "nome": "Tim Peters", "categoria": "Python", "imagem": "07-tim-peters.jpg"},
    {"id": 8, "nome": "Raymond Hettinger", "categoria": "Python", "imagem": "08-raymond-hettinger.jpg"},
    {"id": 9, "nome": "Travis Oliphant", "categoria": "Python", "imagem": "09-travis-oliphant.jpg"},
    {"id": 10, "nome": "Wes McKinney", "categoria": "Python", "imagem": "10-wes-mckinney.jpg"},

    {"id": 11, "nome": "Edgar F. Codd", "categoria": "Banco de Dados", "imagem": "11-edgar-codd.jpg"},
    {"id": 12, "nome": "Larry Ellison", "categoria": "Banco de Dados", "imagem": "12-larry-ellison.jpg"},
    {"id": 13, "nome": "Michael Widenius", "categoria": "Banco de Dados", "imagem": "13-michael-widenius.jpg"},
    {"id": 14, "nome": "Salvatore Sanfilippo", "categoria": "Banco de Dados", "imagem": "14-salvatore-sanfilippo.jpg"},
    {"id": 15, "nome": "Eliot Horowitz", "categoria": "Banco de Dados", "imagem": "15-eliot-horowitz.jpg"},

    {"id": 16, "nome": "Linus Torvalds", "categoria": "Sistemas Operacionais", "imagem": "16-linus-torvalds.jpg"},
    {"id": 17, "nome": "Dennis Ritchie", "categoria": "Sistemas Operacionais", "imagem": "17-dennis-ritchie.jpg"},
    {"id": 18, "nome": "Richard Stallman", "categoria": "Sistemas Operacionais", "imagem": "18-richard-stallman.jpg"},
    {"id": 19, "nome": "Bill Gates", "categoria": "Sistemas Operacionais", "imagem": "19-bill-gates.jpg"},
    {"id": 20, "nome": "Steve Jobs", "categoria": "Sistemas Operacionais", "imagem": "20-steve-jobs.jpg"},

    {"id": 21, "nome": "Paulo Silveira", "categoria": "Brasil", "imagem": "21-paulo-silveira.jpg"},
    {"id": 22, "nome": "Guilherme Silveira", "categoria": "Brasil", "imagem": "22-guilherme-silveira.jpg"},
    {"id": 23, "nome": "Gustavo Guanabara", "categoria": "Brasil", "imagem": "23-gustavo-guanabara.jpg"},
    {"id": 24, "nome": "Maurício Aniche", "categoria": "Brasil", "imagem": "24-mauricio-aniche.jpg"},
    {"id": 25, "nome": "Andre David", "categoria": "Brasil", "imagem": "25-andre-david.jpg"},
    {"id": 26, "nome": "Guilherme Lima", "categoria": "Brasil", "imagem": "26-guilherme-lima.jpg"},
    {"id": 27, "nome": "Gi Space Coding", "categoria": "Brasil", "imagem": "27-gi-space-coding.jpg"},
    {"id": 28, "nome": "Vinicius Neves", "categoria": "Brasil", "imagem": "28-vinicius-neves.jpg"},
    {"id": 29, "nome": "Rafaela Ballerini", "categoria": "Brasil", "imagem": "29-rafaela-ballerini.jpg"},
    {"id": 30, "nome": "Você", "categoria": "Brasil", "imagem": "30-voce.jpg"}
]

PASTA_FIGURINHAS = Path(__file__).parent / "figurinhas"


@app.get("/", summary="Página inicial", tags=["Home"])
def home():
    return {
        "mensagem": "Bem-vindo ao Álbum de Figurinhas IA!"
    }


@app.get("/figurinhas", summary="Listar figurinhas", tags=["Figurinhas"])
def listar_figurinhas():
    return figurinhas


@app.get("/figurinhas/{id}", summary="Buscar figurinha por ID", tags=["Figurinhas"])
def buscar_figurinha(id: int):

    for figurinha in figurinhas:
        if figurinha["id"] == id:
            return figurinha

    raise HTTPException(
        status_code=404,
        detail="Figurinha não encontrada."
    )


@app.get("/figurinhas/{id}/imagem", summary="Exibir imagem da figurinha", tags=["Figurinhas"])
def imagem_figurinha(id: int):

    figurinha = next(
        (f for f in figurinhas if f["id"] == id),
        None
    )

    if figurinha is None:
        raise HTTPException(
            status_code=404,
            detail="Figurinha não encontrada."
        )

    caminho = PASTA_FIGURINHAS / figurinha["imagem"]

    if not caminho.exists():
        raise HTTPException(
            status_code=404,
            detail="Arquivo de imagem não encontrado."
        )

    return FileResponse(caminho)