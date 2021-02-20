"""
Authors:
    Liat Cohen  205595283
    Adir Biran  308567239
    12/2020
"""

from tkinter import *
from PIL import ImageTk, Image


# Scrollable frame class
class ScrollableFrame:
    def __init__(self, root, height, image_size, images_per_row, pad_x, pad_y, back_ground='white'):
        # init frame's parameters
        self.back_ground = back_ground
        self.image_size = image_size
        self.images_per_row = images_per_row
        self.pad_x = pad_x
        self.pad_y = pad_y

        # Main frame
        self.main_frame = Frame(root, relief=GROOVE, width=50, height=50, bg=self.back_ground)
        self.main_frame.pack()

        # Inner canvas
        self.canvas = Canvas(self.main_frame, width=self.image_size*images_per_row + self.pad_x*(images_per_row+2), height=height, bg=self.back_ground)
        self.window = Frame(self.canvas, bg=self.back_ground)

        # Scrollbar
        scroll_bar = Scrollbar(self.main_frame, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=scroll_bar.set)
        scroll_bar.pack(side="right", fill="y")

        # Creating the window
        self.canvas.pack(side="left")
        self.canvas.create_window((0, 0), window=self.window, anchor='n')
        self.window.bind("<Configure>", self.configure_scrolling)

    # Filling the images with the commands
    def fill_data(self, images_paths, command_bind_on_click):

        # Indexes for the grid
        i = 1
        j = 1

        # Looping each image
        for path in images_paths:
            img = Image.open(path)
            img = img.resize((self.image_size, self.image_size), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            image = Button(self.window, image=img, bg=self.back_ground, command=lambda r=path: command_bind_on_click(r))
            image.image = img
            image.grid(row=j, column=i, padx=self.pad_x, pady=self.pad_y)

            # Pictures per row
            if i % self.images_per_row == 0:
                j += 1
                i = 0
            i += 1

    # Configuring the scrolling function
    def configure_scrolling(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

