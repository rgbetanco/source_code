import tkinter as tk
import Dispence as ds
import Recharge as rc

class Ads(tk.Tk):

    def close(self, event):
        self.destroy()

    def dispence(self, event):
        ds.Dispence()

    def recharge(self, event):
        rc.Recharge(self.sales_card)

    def __init__(self):
        super().__init__()
        self.title('Videos Promocionales')
        self.geometry('1024x600')

        self.label = tk.Label(self, text='Inserte tarjeta (d) / (r)')
        self.label.pack(expand=True)

        #TODO: Change to read user card
        self.bind('d', self.dispence)

        #TODO: Change to read manager card
        self.sales_card = 'ABC'
        self.bind('r', self.recharge)

        self.bind('q', self.close)

        self.protocol("WM_DELETE_WINDOW", self.destroy)
        self.mainloop()

