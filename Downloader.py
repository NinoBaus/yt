import requests
from bs4 import BeautifulSoup as Soup
# import youtube_dl
import os
import time
# from __future__ import unicode_literals
from sys import argv




# with requests.session() as s:
#     play_list = s.get('https://www.youtube.com/playlist?list=PLS4c1i4S5UCnXbIQJpZhoCiECB3z09n6L')
#     supa = Soup(play_list.text , 'html.parser')
#     linkovi = supa.findAll('a' , href=True)
#     pesme = []
#     for l in linkovi:
#         if '/watch' not in str(l):
#             pass
#         elif 'index' not in str(l):
#             pass
#         else:
#             link = l['href']
#             full_link = 'https://www.youtube.com' + link
#             pesme.append(full_link)
#
#     # full_lista = set(pesme)
# full_lista = ('https://www.youtube.com/playlist?list=PLS4c1i4S5UCkFbaSqfczByyH4qPGwSgZG',)
#     # for l in full_lista:
#     #     print(l)
#     # print(set(pesme))



# def index_finder(youtube_list):
#     try:
#         with requests.session() as s:
#             play_list = s.get(youtube_list[0])
#             supa = Soup(play_list.text , 'html.parser')
#             index_finder = supa.findAll('a' , href=True)
#             pesme = []
#             for l in index_finder:
#                 if '/watch' not in str(l):
#                     pass
#                 elif 'index' not in str(l):
#                     pass
#                 else:
#                     link = l['href']
#                     full_link = 'https://www.youtube.com' + link
#                     pesme.append(full_link)
#             index = set(pesme)
#             return len(index)
#     except Exception as e:
#         print(e)
#         pass


def downloader(youtube_list , direct):
    import youtube_dl
    try:
        #audio
        # download_options = {
        #     'ignoreerrors': True,
        #     'format': "bestaudio/best",
        #     'outtmpl': "%(title)s.%(ext)s",
        #     'nocheckcertificate': True,
        #     'postprocessors': [{
        #         'key': 'FFmpegExtractAudio',
        #         'preferredcodec': 'mp3',
        #         'preferredquality': '320'
        #     }]
        # }
        #video
        download_options = {
            'ignoreerrors': True,
            'format': "bestvideo[height=480][ext=mp4]+bestaudio[ext=m4a]",
            'outtmpl': "%(title)s.%(ext)s",
            'nocheckcertificate': True
            # 'postprocessors': [{
            #     'key': 'FFmpegExtractAudio',
            #     'preferredcodec': 'mp3',
            #     'preferredquality': '320'
            # }]

        }
        if not os.path.exists(direct):
            os.mkdir(direct)
            os.chdir(direct)
        else:
            os.chdir(direct)

        #Download songs

        with youtube_dl.YoutubeDL(download_options) as dl:
            try:
                dl.download([youtube_list])
            except Exception as e:
                print("Buguvanje: " + str(e))
    except Exception as e:
        print("Bug :" + str(e))
        pass




# test = ('https://www.youtube.com/watch?v=Css4GfsHrWA' , )
t = 'https://www.youtube.com/watch?v=vLPKXSdFSfM&list=UUqYgxBwP0I0O8A52O6qEOrw'
downloader(t , "Video")