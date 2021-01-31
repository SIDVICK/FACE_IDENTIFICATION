import cv2
from tkinter import*

root = Tk()


def myClick():

# Load the cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam. 
    cap = cv2.VideoCapture(0)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')

    while True:
    # Read the frame
        _, img = cap.read()
    # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # Display
        cv2.imshow('img', img)
    # Stop if escape key is pressed
        k = cv2.waitKey(30) & 0xff
        if k==27:
            break
# Release the VideoCapture object
    cap.release()

myLabel = Label(root, text="Please click here to identify your face")
myLabel.pack()
btn= Button(root, text= "IDENTIFY", command=myClick)
btn.pack()

lbl =  Label(root,  text=" This is part 1 for authentication, where i have written code to identify face through webcam . will be integratiing it with authentication module")
lbl.pack()

root.mainloop()
