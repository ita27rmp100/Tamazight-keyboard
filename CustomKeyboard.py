import keyboard , sys , os , json
from plyer import notification

# GET kabyle letters from json file
with open(os.path.join(os.path.dirname(__file__),"kabyle.json"),mode="r",encoding="UTF-8") as Jfile : 
    letters =  json.load(Jfile)
# Functions that handle with the presses of keys
WriteKabyle = True
Upper = False
shiftActive = False
modes = ['off','on']
def notify(ttle,msg) :
    notification.notify(
        title=ttle,
        message= msg,
        app_name="CustomKeyboard",
        app_icon="kabyle_keyboard.ico",
        timeout=1
    )
def shiftDown(e) :
    global shiftActive
    shiftActive = not shiftActive
def shiftUp(e) :
    global shiftActive
    shiftActive = not shiftActive
def toogleMode() :
    global modes , WriteKabyle
    WriteKabyle = not WriteKabyle
    notify("Change Langauge",f"The Kabyle keyboard is {modes[int(WriteKabyle)]}")
def UpperToggle() :
    global Upper
    Upper = not Upper
def upperWrite(v) :
    if Upper or shiftActive :
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
    notify("Exit","The kabyle keyboard has been exited")
    keyboard.unhook_all()
    sys.exit()

# replacement of keys :
for k, v in letters.items() :
    keyboard.on_press_key(
        k,
        lambda e,repl = v  , origin = k: ReplaceClick(origin,repl),
        suppress=True
    )
    
keyboard.on_press_key("caps lock",lambda e :UpperToggle(),suppress=False)
keyboard.on_press_key("end",lambda e : stop(),suppress=False)
keyboard.on_press_key("esc",lambda e : toogleMode(),suppress=False)
keyboard.on_press_key("shift",lambda e : shiftDown(e),suppress=False)
keyboard.on_release_key("shift",lambda e : shiftUp(e),suppress=False)
keyboard.wait()