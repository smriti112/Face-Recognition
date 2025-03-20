import cv2
import os

# Set the correct path to the Haar Cascade file
cascade_path = r"C:\path_to_folder\haarcascade_frontalface_default.xml"  # Replace with the correct path

# Check if the file exists at the given path
if not os.path.exists(cascade_path):
    print(f"Error: The file at {cascade_path} does not exist!")
else:
    # Load the Haar Cascade Classifier
    faceCascade = cv2.CascadeClassifier(cascade_path)

    if faceCascade.empty():
        print("Error: Unable to load the Haar Cascade classifier.")
    else:
        print("Haar Cascade classifier loaded successfully.")

