from logic import logic
import keyboard 
import sys
import argparse
import time

'''
 TODO
 1) handle keyboardInterrupt
 2) handle MaxRetryError
 3) add graphics
'''

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

    while keyboard.is_pressed('q') == False:
        if(keyboard.is_pressed('s') == True):
            song = input('Enter new song==> ')
            yt_app.search(query = song) #Not working yet
            time.sleep(0.1)

        elif(keyboard.is_pressed('l') == True):
            yt_app.next() #Working without issues
            time.sleep(0.1)

        elif(keyboard.is_pressed('f') == True):
            yt_app.play_pause() #Working without issues
            time.sleep(0.1)

        elif(keyboard.is_pressed('g') == True):
            yt_app.seek_forward() #Not working proerply (seeking 10 seconds more)
            time.sleep(0.1) #working with no keypress in 5 milisecond
        
        elif(keyboard.is_pressed('d') == True):
            count = yt_app.seek_backward() #Not working proerply (seeking 10 seconds more)
            time.sleep(0.1) #working with no keypress in 5 milisecond

        elif(keyboard.is_pressed('q') == True):
            yt_app.close() # working but need to quit terminal command

if __name__ == "__main__":
    args = args_parser()
    format(args)
