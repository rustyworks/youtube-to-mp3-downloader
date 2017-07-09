import os
import shlex
import subprocess
import sys


CURRENT_PATH = os.getcwd()


def main():
    with open('links.txt') as urls:
        for url in urls:
            if url.find('www.youtube.com') == -1:
                url = append_youtube_url(url)
            cmd = shlex.split('youtube-dl --extract-audio --audio-format mp3 ' + url)
            print('last url: ' + url)
            subprocess.call(cmd)

def append_youtube_url(url):
    return 'https://www.youtube.com' + url


if __name__ == '__main__':
    main()
