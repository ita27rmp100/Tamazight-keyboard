import msvcrt , pyautogui
# kabyle alphabet
kabyle_alphabet = [
    'a', 'e', 'i', 'u',
    'b', 'd', 'f', 'g', 'ɣ', 'h', 'ḥ', 'j', 'k', 'l',
    'm', 'n', 'p', 'q', 'r', 'ṛ', 's', 'ṣ', 't', 'ṭ',
    'v', 'w', 'x', 'y', 'z', 'ẓ'
]

while True :
    print("Press any key (Windows only)...")
    key = msvcrt.getch()  # Waits for a key press
    print(f"You pressed: {key.decode('utf-8')}")
    pyautogui.hotkey(key.decode('utf-8'))
    if(key.decode('utf-8')=="R") :
        pyautogui.write("ṛ")

