# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 18:51:09 2020

@author: OCAC
"""

#Playing Video-images coming in a frame in a loop
#Whatever we are doing with images we can do it with video but in a loop.
import cv2
cap=cv2.VideoCapture(0) #0 for default camera in laptop
#video file path for video from a file(for more than one camera in system)
#usb bus number for usb camera 1,2,3(for external cameras attached to system)

face_data=r"C:\RAJ\FILES\AIML\Datasets\data\haarcascades\haarcascade_frontalface_alt.xml"
                    #set of previously stored coded faces whic we are importing
classifier=cv2.CascadeClassifier(face_data)

if (cap.isOpened()):
    while True:
        ret,frame=cap.read()     #frame is the current frame(it is a image)
        if frame is not None:     #to confirm that imshow()does not get None type object
            """All operations will be done here"""
            faces = classifier.detectMultiScale(frame) #faces variable gives 4 values(x,y,w,h)
            for x,y,w,h in faces:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                
                
            cv2.imshow('video',frame)
            if cv2.waitKey(1)==ord(' '):
                break                     #ord returns the ascii code of q
        else:
            break
cv2.destroyAllWindows()
cap.release()
