from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

class Dispence(tk.Toplevel):
    global bg_color
    bg_color = '#06497e'
    global danger_color
    danger_color = '#db0b0b'
    global label_size
    label_size = 48
    global label_font
    label_font = 'Times New Roman'

    def close(self, event):
        self.destroy()

    def __init__(self):
        super().__init__()
        self.title('Dispensar Agua')
        self.geometry('1024x600')
        self.configure(background=bg_color)

        saldo = IntVar()

        buttons_frm = tk.Frame(self)
        buttons_frm.configure(background=bg_color)

        #img_canvas = Canvas(buttons_frm, width=1024, height=600)
        #img_canvas.grid(row=0, column=0, rowspan=3, columnspan=4)
        
        #img = ImageTk.PhotoImage(Image.open("v2/bg_v2.jpg"))
        #img_canvas.create_image(0,0,anchor=tk.NW, image=img)
        #img_canvas.image = img
        
        label = tk.Label(buttons_frm, text='Saldo en cordobas : {}'.format(saldo.get()), font=(label_font, label_size), pady=80)
        label.configure(background=bg_color)
        label.grid(row=0, columnspan=2)

        stop_btn = tk.Button(buttons_frm, text='Detener', highlightbackground=bg_color, bg=danger_color, fg=danger_color, font=(label_font, label_size), padx=50, pady=20)
        stop_btn.grid(row=1, column=0)

        start_btn = tk.Button(buttons_frm, text='Dispensar', highlightbackground=bg_color, font=(label_font, label_size), padx=50, pady=20)
        start_btn.grid(row=1, column=1)

        cancel_btn = tk.Button(buttons_frm, text='Regresar', command=self.destroy, highlightbackground=bg_color, font=(label_font, label_size), padx=100, pady=20)
        cancel_btn.grid(row=2, columnspan=2, pady=20)

        buttons_frm.pack(expand=True)

        self.bind('q', self.close)

        self.protocol("WM_DELETE_WINDOW", self.destroy)

#TODO:
'''
Necesito simular el flujo de agua dispensada con un timer, ejemplo: cada 50 miliseconds dispensado
equivaldrian a un cordoba deducido del saldo de la tarjeta
'''