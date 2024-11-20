# YouTube Video & Audio Downloader

## Introduction

This Python program allows you to download **YouTube videos** and **audio** easily. You can also download entire playlists either as **audio** or **video**. The program is designed to be simple to use, with clear prompts that guide you through the process of downloading.

Once you run the program, you will be prompted to select what you want to download and how you want it (e.g., video/audio quality). Follow the on-screen instructions, and the program will handle the rest.

---

## Libraries Used

1. **Pytube**  
   - This library is used to interact with YouTube and download videos and audio.  
   - Install it via pip:  
     ```bash
     pip install pytube
     ```

2. **OS**  
   - This is a standard Python library that is used for file manipulation, such as renaming files.  
   - It comes pre-installed with Python, so no need to install it separately.

---

## Installation Guide

1. **Install Python**  
   Make sure Python 3.x is installed on your system. You can download it from [here](https://www.python.org/downloads/).

2. **Install Required Libraries**  
   After Python is installed, open your terminal or command prompt and run the following command to install `pytube`:
   ```bash
   pip install pytube

    Download the Program
    Download the script or copy it into your own Python file (e.g., yt_downloader.py).

    Run the Program
    Open your terminal or command prompt, navigate to the folder containing the script, and run:

    python yt_downloader.py

Usage Example

Once the program is running, you will see prompts like this:

You want to download video or music?
Enter 0: Music , 1: Video , 2: Playlist: 

Video Download Example:

If you want to download a video, the program will ask you to provide a YouTube link and the desired quality:

Enter the link: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Enter the quality of the video:
1: 1080p , 2: 720p , 3: 480p , 4: 360p , 5: 144p

After selecting a quality, the video will be downloaded in .mp4 format.
Music Download Example:

If you want to download audio, the program will ask you to provide a YouTube link:

Enter the link: https://www.youtube.com/watch?v=dQw4w9WgXcQ

The program will download the audio and convert it into an .mp3 file.
Playlist Download Example:

If you want to download an entire playlist, the program will ask if you want to download the playlist as audio or video:

You want to download the playlist in video or audio?
Enter 0: Audio , 1: Video: 

The program will then proceed to download all the videos or audio from the playlist, depending on your choice.
Known Issues / Bugs

    1080p & 480p Videos:
    There is no audio available in 1080p and 480p videos because the itags that combine both audio and video at these resolutions are currently not working in Pytube. If you have any suggestions or fixes, feel free to contribute to the program!

    Limited Video Qualities:
    The available quality options are limited to the itags provided by YouTube for the given video. If a certain resolution or quality is unavailable, the program will notify you.

Contributing

If you have any fixes, suggestions, or want to improve the program, feel free to fork this repository and create a pull request. Contributions are welcome!
License

This project is licensed under the MIT License - see the LICENSE file for details.
Example of Prompts:

Here is a step-by-step example of what the user would see when using the script:

    Prompt 1 (Select what you want to download):

You want to download video or music?
Enter 0: Music , 1: Video , 2: Playlist:

Prompt 2 (Video Quality Selection):

Enter the quality of the video:
1: 1080p , 2: 720p , 3: 480p , 4: 360p , 5: 144p

Prompt 3 (Playlist Audio/Video Option):

You want to download the playlist in video or audio?
Enter 0: Audio , 1: Video:

Final Output (File Download):

    Downloading video...

This should provide a better understanding of how to use the script, as well as installation and troubleshooting steps!


---

This version of the README follows GitHub's Markdown format, which is commonly used for repository documentation. It includes the installation instructions, usage examples, and known issues, along with formatting for easier readability.

You said:
give the code so i just can copy pasre it in readme
ChatGPT said:
ChatGPT

Here’s the code in a format you can directly copy and paste into your GitHub README.md file:

# YouTube Video & Audio Downloader

## Introduction

This Python program allows you to download **YouTube videos** and **audio** easily. You can also download entire playlists either as **audio** or **video**. The program is designed to be simple to use, with clear prompts that guide you through the process of downloading.

Once you run the program, you will be prompted to select what you want to download and how you want it (e.g., video/audio quality). Follow the on-screen instructions, and the program will handle the rest.

---

## Libraries Used

1. **Pytube**  
   - This library is used to interact with YouTube and download videos and audio.  
   - Install it via pip:  
     ```bash
     pip install pytube
     ```

2. **OS**  
   - This is a standard Python library that is used for file manipulation, such as renaming files.  
   - It comes pre-installed with Python, so no need to install it separately.

---

## Installation Guide

1. **Install Python**  
   Make sure Python 3.x is installed on your system. You can download it from [here](https://www.python.org/downloads/).

2. **Install Required Libraries**  
   After Python is installed, open your terminal or command prompt and run the following command to install `pytube`:
   ```bash
   pip install pytube

    Download the Program
    Download the script or copy it into your own Python file (e.g., yt_downloader.py).

    Run the Program
    Open your terminal or command prompt, navigate to the folder containing the script, and run:

    python yt_downloader.py

Usage Example

Once the program is running, you will see prompts like this:

You want to download video or music?
Enter 0: Music , 1: Video , 2: Playlist: 

Video Download Example:

If you want to download a video, the program will ask you to provide a YouTube link and the desired quality:

Enter the link: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Enter the quality of the video:
1: 1080p , 2: 720p , 3: 480p , 4: 360p , 5: 144p

After selecting a quality, the video will be downloaded in .mp4 format.
Music Download Example:

If you want to download audio, the program will ask you to provide a YouTube link:

Enter the link: https://www.youtube.com/watch?v=dQw4w9WgXcQ

The program will download the audio and convert it into an .mp3 file.
Playlist Download Example:

If you want to download an entire playlist, the program will ask if you want to download the playlist as audio or video:

You want to download the playlist in video or audio?
Enter 0: Audio , 1: Video: 

The program will then proceed to download all the videos or audio from the playlist, depending on your choice.
Known Issues / Bugs

    1080p & 480p Videos:
    There is no audio available in 1080p and 480p videos because the itags that combine both audio and video at these resolutions are currently not working in Pytube. If you have any suggestions or fixes, feel free to contribute to the program!

    Limited Video Qualities:
    The available quality options are limited to the itags provided by YouTube for the given video. If a certain resolution or quality is unavailable, the program will notify you.

Contributing

If you have any fixes, suggestions, or want to improve the program, feel free to fork this repository and create a pull request. Contributions are welcome!
License

This project is licensed under the MIT License - see the LICENSE file for details.
Example of Prompts:

Here is a step-by-step example of what the user would see when using the script:

    Prompt 1 (Select what you want to download):

You want to download video or music?
Enter 0: Music , 1: Video , 2: Playlist:

Prompt 2 (Video Quality Selection):

Enter the quality of the video:
1: 1080p , 2: 720p , 3: 480p , 4: 360p , 5: 144p

Prompt 3 (Playlist Audio/Video Option):

You want to download the playlist in video or audio?
Enter 0: Audio , 1: Video:

Final Output (File Download):

    Downloading video...

This should provide a better understanding of how to use the script, as well as installation and troubleshooting steps!


---

Simply copy this content and paste it into your `README.md` file in your GitHub repository. This format will ensure that it renders correctly with proper headings, code blocks, and links on GitHub.

