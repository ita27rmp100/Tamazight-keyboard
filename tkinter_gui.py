import tkinter as tk

class OnScreenKeyboardTk(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("On-Screen Keyboard")
        self.configure(bg='#1e1e1e')
        # Reduced size
        self.geometry('900x350')
        self.resizable(False, False)

        # Key layout with (label, colspan)
        rows = [
            [('Esc',1), ('ẓ ḥ',1), ('1 !',1), ('2 @',1), ('3 ṭ',1), ('4 $',1), ('5 %',1),
             ('6 ^',1), ('7 &',1), ('8 *',1), ('9 (',1), ('0 )',1), ('- _',1), ('= +',1), ('Back',1.6)],
            [('Tab',1.2), ('Q',1), ('W',1), ('E',1), ('R',1), ('T',1), ('Y',1), ('U',1),
             ('I',1), ('ɣ',1), ('P',1), ('[ {',1), ('] }',1), ('\\ |',1), ('Del',1)],
            [('Caps',1.5), ('A',1), ('S',1), ('D',1), ('F',1), ('G',1), ('H',1), ('J',1),
             ('K',1), ('L',1), ('; :',1), ("' \"",1), ('Enter',1.8)],
            [('Shift',2), ('Z',1), ('X',1), ('ṣ',1), ('V',1), ('B',1), ('N',1), ('M',1),
             (', <',1), ('. >',1), ('/ ?',1), ('Shift',2)],
            [('Ctrl',1), ('Win',1), ('Alt',1), ('Space',4), ('Alt',1), ('Ctrl',1),
             ('←',1), ('↓',1), ('→',1)]
        ]

        # create buttons
        for r, row in enumerate(rows):
            c = 0
            for label, span in row:
                btn = tk.Button(
                    self, text=label, fg='white', bg='#2e2e2e', activebackground='#3e3e3e',
                    activeforeground='white', bd=0, font=('Segoe UI',8), relief='flat'
                )
                # width proportional to span
                btn.grid(row=r, column=c, columnspan=int(span*2), padx=1, pady=1, sticky='nsew')
                c += int(span*2)

        # grid weights
        for i in range(c):
            self.grid_columnconfigure(i, weight=1)
        for i in range(len(rows)):
            self.grid_rowconfigure(i, weight=1)

if __name__ == '__main__':
    OnScreenKeyboardTk().mainloop()