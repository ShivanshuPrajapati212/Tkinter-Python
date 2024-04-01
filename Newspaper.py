from tkinter import *
import os
from PIL import Image , ImageTk

# Base 

root = Tk()

root.title("Newspaper GUI by ShivanshuWeb")
root.geometry("1080x720")

# Neccesary Variables 

directory = 'D:\\Code Playground\\Tkinter Python\\Images'
txt_directory = 'D:\\Code Playground\\Tkinter Python\\Texts'
files = os.listdir('D:\\Code Playground\\Tkinter Python\\Images')
txts = os.listdir('D:\\Code Playground\\Tkinter Python\\Texts')
i = 0
s = 0
tk_images =[]

image_paths = [os.path.join(directory, item) for item in files if os.path.isfile(os.path.join(directory, item))]
txt_names = [file for file in os.listdir(txt_directory) if file.endswith('.txt')]

# Title 

title_label = Label(text="Newspaper GUI by ShivanshuWeb",bg='blueviolet',fg='white',font='comicsansms 15 bold',padx=2000,pady=5)
title_label.pack(anchor='center',side='top',fill=Y)


# Main Content 

for image_path in image_paths:
    image = Image.open(image_path)
    image =  image.resize((100,100),Image.Resampling.BICUBIC)
    tk_image = ImageTk.PhotoImage(image)
    tk_images.append(tk_image)

for tk_image in tk_images:
    label = Label(root, image=tk_image)
    label.pack(anchor='nw',padx=50,pady=50)


for txt_name in txt_names:
    txt_path = os.path.join(txt_directory, txt_name)
    with open(txt_path,'r') as f:
        content = f.read()
    text_label = Label(text=content,font='comicsansms 12',padx=50,pady=50)
    text_label.pack(side="right",anchor='center')
    
    



# Loop 
root.mainloop()