import cv2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture('video\solidWhiteRight.mp4')

while(True):
    ret,frame = cap.read()

    if ret:
        blur = cv2.GaussianBlur(frame,(7,7),0)
        #cv2.imshow('blur', blur)
        gray = cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)
        #cv2.imshow('gray', gray)


        low = np.array([200]) #200/220
        high = np.array([220])


        mask = cv2.inRange(gray,low,high)
        #cv2.imshow('mask', mask)
        canny = cv2.Canny(mask,50,150)
        #cv2.imshow('canny', canny)
        dilated = cv2.dilate(canny, (7, 7), iterations=7)


        roi_mask = np.zeros(dilated.shape,dtype=np.uint8)
        ROI = np.array([[(0,800),(1400,800),(1400,350),(0,350)]])
        cv2.fillPoly(roi_mask,ROI,255)
        

        ROI_canny = cv2.bitwise_and(dilated,roi_mask)        
        try:
            lines = cv2.HoughLinesP(ROI_canny,1,np.pi/180,50,maxLineGap=200,minLineLength=20) # 50/200/20
            for line in lines:
                x1,y1,x2,y2 = line[0]
                m = (y2-y1)/(x2-x1)
                #print('m: ', m, '\n')
                if m < 0: # LEFT CAR LANE
                    cv2.line(frame,(x1,y1),(x2,y2),(255,0,0),5) 
                    #print('LEFT:  x1-x2: ',x1-x2,',  y1-y2:',y1-y2, '\n')
                else: # RIGHT CAR LANE
                    cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),10)
                    #print('RIGHT:  x1-x2: ',x1-x2,',  y1-y2:',y1-y2, '\n')

                # print('x1:',x1,', y1:',y1,', x2:',x2,', y2:',y2, '\n')
        except:
            pass
        cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == 27: # esc退出
        break

cap.release()
cv2.destroyAllWindows()