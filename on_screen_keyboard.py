import tkinter as tk
import pyautogui , sys

class OnScreenKeyboardTk(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("On-Screen Keyboard")
        self.configure(bg='#1e1e1e')
        # Reduced size
        self.geometry('900x378')
        self.resizable(False, False)

        # Key layout with (label, colspan, keycode)
        rows = [
            [('Esc',1,'esc'), ('ẓ ḥ',1,'z'), ('1 !',1,'1'), ('2 @',1,'2'), ('3 ṭ',1,'3'), ('4 $',1,'4'), ('5 %',1,'5'),
             ('6 ^',1,'6'), ('7 &',1,'7'), ('8 *',1,'8'), ('9 (',1,'9'), ('0 )',1,'0'), ('- _',1,'-'), ('= +',1,'='), ('Back',2,'backspace')],
            [('Tab',1.2,'tab'), ('Q',1,'q'), ('W',1,'w'), ('E',1,'e'), ('R',1,'r'), ('T',1,'t'), ('Y',1,'y'), ('U',1,'u'),
             ('I',1,'i'), ('ɣ',1,'g'), ('P',1,'p'), ('[ {',1,'['), ('] }',1,']'), ('\\ |',1,'\\'), ('Del',2,'delete')],
            [('Caps',1.5,'capslock'), ('A',1,'a'), ('S',1,'s'), ('D',1,'d'), ('F',1,'f'), ('G',1,'g'), ('H',1,'h'), ('J',1,'j'),
             ('K',1,'k'), ('L',1,'l'), ('; :',1,';'), ("' \"",1,"'"), ('Enter',3.8,'enter')],
            [('Shift',3,'shift'), ('Z',1,'z'), ('X',1,'x'), ('ṣ',1,'s'), ('V',1,'v'), ('B',1,'b'), ('N',1,'n'), ('M',1,'m'),
             (', <',1,','), ('. >',1,'.'), ('/ ?',1,'/'), ('Shift',4,'shift')],
            [('Ctrl',1,'ctrl'), ('Win',1,'win'), ('Alt',1,'alt'), ('Space',6,'space'), ('Alt',1,'alt'), ('Ctrl',1,'ctrl'),
            ('←',1,'left'), ('↓',1.2,'down'), ('→',1.2,'right'),('↑',1.2,'top')]
        ]

        for r, row in enumerate(rows):
            c = 0
            for label, span, key in row:
                btn = tk.Button(
                    self, text=label, fg='white', bg='#2e2e2e', activebackground='#3e3e3e',
                    activeforeground='white', bd=0, font=('Segoe UI', 8), relief='flat',
                    command=lambda k=key: self.press_key(k)
                )
                btn.grid(row=r, column=c, columnspan=int(span*2), padx=1, pady=1, sticky='nsew')
                c += int(span*2)

        # grid weights
        for i in range(c): self.grid_columnconfigure(i, weight=1)
        for i in range(len(rows)): self.grid_rowconfigure(i, weight=1)

    def press_key(self, key):
        # simulate modifiers correctly
        if key in ['shift', 'ctrl', 'alt', 'win', 'capslock']:
            pyautogui.keyDown(key)
            pyautogui.keyUp(key)
        else:
            pyautogui.hotkey(key)

if __name__ == '__main__':
    OnScreenKeyboardTk().mainloop()
