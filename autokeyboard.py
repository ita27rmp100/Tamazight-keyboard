import keyboard , pyautogui
# kabyle alphabet
kabyle_alphabet = [
    'a', 'e', 'i', 'u',
    'b', 'd', 'f', 'g', 'ɣ', 'h', 'ḥ', 'j', 'k', 'l',
    'm', 'n', 'p', 'q', 'r', 'ṛ', 's', 'ṣ', 't', 'ṭ',
    'v', 'w', 'x', 'y', 'z', 'ẓ'
]

while True :
    print("Press any key (Windows only)...")
    key = keyboard.read_event()  # Waits for a key press
    print(f"You pressed: {key.name}")
    if(key.name=="R") :
        pyautogui.write("ṛ")

