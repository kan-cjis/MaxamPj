from align import autoAlign
import json

import googleOCR
import selectROI
import cv2
import shutil

a = [["Chinese name", 283, 1552, 315, 62],
     ["English name", 899, 1552, 363, 62],
     ["HKID", 284, 1622, 320, 91], ["HKPRY", 1048, 1695, 20, 19], ["HKPRN", 1241, 1695, 19, 19],
     ["plzSpecify", 304, 1817, 639, 62],
     ["WorkHKY", 688, 1796, 20, 18], ["WorkHKN", 881, 1795, 19, 20], ["Mobile", 272, 1948, 320, 66],
     ["Email", 919, 1958, 336, 55], ["Flat", 389, 2054, 248, 59],
     ["Floor", 723, 2057, 248, 55], ["Building", 1169, 2052, 251, 61],
     ["Street", 487, 2117, 937, 62], ["District", 497, 2234, 9, 14]]

refImg = "C:/Users/kench/PycharmProjects/pythonProject2/baseline.jpg"
aliImg = "C:/Users/kench/PycharmProjects/pythonProject2/test/demo/TEST6.jpg"
OutputImgPath = "C:/Users/kench/PycharmProjects/pythonProject2/test/demo/alignmentResult.jpg"

autoAlign(refImg, aliImg, OutputImgPath)

HighlightedPath = "C:/Users/kench/PycharmProjects/pythonProject2/test/demo/HighlightedOutput.jpg"
#use this if normal
shutil.copy2(OutputImgPath, HighlightedPath)

# use this without alignment
# OutputImgPath=aliImg
# shutil.copy2(aliImg, HighlightedPath)



########
print("Received scanned image...")
print("Start ROI selection...")


for x in range(a.__len__()):
    CroppedImg = "C:/Users/kench/PycharmProjects/pythonProject2/test/demo/ROI/" + str(a[x][0]) + "_cropped_img.jpg"
    cv2.imwrite(CroppedImg, selectROI.selectROIExtract(a[x][1], a[x][2], a[x][3], a[x][4], OutputImgPath))
    cv2.imwrite(HighlightedPath, selectROI.selectROIHighlight(a[x][1], a[x][2], a[x][3], a[x][4], HighlightedPath))
print("ROI selection finished...")
print("Start OCR handwritten text...")

# for x in range(1):
# for x in range(a.__len__()):
#     resultJSON = googleOCR.googleOCRFunc2("C:/Users/kench/PycharmProjects/pythonProject2/test/demo/ROI/" + str(a[x][0]) + "_cropped_img.jpg")
#     with open("C:/Users/kench/PycharmProjects/pythonProject2/test/demo/ROI/" + str(a[x][0])+'.json', 'w') as jsonfile:
#         json.dump(resultJSON, jsonfile)