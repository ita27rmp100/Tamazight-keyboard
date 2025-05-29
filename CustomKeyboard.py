import keyboard, time, pyautogui
from plyer import notification
# kabyle keys
letters = {
    "o":"ɣ",
    "[":"ṭ",
    "]":"ṛ",
    "\ ":"ḍ",
    ";":"ǧ",
    "'":"ḥ",
    "c":"ṣ",
    ",":"ẓ",
    ".":"č",
    "/":"ɛ"
}


# using the keyboard
WriteKabyle = True
modes = ['off','on']
def toogleMode() :
    global modes , WriteKabyle
    WriteKabyle = not WriteKabyle
    notification.notify(
        title="Change Langauge",
        message= f"The Kabyle keyboard is {modes[int(WriteKabyle)]}",
        app_name="CustomKeyboard",
        app_icon="kabyle_keyboard.ico",
        timeout=2
    )


# replacement of keys :
for k, v in letters.items() :
    keyboard.on_press_key(
        k,
        lambda e,repl = v : keyboard.write(repl),
        suppress=True
    )
ɣ
keyboard.on_press_key("esc",lambda e : toogleMode(),suppress=False)
keyboard.wait()