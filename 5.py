from tkinter import *

root = Tk()


root.geometry("1080x720")

f1 = Frame(root,bg="red",borderwidth=5,relief=SUNKEN)
f1.pack(side=LEFT,fill=Y)
f2 = Frame(root,bg="blue",borderwidth=5,relief=SUNKEN)
f2.pack(side=TOP,fill=X)
f3 = Frame(root,bg="blueviolet",borderwidth=5,relief=SUNKEN)
f3.pack(side=BOTTOM,fill=X)
f4 = Frame(root,bg="green",borderwidth=5,relief=SUNKEN)
f4.pack(side=TOP,fill="both")



l1 = Label(f1,text="Hierchey ",bg='red',fg='white',font='Comicsansms 15 bold')
l1.pack(pady=150,padx=25)
l2 = Label(f2,text="Welcome To VS Code ",bg='blue',fg='white',font='Comicsansms 15 bold')
l2.pack(pady=15)
l3 = Label(f3,text="Terminal",bg='blueviolet',fg='white',font='Comicsansms 15 bold')
l3.pack(pady=50)
l4 = Label(f4,text="Main Code",bg='green',fg='white',font='Comicsansms 15 bold')
l4.pack(pady=(30,730))







root.mainloop()