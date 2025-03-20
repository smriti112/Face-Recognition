from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1130x590+0+0")
        self.root.title("Face Recognition System")

        # Title label
        title_lbl = Label(self.root, text="DEVELOPER", font=("times new roman", 35, "bold"), bg="white", fg="BLUE")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Top image
        img_top = Image.open(r"college_images\developer(2).jpg")
        img_top = img_top.resize((1530, 720), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        # Label to display top image
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=720)

        # Main frame
        main_frame = Frame(f_lbl, bd=2, bg="white")
        main_frame.place(x=1000, y=0, width=500, height=600)

        # Developer image
        img_top1 = Image.open(r"college_images\ttrain.jpg")
        img_top1 = img_top1.resize((1530, 720), Image.Resampling.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        # Label to display developer image
        f_lbl1 = Label(main_frame, image=self.photoimg_top1)
        f_lbl1.place(x=300, y=0, width=200, height=200)

        # Developer labels
        dev_label = Label(main_frame, text="ASB", font=("times new roman", 20, "bold"), bg="white")
        dev_label.grid(x=0, y=5)

        dev_label = Label(main_frame, text="Project - E ATTENDANCE", font=("times new roman", 20, "bold"), bg="white")
        dev_label.grid(x=0, y=40)

        # Image 2
        img2 = Image.open(r"college_images\s3.jpg")
        img2 = img2.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        # Label to display image 2
        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=890, y=0, width=450, height=130)


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
