from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Digital Clock")
root.geometry("500x250")
root.configure(bg="black")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

# Use the font after installing DS-Digital
label = Label(root, font=("DS-Digital", 80), background="black", foreground="cyan")
label.pack(anchor='center', pady=20)

time()
root.mainloop()
