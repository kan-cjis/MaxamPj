import cv2


def selectROIExtract(x, y, w, h, imageNeedToCrop):
    # GIMP's y coordinate= x variable,already flipped in below code,so plz ignore
    # x = 65
    # y = 522
    # w = 207
    # h = 89

    # img = cv2.imread("form2.jpg")
    img = cv2.imread(imageNeedToCrop)
    cropped_img = img[y:y + h, x:x + w]
    # cv2.imshow("cropped", cropped_img)
    # cv2.waitKey(0)
    # cv2.imwrite("crop.jpg", cropped_img)

    return cropped_img


def selectROIHighlight(x, y, w, h, imageNeedToHighlight):
    img = cv2.imread(imageNeedToHighlight)
    highlighedImg = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # croped_img = img[y:y + h, x:x + w]
    # cv2.imshow("cropped", croped_img)
    # cv2.waitKey(0)
    # cv2.imwrite("crop.jpg", croped_img)

    return highlighedImg
