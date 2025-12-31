import os
import shutil

# Pasta que será organizada
PASTA_ORIGEM = os.path.expanduser("~/Downloads")

# Caminhos das bibliotecas padrão
DESTINOS = {
    "imagens": os.path.expanduser("~/Pictures"),
    "videos": os.path.expanduser("~/Videos"),
    "musicas": os.path.expanduser("~/Music"),
    "documentos": os.path.expanduser("~/Documents"),
    "outros": os.path.expanduser("~/Documents/Outros")
}

# Extensões por categoria
EXTENSOES = {
    "imagens": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "videos": [".mp4", ".mkv", ".avi", ".mov"],
    "musicas": [".mp3", ".wav", ".flac"],
    "documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"]
}

# Cria pastas se não existirem
for pasta in DESTINOS.values():
    os.makedirs(pasta, exist_ok=True)

# Organiza os arquivos
for arquivo in os.listdir(PASTA_ORIGEM):
    caminho = os.path.join(PASTA_ORIGEM, arquivo)

    if not os.path.isfile(caminho):
        continue

    extensao = os.path.splitext(arquivo)[1].lower()
    movido = False

    for categoria, extensoes in EXTENSOES.items():
        if extensao in extensoes:
            shutil.move(caminho, DESTINOS[categoria])
            movido = True
            break

    if not movido:
        shutil.move(caminho, DESTINOS["outros"])

print("Organização concluída com sucesso!")
