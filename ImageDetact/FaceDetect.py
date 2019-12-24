import numpy as np
import cv2
import datetime

cap = cv2.VideoCapture(0)
frame_rate = cap.get(5)
draw_speed = 6
prev_faces = []
frame_counter = frame_rate
# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # draw the text and timestamp on the frame
    # text = 'Rec'
    # cv2.putText(frame, "Room Status: {}".format(text), (10, 20),
    #    cv2.FONT_HERSHEY_TRIPLEX , .5, (0, 0, 0), 1)
    # cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S %p"),
    #     (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
 

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_counter = frame_counter % draw_speed
    if frame_counter == 0:
        # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 6)
        prev_faces = faces
    else:
        faces = prev_faces
    frame_counter = frame_counter + 1

    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        # Detect eyes
        eyes = eye_cascade.detectMultiScale(roi_gray)
        # Draw rectangle around the eyes
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 2)


    # Display the resulting frame
    cv2.imshow('Original frame', frame)
    #cv2.imshow('HSV frame', hsv)
    #cv2.imshow('GRAY frame', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()