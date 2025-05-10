"""
Author: Stephen Littman
Date: 4/5/2025
Program: Final Project
Version: 1.0

Description:
This program is a picture reconnaissance tkinter tool that uses collect_all_images to detect a face in an image.
find_matching_faces() has 3 perimeters: image_folder, reference_image, and output_folder and uses all three to do the magic.
The program uses the tkinter library for a GUI that allows the user to select an image file from their computer.
There are 4 buttons in the GUI:
1. Select Image: This button allows the user to select an image file from their computer that will be used for reference_image_path.
Once the image is selected, the program will display the image in the GUI. 
2. Select Folder: This button allows the user to select a folder of images that will be used for image_folder.
Once the folder is selected, the program will display the folder path in the GUI.
3. Select Folder: This button allows the user to select a folder where the output images will be for output folder.
Once the folder is selected, the program will display the folder path in the GUI.
4. Detect Faces: This button detects faces in the selected image and copies the image to the output folder if a face is found.
Once this button is clicked, the program will display a pop up message box indicating that it is processing.
When the processing is complete, the program will display a pop up message box indicating that the processing is complete.


This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
Copyright (C) 2025 Stephen Littman
"""

# Import necessary libraries
import os
import sys
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import scrolledtext
from collect_all_images import find_matching_faces
from PIL import Image, ImageTk 
import turtle
# Import Turtle animation module
import animation



# Constants
THUMBNAIL_SIZE = (120, 120)  # Size for the thumbnail image
ALT_FONT = "TkDefaultFont 8 bold"  # Alternate font for text
LABEL_FONT = "TkDefaultFont 10 bold"  # Font for labels
DEFAULT_FONT = "TkDefaultFont 16 bold"  # Default font for text
SELECTION_BUTTON_PAD = 20  # Padding for selection buttons
LABEL_PAD = 10  # Padding for labels
WIDTH = 800  # Width of the main window
HEIGHT = 600  # Height of the main window
LOGO = "assets\\logo.png"  # Path to the logo image
AUTHOR = "assets\\author.png"  # Path to the author image
ICON = "assets\\favicon.ico"  # Path to the icon image


