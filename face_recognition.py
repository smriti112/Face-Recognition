from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os
import numpy as np
from datetime import datetime

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x690+0+0")
        self.root.title("Face Recognition System")

        # Title Label
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1370, height=35)

        # 1st Image (Top Image)
        img_top = Image.open(r"college_images\face_detector1.jpg")  # Ensure this path is correct
        img_top = img_top.resize((650, 590), Image.LANCZOS)  # Use LANCZOS instead of ANTIALIAS
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_1bl_top = Label(self.root, image=self.photoimg_top)
        f_1bl_top.place(x=0, y=55, width=650, height=590)  # Label for the first image

        # 2nd Image (Bottom Image)
        img_bottom = Image.open(r"college_images\phone.jpg")  # Ensure this path is correct
        img_bottom = img_bottom.resize((750, 590), Image.LANCZOS)  # Use LANCZOS instead of ANTIALIAS
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_1bl_bottom = Label(self.root, image=self.photoimg_bottom)
        f_1bl_bottom.place(x=650, y=55, width=750, height=590)  # Label for the second image

        # Face Recognition Button
        b1_1 = Button(f_1bl_bottom, text="Face Recognition", cursor="hand2", font=("times new roman", 18, "bold"), bg="Red", fg="yellow", command=self.face_recog)
        b1_1.place(x=275, y=520, width=200, height=35)  # Ensure button is visible in the bottom image area

    # Mark attendance function
    def mark_attendance(self, roll, name, department):
        with open("attendance.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split(",")
                name_list.append(entry[0])

            # If student not already marked, then mark attendance
            if roll not in name_list:
                now = datetime.now()
                date = now.strftime("%d/%m/%Y")
                time = now.strftime("%H:%M:%S")
                f.writelines(f"\n{roll},{name},{department},{time},{date},Present")

    # Face Recognition function
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)

                # Predict face
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                # Connect to the MySQL database
                conn = mysql.connector.connect(host="localhost", username="root", password="W7301@jqir#", database="Face_Recogniser")
                my_cursor = conn.cursor()

                my_cursor.execute(f"SELECT Name, Roll, Dep FROM student WHERE Student_id = {id}")
                result = my_cursor.fetchone()

                if result:
                    name, roll, department = result
                    if confidence > 70:
                        cv2.putText(img, f"Roll: {roll}", (x, y - 55), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Name: {name}", (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Dept: {department}", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 3)

                        # Mark attendance
                        self.mark_attendance(roll, name, department)
                    else:
                        cv2.putText(img, "Unknown", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
                else:
                    cv2.putText(img, "Unknown", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)

            return img

        # Load classifiers
        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            if not ret:
                break
            img = draw_boundary(img, face_cascade, 1.1, 10, (255, 0, 0), "Face", clf)
            cv2.imshow("Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Enter key to exit
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()

