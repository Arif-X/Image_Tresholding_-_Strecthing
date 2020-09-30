import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read Image
pict = cv2.imread('images.jpeg', 0)

# Change image to gray scale
pic = cv2.cvtColor(pict, cv2.COLOR_BAYER_BG2GRAY)

# Histogram method
def hist(img):
    plt.hist(img.ravel(), 256, [0, 256])
    plt.show()

# Show gray scale original image
cv2.imshow('Original Image', pic)
hist(pic)

# Collecting array
arr = np.zeros((pic.shape[0], pic.shape[1]), dtype='uint8')

# Find max and min value
maximum = np.max(pic)
minimum = np.min(pic)

# Find average value
for i in range(pic.shape[0]):
    for j in range(pic.shape[1]):
        arr[i, j] = 255 * pic[i, j] / (maximum - minimum)

hist(arr)

# The ttretched image
cv2.imshow('Stretching image', arr)

cv2.waitKey(0)
