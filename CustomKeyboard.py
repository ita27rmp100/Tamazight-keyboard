import keyboard
from plyer import notification
# kabyle keys
letters = {
    "o":"ɣ",
    "[":"ṭ",
    "]":"ṛ",
    "\\":"ḍ",
    ";":"ǧ",
    "'":"ḥ",
    "c":"ṣ",
    ",":"ẓ",
    ".":"č",
    "/":"ɛ",
    "-":",",
    "=":"."
}
# Functions that trait the pressesof keys
WriteKabyle = True
Upper = False
modes = ['off','on']
def toogleMode() :
    global modes , WriteKabyle
    WriteKabyle = not WriteKabyle
    notification.notify(
        title="Change Langauge",
        message= f"The Kabyle keyboard is {modes[int(WriteKabyle)]}",
        app_name="CustomKeyboard",
        app_icon="kabyle_keyboard.ico",
        timeout=1
    )
def UpperToggle() :
    global Upper
    Upper = not Upper
def upperWrite(v) :
    if Upper :
        keyboard.write(str(v).upper())
    else :
        keyboard.write(v)
def ReplaceClick(o,v) :
    global WriteKabyle
    if WriteKabyle :
        upperWrite(v)
    else :
        upperWrite(o)
def stop() :
    exit()
# replacement of keys :
for k, v in letters.items() :
    keyboard.on_press_key(
        k,
        lambda e,repl = v  , origin = k: ReplaceClick(origin,repl),
        suppress=True
    )
keyboard.on_press_key("caps lock",lambda e :UpperToggle(),suppress=False)
keyboard.on_press_key("esc",lambda e : toogleMode(),suppress=False)
keyboard.on_press_key("end",lambda e : stop(),suppress=False)
keyboard.wait()