
import cv2
import numpy as np

def get_grayscale(img):
    tmp_image = np.array(img)
    return cv2.cvtColor(tmp_image, cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(img):
    tmp_image = np.array(img)
    return cv2.medianBlur(tmp_image,5)

def threshold(img):
    return cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]