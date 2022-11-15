import requests # requests module 
from bs4 import BeautifulSoup # BeautifulSoup module 
import json # json module for getting json output 
import csv # csv module for storing data in .csv format
import re # regx module for 
from pytube import YouTube

class YouTubeCrawler:
    video_links = []
    channel_link = str(input("put your channel link: ")).lstrip().rstrip()
    base_url = 'https://www.youtube.com/watch?v='
    SAVE_PATH = "F:\youtube"
    '''#headers = {
        'authority': 'www.google.com'
        ,'accept-encoding': 'gzip, deflate, br'
        ,'accept-language': 'en-US,en;q=0.9'
        ,'cache-control': 'max-age=0'
        ,'sec-ch-ua-mobile': '?0'
        ,'sec-ch-ua-model': ""
        ,'sec-ch-ua-platform': "Windows"
        ,'sec-ch-ua-platform-version': "10.0.0"
        ,'sec-ch-ua-wow64': '?0'
        ,'sec-fetch-dest': 'document'
        ,'sec-fetch-mode': 'navigate'
        ,'sec-fetch-site': 'same-origin'
        ,'sec-fetch-user': '?1'
        ,'upgrade-insecure-requests': '1'
        ,'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}'''
    def videodownloader(self,link_list):
        for i in range(len(link_list)):
            try:
                yt=YouTube(f'{self.base_url}{link_list[i]}')
                print(yt.title)
            except:
                print("Connection while parsing video titles")
        video_no = input("Put Your Video No here! (for downloading all of videos write 'all')")
        if (str(video_no.strip().lower())) == "all":
                for i in range(len(link_list)):
                    try:
                        yt = YouTube(f'{self.base_url}{link_list[i]}')
                        print(yt.title)
                        try:
                            streams = yt.streams.filter(file_extension='mp4')
                            print(streams)
                            stream = yt.streams.get_by_itag(int(input("write the itag")))
                            print("Downloading... ... ... ")
                            stream.download()
                        except:
                            print("Error accoured while downloading")
                        print(f"{yt.title}'s Download Compeleted!")
                    except:
                        print("Error accoured while parsing the videos")
        else:
            try:
                yt = YouTube(f'{self.base_url}{link_list[int(video_no)-1]}')
                print(yt.title)
                try:
                    streams = yt.streams.filter(file_extension='mp4')
                    print(streams)
                    stream = yt.streams.get_by_itag(int(input("write the itag")))
                    print("Downloading... ... ... ")
                    stream.download()
                except:
                    print("Error Happend while downloading the single video")
                print(f"{yt.title}'s Download Compeleted!")
            except:
                print("ERROR SHIT")
    def responsecrawler(self):
        return requests.get(self.channel_link)
    def store_respose(self,response):
        if response.status_code == 200:
            print("Saving Response into 'res.html'")
            with open('res.html',"w",encoding="utf-8") as f:
                f.write(response.text)
                f.close()
            print("Done!")
    def load_response(self):
        html = ''
        with open("res.html","r",encoding="utf-8") as f:
            for line in f.read():
                html += line 
        return html       
    def linkparser(self,html):
        contents = BeautifulSoup(html,features="html.parser")
        pattern = re.compile('(?<=\/watch\?)v\=(.*?)(?=\")')
        items = pattern.findall(str(contents))
        for item in items:
            if item is not None:
                if item not in self.video_links:
                    self.video_links.append(item)
        print(f'total links: {len(self.video_links)}')
    def run(self):
        response = self.responsecrawler()
        self.store_respose(response)
        html = self.load_response()
        self.linkparser(html)
        self.videodownloader(self.video_links)
if __name__ == "__main__":
    youtube = YouTubeCrawler()
    youtube.run()