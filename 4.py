from tkinter import *

root = Tk()

root.geometry("1080x720")
root.title("GUI With Shivanshu")

# root.minsize(1080,720)
# root.maxsize(1080,720)

title_label = Label(text="""
bg: The normal background color displayed behind the label and indicator.
fg: This option specifies the color of the text (foreground color). If you are displaying a bitmap, this is the color that will appear at the position of the 1-bits in the bitmap.
padx: Extra space added to the left and right of the text within the widget. Default is 1.
pady: Extra space added above and below the text within the widget. Default is 1.
relief: Specifies the appearance of a decorative border around the label. There are five types of reliefs, such that FLAT, RAISED, SUNKEN, GROOVE, RIDGE. The default is FLAT.
font: If you are displaying text in this label (with the text or textvariable option), the font option specifies the style, size, and other characteristics (i.e. bold, italic, etc.) of the font, and in this style, the text will be displayed.
text: To display one or more lines of text in a label widget, set this option to a string containing the text. Internal newlines (“\n”) will force a line break.
justify: Specifies how multiple lines of text will be aligned with respect to each other: LEFT for flush left, CENTER for centered (the default), or RIGHT for right-justified.
height: The vertical dimension of the new frame.
width: The horizontal dimension of the new frame. If this option is not set, the label will be sized to fit its contents.
""",bg = "red",fg="white",padx=50,pady=50,font='comicsansms 12 bold',borderwidth=3,relief=SUNKEN)
title_label.pack(anchor='center',side='top',fill=X)


root.mainloop()