# YT-CMD
---

Hey beautiful people of the internet, hope you all are doing well.
We all know how annoying youtube comments are, people spamming "Who else is listening in 2020" and not to mention the youtube advertisement.
As a software developer and melomaniac at the same time, I developed a CLI program which can play music videos from youtube in background without disturbing the workflow. All it takes a command prompt.

# Description
---

- yt-cmd is a CLI program which is currently in <b>active development phase</b>. It lets you play your favourite songs straight from your command prompt. 
- Feel free to raise an issue if you find any bug. Right now, it just plays a single song.
- In the near future, I am planning to play playlist in the later phase.

# Installation
---

These instructions will set the copy of this project in your system and let you play with the youtube from the command line interface.

# Prerequisites
---

- Windows Operating System
- Mozilla Firefox
- Python3
- PIP

# Steps to install
---

1) Clone this repository
 ```sh 
 git clone https://github.com/kushalg36/yt-cmd.git
 ```

2) Get into the project
 ```sh 
 cd yt-cmd
 ```

3) Run the batch file to install all the dependencies
 ```sh 
 main.bat
 ```

4) Get your youtube data API key from [here](https://console.developers.google.com) adn save it to your enviroment variable with the name **api_key**

# Using yt-cmd
---

Post installation, you can start the application by-
 
- Run the python file to play any song ( SONG_NAME must be in doublequote ) 
 ```sh 
 python run.py -s SONG_NAME
 ```
 
- To play/pause any song-
 ```sh 
 f
 ```
 
- To seek forward 5 seconds-
 ```sh  
 g
 ```

- To seek forward 5 seconds-
 ```sh  
 d
 ```

- To play next song-
 ```sh 
 l
 ```

- To quit the youtube-
 ```sh 
 q
 ```

- To play any song in between other song-
 ```sh 
 s
 ```

 **!!!Don't keyboard interrupt (Ctrl + C) as it can't handle this exception right now. In case of pressed it anyway, you have to close firefox from background process of Task Manager!!!**

# TODO
---

1) handle keyboardInterrupt ---DONE
2) handle MaxRetryError ---DONE
3) add graphics
4) add colors
5) show video name and artist ---DONE
6) ctrl + C should also stop music 
7) wait until  