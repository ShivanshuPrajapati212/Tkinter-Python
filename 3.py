from tkinter import *

root = Tk()

root.geometry("1080x720")

root.minsize(1080,720)
root.maxsize(1080,720)

#Image

photo = PhotoImage(file='Image.png')

label = Label(image=photo)
label.pack()


root.mainloop()