
import cv2
import numpy as np

def get_grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(img):
    return cv2.medianBlur(img, 3)

def threshold(img):
    return cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]