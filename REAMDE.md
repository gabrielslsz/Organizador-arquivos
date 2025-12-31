# Organizador Automático de Arquivos em Python

Este projeto é um organizador automático de arquivos, desenvolvido em Python, que ajuda a manter pastas organizadas separando arquivos por tipo (imagens, vídeos, músicas, documentos etc.).

Ele possui interface gráfica simples, onde o usuário apenas seleciona a pasta desejada e o sistema faz todo o trabalho.

## Funcionalidades

Organiza arquivos automaticamente por extensão

Move arquivos para as bibliotecas padrão do Windows

Cria pastas automaticamente se não existirem

Ignora arquivos do sistema (como desktop.ini)

Evita sobrescrever arquivos duplicados

Renomeia automaticamente quando necessário

Interface gráfica simples com Tkinter

Compatível com Windows

## Organização realizada

Os arquivos são movidos para:

Imagens → .jpg, .jpeg, .png, .gif, .webp

Vídeos → .mp4, .mkv, .avi, .mov

Músicas → .mp3, .wav, .flac

Documentos → .pdf, .docx, .txt, .xlsx, .pptx

Outros → qualquer extensão não reconhecida

### Interface

O programa abre uma janela com um botão:

Selecionar pasta e organizar

Após escolher a pasta, os arquivos são organizados automaticamente e uma mensagem final confirma a conclusão.

### Tecnologias utilizadas

Python 3.10+

Tkinter (interface gráfica)

OS

Shutil

#### Como executar o projeto
#### Clone o repositório
git clone https://github.com/gabrielslsz/Organizador-arquivos.git

#### Acesse a pasta
cd organizador-arquivos

#### Execute o programa
python index.py


#### Certifique-se de estar usando o Python instalado no Windows (não WSL).

#### Estrutura do projeto
organizador-arquivos/
│
├── index.py
├── README.md

#### Comportamentos inteligentes

Se um arquivo já existir no destino, ele será renomeado automaticamente:

arquivo.pdf
arquivo_1.pdf
arquivo_2.pdf


Arquivos ocultos do sistema são ignorados.

#### Possíveis melhorias futuras

Criar versão .exe

Barra de progresso

Logs em arquivo .txt

Organização por data (Ano / Mês)

Interface mais moderna

Configuração personalizada por usuário

Versão Linux / WSL

Suporte a mais extensões

##### Autor

Gabriel Silva Sousa
Estudante de Análise e Desenvolvimento de Sistemas
Desenvolvedor Backend

Projeto criado com foco em aprendizado, organização pessoal e portfólio