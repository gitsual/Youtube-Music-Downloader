import pafy, pyglet
import urllib.request
import itertools
from urllib.parse import *
from bs4 import BeautifulSoup


class Youtube_mp3():
    def __init__(self):
        self.lst = []
        self.dict = {}
        self.dict_names = {}
        self.playlist = []

    def url_search(self, search_string, max_search):
        textToSearch = search_string
        query = urllib.parse.quote(textToSearch)
        url = "https://www.youtube.com/results?search_query=" + query
        response = urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'lxml')
        i = 1
        for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
            if len(self.dict) < max_search:
                self.dict[i] = 'https://www.youtube.com' + vid['href']
                i += 1
            else:
                break


    def get_search_items(self, max_search):

        if self.dict != {}:
            i = 1
            for url in self.dict.values():
                try:
                    info = pafy.new(url)
                    self.dict_names[i] = info.title
                    print("{0}. {1}".format(i, info.title))
                    i += 1

                except ValueError:
                    pass

    def download_media(self, num):
        url = self.dict[int(num)]
        info = pafy.new(url)
        audio = info.getbestaudio(preftype="m4a")
        song_name = self.dict_names[int(num)]
        print("Downloading: {0}.".format(self.dict_names[int(num)]))
        print(song_name)
        file_name = song_name + '.m4a'
        new_file_name = file_name.replace("/", " ")
        if song_name == '':
            audio.download(remux_audio=True)
        else:
            audio.download(filepath = new_file_name, remux_audio=True)


    def bulk_download(self, url):
        info = pafy.new(url)
        audio = info.getbestaudio(preftype="m4a")
        song_name = self.dict_names[int(num)]
        print("Downloading: {0}.".format(self.dict_names[int(num)]))
        print(song_name)
 #       file_name = song_name[:11] + '.m4a'
        file_name = song_name + '.m4a'
        new_file_name = file_name.replace("/", " ")
        if song_name == '':
            audio.download(remux_audio=True)
        else:
            audio.download(filepath = new_file_name, remux_audio=True)

    def add_playlist(self, search_query):
        url = self.url_search(search_query, max_search=1)
        self.playlist.append(url)





if __name__ == '__main__':
    print('Youtube Music Downloader')
    downloadList = open('../list-to-download.txt', 'r')
    downloadedList = open('downloaded.txt', 'r+')
    x = Youtube_mp3()
    for song in downloadList:
        alreadyDownloaded = False
        downloadedList.seek(0)
        for downloadedSong in downloadedList:
            if song==downloadedSong:
                alreadyDownloaded = True
                print("Already downloaded:\n\t" + song)
        if alreadyDownloaded == False:
            x.dict = {}
            x.dict_names = {}
            x.url_search(song, 1)
            valor = x.get_search_items(1)
            x.download_media(1)
            downloadedList.write(song)
