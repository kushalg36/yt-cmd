from logic import logic
import keyboard 
import sys,traceback
import argparse
import time

def args_parser():
        """
        Parse Command line arguments
        """
        parser = argparse.ArgumentParser(description='yt-play: Play music from terminal')
        parser.add_argument('-s','--song',type=str,help='Enter song name to be played')
        return parser.parse_args()

class run_logic:
    def __init__(self):
        """
        Initialize the logic class
        """
        self.yt_app = logic()

    def app_close(self):
        """
        Close application
        """
        self.yt_app.close()

    def format(self,args):
        """
        Key formating
        """
        self.yt_app.search(args.song)

        while keyboard.is_pressed('q') == False:
            if(keyboard.is_pressed('s') == True):
                song = input('Enter new song==> ')
                self.yt_app.search(query = song) #Not working yet
                time.sleep(0.1)

            elif(keyboard.is_pressed('l') == True):
                self.yt_app.next() #Working without issues
                time.sleep(0.1)

            elif(keyboard.is_pressed('f') == True):
                self.yt_app.play_pause() #Working without issues
                time.sleep(0.1)

            elif(keyboard.is_pressed('g') == True):
                self.yt_app.seek_forward() #Not working proerply (seeking 10 seconds more)
                time.sleep(0.1) #working with no keypress in 5 milisecond
            
            elif(keyboard.is_pressed('d') == True):
                count = self.yt_app.seek_backward() #Not working proerply (seeking 10 seconds more)
                time.sleep(0.1) #working with no keypress in 5 milisecond

            elif(keyboard.is_pressed('q') == True):
                self.yt_app.close() # working but need to quit terminal command

if __name__ == "__main__":
    run_app =  run_logic()
    try:
        args = args_parser()
        run_app.format(args)
    except (KeyboardInterrupt, SystemExit):
        print('Shutdown requested...exiting')
    except Exception:
        print('Encountered some error! Please restart the application')   
    finally:
        run_app.app_close()