from tkinter import *
import tkinter as tk
from tkinter import messagebox

class Recharge(tk.Toplevel):

    def agregar_saldo(self, amount):
        self.nuevo_saldo.set(self.nuevo_saldo.get() + amount)
        self.agregar_saldo_text.set('Agregar C$: {}'.format(self.nuevo_saldo.get()))
        self.label2.config(text=self.agregar_saldo_text.get())

    def zero_saldo(self):
        self.nuevo_saldo.set(0)
        self.agregar_saldo_text.set('Agregar C$: {}'.format(self.nuevo_saldo.get()))
        self.label2.config(text=self.agregar_saldo_text.get())

    def close(self, event):
        self.destroy()
    
    def confirm(self):
        if self.user_card.get() != "" :
            if self.nuevo_saldo.get() > 0 :
                if self.sales_card.get() != "":
                    confirm = messagebox.askyesno('Confirmar','Porfavor confirme la operacion')
                    if confirm :
#TODO: ACTUALIZAR LA BASE DE DATOS LOCAL CON EL NUEVO MONTO
                        print('Vendedor: {}'.format(self.sales_card.get()) + ' esta vendiendo {} '.format(self.nuevo_saldo.get()) + ' a la tarjeta {} '.format(self.user_card.get()))
                        self.user_card.set("")
                        self.destroy()
                    else :
                        self.error_lbl.config(text="")    
                else :
                    self.error_lbl.config(text=self.no_sales_card_text)    
            else :
                self.error_lbl.config(text=self.no_amount_text)
        else :
            self.error_lbl.config(text=self.no_user_card_text)
      
    def card_inserted(self, event):
#SIMULATE GETTING THE USER CARD TYPE FROM DB
        card_type = 'USER'
#SIMULATE I READ THE NUMBER FROM THE CARD AND GET THE AMOUNT FROM DB
        if card_type == 'USER':
            self.user_card.set("XYZ")
        elif card_type == 'SALES':
            self.sales_card.set("ABC")
        #RESET ERROR MESSAGE    
        self.error_lbl.config(text="")

    def __init__(self, sales_card_param):
        super().__init__()
        self.title('Realizar recarga')
        self.geometry('1024x600')
#SALDO ORIGINAL EN TARJETA DE USUARIO
        self.sales_card = StringVar()
        self.sales_card.set(sales_card_param)
        self.saldo = IntVar()
        self.saldo_text = StringVar()
        self.saldo_text.set('Saldo C$: {}'.format(self.saldo.get()))
#AGREGAR SALDO AL SALDO ORIGINAL
        self.user_card = StringVar()
        self.nuevo_saldo = IntVar()
        self.agregar_saldo_text = StringVar()
        self.agregar_saldo_text.set('Agregar C$: {}'.format(self.nuevo_saldo.get()))
        self.no_user_card_text = 'Inserte la tarjeta del usuario'
        self.no_sales_card_text = 'Inserte la tarjeta del vendedor'
        self.no_amount_text = 'El monto debe de ser mayor que cero'

        self.buttons_frm = tk.Frame(self)

        self.label = tk.Label(self.buttons_frm, text=self.saldo_text.get())
        self.label.grid(row=0, columnspan=4)

        self.label2 = tk.Label(self.buttons_frm, text=self.agregar_saldo_text.get())
        self.label2.grid(row=1, columnspan=4)

        self.five_btn = tk.Button(self.buttons_frm, text='C$ 5', command=lambda: self.agregar_saldo(5))
        self.five_btn.grid(row=2, column=0)

        self.ten_btn = tk.Button(self.buttons_frm, text='C$ 10', command=lambda: self.agregar_saldo(10))
        self.ten_btn.grid(row=2, column=1)

        self.hundred_btn = tk.Button(self.buttons_frm, text='C$ 100', command=lambda: self.agregar_saldo(100))
        self.hundred_btn.grid(row=2, column=3)

        self.delete_btn = tk.Button(self.buttons_frm, text='Borrar', command=self.zero_saldo)
        self.delete_btn.grid(row=3, columnspan=4, pady=10)

        self.confirm_btn = tk.Button(self.buttons_frm, text='Confirmar', command=self.confirm)
        self.confirm_btn.grid(row=4, columnspan=4)

        self.cancel_btn = tk.Button(self.buttons_frm, text='Regresar', command=self.destroy)
        self.cancel_btn.grid(row=5, columnspan=4, pady=20)

        self.error_lbl = tk.Label(self.buttons_frm, text=self.no_user_card_text, fg='red')
        self.error_lbl.grid(row=6, columnspan=4, pady=10)

        self.buttons_frm.pack(expand=True)
        
        self.bind('q', self.close)

    #USER TAP WITH CARD SIMULATION
        self.bind('c', self.card_inserted)

        self.protocol("WM_DELETE_WINDOW", self.destroy)

#TODO:
'''
Agregar en la base de datos una tarjeta nueva con su nuevo saldo, leer el saldo
y el tipo de tarjeta desde la base de datos 
'''