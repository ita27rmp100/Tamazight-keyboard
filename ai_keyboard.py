import tkinter as tk
import pyautogui
import ctypes

# --- Windows constants to prevent focus ---
GWL_EXSTYLE = -20
WS_EX_NOACTIVATE = 0x08000000
WS_EX_TOOLWINDOW = 0x00000080

# --- callback to fire when any key button is pressed ---
upper = False
def press_key(key):
    global upper
    t.after(10, t.withdraw)  # Temporarily hide to give up focus

    def typing():
        global upper
        if key in ('shift', 'ctrl', 'alt', 'win', 'capslock'):
            pyautogui.keyDown(key)
            pyautogui.keyUp(key)
            if key == "capslock":
                upper = bool(abs(upper - 1))
        else:
            char = key if not upper else key.upper()
            pyautogui.write(char)

        t.deiconify()     # Show window again
        t.lift()          # Bring to front
        t.attributes("-topmost", True)

    t.after(100, typing)

# --- create the main window ---
t = tk.Tk()
t.title("On-Screen Keyboard")
t.configure(bg='#1e1e1e')
t.attributes("-topmost", True)
t.geometry('900x378')
t.resizable(False, False)
t.overrideredirect(True)  # Remove window borders

# --- Apply WS_EX_NOACTIVATE and WS_EX_TOOLWINDOW styles (no focus stealing) ---
hwnd = ctypes.windll.user32.GetParent(t.winfo_id())
style = ctypes.windll.user32.GetWindowLongPtrW(hwnd, GWL_EXSTYLE)
style |= WS_EX_NOACTIVATE | WS_EX_TOOLWINDOW
ctypes.windll.user32.SetWindowLongPtrW(hwnd, GWL_EXSTYLE, style)

# --- define the rows of keys: (label, colspan, pyautogui code) ---
rows = [
    [('Ṛrḥ',1,'esc'), ('~',1,'z'), ('1',1,'1'), ('2',1,'2'),
     ('3',1,'3'), ('4',1,'4'), ('5',1,'5'), ('6',1,'6'),
     ('7',1,'7'), ('8',1,'8'), ('9',1,'9'), ('0',1,'0'),
     (',',1,','), ('.',1,'.'), ('Uɣal',2,'backspace')],
    [('iferdis',1.2,'tab'), ('Q',1,'q'), ('W',1,'w'), ('E',1,'e'),
     ('R',1,'r'), ('T',1,'t'), ('Ɣ',1,'y'), ('U',1,'u'),
     ('I',1,'i'), ('ɣ',1,'ɣ'), ('P',1,'p'), ('ṭ',1,'ṭ'),
     ('Ṛ',1,'ṛ'), ('Ḍ',1,'ḍ'), ('Semsay',2,'delete')],
    [('Caps',1.5,'capslock'), ('A',1,'a'), ('S',1,'s'), ('D',1,'d'),
     ('F',1,'f'), ('G',1,'g'), ('H',1,'h'), ('J',1,'j'),
     ('K',1,'k'), ('L',1,'l'), ('Ǧ',1,'ǧ'), ("Ḥ",1,"ḥ"),
     ('Sekcem',3.8,'enter')],
    [('Beddel',2,'shift'), ('Z',1,'z'), ('X',1,'x'), ('ṣ',1,'ṣ'),
     ('V',1,'v'), ('B',1,'b'), ('N',1,'n'), ('M',1,'m'),
     ('Ẓ',1,'ẓ'), ('Č',1,'č'), ('Ɖ',1,'ɛ'), ('Beddel',3,'shift')],
    [('Sefrek',1,'ctrl'), ('Win',1,'win'), ('Nniḍen',1,'alt'),
     ('Tallunt',6,'space'), ('Nniḍen',1,'alt'), ('Sefrek',1,'ctrl'),
     ('←',1,'left'), ('↓',1.2,'down'), ('→',1.2,'right'), ('↑',1.2,'top')]
]

# --- create all the buttons ---
for r, row in enumerate(rows):
    col = 0
    for label, span, keycode in row:
        btn = tk.Button(
            t,
            text=label,
            fg='white',
            bg='#2e2e2e',
            activebackground='#3e3e3e',
            activeforeground='white',
            bd=0,
            font=('Segoe UI', 8),
            relief='flat',
            command=lambda k=keycode: press_key(k)
        )
        btn.grid(row=r, column=col, columnspan=int(span*2),
                 padx=1, pady=1, sticky='nsew')
        col += int(span*2)

# --- make the grid cells expand evenly ---
total_cols = col
for c in range(total_cols):
    t.grid_columnconfigure(c, weight=1)
for rr in range(len(rows)):
    t.grid_rowconfigure(rr, weight=1)

# --- start the GUI loop ---
t.mainloop()

