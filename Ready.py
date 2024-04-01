from tkinter import *

root = Tk()

root.geometry('500x400')

label = Label(text="Ready",bg='red',fg='white',font='comicsansms 15 bold',padx=2000,pady=10)
label.pack(anchor='center',side='bottom',fill=Y)

root.mainloop()