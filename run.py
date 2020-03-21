from logic import logic
import keyboard 
import sys,traceback
import argparse
import time

'''
 TODO
 1) handle keyboardInterrupt ---DONE
 2) handle MaxRetryError ---DONE
 3) add graphics
 4) add colors
 5) show video name and artist ---DONE
 6) ctrl + C should also stop music ---DONE with bugs
 7) wait until  
'''

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
                self.yt_app.search(query = song)
                time.sleep(0.1)

            elif(keyboard.is_pressed('l') == True):
                self.yt_app.next()
                time.sleep(0.1)

            elif(keyboard.is_pressed('f') == True):
                self.yt_app.play_pause() 
                time.sleep(0.1)

            elif(keyboard.is_pressed('g') == True):
                self.yt_app.seek_forward() 
                time.sleep(0.1) 
            
            elif(keyboard.is_pressed('d') == True):
                count = self.yt_app.seek_backward() 
                time.sleep(0.1) 

            elif(keyboard.is_pressed('q') == True):
                self.yt_app.close() 

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