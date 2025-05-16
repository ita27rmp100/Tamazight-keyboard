import keyboard, time

# letters = {
#     "o":"ɣ",
#     "c":"ṣ",
#     "shift_r":"ḥ",
#     "ctrl_r":"ṛ",
#     "alt_l":"ṭ",
#     "caps_lock":"ẓ",
# }

# def on_key(event) :
#     if event.even_type != 'down' :
#         return
#     name = event.name
#     if name in letters :
#         keyboard.press_and_release("backspace")
#         keyboard.write(letters[name])
# keyboard.hook(on_key)
    
def type(n) :
    keyboard.press_and_release("backspace")
    keyboard.write(n)
while True :
    if keyboard.is_pressed("o") :
        keyboard.press_and_release("backspace")
        keyboard.write("ɣ")
        time.sleep(0.1)
    elif keyboard.is_pressed("c") :
        ṣ
    elif keyboard.is_pressed("shift") :
        keyboard.press_and_release("backspace")
        keyboard.write("ḥ")
        time.sleep(0.1)
    #     type("ṣḥ)
    # elif keyboard.is_pressed("ctrl_r")
    #     type("ṛ")
    # elif keyboard.is_pressed("alt_l") :
    #     type("ṭ")
    # elif keyboard.is_pressed("caps_lock") :
    #     type("ẓ")