from pytube import YouTube
from typing import Literal

DL_TYPES = ['mp4', 'mp3']


class Downloader(object):
    def __init__(self, save_path):
        self.save_path = save_path

    def download(self, links: list, filetype: DL_TYPES):
        for link in links:
            # sometimes there are connection errors, just try again 10 times
            i = 0
            while i < 10:
                try:
                    yt = YouTube(link)
                    break
                except:
                    i += 1
            if i == 11:
                print("Connection error")
                raise KeyboardInterrupt
            d = yt.streams.filter(adaptive=True)[-1]
            d.download(output_path=self.save_path)
            print(f"Download for link: {link} complete")


if __name__ == '__main__':
    d = Downloader(save_path=r"C:\Users\Kevin\Downloads")
    download_list = [r'https://www.youtube.com/watch?v=zMft9oH5vkY']
    d.download(links=download_list, filetype='mp3')
