from tkinter import *
import tkinter as tk

class Dispence(tk.Toplevel):

    def close(self, event):
        self.destroy()

    def __init__(self):
        super().__init__()
        self.title('Dispensar Agua')
        self.geometry('1024x600')

        saldo = IntVar()

        buttons_frm = tk.Frame(self)

        label = tk.Label(buttons_frm, text='Saldo en cordobas : {}'.format(saldo.get()))
        label.grid(row=0, columnspan=2)

        stop_btn = tk.Button(buttons_frm, text='Detener')
        stop_btn.grid(row=1, column=0)

        start_btn = tk.Button(buttons_frm, text='Dispensar')
        start_btn.grid(row=1, column=1)

        cancel_btn = tk.Button(buttons_frm, text='Regresar', command=self.destroy)
        cancel_btn.grid(row=2, columnspan=2, pady=20)

        buttons_frm.pack(expand=True)

        self.bind('q', self.close)

        self.protocol("WM_DELETE_WINDOW", self.destroy)

#TODO:
'''
Necesito simular el flujo de agua dispensada con un timer, ejemplo: cada 50 miliseconds dispensado
equivaldrian a un cordoba deducido del saldo de la tarjeta
'''