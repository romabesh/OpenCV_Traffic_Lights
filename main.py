import cv2 as cv
import numpy as np

name = ["green", "red", "yellow"]
path = "img//traffic_lights_"

#[x,y,[b,g,r]]

for filename in name:
    img = cv.imread(path + str(filename) + ".jpg")

    cv.rectangle(img, (20, 50), (120, 150), [0, 0, 255], thickness=1)
    cv.rectangle(img, (20, 175), (120, 275), [0, 255, 255], thickness=1)
    cv.rectangle(img, (20, 290), (120, 390), [0, 255, 0], thickness=1)
    #cv.imshow("img " + str(filename), img)

    #bgr
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    v = hsv[:, :, 2]
    cv.imshow("hsv_" + str(filename), v)

    #столбцы, строки
    red_sum = np.sum(v[50:150, 20:120])
    yellow_sum = np.sum(v[175:275, 20:120])
    green_sum = np.sum(v[290:390, 20:120])

    print(str(red_sum) + " | " + str(yellow_sum) + " | " + str(green_sum))

    if red_sum > yellow_sum and red_sum > green_sum:
        print("Red")
    elif yellow_sum > red_sum and yellow_sum > green_sum:
        print("Yellow")
    elif green_sum > red_sum and green_sum > yellow_sum:
        print("Green")
    else:
        print("Error!")

    cv.imshow(str(filename) + str("_img"), img)

cv.waitKey(0)
cv.destroyAllWindows()