########################## Import ########################

from logging import root
import tkinter as tk
from tkinter import *

#import tkmacosx as tkMac
from tkinter import ttk
# import datetime
# from tkinter import messagebox
# import time


class sap:
    def __init__(self, root):
            self.root=root

            frame=Frame(root, bg='white', width=250, height=250)
            frame.pack(fill=BOTH)
            text=Label(frame, text='Hier schrijf je u tekst neer'
            '\n'
            '\n'
            '\ninformation about us here'
            '\n'
            '\n'
            '\nthis application was created by' 
            '\n'
            '\nChristoph Kenens',font='ariall 10 bold',bg='white',fg='Black')
            text.place(x=15,y=10)

def main():        
    root = tk.Tk()
    app=sap(root)
    root.title("Sap")
    root.geometry("250x250+250+200")
    root.resizable(0, 0)
    root.mainloop()

if __name__=='__main__':
    main()
