import os
import numpy as np
import cv2
from matplotlib import pyplot as plt


# Define the piecewise function
def piecewise_function(lookup_table):
    return np.piecewise(
        lookup_table,
        [lookup_table <= 28, lookup_table > 28],
        [lambda x: x, lambda x: (4.829787234 * x) - 107.234042553],
    )


current_dir = os.path.dirname(os.path.realpath(__file__))

# Load the image
img = cv2.imread(current_dir + "/img.png", cv2.IMREAD_GRAYSCALE)

# Convert the image to grayscale
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

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

# Powerlaw Calculation
plt.figure("Powerlaw Image", figsize=(6, 6))
lookup_table[:] = np.arange(256)
lookup_table[:] = np.int64(np.round(np.power(lookup_table, 0.4) * 27.79227563))
result2 = cv2.LUT(img, lookup_table)

# Powerlaw image
plt.subplot(211)
plt.title("Powerlaw Image")
plt.imshow(result2, "gray")

# Powerlaw histogram
hist_full = cv2.calcHist([result2], [0], None, [256], [0, 256])
plt.subplot(212)
plt.title("Histogram of Powerlaw Image", loc="left")
plt.plot(hist_full)
plt.show(block=True)

# Wait for just one button press
