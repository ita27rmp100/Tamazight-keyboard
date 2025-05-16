import keyboard, time
# kabyle keys
letters = {
    "o":"ɣ",
    "c":"ṣ",
    "~":"ḥ",
    ":":"ṛ",
    "#":"ṭ",
    "`":"ẓ",
}
# replace the blocked key
def new_click(n) :
    try:
        if n in letters.keys() :
            time.sleep(0.1)
            keyboard.press_and_release("backspace")
            keyboard.write(letters[n])
    except :
        exit()
# using the keyboard
while True :
    new_click(keyboard.read_key())