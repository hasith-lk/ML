import numpy as np
import cv2
import datetime

cap = cv2.VideoCapture(0)
print ('frame rate ', cap.get(5))


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # draw the text and timestamp on the frame
    text = 'Rec'
    cv2.putText(frame, "Room Status: {}".format(text), (10, 20),
       cv2.FONT_HERSHEY_TRIPLEX , .5, (0, 0, 0), 1)
    cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S %p"),
        (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
 

    # Our operations on the frame come here
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask= mask)



    # Display the resulting frame
    cv2.imshow('Original frame', frame)
    #cv2.imshow('HSV frame', hsv)
    cv2.imshow('GRAY frame', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


#======================
#import cv2
#flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
#print (flags)
#======================