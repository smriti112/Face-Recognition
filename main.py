from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1130x590+0+0")
        self.root.title("Face Recognition System")

        img = Image.open(r"college_images/Stanford.jpg")  # Fixed path
        img = img.resize((700, 130), Image.Resampling.LANCZOS)  # Updated resize method
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=600, height=130)

        img1 = Image.open(r"college_images/fface.png")  # Fixed path
        img1 = img1.resize((450, 130), Image.Resampling.LANCZOS)  # Updated resize method
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=460, y=0, width=450, height=130)

        img2 = Image.open(r"college_images/u.jpg")  # Fixed path
        img2 = img2.resize((400, 130), Image.Resampling.LANCZOS)  # Updated resize method
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=850, y=0, width=450, height=130)

        img3 = Image.open(r"college_images/bground.jpg")  # Fixed path
        img3 = img3.resize((1330, 590), Image.Resampling.LANCZOS)  # Updated resize method
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bgimg = Label(self.root, image=self.photoimg3)
        bgimg.place(x=0, y=130, width=1330, height=500)

        title_lbl = Label(bgimg, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",
                          font=("times new roman", 25, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1280, height=37)

        # student button
        img4 = Image.open(r"college_images/student.jpg")  # Fixed path
        img4 = img4.resize((150, 150), Image.Resampling.LANCZOS)  # Updated resize method
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bgimg, image=self.photoimg4, command=self.student_details, cursor="hand2")
        b1.place(x=250, y=70, width=150, height=130)

        b1 = Button(bgimg, text="Student Details", command=self.student_details, cursor="hand2",
                    font=("times new roman", 10, "bold"), bg="darkblue", fg="white")
        b1.place(x=250, y=180, width=150, height=30)

        # Detect face button
        img5 = Image.open(r"college_images/face_detector1.jpg")  # Fixed path
        img5 = img5.resize((150, 150), Image.Resampling.LANCZOS)  # Updated resize method
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bgimg, image=self.photoimg5, cursor="hand2", command=self.face_data)
        b1.place(x=450, y=70, width=150, height=130)

        b1 = Button(bgimg, text="Face Detector", cursor="hand2", command=self.face_data,
                    font=("times new roman", 10, "bold"), bg="darkblue", fg="white")
        b1.place(x=450, y=180, width=150, height=30)

        # Attendance button
        img6 = Image.open(r"college_images/attendance.jpg")  # Fixed path
        img6 = img6.resize((150, 150), Image.Resampling.LANCZOS)  # Updated resize method
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bgimg, image=self.photoimg6, cursor="hand2", command=self.attendance_data)
        b1.place(x=650, y=70, width=150, height=130)

        b1 = Button(bgimg, text="Attendance", cursor="hand2", command=self.attendance_data,
                    font=("times new roman", 10, "bold"), bg="darkblue", fg="white")
        b1.place(x=650, y=180, width=150, height=30)

        # Help button
        img7 = Image.open(r"college_images/help_desk.jpg")  # Fixed path
        img7 = img7.resize((150, 150), Image.Resampling.LANCZOS)  # Updated resize method
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bgimg, image=self.photoimg7, cursor="hand2")
        b1.place(x=850, y=70, width=150, height=130)

        b1 = Button(bgimg, text="Help Desk", cursor="hand2", font=("times new roman", 10, "bold"),
                    bg="darkblue", fg="white")
        b1.place(x=850, y=180, width=150, height=30)

        # Train button
        img8 = Image.open(r"college_images/Train.jpg")  # Fixed path
        img8 = img8.resize((150, 150), Image.Resampling.LANCZOS)  # Updated resize method
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bgimg, image=self.photoimg8, cursor="hand2", command=self.train_data)
        b1.place(x=250, y=250, width=150, height=130)

        b1 = Button(bgimg, text="Train Data", cursor="hand2", command=self.train_data,
                    font=("times new roman", 10, "bold"), bg="darkblue", fg="white")
        b1.place(x=250, y=360, width=150, height=30)

        # Photos button
        img9 = Image.open(r"college_images/photos.jpg")  # Fixed path
        img9 = img9.resize((150, 150), Image.Resampling.LANCZOS)  # Updated resize method
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bgimg, image=self.photoimg9, cursor="hand2", command=self.open_img)
        b1.place(x=450, y=250, width=150, height=130)

        b1 = Button(bgimg, text="Photos", cursor="hand2", command=self.open_img,
                    font=("times new roman", 10, "bold"), bg="darkblue", fg="white")
        b1.place(x=450, y=360, width=150, height=30)

        # Developer button
        img10 = Image.open(r"college_images/developer.jpg")  # Fixed path
        img10 = img10.resize((150, 150), Image.Resampling.LANCZOS)  # Updated resize method
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bgimg, image=self.photoimg10, cursor="hand2")
        b1.place(x=650, y=250, width=150, height=130)

        b1 = Button(bgimg, text="Developer", cursor="hand2", font=("times new roman", 10, "bold"),
                    bg="darkblue", fg="white")
        b1.place(x=650, y=360, width=150, height=30)

        # Exit button
        img11 = Image.open(r"college_images/exit.jpg")  # Fixed path
        img11 = img11.resize((150, 150), Image.Resampling.LANCZOS)  # Updated resize method
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bgimg, image=self.photoimg11, cursor="hand2")
        b1.place(x=850, y=250, width=150, height=130)

        b1 = Button(bgimg, text="Exit", cursor="hand2", font=("times new roman", 10, "bold"),
                    bg="darkblue", fg="white")
        b1.place(x=850, y=360, width=150, height=30)

    def open_img(self):
        os.startfile(r"data")  # Corrected path

    # Function buttons
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
