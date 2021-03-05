import os
import cv2
import numpy as np

image_path = 'form2crop.jpg'
image = cv2.imread(image_path)
gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# img_bin is bad performance in alignment form , in maxiam form, full time/part time checkbox can identify rectgular
# box in 3 approach , so maxim might change checkbox by better chance
# th1, img_bin = cv2.threshold(gray_scale, 122, 225, cv2.THRESH_BINARY)
# th3, img_bin2 = cv2.threshold(gray_scale, 0, 225, cv2.THRESH_OTSU)
th2, img_bin = cv2.threshold(gray_scale, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)

img_bin = ~img_bin
# img_bin2 = ~img_bin2
# img_bin3 = ~img_bin3
# cv2.imshow("binary", img_bin)
# cv2.imshow("binary2", img_bin2)
# cv2.imshow("binary3", img_bin3)
# cv2.waitKey(0)
# cv2.imwrite("crop.jpg", crop_img)


# ## selecting min size as 15 pixels Assumption 1: we are assuming a checkbox will be at least 15x15 size. Why? To
# avoid boxes in text getting detected as False positives. Why did I choose 15 pixels? Just a value to get started.
# You might need to change it later depending on our data, or we can set the line_min_width as a function of the
# image size.
line_min_width = 14
kernal_h = np.ones((1, line_min_width), np.uint8)
kernal_v = np.ones((line_min_width, 1), np.uint8)
img_bin_h = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, kernal_h)

# cv2.imshow("binary_h", img_bin_h)
# cv2.waitKey(0)
img_bin_v = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, kernal_v)
img_bin_final = img_bin_h | img_bin_v

_, labels, stats, _ = cv2.connectedComponentsWithStats(~img_bin_final, connectivity=8, ltype=cv2.CV_32S)

# cv2.imshow("binary_h", img_bin_final)
# cv2.waitKey(0)


for x, y, w, h, area in stats[2:]:
    img_bin_final_final = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# cv2.imshow("binary_h", img_bin_final_final)
# cv2.waitKey(0)

final_kernel = np.ones((3, 3), np.uint8)
img_bin_final = cv2.dilate(img_bin_final, final_kernel, iterations=1)
# cv2.imshow("binary_final_final", img_bin_final_final)

cv2.imshow("binary_final", img_bin_final)
cv2.waitKey(0)