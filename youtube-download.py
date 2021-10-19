import re
import os
import moviepy.editor as mp
from pytube import YouTube
from pytube import Playlist
from pytube import Channel


def opcao1():

    print("Para baixar um vídeo do YouTube")
    link = input("Informe a URL do seu vídeo:   ")
    yt = YouTube(link)
    download_type = int(input("\n1 - Para baixar o vídeo; \n2 - Para baixar apenas o audio (.MP3).\n -> "))

    if (download_type == 1):
        print(f'Downloading {yt.title} WAIT')
        baixando = yt.streams.get_highest_resolution()
        baixando.download()

    elif (download_type == 2):
        print(f'Downloading {yt.title} WAIT')
        baixando = yt.streams.filter(only_audio=True)
        baixando[0].download('temp') 
        folder = "temp"
        for file in os.listdir(folder):
            if re.search('mp4', file):
                mp4_path = os.path.join(folder,file)
                mp3_path = os.path.join('.',os.path.splitext(file)[0]+'.mp3')
                new_file = mp.AudioFileClip(mp4_path)
                new_file.write_audiofile(mp3_path)
                os.remove(mp4_path)

    else:
        print("OPAÇÃO INVALIDA, TENTE NOVAMENTE")        
        

def opcao2():

    print("Para baixar vídeos de uma Playlist do YouTube\n")
    print("-- ATENÇÃO --\nPara baixar vídeos de uma playlist a URL deve ter o seguinte formato:\nhttps://www.youtube.com/playlist?list=ID_PLAYLIST\n")
    linkplaylist = input("Informe a URL da sua Playlist:   ")
    p = Playlist(linkplaylist)
    download_type = int(input("\n1 - Para baixar os vídeos; \n2 - Para baixar apenas os audios (.MP3).\n -> "))

    if (download_type == 1):
        print(f'Playlist name: {p.title}')
        qtd = int(input("Informe quantos vídeos quer baixar dessa playlist: "))
        for video in p.videos[:qtd]:
            print(f'Downloading {p.title} WAIT')
            video.streams.first().download()
        print("Download de", qtd, " vídeos concluído!")

    elif (download_type == 2):
        print(f'Playlist name: {p.title}')
        qtd = int(input("Informe quantos vídeos quer baixar dessa playlist: "))
        for video in p.videos[:qtd]:
            print(f'Downloading {p.title} WAIT')
            video.streams.first().download('temp')
            convertendo()
        print("Download de", qtd, "vídeos concluído!")
    
    else:
        print("OPAÇÃO INVALIDA, TENTE NOVAMENTE")
        

def opcao3():

    print("Para baixar vídeos de um Channel do YouTube\n")
    print("-- ATENÇÃO --\nPara baixar vídeos de uma playlist a URL deve ter o seguinte formato:\nhhttps://www.youtube.com/c/CHANNEL_NAME\n")
    linkchannel = input("Informe a URL do seu vídeo:   ")
    c = Channel(linkchannel)
    download_type = int(input("\n1 - Para baixar os vídeos; \n2 - Para baixar apenas os audios (.MP3).\n -> "))

    if (download_type == 1):
        print(f'Downloading: {c.channel_name}')
        qtd = int(input("Informe quantos vídeos quer baixar desse canal: "))
        for video in c.videos[:qtd]:
            print(f'Downloading {c.channel_name} WAIT')
            video.streams.first().download()
        print("Download de",qtd, " vídeos concluído!")

    elif (download_type == 2):
        print(f'Downloading: {c.channel_name}')
        qtd = int(input("Informe quantos vídeos quer baixar desse canal: "))
        for video in c.videos[:qtd]:
            print(f'Downloading {c.channel_name} WAIT')
            video.streams.first().download('temp')
            convertendo()
        print("Download de", qtd, "vídeos concluído!")

    else:
        print("OPAÇÃO INVALIDA, TENTE NOVAMENTE")


def convertendo():
    
    folder = "temp"
    for file in os.listdir(folder):
        if re.search('3gpp', file):
            temp_path = os.path.join(folder, file)
            root_path = os.path.join('.', os.path.splitext(file)[0]+'.mp3')
            new_file = mp.AudioFileClip(temp_path)
            new_file.write_audiofile(root_path)
            os.remove(temp_path)

opcoes = { 1:opcao1, 2:opcao2, 3:opcao3}

escolha = int(input("\n--> Escolha uma opção <-- \n 1 - Download simples; \n 2 - Para download de uma playlist; \n 3 - Para download de um canal. \n-> "))
opcoes.get(escolha)()
