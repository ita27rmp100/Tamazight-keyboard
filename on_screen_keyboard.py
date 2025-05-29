from tkinter import *
import pyautogui


# --- callback to fire when any key button is pressed ---
upper = False
def press_key(key):
    global upper
    skey = str(key)
    if skey in ('shift', 'ctrl', 'alt', 'win', 'capslock','enter',"left","right","top","down"):
        pyautogui.keyDown(key)
        pyautogui.keyUp(key)
        if key == "capslock" :
            upper = bool(abs(upper-1))
    elif skey == "space" :
        written.insert(END,' ')
    elif skey == "backspace" :
        current = written.get()
        written.delete(0,END)
        written.insert(0,current[:-1])
    elif skey == "delete" :
        written.delete(0,END)
    elif skey == "esc" :
        t.iconify()
    else:
        if not upper :
            written.insert(END,key)
        else :
            written.insert(END,skey.upper())
def BlockExKeyBoard(event) :
    return "break"
# --- GUI settings ---
t = Tk()
t.title("Tifrat n ugdil")
t.configure(bg='#1e1e1e')
t.attributes("-topmost",True)
t.focus_force()
t.geometry('900x390')
t.resizable(False, False)
t.iconbitmap("kabyle_keyboard.ico")
# define the menu of copy,cut, paste
my_menu = Menu(t,tearoff=0,activeborderwidth=0)
file_menu = Menu(my_menu,tearoff=0,activeborderwidth=0)
my_menu.add_command(label="Nɣel "+" "*20,command=lambda :pyautogui.hotkey("ctrl","c"))
my_menu.add_command(label="Gzem  ",command=lambda :pyautogui.hotkey("ctrl","x"))
my_menu.add_command(label="Senteḍ",command=lambda :pyautogui.hotkey("ctrl","v"))
def my_pop(e) : 
    my_menu.tk_popup(e.x_root,e.y_root)
t.bind("<Button-3>",my_pop)
# --- define the rows of keys: (label, colspan, pyautogui code) ---
rows = [
    [('Ṛeḥ',1,'esc'), ('~',1,'z'), ('1',1,'1'), ('2',1,'2'),
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
     ('Ẓ',1,'ẓ'), ('Č',1,'č'), ('Ɛ',1,'ɛ'), ('Beddel',3,'shift')],
    [('Sefrek',1,'ctrl'), ('Win',1,'win'), ('Nniḍen',1,'alt'),
     ('Tallunt',6,'space'), ('Nniḍen',1,'alt'), ('Sefrek',1,'ctrl'),
     ('←',1,'left'), ('↓',1.2,'down'), ('→',1.2,'right'), ('↑',1.2,'top')]
]
# Create the gui components
written = Entry(t,font=("Segoe UI",14),background="#4c4c4c",fg="white",bd=2)
written.grid(row=0,column=0,columnspan=30,sticky='nsew',padx=0,pady=0)
written.bind("<Key>",BlockExKeyBoard)
written.focus_set()
for r, row in enumerate(rows):
    col = 0
    t.grid_rowconfigure(r+1,minsize=50,weight=1)
    for label, span, keycode in row:
        btn = Button(
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
        btn.grid(row=r+1, column=col, columnspan=int(span*2),  # row+1 to account for Entry
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