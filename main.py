from pytube import YouTube
from pytube import Playlist

import os

def vorm():
    print("You want to download video or music ?")
    vorme=input("Enter 0: Music , 1: Video  , 2 : PLaylist ; : ")
    if vorme=="1":
        video()
    elif vorme=="0":
        music()
    elif vorme=="2":
        playlist()
    else:
        print("Enter a valid number")
        vorm()



def music() :
    link =input("Enter the link :")
    yt = YouTube(link)
    stream = yt.streams.get_by_itag(251)
    a=stream.download()
    my_file = a
    base = os.path.splitext(my_file)[0]
    os.rename(my_file, base + '.mp3')

def video():
    link = input("Enter the link :")
    yt = YouTube(link)
    print("Enter the quality of the video:")
    vq=int(input("1:1080 , 2:720 , 3:480 , 4:360 , 5:144"))
    if vq in (1,2,3,4,5):
        if vq==2:
            stream = yt.streams.get_by_itag(22)
            a = stream.download()
            my_file = a
            base = os.path.splitext(my_file)[0]
            os.rename(my_file, base + '.mp4')
        elif vq==1:
            print("Sorry For the inconvenience but 1080p videos dont have audio cause itags with 1080 audio/video are not working if you got any solution then please tell ")
            tf=int(input("To cancel operation press 1 to continue press 0"))
            if tf==0:
                stream = yt.streams.get_by_itag(137)
                a = stream.download()
                my_file = a
                base = os.path.splitext(my_file)[0]
                os.rename(my_file, base + '.mp4')
            else:
                vorm()

        elif vq==3:
            print("Sorry For the inconvenience but 1080p videos dont have audio cause itags with 1080 audio/video are not working if you got any solution then please tell ")
            tf = int(input("To cancel operation press 1 to continue press 0"))
            if tf==0:
                stream = yt.streams.get_by_itag(135)
                a = stream.download()
                my_file = a
                base = os.path.splitext(my_file)[0]
                os.rename(my_file, base + '.mp4')
            else:
                vorm()
        elif vq==4:
            stream = yt.streams.get_by_itag(18)
            a = stream.download()
            my_file = a
            base = os.path.splitext(my_file)[0]
            os.rename(my_file, base + '.mp4')
        elif vq==5:
            stream = yt.streams.get_by_itag(17)
            a = stream.download()
            my_file = a
            base = os.path.splitext(my_file)[0]
            os.rename(my_file, base + '.mp4')

    else:
        print("Invalid Quality")
        video()
def playlist():
    print("You want to download the playlist in video or audio ?")
    vorme = input("Enter 0: Audio , 1: Video ;  : ")
    if vorme == "1":
        p_video()
    elif vorme == "0":
        p_music()
def p_music():
    link = input("Enter the link :")
    playlist= Playlist(link)
    for audio in playlist:
        yt=YouTube(audio)
        stream = yt.streams.get_by_itag(251)
        a = stream.download()
        my_file = a
        base = os.path.splitext(my_file)[0]
        os.rename(my_file, base + '.mp3')
def p_video():
    link = input("Enter the link :")
    playlist = Playlist(link)
    print("Enter the quality of the video:")
    vq = int(input("1:1080 , 2:720 , 3:480 , 4:360 , 5:144"))
    if vq in (1, 2, 3, 4, 5):
        if vq == 2:
            for video in playlist:
                yt=YouTube(video)
                stream = yt.streams.get_by_itag(22)
                a = stream.download()
                my_file = a
                base = os.path.splitext(my_file)[0]
                os.rename(my_file, base + '.mp4')
        elif vq == 1:
            print(
                "Sorry For the inconvenience but 1080p videos dont have audio cause itags with 1080 audio/video are not working if you got any solution then please tell ")
            tf = int(input("To cancel operation press 1 to continue press 0"))
            if tf == 0:
                for video in playlist:
                    yt = YouTube(video)
                    stream = yt.streams.get_by_itag(137)
                    a = stream.download()
                    my_file = a
                    base = os.path.splitext(my_file)[0]
                    os.rename(my_file, base + '.mp4')
            else:
                vorm()

        elif vq == 3:
            print(
                "Sorry For the inconvenience but 1080p videos dont have audio cause itags with 1080 audio/video are not working if you got any solution then please tell ")
            tf = int(input("To cancel operation press 1 to continue press 0"))
            if tf == 0:
                for video in playlist:
                    yt = YouTube(video)
                    stream = yt.streams.get_by_itag(135)
                    a = stream.download()
                    my_file = a
                    base = os.path.splitext(my_file)[0]
                    os.rename(my_file, base + '.mp4')
            else:
                vorm()
        elif vq == 4:
            for video in playlist:
                yt=YouTube(video)
                stream = yt.streams.get_by_itag(18)
                a = stream.download()
                my_file = a
                base = os.path.splitext(my_file)[0]
                os.rename(my_file, base + '.mp4')
        elif vq == 5:
            for video in playlist:
                yt=YouTube(video)
                stream = yt.streams.get_by_itag(17)
                a = stream.download()
                my_file = a
                base = os.path.splitext(my_file)[0]
                os.rename(my_file, base + '.mp4')
    else:
        print("Invalid Quality")
        p_video()



vorm()