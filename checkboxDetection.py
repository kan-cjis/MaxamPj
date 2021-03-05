import os
import cv2
import numpy as np


# line_min_width=15
# image_path = 'form2.jpg'
def detect_box(image_path, line_min_width=15):
    image = cv2.imread(image_path)
    gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    th1, img_bin = cv2.threshold(gray_scale, 150, 225, cv2.THRESH_BINARY)
    kernal_h = np.ones((1, line_min_width), np.uint8)
    kernal_v = np.ones((line_min_width, 1), np.uint8)
    img_bin_h = cv2.morphologyEx(~img_bin, cv2.MORPH_OPEN, kernal_h)
    img_bin_v = cv2.morphologyEx(~img_bin, cv2.MORPH_OPEN, kernal_v)
    img_bin_final = img_bin_h | img_bin_v
    final_kernel = np.ones((3, 3), np.uint8)
    img_bin_final = cv2.dilate(img_bin_final, final_kernel, iterations=1)
    ret, labels, stats, centroids = cv2.connectedComponentsWithStats(~img_bin_final, connectivity=8, ltype=cv2.CV_32S)
    return stats, labels, img_bin_final,image


stat2, label2,finalpic,image = detect_box(image_path='form2crop.jpg', line_min_width=15)
for x,y,w,h,area in stat2[2:]:
    finalpic2 = cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

# cv2.imshow("binary3", finalpic)
cv2.imshow("binary4", finalpic2)
cv2.waitKey(0)

