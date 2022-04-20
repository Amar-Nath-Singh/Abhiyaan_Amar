import cv2
import numpy as np
def nothing(x):
    pass
cap = cv2.VideoCapture('bolt_test_pothole.mp4')
while(cap.isOpened()):
    lower_range = np.array([200, 200, 200])
    upper_range = np.array([255, 255, 255])
    ret, img = cap.read()
    if ret:
        frame = img[370:,150:1080]
        mask = cv2.inRange(frame, lower_range, upper_range)
        contours,hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 600 and area < 3500:
                x,y,w,h = cv2.boundingRect(contour)
                if w < 120 and h < 60:
                    x=x+150
                    y=y+370
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.imshow("Frame",img)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
