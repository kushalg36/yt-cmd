import keyboard

while True:
    try:
        if keyboard.is_pressed('q'):
            print('You pressed A key!')
            break
    except:
        break