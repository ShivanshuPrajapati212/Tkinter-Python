import tkinter as tk
from PIL import Image, ImageTk
import os

def bulk_pack_images(directory):
    # Get a list of all image files in the directory
    image_files = [file for file in os.listdir(directory) if file.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

    # Create a canvas to display the images
    canvas = tk.Canvas(root)
    canvas.pack()

    # Loop through the image files and pack them onto the canvas
    for i, image_file in enumerate(image_files):
        # Open the image file using PIL
        image = Image.open(os.path.join(directory, image_file))

        # Resize the image if needed
        if image.width > 400 or image.height > 400:
            image.thumbnail((400, 400))

        # Convert the image to Tkinter-compatible format
        tk_image = ImageTk.PhotoImage(image)

        # Create a label to display the image on the canvas
        label = tk.Label(canvas, image=tk_image)
        label.image = tk_image  # Keep a reference to the image to prevent garbage collection
        label.pack()

        # Add some spacing between images
        canvas.create_line(0, (i + 1) * 400, 800, (i + 1) * 400)

# Create the Tkinter window
root = tk.Tk()
root.title("Bulk Image Packer")

# Specify the directory containing the images
image_directory = "D:/Code Playground/Tkinter Python"

# Call the function to bulk pack the images onto the canvas
bulk_pack_images(image_directory)

# Start the Tkinter event loop
root.mainloop()
