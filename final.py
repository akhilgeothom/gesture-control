# import pkg_resources
# pkg_resources.require("cv2==3.4.5.20")
import cv2
import numpy as np
import pyautogui
import math

pyautogui.FAILSAFE = False

def findDefects():
    cap = cv2.VideoCapture(2)
    kernel=(5,5)
    if(cap.isOpened()==False):
        print('Unable to read camera feed')
    count=0
    global cx;global cy;

    while(True):
        ret, frame = cap.read()
        frame=cv2.resize(frame,(1920,1080))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.bilateralFilter(gray,10,50,50)
        ret,thresh1 = cv2.threshold(blur,110,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
        thresh1 = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, kernel)
        thresh1 = cv2.morphologyEx(thresh1, cv2.MORPH_CLOSE, kernel)

        blah,contours,hierarchy = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        # blah,contours = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        max_area=0;ci=0;

        for i in range(len(contours)):
            cnt=contours[i]
            area = cv2.contourArea(cnt)
            if(area>max_area):
                max_area=area
                ci=i
        cnt = contours[ci]
        hull = cv2.convexHull(cnt)
        moments = cv2.moments(cnt)
        if moments['m00']!=0:
            cx = int(moments['m10']/moments['m00'])
            cy = int(moments['m01']/moments['m00'])

        #print(cx,cy,end='\r')
        center = (cx,cy)
        pyautogui.moveTo(cx,cy)
        cnt = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)

        drawing = np.zeros(frame.shape,np.uint8)
        frame = cv2.circle(drawing,center,5,[0,255,255],2)
        frame = cv2.drawContours(drawing,[cnt],0,(0,255,0),2)
        frame = cv2.drawContours(drawing,[hull],0,(0,0,255),2)

        hull = cv2.convexHull(cnt,returnPoints = False)

        defects = cv2.convexityDefects(cnt,hull)

        if defects is None:
            continue

        mind=0;maxd=0;i=0;fin=0;


        for i in range(defects.shape[0]):
            s,e,f,d = defects[i,0]
            start = tuple(cnt[s][0])
            end = tuple(cnt[e][0])
            far = tuple(cnt[f][0])
            dist = cv2.pointPolygonTest(cnt,center,True)
            frame = cv2.line(frame,start,end,[255,0,0],2)
            frame = cv2.circle(frame,far,5,[0,0,255],-1)
            a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
            b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
            c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
            angle = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))
            if angle <= math.pi / 2:
                fin+=1
                #cv2.circle(drawing, far, 8, [211, 84, 0], -1)
        #print('fingers=',fin)


        cv2.imshow('frame',frame)
        if cv2.waitKey(5) & 0xFF == 27:
            break
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
        if(fin<=3):
            count=count+1
            clicker(count)
            

    cap.release()
    cv2.destroyAllWindows()

def clicker(count1):
    #print('yo',count1)
    #print(cx,cy)
    pyautogui.click(cx,cy,2,0,'left')

cx=0;cy=0;
findDefects()