from tkinter import *

root = Tk()
root.geometry("500x300")

Label(root, text="Welcome to ShivanshuWeb",font="comisansms 15 bold").grid(row=0,column=3)


def getinfo():
    print(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),foodservicevalue.get()}")
    with open('Checkbox.txt','a') as f:
        f.write(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),foodservicevalue.get()}")



# Text Labels
name = Label(root,text="Name")
phone = Label(root,text="Phone")
gender = Label(root,text="Gender")

# Packing
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)


# Variables Creation
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
foodservicevalue = IntVar()

# Making Entry Boxes
name_entry = Entry(root,textvariable=namevalue)
phone_entry = Entry(root,textvariable=phonevalue)
gender_entry = Entry(root,textvariable=gendervalue)

# Packing
name_entry.grid(row=1,column=3)
phone_entry.grid(row=2,column=3)
gender_entry.grid(row=3,column=3)

# MARK: CheckBox Creation
foodservice = Checkbutton(text="Want To get Food?", variable=foodservicevalue)
foodservice.grid(row=4,column=3)

# Button Creation and assigning it a command
submit_btn = Button(text="Submit",command=getinfo)
submit_btn.grid(row=5,column=3)



root.mainloop()