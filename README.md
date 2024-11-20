# YouTube Video & Audio Downloader

## Overview

This Python script allows you to download **YouTube videos** and **audio** in various qualities, as well as entire **playlists** in either **audio** or **video** formats. The program is simple to use and guides you through the download process.

## Libraries

- **Pytube**:  
  Used for downloading YouTube videos and audio. Install with:  
  ```bash
  pip install pytube

    OS:
    A standard Python library for file operations (pre-installed).

Installation

    Install Python: Make sure Python 3.x is installed. Download here.
    Install Pytube:
    Run this in your terminal:

pip install pytube

Run the Program:
Save the script as yt_downloader.py and run:

    python yt_downloader.py

Usage

Upon running the program, you’ll be prompted to choose between video, audio, or playlist. Depending on your choice, you’ll then select the quality or format.
Example Prompts

    Choose Download Type:

You want to download video or music?  
Enter 0: Music, 1: Video, 2: Playlist:

Select Video Quality:

Enter the quality of the video:  
1: 1080p, 2: 720p, 3: 480p, 4: 360p, 5: 144p

Playlist Option:

    Enter 0: Audio, 1: Video

Known Issues

    No Audio in 1080p/480p:
    These resolutions have no combined audio/video streams due to Pytube limitations. If you have a fix, please contribute!
