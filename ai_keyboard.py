import tkinter as tk
import pyautogui

letters = {
    "o":"ɣ",
    "c":"ṣ",
    "~":"ḥ",
    ":":"ṛ",
    "#":"ṭ",
    "`":"ẓ",
}

# --- callback to fire when any key button is pressed ---
def press_key(key):
    if key in ('shift', 'ctrl', 'alt', 'win', 'capslock'):
        pyautogui.keyDown(key)
        pyautogui.keyUp(key)
    else:
        pyautogui.hotkey(key)

# --- create the main window ---
t = tk.Tk()
t.title("On-Screen Keyboard")
t.configure(bg='#1e1e1e')
t.geometry('900x378')
t.resizable(False, False)

# --- define the rows of keys: (label, colspan, pyautogui code) ---
rows = [
    [('Esc',1,'esc'), ('ẓ ḥ',1,'z'), ('1 !',1,'1'), ('2 @',1,'2'),
     ('3 ṭ',1,'3'), ('4',1,'4'), ('5 %',1,'5'), ('6 ^',1,'6'),
     ('7 &',1,'7'), ('8 *',1,'8'), ('9 (',1,'9'), ('0 )',1,'0'),
     ('- _',1,'-'), ('= +',1,'='), ('Back',2,'backspace')],
    [('Tab',1.2,'tab'), ('Q',1,'q'), ('W',1,'w'), ('E',1,'e'),
     ('R',1,'r'), ('T',1,'t'), ('Y',1,'y'), ('U',1,'u'),
     ('I',1,'i'), ('ɣ',1,'g'), ('P',1,'p'), ('[ {',1,'['),
     ('] }',1,']'), ('\\ |',1,'\\'), ('Del',2,'delete')],
    [('Caps',1.5,'capslock'), ('A',1,'a'), ('S',1,'s'), ('D',1,'d'),
     ('F',1,'f'), ('G',1,'g'), ('H',1,'h'), ('J',1,'j'),
     ('K',1,'k'), ('L',1,'l'), ('; :',1,';'), ("' \"",1,"'"),
     ('Enter',3.8,'enter')],
    [('Shift',3,'shift'), ('Z',1,'z'), ('X',1,'x'), ('ṣ',1,'s'),
     ('V',1,'v'), ('B',1,'b'), ('N',1,'n'), ('M',1,'m'),
     (', <',1,','), ('. >',1,'.'), ('/ ?',1,'/'), ('Shift',4,'shift')],
    [('Ctrl',1,'ctrl'), ('Win',1,'win'), ('Alt',1,'alt'),
     ('Space',6,'space'), ('Alt',1,'alt'), ('Ctrl',1,'ctrl'),
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
