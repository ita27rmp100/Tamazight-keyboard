import pyautogui
from pynput import keyboard
# kabyle alphabet
kabyle_alphabet = [
    'a', 'e', 'i', 'u',
    'b', 'd', 'f', 'g', 'ɣ', 'h', 'ḥ', 'j', 'k', 'l',
    'm', 'n', 'p', 'q', 'r', 'ṛ', 's', 'ṣ', 't', 'ṭ',
    'v', 'w', 'x', 'y', 'z', 'ẓ'
]

def on_press(key) :
    try :
        if key.char == "o" :
            pyautogui.write("ɣ")
        elif key.char == "c" :
            pyautogui.write("ṣ")
        else :
            pyautogui.write(key.char)
    except AttributeError :
        if key == keyboard.Key.shift_r :
            pyautogui.write("ḥ")
        elif key == keyboard.Key.ctrl_r :
            pyautogui.write("ṛ")
        elif key == keyboard.Key.alt_l :
            pyautogui.write("ṭ")
        elif key == keyboard.Key.caps_lock :
            pyautogui.write("ẓ")
        else :
            pass

def on_release(key):
    if key == keyboard.Key.esc:  # Exit on 'Esc' key
        print("Exiting...")
        return False
with keyboard.Listener(on_press=on_press,on_release=on_release) as l :
    l.join()