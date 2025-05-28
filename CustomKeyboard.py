import keyboard, time, pyautogui
from plyer import notification
# kabyle keys
letters = {
    "o":"ɣ",
    "c":"ṣ",
    "~":"ḥ",
    ":":"ṛ",
    "#":"ṭ",
    "`":"ẓ",
}


# using the keyboard
WriteKabyle = True
mode = ['on','off']
def click(event) :
    global WriteKabyle, mode
    key = str(event.name).lower()
    print(key)
    if key == "esc":  
        WriteKabyle = not WriteKabyle
        notification.notify(
            title="Change Langauge",
            message= f"The Kabyle keyboard is {mode[int(WriteKabyle)]}",
            app_name="CustomKeyboard",
            app_icon="kabyle_keyboard.ico",
            timeout=3
        )
    elif key in letters.keys() and WriteKabyle :
        keyboard.write(letters[key])
    else :
        keyboard.press(key)
# while True :
keyboard.on_press(click)
keyboard.wait()