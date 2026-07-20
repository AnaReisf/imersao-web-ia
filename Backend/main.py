# pyrefly: ignore [missing-import]
import os
# pyrefly: ignore [missing-import]
import glob
# pyrefly: ignore [missing-import]
from fastapi import FastAPI, HTTPException
# pyrefly: ignore [missing-import]
from fastapi.responses import FileResponse
# pyrefly: ignore [missing-import]
from fastapi.middleware.cors import CORSMiddleware

# Cria a instância principal da aplicação FastAPI
app = FastAPI()

# Configura o middleware CORS para aceitar requisições de qualquer origem
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define o caminho absoluto da pasta de imagens (para encontrar a pasta independente de onde for executado)
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

# Lista de figurinhas cadastradas (todas as 40 figurinhas do álbum)
# Deixamos ativas apenas as figurinhas cujas imagens existem na pasta figurinhas/
# Como todas as 40 imagens existem, mantemos todas ativas.
figurinhas = [
    {"id": 1, "nome": "Harry Potter", "categoria": "Grifinória", "imagem_url": "/figurinhas/1/imagem"},
    {"id": 2, "nome": "Alvo Dumbledore", "categoria": "Grifinória", "imagem_url": "/figurinhas/2/imagem"},
    {"id": 3, "nome": "Godric Gryffindor", "categoria": "Grifinória", "imagem_url": "/figurinhas/3/imagem"},
    {"id": 4, "nome": "Hermione Granger", "categoria": "Grifinória", "imagem_url": "/figurinhas/4/imagem"},
    {"id": 5, "nome": "Rony Weasley", "categoria": "Grifinória", "imagem_url": "/figurinhas/5/imagem"},
    {"id": 6, "nome": "Lord Voldemort", "categoria": "Sonserina", "imagem_url": "/figurinhas/6/imagem"},
    {"id": 7, "nome": "Severo Snape", "categoria": "Sonserina", "imagem_url": "/figurinhas/7/imagem"},
    {"id": 8, "nome": "Salazar Slytherin", "categoria": "Sonserina", "imagem_url": "/figurinhas/8/imagem"},
    {"id": 9, "nome": "Draco Malfoy", "categoria": "Sonserina", "imagem_url": "/figurinhas/9/imagem"},
    {"id": 10, "nome": "Belatriz Lestrange", "categoria": "Sonserina", "imagem_url": "/figurinhas/10/imagem"},
    {"id": 11, "nome": "Luna Lovegood", "categoria": "Corvinal", "imagem_url": "/figurinhas/11/imagem"},
    {"id": 12, "nome": "Cho Chang", "categoria": "Corvinal", "imagem_url": "/figurinhas/12/imagem"},
    {"id": 13, "nome": "Rowena Ravenclaw", "categoria": "Corvinal", "imagem_url": "/figurinhas/13/imagem"},
    {"id": 14, "nome": "Professor Flitwick", "categoria": "Corvinal", "imagem_url": "/figurinhas/14/imagem"},
    {"id": 15, "nome": "Dama Cinzenta", "categoria": "Corvinal", "imagem_url": "/figurinhas/15/imagem"},
    {"id": 16, "nome": "Newton Scamander", "categoria": "Lufa-Lufa", "imagem_url": "/figurinhas/16/imagem"},
    {"id": 17, "nome": "Pomona Sprout", "categoria": "Lufa-Lufa", "imagem_url": "/figurinhas/17/imagem"},
    {"id": 18, "nome": "Helga Hufflepuff", "categoria": "Lufa-Lufa", "imagem_url": "/figurinhas/18/imagem"},
    {"id": 19, "nome": "Cedrico Diggory", "categoria": "Lufa-Lufa", "imagem_url": "/figurinhas/19/imagem"},
    {"id": 20, "nome": "Ministro Grogan Stump", "categoria": "Lufa-Lufa", "imagem_url": "/figurinhas/20/imagem"},
    {"id": 21, "nome": "Minerva McGonagall", "categoria": "Professores e Funcionários", "imagem_url": "/figurinhas/21/imagem"},
    {"id": 22, "nome": "Remo Lupin", "categoria": "Professores e Funcionários", "imagem_url": "/figurinhas/22/imagem"},
    {"id": 23, "nome": "Rúbeo Hagrid", "categoria": "Professores e Funcionários", "imagem_url": "/figurinhas/23/imagem"},
    {"id": 24, "nome": "Gilderoy Lockhart", "categoria": "Professores e Funcionários", "imagem_url": "/figurinhas/24/imagem"},
    {"id": 25, "nome": "Alastor Moody", "categoria": "Professores e Funcionários", "imagem_url": "/figurinhas/25/imagem"},
    {"id": 26, "nome": "Bichento", "categoria": "Criaturas Mágicas", "imagem_url": "/figurinhas/26/imagem"},
    {"id": 27, "nome": "Edwigis", "categoria": "Criaturas Mágicas", "imagem_url": "/figurinhas/27/imagem"},
    {"id": 28, "nome": "Dobby", "categoria": "Criaturas Mágicas", "imagem_url": "/figurinhas/28/imagem"},
    {"id": 29, "nome": "Biguço", "categoria": "Criaturas Mágicas", "imagem_url": "/figurinhas/29/imagem"},
    {"id": 30, "nome": "Fawkes", "categoria": "Criaturas Mágicas", "imagem_url": "/figurinhas/30/imagem"},
    {"id": 31, "nome": "Sirius Black", "categoria": "Aliados", "imagem_url": "/figurinhas/31/imagem"},
    {"id": 32, "nome": "Gina Weasley", "categoria": "Aliados", "imagem_url": "/figurinhas/32/imagem"},
    {"id": 33, "nome": "Neville Longbottom", "categoria": "Aliados", "imagem_url": "/figurinhas/33/imagem"},
    {"id": 34, "nome": "Fred Weasley", "categoria": "Aliados", "imagem_url": "/figurinhas/34/imagem"},
    {"id": 35, "nome": "George Weasley", "categoria": "Aliados", "imagem_url": "/figurinhas/35/imagem"},
    {"id": 36, "nome": "Tiago Potter", "categoria": "Lendas & Você", "imagem_url": "/figurinhas/36/imagem"},
    {"id": 37, "nome": "Lílian Potter", "categoria": "Lendas & Você", "imagem_url": "/figurinhas/37/imagem"},
    {"id": 38, "nome": "Ninfadora Tonks", "categoria": "Lendas & Você", "imagem_url": "/figurinhas/38/imagem"},
    {"id": 39, "nome": "Quirino Quirrell", "categoria": "Lendas & Você", "imagem_url": "/figurinhas/39/imagem"},
    {"id": 40, "nome": "Você", "categoria": "Lendas & Você", "imagem_url": "/figurinhas/40/imagem"}
]

# Define a rota para obter a lista de figurinhas no caminho "/figurinhas"
@app.get("/figurinhas")
def listar_figurinhas():
    """
    Retorna a lista de todas as figurinhas disponíveis.
    """
    return figurinhas

# Define a rota para obter a imagem de uma figurinha pelo ID no caminho "/figurinhas/{id}/imagem"
@app.get("/figurinhas/{id}/imagem")
def obter_imagem_figurinha(id: int):
    """
    Busca o arquivo de imagem da figurinha na pasta figurinhas/
    usando glob para encontrar o prefixo {id:02d}[!0-9]*.
    """
    padrao = os.path.join(PASTA_IMAGENS, f"{id:02d}[!0-9]*")
    arquivos = glob.glob(padrao)
    
    # Se não encontrar nenhum arquivo que corresponda ao padrão, retorna 404
    if not arquivos:
        raise HTTPException(status_code=404, detail="Imagem não encontrada")
    
    # Retorna o arquivo de imagem encontrado
    return FileResponse(arquivos[0])
