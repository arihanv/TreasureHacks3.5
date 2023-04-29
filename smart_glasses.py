#importing required libraries
# import jetson.inference
# import jetson.utils
import numpy as np 
import jetson


import cv2
#Initializing the variables
talk=True
#welcome message
object="welcome to Smart glasses"
confidence=0
old_object=''
# print(cv2._version_)
#dimentions of the video frame
width=1280
height=720
flip=2

import time
#to detect the object
import os
#to convert text to speech
from gtts import gTTS
import threading

#creating function to make it speak
def speak():
    #global variables
    global talk
    global object
    while True:
        #this is to create an audio file using gTTS library
        if talk == True:
            #This line makes the model to speak slowly in english language
            output=gTTS(text=object, lang='en',slow=False)
            #saving the audio output in mp3 format
            output.save('audio.mp3')
            #this mwill gives audio single to the speakers
            os.system('mpg123 audio.mp3')
            #after completing the 1 single we need to stop the model, other wise it keep on saying the same object again and again
            talk=False
x=threading.Thread(target=speak, daemon=True)
x.start()

#to cpature video from the web camera
cam=cv2.VideoCapture('/dev/video0')
#intializing the dimentions of the frame
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
#intializing the dimensions of the frame
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
#google net is an pre trainned model which has a capability
#to detect the object and recognize it
net=jetson.inference.imageNet('googlenet')
#for font of the text
font=cv2.FONT_HERSHEY_SIMPLEX
timeMark=time.time()
fpsFilter=0

#creating the function
while True:
    #after capturing the image we need to read it inorder to recoginse the object
    ret, frame=cam.read()
    img=cv2.cvtColor(frame,cv2.COLOR_BGR2RGBA).astype(np.float32)
    img=jetson.utils.cudaFromNumpy(img)
    #instead of speaking the every object it assumed we are making the model to speak only if it have a confidence over 60%
    if talk==False:
        classID, confidence = net.Classify(img,width,height)
        if confidence>=.6:
            object=net.GetClassDesc(classID)
            if object!=old_object:
                talk=True
        #if the model is not confident enough of the object, it won't say anything
        if confidence<.4:
            object=''
        old_object=object

    dt=time.time()-timeMark
    timeMark=time.time()
    fps=1/dt
    fpsFilter=.95*fpsFilter + .05 *fps
    #the line that prints the results on the top of the frame
    cv2.putText(object+"  "+str(round(confidence,2)),(0,30),font,1,(255,255,255),2)
    cv2.imshow('WebCam',frame)
    cv2.moveWindow('nanoCam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()