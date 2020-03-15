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

def args_parser():
    """
    Parse Command line arguments
    """
    parser = argparse.ArgumentParser(description='yt-play: Play music from terminal')
    parser.add_argument('-s','--song',type=str,help='Enter song name to be played')
    return parser.parse_args()

def format(args):
    """
    Key formating
    """
    yt_app = logic()
    yt_app.search(args.song)

    # key = ''
    
    # while key != 'q':
    #     key = 

if __name__ == "__main__":
    args = args_parser()
    format(args)
