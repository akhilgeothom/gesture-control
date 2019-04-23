import cv2
import numpy as np
import app
import os
import pyautogui

palm_cascade = cv2.CascadeClassifier('xml/palm.xml')

cap = cv2.VideoCapture(0)
posx = 0
posy = 0
while True:
    ret,img = cap.read()
    grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    palms = palm_cascade.detectMultiScale(grey,1.25,5)
    maxw = maxh = 90
    curx = cury = 0
    for (x,y,w,h) in palms:
        cv2.rectangle(grey, (x,y), (x+w, y+h), (255, 0, 0), 2)
        # print (x,y,w,h)
        if(maxh + maxw < h + w):
            maxh = h
            maxw = w
            curx = x
            cury = y
    # print(curx)
    if (maxh!=90):
        cv2.rectangle(grey, (curx,cury), (curx+maxw, cury+maxh), (0, 255, 0), 2)
    cv2.imshow('img',grey)

    if(posx-10 > curx):
        pyautogui.press('left')
        print('l')

    elif(posx+10 < curx):
        pyautogui.press('right')
        print('r')

    posx = curx
    posy = cury
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    print(posx)
cap.release()
cv2.destroyAllWindows()
