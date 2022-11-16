from pytube import YouTube
import requests
class SingleVideoDownloader:
    video_link = str(input("put video link here:")).strip()
    def downloader(self):
        try:
            yt = YouTube(self.video_link)
            print(f"Video Title: {yt.title}")
            try:
                print(yt.streams.filter(file_extension="mp4"))
                itag = int(input("pick your itag"))
                stream = yt.streams.get_by_itag(itag)
                print("Downloading ....")
                stream.download()
            except:
                print("Error accoured while downloading the video")
        except:
            print("Error accroured while loading the video ")
    def run(self):
        self.downloader()

if __name__ == "__main__":
    singlevideo = SingleVideoDownloader()
    singlevideo.run()

