from tkinter import *
import pandas as pd
import os

def get_info():
    # Retrieve the values when the button is clicked
    user = user_input.get()
    password = pass_input.get()
    Id = id_input.get()
    
    # Print the values to the console (optional)
    print(user, password, Id)
    
    # Data to append
    data_to_append = {'Username': [user], 'Password': [password], 'Id': [Id]}
    df_to_append = pd.DataFrame(data_to_append)
    
    # Check if the CSV file exists to determine if headers should be written
    file_path = 'D:\\Code Playground\\Tkinter Python\\Input_Form.csv'
    file_exists = os.path.isfile(file_path)
    
    # Append data to the CSV, include header if file does not exist
    df_to_append.to_csv(file_path, mode='a', header=not file_exists, index=False)

root = Tk()
root.geometry("1080x720")

# Create labels and entry widgets
user_label = Label(root, text="Username:")
user_label.grid(row=0, column=0)
pass_label = Label(root, text="Password:")
pass_label.grid(row=1, column=0)
id_label = Label(root, text="Unique Id:")
id_label.grid(row=2, column=0)

uservar = StringVar()
passvar = StringVar()
idvar = StringVar()

user_input = Entry(root, textvariable=uservar)
user_input.grid(row=0, column=1)
pass_input = Entry(root, textvariable=passvar)
pass_input.grid(row=1, column=1)
id_input = Entry(root, textvariable=idvar)
id_input.grid(row=2, column=1)

# Create a submit button
Button(root, text="Submit", command=get_info).grid(row=3, column=0)

root.mainloop()