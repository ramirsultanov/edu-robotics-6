import cv2
import numpy as np
import random as rnd

image = cv2.imread("resources/input.png")

cv2.imshow("original", image)

lev = 0

noised = image.copy()


def process():
    # Noising image
    global noised
    noised = image.copy()
    level = lev
    for i in range(noised.shape[0]):
        for j in range(noised.shape[1]):
            if rnd.random() < level:
                if rnd.randint(0, 1) == 0:
                    noised[i][j] = 0
                else:
                    noised[i][j] = 255
    cv2.imshow("noised", noised)

    mean = np.ones((10, 10), np.float32) / 25
    meaned = cv2.filter2D(noised, -1, mean)
    cv2.imshow("meaned", meaned)

    gaussianed = cv2.GaussianBlur(noised, (5, 5), 0)
    cv2.imshow("gaussianed", gaussianed)

    medianed = cv2.medianBlur(noised, 5)
    cv2.imshow("medianed", medianed)

    bilateralled = cv2.bilateralFilter(noised, 9, 75, 75)
    cv2.imshow("bilateralled", bilateralled)

    laplacian = np.array((
        [0, 1, 0],
        [1, -4, 1],
        [0, 1, 0]), dtype="int")
    laplacianed = cv2.filter2D(noised, -1, laplacian)
    cv2.imshow("laplacianed", laplacianed)

    sobel_x = np.array(
        [[-1, 0, 1],
         [-2, 0, 2],
         [-1, 0, 1]])
    sobel_x_ed = cv2.filter2D(noised, -1, sobel_x)
    cv2.imshow("sobel_x_ed", sobel_x_ed)

    sobel_y = np.array(
        [[-1, -2, -1],
         [0, 0, 0],
         [1, 2, 1]])
    sobel_y_ed = cv2.filter2D(noised, -1, sobel_y)
    cv2.imshow("sobel_y_ed", sobel_y_ed)

    scharr_x = np.array(
        [[-3, 0, 3],
         [-10, 0, 10],
         [-3, 0, 3]])
    scharr_x_ed = cv2.filter2D(noised, -1, scharr_x)
    cv2.imshow("scharr_x_ed", scharr_x_ed)

    scharr_y = np.array(
        [[-3, -10, 3],
         [0, 0, 0],
         [-3, 10, 3]])
    scharr_y_ed = cv2.filter2D(noised, -1, scharr_y)
    cv2.imshow("scharr_y_ed", scharr_y_ed)

    thresh1 = 100
    thresh2 = 200
    cannyed = cv2.Canny(noised, thresh1, thresh2)
    cv2.imshow("cannyed", cannyed)

    cv2.waitKey(1)


process()


def on_slider_change(val):
    global lev
    lev = val / 100
    process()


wName = "slider"
cv2.namedWindow(wName)
sliderName = 'noiseLevel'
cv2.createTrackbar(sliderName, wName, 0, 100, on_slider_change)

exited = False


def on_button_close(arg1, arg2):
    global exited
    exited = True


butName = 'close'
cv2.createButton(butName, on_button_close)

while True:
    key = cv2.waitKey(20) & 0xFF
    if key == 27 or exited:  # ASCII ESCape
        break
