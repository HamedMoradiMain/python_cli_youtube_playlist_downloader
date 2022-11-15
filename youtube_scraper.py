import requests # requests module 
from bs4 import BeautifulSoup # BeautifulSoup module 
import json # json module for getting json output 
import csv # csv module for storing data in .csv format
import re # regx module for 
from pytube import YouTube

class YouTubeCrawler:
    video_links = []
    base_url = 'https://www.youtube.com/watch?v='
    SAVE_PATH = "F:\youtube"
    def downloader(self,link):
        try:
            yt=YouTube(f'{self.base_url}{link}')
        except:
            print("Connection Error!")
        #mp4files = yt.filter('mp4')
        mp4_format=yt.streams.filter(file_extension='mp4')
        d_video = yt.streams.get_by_itag(18)
        try:
            d_video.download()
        except:
            print("Error!")
        print("download completed!")
    def loadresponse(self):
        html = ''
        with open("res.html","r",encoding="utf-8") as f:
            for line in f.read():
                html += line
                f.close()
            return html
    def parse(self,html):
        content = BeautifulSoup(html,features="html.parser")
        links = content.findAll("a",{"class":re.compile("yt-simple-endpoint inline-block style-scope ytd-thumbnail")})
        gross_content = []
        #print(links)
        for link in links:
            gross_content.append(str(link))
        with open("gross.json",'w',encoding='utf-8') as f:
            json.dump(gross_content,f,ensure_ascii=False,indent=4)
            f.close()
        '''if link.attrs['href'] is not None:
                if link.attrs['href'] not in self.video_links:
                    print(link.attrs['href'])
                    self.video_links.append(link.attrs['href'])'''
        #print(f"total links{len(self.video_links)}")
    def link_exporter(self):
        with open('gross.json','r',encoding='utf-8') as f:
            data = json.load(f)
            pattern = re.compile('(?<=\/watch\?)v\=(.*?)(?=\")')
            for line in data:
                #print(line)
                link = pattern.findall(line)
                if link is not None:
                    if link not in self.video_links:
                        print(link)
                        self.video_links.append(link)
        print(f'total links: {len(self.video_links)}')
        with open("finalLinks.json",'w',encoding='utf-8') as f:
            json.dump(self.video_links,f,ensure_ascii=False,indent=4)
            f.close()
    def run(self):
        #html = self.loadresponse()
        #self.parse(html)
        #self.link_exporter()
        link = 'https://www.youtube.com/watch?v=7qPLsm2E0Mc'
        self.downloader(link)
if __name__ == "__main__":
    youtube = YouTubeCrawler()
    youtube.run()