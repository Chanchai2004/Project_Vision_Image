import tkinter as tk
from tkinter import filedialog, Toplevel
import cv2
from PIL import Image, ImageTk

def upload_image():
    # Open file dialog to select an image
    file_path = filedialog.askopenfilename()
    if file_path:
        # Read the image using OpenCV
        global img
        img = cv2.imread(file_path)
        # Display the original image
        display_image(img, original_label)
        # Open the pop-up dialog for further options
        open_options_dialog()

def open_options_dialog():
    global width_entry, height_entry  # Declare these as global to access them in other functions
    options_dialog = Toplevel(root)
    options_dialog.title("Image Options")

    # Create radio buttons for "RGB" and "Grayscale"
    rgb_radio = tk.Radiobutton(options_dialog, text="RGB", variable=option, value="RGB")
    grayscale_radio = tk.Radiobutton(options_dialog, text="Grayscale", variable=option, value="Grayscale")
    rgb_radio.pack()
    grayscale_radio.pack()

    # Create text boxes for width and height
    width_label = tk.Label(options_dialog, text="Width:")
    width_label.pack()
    width_entry = tk.Entry(options_dialog)
    width_entry.pack()

    height_label = tk.Label(options_dialog, text="Height:")
    height_label.pack()
    height_entry = tk.Entry(options_dialog)
    height_entry.pack()

    # Create a button to resize and display the image
    resize_button = tk.Button(options_dialog, text="Resize and Display", command=resize_and_display)
    resize_button.pack()

def resize_and_display():
    if img is not None:
        # Get the selected option
        selected_option = option.get()
        
        # Get the desired width and height from the text boxes
        width = int(width_entry.get())  # width_entry is now global
        height = int(height_entry.get())  # height_entry is now global
        
        # Resize the image
        resized_img = cv2.resize(img, (width, height))
        
        # Convert to grayscale if selected
        if selected_option == "Grayscale":
            resized_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
            resized_img = cv2.cvtColor(resized_img, cv2.COLOR_GRAY2RGB)
        else:
            resized_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB)
        
        # Display the resized image
        display_image(resized_img, resized_label)

def display_image(image, label):
    # Convert the image to RGB (OpenCV uses BGR by default)
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Convert the image to a format suitable for Tkinter
    img_pil = Image.fromarray(img_rgb)
    img_tk = ImageTk.PhotoImage(img_pil)
    # Display the image in the label
    label.config(image=img_tk)
    label.image = img_tk

# Set up the main GUI window
root = tk.Tk()
root.title("Image Upload and Resize")

# Create a StringVar to store the selected option
option = tk.StringVar(value="RGB")

# Create labels to display the original and resized images
original_label = tk.Label(root)
original_label.pack(side="left")

resized_label = tk.Label(root)
resized_label.pack(side="right")

# Automatically open the file dialog when the program starts
root.after(0, upload_image)

# Run the GUI event loop
root.mainloop()
