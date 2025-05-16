import keyboard, time
letters = {
    "o":"ɣ",
    "c":"ṣ",
    "~":"ḥ",
    ":":"ṛ",
    "#":"ṭ",
    "`":"ẓ",
}
def new_click(n) :
    try:
        if n in letters.keys() :
            time.sleep(0.1)
            keyboard.press_and_release("backspace")
            keyboard.write(letters[n])
    except :
        exit()
while True :
    new_click(keyboard.read_key())