import keyboard

def click(event) :
    print(event.name)

keyboard.on_press(click)

keyboard.wait()