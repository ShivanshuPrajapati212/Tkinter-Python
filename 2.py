from tkinter import *

root = Tk()  # Making the root object for Tkinter

#Logic GUI

root.geometry("1080x720")  # Width X Height

root.maxsize(1080,720)
root.minsize(1080,720)

label = Label(text="This is a Label")
label.pack()

root.mainloop()  # Staring the while loop