# Function to get the resource path for PyInstaller to make the (.exe) file.
def resource_path(relative_path):
    # Get absolute path to resource, works for dev and for PyInstaller
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class PictureReconnaissanceApp:
    # This is the main class for the Picture Reconnaissance application.
    def __init__(self, master):
        self.master = master
        # Set the icon for the main window
        master.iconbitmap(resource_path(ICON))  
        # Set the title and size of the main window
        self.master.title("Picture Reconnaissance")
        self.master.geometry(f"{WIDTH}x{HEIGHT}")
        # Set the background color of the main window
        self.master.configure(bg="cyan")  

        # Create a default values for labels that display the image path, folder path and destination folder path
        self.image_path = "No image selected"
        self.image_folder = "No folder selected"
        self.destination_folder = "No destination folder selected"


        # -------------- Startup Animation --------------
        # Create a canvas for the turtle animation
        self.canvas = tk.Canvas(self.master, width=WIDTH, height=HEIGHT)
        self.canvas.pack(fill="both", expand=True)

        # Initiate turtle screen and set the background color
        self.screen = turtle.TurtleScreen(self.canvas)
        self.screen.bgcolor("black")

        # Run animation inside the main window
        self.master.after(1000, animation.draw_animation(self.screen))

        # Delete the turtle to clear the screen
        self.canvas.destroy()  # Delete the turtle to clear the screen
        # ----------- End of Startup Animation -----------


        # __________FRAMES WILL BE REFERED TO AS SCREENS____________
        # -------------------- Create Screens --------------------
        # Create a about frame for about 
        self.about_frame = tk.Frame(self.master, width=WIDTH, height=HEIGHT, bg="green")
        # Create a manual frame
        self.manual_frame = tk.Frame(self.master, width=WIDTH, height=HEIGHT, bg="snow")
        # Create a frame for the main content
        self.main_frame = tk.Frame(self.master, width=WIDTH, height=HEIGHT, bg="cyan")
        self.main_frame.pack(fill="both", expand=True)
        # ------------------- End of Screens --------------


        # ------------------- Create Menu Bar -------------------
        self.menu_bar = tk.Menu(self.master)
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="About", command=self.load_about)
        self.help_menu.add_command(label="User Manual", command=self.load_manual)
        self.menu_bar.add_command(label="Main", command=self.load_main)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)
        self.menu_bar.add_command(label="Exit", command=self.master.quit)
        # Set menu bar color
        self.menu_bar.config(bg="green", fg="black")
        #self.menu_bar.add_cascade(label="Settings", 
        self.master.config(menu=self.menu_bar)
        # ------------------- End of Menu Bar --------------


        # ------------------- Main Screen Widgets -------------------
        # Image label to display the selected image
        self.image_path_label = tk.Label(self.main_frame, text=self.image_path, font=LABEL_FONT)
        self.image_path_label.pack(pady=LABEL_PAD)

        # Buttons for selecting image
        self.select_image_button = tk.Button(self.main_frame, text="Select Image", font=DEFAULT_FONT, command=self.select_image)
        self.select_image_button.pack(pady=SELECTION_BUTTON_PAD)

        # Label to display the image folder path
        self.image_folder_path = tk.StringVar()
        self.image_folder_label = tk.Label(self.main_frame, text=self.image_folder, font=LABEL_FONT)
        self.image_folder_label.pack(pady=LABEL_PAD)
        
        # Button for selecting image folder path
        self.select_folder_button = tk.Button(self.main_frame, text="Select Folder", font=DEFAULT_FONT, command=self.select_folder)
        self.select_folder_button.pack(pady=SELECTION_BUTTON_PAD)

        # Label to display the destination folder path
        self.destination_folder_path = tk.StringVar()
        self.destination_folder_label = tk.Label(self.main_frame, text=self.destination_folder, font=LABEL_FONT)
        self.destination_folder_label.pack(pady=LABEL_PAD)

        # Button for selecting destination folder path
        self.select_destination_button = tk.Button(self.main_frame, text="Select Output Folder", font=DEFAULT_FONT, command=self.select_destination_folder)
        self.select_destination_button.pack(pady=SELECTION_BUTTON_PAD)

        # Button for starting the face detection process
        self.detect_faces_button = tk.Button(self.main_frame, text="Detect Faces", font=DEFAULT_FONT, command=self.detect_faces)
        self.detect_faces_button.pack(pady=LABEL_PAD)

        # ------------------- End of Main Screens Widgets --------------


        # ------------------- About Screen Widgets -------------------
        self.scrollbar = tk.Scrollbar(self.about_frame, orient="vertical")
        # Label for the about section
        self.about_label = tk.Label(self.about_frame, text="About this Author", font=DEFAULT_FONT)
       
        self.about_author_label = tk.Label(self.about_frame, text="Author: Stephen Littman", font=LABEL_FONT)
        # Image of author
        author_image = Image.open(AUTHOR)
        author_image.thumbnail(THUMBNAIL_SIZE)
        self.author_image = ImageTk.PhotoImage(author_image)
        self.author_label = tk.Label(self.about_frame, image=self.author_image, font=LABEL_FONT)
        # Alternate text for the author image
        self.author_alt_text = tk.Label(self.about_frame, text="A picture of the author Stephen Littman.", font=ALT_FONT)

        # Image of logo
        logo_image = Image.open(LOGO)
        logo_image.thumbnail(THUMBNAIL_SIZE)
        self.logo_image = ImageTk.PhotoImage(logo_image)
        self.logo_label = tk.Label(self.about_frame, image=self.logo_image, font=LABEL_FONT)
        # Alternate text for the logo
        self.alt_text = tk.Label(self.about_frame, text="An anarchy sign wearing a jeweled crown.", font=ALT_FONT)

        self.about_github_label = tk.Label(self.about_frame, text="Alias: AnarchKing", font=LABEL_FONT)
        self.about_projects_label = tk.Label(self.about_frame, text="GitHub: github.com/anarchking", font=LABEL_FONT)
        self.about_linkedin_label = tk.Label(self.about_frame, text="Linkedin: www.linkedin.com/in/stephen-littman", font=LABEL_FONT)

        self.about_back_button = tk.Button(self.about_frame, text="Back", font=DEFAULT_FONT, command=self.load_main)
        # ------------------- End of About Screen Widgets --------------


        # ------------------- Manual Screen Widgets -------------------
        self.manual_label = scrolledtext.ScrolledText(self.manual_frame, height=21, font=DEFAULT_FONT)
        self.manual_label.insert(tk.INSERT, "-- User Manual --\n\n")
        self.manual_label.insert(tk.INSERT, "This program is a picture reconnaissance tool that uses Facial Recognition \nto detect a face in an image then copy the image to a new destination.\n\n")
        self.manual_label.insert(tk.INSERT, "1. Select Image: This button allows the user to select an image file from their computer that will be used for reference_image_path.\n\n")
        self.manual_label.insert(tk.INSERT, "2. Select Folder: This button allows the user to select a folder of images that will be used for image_folder.\n\n")
        self.manual_label.insert(tk.INSERT, "3. Select Destination Folder: This button allows the user to select a folder where the output images will be for output folder.\n\n")
        self.manual_label.insert(tk.INSERT, "4. Detect Faces: This button detects faces in the selected image and copies the image to the output folder if a face is found.\n\n")
        self.manual_label.insert(tk.INSERT, "5. Exit: This button closes the application.\n\n")
        self.manual_label.insert(tk.INSERT, "6. Help Menu: This menu allows the user to access the about and user manual sections.\n\n")
        self.manual_label.insert(tk.INSERT, "7. About: This button displays information about the program.\n\n")
        self.manual_label.insert(tk.INSERT, "8. User Manual: This button displays the user manual for the program.\n\n")
        self.manual_label.config(state=tk.DISABLED)  # Disable editing of the text widget
        self.manual_back_button = tk.Button(self.manual_frame, text="Back", font=DEFAULT_FONT, command=self.load_main)
        # ------------------- End of Manual Screen Widgets --------------


    # Methods for loading main screen
    def load_main(self):
        # This method is used to load the main frame of the program.
        # It hides all other frames and shows the main frame.
        self.main_frame.tkraise()
        self.image_path_label.pack(pady=LABEL_PAD)
        self.image_folder_label.pack(pady=LABEL_PAD)
        self.destination_folder_label.pack(pady=LABEL_PAD)
        self.select_image_button.pack(pady=SELECTION_BUTTON_PAD)
        self.select_folder_button.pack(pady=SELECTION_BUTTON_PAD)
        self.select_destination_button.pack(pady=SELECTION_BUTTON_PAD)
        self.detect_faces_button.pack(pady=LABEL_PAD)
        self.about_frame.pack_forget()
        self.manual_frame.pack_forget()
        self.main_frame.pack(fill="both", expand=True)


    # Methods for loading about screen
    def load_about(self):
        # This method is used to load the about section of the program.
        # It hides all other frames and shows the about frame.
        self.about_frame.tkraise()
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.about_label.pack(pady=LABEL_PAD)
        self.about_author_label.pack(pady=LABEL_PAD)
        self.author_label.pack()
        self.author_alt_text.pack()
        self.about_github_label.pack(pady=LABEL_PAD)
        self.about_projects_label.pack(pady=LABEL_PAD)
        self.about_linkedin_label.pack(pady=LABEL_PAD)
        self.logo_label.pack()
        self.alt_text.pack()
        self.about_back_button.pack(pady=LABEL_PAD)
        self.main_frame.pack_forget()
        self.manual_frame.pack_forget()
        self.about_frame.pack(fill="both", expand=True)


    # Methods for loading manual screen
    def load_manual(self):
        # This method is used to load the user manual section of the program.
        # It hides all other frames and shows the user manual frame.
        self.manual_frame.tkraise()
        self.manual_label.pack(pady=LABEL_PAD)
        self.manual_back_button.pack(pady=LABEL_PAD)
        self.main_frame.pack_forget()
        self.about_frame.pack_forget()
        self.manual_frame.pack(fill="both", expand=True)


    # Method for selecting an image file
    # This method opens a file dialog to select an image file and displays it in the GUI.
    # It also sets the image_path variable to the selected file path.
    def select_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if self.image_path:
            self.display_image(self.image_path)
            print(f"Selected image: {self.image_path}")
        else:
            print("No image selected.")
            messagebox.showerror("Error", "No image selected.")


    # Method for displaying the selected image in the GUI
    # This method takes the image path as an argument, opens the image, and displays it in a label.
    # It also resizes the image to fit preview.
    def display_image(self, image_path):
        image = Image.open(image_path)
        image.thumbnail(THUMBNAIL_SIZE)
        self.image = ImageTk.PhotoImage(image)
        self.image_path_label.config(image=self.image)
        self.image_path_label.image = self.image
        self.image_path_label.pack(pady=20)


    # Method for selecting a folder of images
    # This method opens a file dialog to select a folder 
    # and sets the image_folder variable to the selected folder path.
    # It also displays the folder path in the GUI.
    def select_folder(self):
        self.image_folder = filedialog.askdirectory()
        if self.image_folder:
            print(f"Selected folder: {self.image_folder}")
            self.image_folder_label.config(text=self.image_folder)
        else:
            print("No folder selected.")
            messagebox.showerror("Error", "No folder selected.")


    # Method for selecting a destination folder
    # This method opens a file dialog to select a destination folder
    # and sets the destination_folder variable to the selected folder path.
    # It also displays the folder path in the GUI.
    def select_destination_folder(self):
        self.destination_folder = filedialog.askdirectory()
        if self.destination_folder:
            print(f"Selected output folder: {self.destination_folder}")
            self.destination_folder_label.config(text=self.destination_folder)
        else:
            print("No output folder selected.")
            messagebox.showerror("Error", "No output folder selected.")


    # Method for detecting faces in the selected image
    # This method checks if the image, folder, and destination folder are selected.
    # If they are, it calls the find_matching_faces function from the collect_all_images module
    # to process the images in the selected folder and copy matching images to the destination folder. 
    def detect_faces(self):
        if not self.image_path or not self.image_folder or not self.destination_folder:
            messagebox.showerror("Error", "Please select an image, folder, and destination folder.")
            return

        messagebox.showinfo("Processing", "Processing... Please wait.")
        try:
            print(f"Processing images in {self.image_folder} with reference image {self.image_path} and output folder {self.destination_folder}")
            find_matching_faces(self.image_folder, self.image_path, self.destination_folder)
            messagebox.showinfo("Success", "Processing complete. Matching images copied to output folder.")
        except Exception as e:
            print(f"Error: {e}")
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            self.image_path_label.config(image="")
            self.image_path_label.image = None
            self.image_path = ""
            self.image_folder = ""
            self.destination_folder = ""
            print("Resetting image, folder, and output folder.")


# Main function to run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = PictureReconnaissanceApp(root)
    root.mainloop()