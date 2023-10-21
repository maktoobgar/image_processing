import os
import numpy as np
import cv2
from matplotlib import pyplot as plt

current_dir = os.path.dirname(os.path.realpath(__file__))

# Load the image
img = cv2.imread(current_dir + "/img.png", cv2.IMREAD_GRAYSCALE)

# Convert the image to grayscale
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# Define the piecewise function
def piecewise_function(gray):
    return np.piecewise(
        gray,
        [gray <= 28, gray > 28],
        [lambda x: x, lambda x: (4.829787234 * x) - 107.234042553],
    )


# Create a lookup table
lookup_table = np.zeros((256,), dtype=np.uint8)
lookup_table[:76] = piecewise_function(np.arange(256))[:76]
lookup_table[76:] = np.arange(256)[76:]

# Apply the lookup table to the grayscale image
result = cv2.LUT(img, lookup_table)

# Display the result
plt.subplot(221)
plt.imshow(result, "gray")

# Create histogram
hist_full = cv2.calcHist([result], [0], None, [256], [0, 256])
plt.subplot(222)
plt.plot(hist_full)

# Powerlaw
lookup_table[:] = np.arange(256)
lookup_table[:] = np.int64(np.round(np.power(lookup_table, 0.4) * 27.79227563))
result2 = cv2.LUT(img, lookup_table)

# Display the result
plt.subplot(223)
plt.imshow(result2, "gray")

# Create histogram
hist_full = cv2.calcHist([result2], [0], None, [256], [0, 256])
plt.subplot(224)
plt.plot(hist_full)
plt.show(block=True)

# Wait for just one button press
