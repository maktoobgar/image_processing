import os
import numpy as np
import cv2
from matplotlib import pyplot as plt


# Define the piecewise function
def piecewise_function(lookup_table):
    return np.piecewise(
        lookup_table,
        [lookup_table <= 28, lookup_table > 28],
        [lambda x: 0, lambda x: (3.191489362 * x) - 89.361702128],
    )


# Define the piecewise function
def piecewise_function_of_another_slide(lookup_table):
    return np.piecewise(
        lookup_table,
        [lookup_table <= 50, lookup_table > 50],
        [lambda x: 0, lambda x: (1.7 * x) - 85],
    )


current_dir = os.path.dirname(os.path.realpath(__file__))

# Load the image
img = cv2.imread(current_dir + "/img.png", cv2.IMREAD_GRAYSCALE)

# Create a lookup table
lookup_table = np.zeros((256,), dtype=np.uint8)
lookup_table[:76] = piecewise_function(np.arange(256))[:76]
lookup_table[76:] = np.arange(256)[76:]

# Apply the lookup table to the grayscale image
result = cv2.LUT(img, lookup_table)

# Show original image + histogram of original image
fig = plt.figure("Original Image", figsize=(6, 6))
plt.subplot(211)
plt.title("Original Image")
plt.imshow(img, "gray")
plt.subplot(212)
plt.title("Histogram of Original Image", loc="left")
hist_full = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist_full)

# Piecewise image
plt.figure("Piecewise Image", figsize=(6, 6))
plt.subplot(211)
plt.title("Piecewise Image")
plt.imshow(result, "gray")

# Piecewise histogram
hist_full = cv2.calcHist([result], [0], None, [256], [0, 256])
plt.subplot(212)
plt.title("Histogram of Piecewise Image", loc="left")
plt.plot(hist_full)

# Create a lookup table
lookup_table = np.zeros((256,), dtype=np.uint8)
lookup_table[50:200] = piecewise_function_of_another_slide(np.arange(256))[50:200]
lookup_table[200:] = 255

# Apply the lookup table to the grayscale image
result = cv2.LUT(img, lookup_table)

# Another Piecewise operation
plt.figure("Piecewise Image, Second Operation", figsize=(6, 6))
plt.subplot(211)
plt.title("Piecewise Image")
plt.imshow(result, "gray")

# Piecewise histogram
hist_full = cv2.calcHist([result], [0], None, [256], [0, 256])
plt.subplot(212)
plt.title("Histogram of Piecewise Image", loc="left")
plt.plot(hist_full)

plt.show(block=True)
