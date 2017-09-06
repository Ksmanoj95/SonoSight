import numpy as np
import cv2

yellow = (253,243,0)
boundary= (0,165,233)
orange = (255,127,40)
royalblue = (63,71,204)
crimson = (238,53,67)

## Create a black image
img = np.zeros((340,640,3), np.uint8)
cv2.rectangle(img,(25,25),(610,310),boundary,3)
cv2.line(img,(280,280),(380,280),royalblue,3)
cv2.line(img,(280,42),(380,42),yellow,3)
cv2.line(img,(45,125),(45,205),royalblue,3)
cv2.line(img,(590,125),(590,205),crimson,3)

contours1 = [np.array([[45,45],[100,45],[45,100],[45,45]])]
cv2.drawContours(img,contours1,0,yellow,-1)

contours2 = [np.array([[540,45],[595,45],[595,100],[540,45]])]
cv2.drawContours(img,contours2,0,orange,-1)

contours3 = [np.array([[595,225],[595,280],[540,280],[595,225]])]
cv2.drawContours(img,contours3,0,orange,-1)

contours4 = [np.array([[45,225],[45,280],[100,280],[45,225]])]
cv2.drawContours(img,contours4,0,royalblue,-1)

img1 = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)

cv2.imshow('win',img1)
cv2.waitKey(0)
