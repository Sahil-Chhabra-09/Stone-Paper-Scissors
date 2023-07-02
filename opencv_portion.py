import cv2 as cv


#defining a video capture object
vid = cv.VideoCapture(0);


while True:
    ret, frame = vid.read();    #setting up an infinite loop to read frames
    if not ret or frame is None: break
    cv.imshow('HiiQt', frame)   #to show frames in the video
    
    #this is to take only the last identical bytes which is of 8bit int value.(0xFF in hexadecimal is = 11111111 in binary)
    if cv.waitKey(1) & 0xFF == ord('q') : break
    
#release the vid capture object
vid.release()
cv.destroyAllWindows()