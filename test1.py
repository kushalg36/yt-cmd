from time import sleep
erase = '\x1b[1A\x1b[2K'#\x1b[1A\x1b[2K

def download(number):
    print(erase + "File {} processed".format(number))

def completed(percent):
    print("({:1.1}% Completed)".format(percent))

for i in range(1,4):
    download(i)
    completed(i/10)
    sleep(1)