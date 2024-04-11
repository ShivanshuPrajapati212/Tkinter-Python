from tkinter import *

root= Tk()
root.geometry("1080x720")

def hello():
    print("Hello Guys")

def name():
    print("Name is Shivanshu")

class btn():
    def __init__(self, frame):
      self.frame = frame
    #   self.button_no = button_no
    def create(self):
        button = Button(self.frame,fg="blue",text="Click me",command=hello)
        button.pack(side=LEFT,padx=20)

f = Frame(root, borderwidth=2,bg='red',relief=SUNKEN)
f.pack(side=TOP,anchor='nw')
f2 = Frame(root, borderwidth=2,bg='red',relief=SUNKEN)
f2.pack(side=TOP,anchor='nw')
f3 = Frame(root, borderwidth=2,bg='red',relief=SUNKEN)
f3.pack(side=TOP,anchor='nw')
f4 = Frame(root, borderwidth=2,bg='red',relief=SUNKEN)
f4.pack(side=TOP,anchor='nw')
f5 = Frame(root, borderwidth=2,bg='red',relief=SUNKEN)
f5.pack(side=TOP,anchor='nw')

b1 = Button(f,fg="blue",text="Click me",command=hello)
b1.pack(side=LEFT,padx=20)
b2 = Button(f,fg="blue",text="NAme Pls", command=name)
b2.pack(side=LEFT,padx=20)
b3 = Button(f,fg="blue",text="Click me")
b3.pack(side=LEFT,padx=20)
b4 = Button(f,fg="blue",text="Click me")
b4.pack(side=LEFT,padx=20)

b5 = Button(f2,fg="blue",text="Click me",command=hello)
b5.pack(side=LEFT,padx=20)
b6 = Button(f2,fg="blue",text="NAme Pls", command=name)
b6.pack(side=LEFT,padx=20)
b7 = Button(f2,fg="blue",text="Click me")
b7.pack(side=LEFT,padx=20)
b8 = Button(f2,fg="blue",text="Click me")
b8.pack(side=LEFT,padx=20)
 
b9 = Button(f3,fg="blue",text="Click me",command=hello)
b9.pack(side=LEFT,padx=20)
b10 = Button(f3,fg="blue",text="NAme Pls", command=name)
b10.pack(side=LEFT,padx=20)
b11 = Button(f3,fg="blue",text="Click me")
b11.pack(side=LEFT,padx=20)
b12 = Button(f3,fg="blue",text="Click me")
b12.pack(side=LEFT,padx=20)
 
b13 = Button(f4,fg="blue",text="Click me",command=hello)
b13.pack(side=LEFT,padx=20)
b14 = Button(f4,fg="blue",text="NAme Pls", command=name)
b14.pack(side=LEFT,padx=20)
b15 = Button(f4,fg="blue",text="Click me")
b15.pack(side=LEFT,padx=20)
b16 = Button(f4,fg="blue",text="Click me")
b16.pack(side=LEFT,padx=20)
 
b17 = Button(f5,fg="blue",text="Click me",command=hello)
b17.pack(side=LEFT,padx=20)
b18 = Button(f5,fg="blue",text="NAme Pls", command=name)
b18.pack(side=LEFT,padx=20)
b19 = Button(f5,fg="blue",text="Click me")
b19.pack(side=LEFT,padx=20)
b20 = Button(f5,fg="blue",text="Click me")
b20.pack(side=LEFT,padx=20)
 
b1 = btn(f)
b1.create()
b2 = btn(f)
b2.create()
b3 = btn(f)
b3.create()
b1 = btn(f)
b1.create()
b1 = btn(f)
b1.create()
b1 = btn(f)
b1.create()
b1 = btn(f)
b1.create()
b1 = btn(f)
b1.create()
b1 = btn(f)
b1.create()
b1 = btn(f)
b1.create()
b1 = btn(f)
b1.create()

root.mainloop()