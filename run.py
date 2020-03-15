from logic import logic
import keyboard 
import sys
import argparse

SHIFT_UP = '\x1b[1A'
DELETE_LINE = '\x1b[2K'

# call logic here


def delete_lines(n):
    for i in range(n):
        sys.stdout.write(SHIFT_UP)
        sys.stdout.write(DELETE_LINE)

def info():
    title = logic.video_info()

def argParse():
    parser = argparse.ArgumentParser(description='yt-play: Play music from terminal')

if __name__ == "__main__":
    yt_logic = logic()
    yt_logic.search(query='talk khalid') #.search(query='talk khalid')
    print(yt_logic.video_info())
    # yt_logic.play_pause()