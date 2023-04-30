import jetson.inference
import jetson.utils
import numpy as np 
import time
import cv2
import os
from gtts import gTTS
import threading
from playsound import playsound

speak=True
item="welcome to sight sense"
confidence=0
itemold=''
width=1280
height=720
flip=2
def sayItem():
    global speak
    global item
    while True:
        if speak == True:
            output=gTTS(text=item, lang='en',slow=False)
            output.save('/home/smartglass/Desktop/pypro/output.mp3')
            #os.system('mpg123 /home/smartglass/Desktop/pypro/output.mp3')
            playsound('output.mp3')
            speak=False
x=threading.Thread(target=sayItem, daemon=True)
x.start()


cam=cv2.VideoCapture('/dev/video0')
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
net=jetson.inference.imageNet('googlenet')
font=cv2.FONT_HERSHEY_SIMPLEX
timeMark=time.time()
fpsFilter=0

while True:
    ret, frame=cam.read()
    img=cv2.cvtColor(frame,cv2.COLOR_BGR2RGBA).astype(np.float32)
    img=jetson.utils.cudaFromNumpy(img)
    
    if speak==False:
        classID, confidence = net.Classify(img,width,height)
        if confidence>=.5:
            item = net.GetClassDesc(classID)                                                                                                                                                                    
            if item != itemold:
                speak=True
                
        if confidence<.5:
            item=''
        itemold=item
    dt=time.time()-timeMark
    timeMark=time.time()
    fps=1/dt
    fpsFilter=.95*fpsFilter + .05 *fps
    cv2.putText(frame,str(round(fpsFilter,1))+" "+item+"  "+str(round(confidence,2)),(0,30),font,1,(0,0,255),2)
    cv2.imshow('WebCam',frame)
    cv2.moveWindow('nanoCam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
