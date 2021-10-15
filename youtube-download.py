from pytube import YouTube
from pytube import Playlist
from pytube import Channel
from pytube.cli import on_progress

def opcao1():

    print("Para baixar um vídeo do YouTube")
    link = input("Informe a URL do seu vídeo:   ")
    yt = YouTube(link)
    print("Titulo: ", yt.title)
    print("Baixando...")
    baixando = yt.streams.get_highest_resolution()
    baixando.download()

def opcao2():
    print("Para baixar vídeos de uma Playlist do YouTube")

    linkplaylist = input("Informe a URL do seu vídeo:   ")
    p = Playlist(linkplaylist)
    print(f'Downloading: {p.title}')
    qtd = int(input("Informe quantos vídeos quer baixar dessa playlist: "))
    for video in p.videos[:qtd]:
        print("Baixando...", {p.title})
        video.streams.first().download()
    print("Download de", qtd, " vídeos concluído!")

def opcao3():
    print("Para baixar vídeos de um Channel do YouTube")

    linkchannel = input("Informe a URL do seu vídeo:   ")
    c = Channel(linkchannel)
    print(f'Downloading: {c.channel_name}')
    qtd = int(input("Informe quantos vídeos quer baixar dessa playlist: "))
    for video in c.videos[:qtd]:
        video.streams.first().download()
    print("Download de",qtd, " vídeos concluído!")

opcoes = { 1:opcao1, 2:opcao2, 3:opcao3}


escolha = int(input("Digite 1 download simples, 2 para download de uma playlist ou 3 para download de um canal \n"))
opcoes.get(escolha)()
