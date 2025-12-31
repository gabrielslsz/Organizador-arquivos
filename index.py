import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox


DESTINOS = {
    "imagens": os.path.expanduser("~/Pictures"),
    "videos": os.path.expanduser("~/Videos"),
    "musicas": os.path.expanduser("~/Music"),
    "documentos": os.path.expanduser("~/Documents"),
    "outros": os.path.expanduser("~/Documents/Outros")
}

EXTENSOES = {
    "imagens": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "videos": [".mp4", ".mkv", ".avi", ".mov"],
    "musicas": [".mp3", ".wav", ".flac"],
    "documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"]
}

IGNORAR = {"desktop.ini"}


def mover_com_nome_unico(origem, destino):
    """Evita erro se arquivo já existir"""
    nome, ext = os.path.splitext(os.path.basename(origem))
    contador = 1
    novo_caminho = os.path.join(destino, nome + ext)

    while os.path.exists(novo_caminho):
        novo_caminho = os.path.join(destino, f"{nome}_{contador}{ext}")
        contador += 1

    shutil.move(origem, novo_caminho)


def organizar_pasta():
    pasta = filedialog.askdirectory(title="Selecione a pasta para organizar")

    if not pasta:
        return

    for destino in DESTINOS.values():
        os.makedirs(destino, exist_ok=True)

    arquivos_movidos = 0

    for arquivo in os.listdir(pasta):
        if arquivo.lower() in IGNORAR:
            continue

        caminho = os.path.join(pasta, arquivo)

        if not os.path.isfile(caminho):
            continue

        extensao = os.path.splitext(arquivo)[1].lower()
        movido = False

        for categoria, lista_ext in EXTENSOES.items():
            if extensao in lista_ext:
                mover_com_nome_unico(caminho, DESTINOS[categoria])
                movido = True
                arquivos_movidos += 1
                break

        if not movido:
            mover_com_nome_unico(caminho, DESTINOS["outros"])
            arquivos_movidos += 1

    messagebox.showinfo(
        "Finalizado",
        f"Organização concluída!\nArquivos movidos: {arquivos_movidos}"
    )


# Interface
janela = tk.Tk()
janela.title("Organizador de Arquivos")
janela.geometry("360x180")
janela.resizable(False, False)

titulo = tk.Label(
    janela,
    text="Organizador Automático de Arquivos",
    font=("Arial", 12, "bold")
)
titulo.pack(pady=15)

botao = tk.Button(
    janela,
    text="Selecionar pasta e organizar",
    command=organizar_pasta,
    width=30,
    height=2
)
botao.pack(pady=20)

janela.mainloop()
