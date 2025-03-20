from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk 
from tkinter import messagebox 
import mysql.connector 
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 35, "bold"), bg="white", fg="darkblue")
        title_lbl.place(x=0, y=0, width=1300, height=45)

        # Top Image
        img_top=Image.open(r"college_images\face_detector1.jpg")
        img_top = img_top.resize((1350, 300), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_1bl = Label(self.root, image=self.photoimg_top)
        f_1bl.place(x=0, y=55, width=1350, height=300)

        # Train Data Button
        b1_1 = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2", font=("times new roman", 30, "bold"), bg="red", fg="white")
        b1_1.place(x=0, y=340, width=1350, height=45)

        # Bottom Image
        img_bottom = Image.open(r"college_images\ttrain.jpg")
        img_bottom = img_bottom.resize((1350, 300), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_1bl = Label(self.root, image=self.photoimg_bottom)
        f_1bl.place(x=0, y=387, width=1350, height=300)

    def train_classifier(self):
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')  # Convert image to grayscale
            imageNp = np.array(img,'uint8')

            # Extract the label from the file name (assuming the label is in the filename)
            id=int(os.path.split(image)[1].split('.')[1])  # Assuming filename format: <label>.jpg
            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13

        ids = np.array(ids)

        # Train the classifier using LBPH
        clf = cv2.face.LBPHFaceRecognizer_create()

        clf.train(faces, ids)
        clf.write("classifier.xml")  # Save the trained model

        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()


