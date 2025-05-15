from pynput import keyboard

def on_press(key) :
    try :
        print(key)
    except AttributeError :
        print(key)

def on_release(key):
    if key == keyboard.Key.esc:  # Exit on 'Esc' key
        print("Exiting...")
        return False
    
with keyboard.Listener(on_press=on_press,on_release=on_release) as l :
    l.join()