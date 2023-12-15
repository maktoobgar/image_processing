import os
import numpy as np
import cv2
from matplotlib import pyplot as plt
from scipy.stats import entropy


current_dir = os.path.dirname(os.path.realpath(__file__))


def main():
    # Load the image
    img = cv2.imread(current_dir + "/lena.png", cv2.IMREAD_GRAYSCALE)

    # Compute the histogram
    hist, _ = np.histogram(img, bins=256)
    prob_dist = hist / hist.sum()

    # Calculate the entropy
    image_entropy = entropy(prob_dist, base=2)

    plt.figure("Original Image", figsize=(6, 6))
    plt.subplot(211)
    plt.title(str(image_entropy))
    plt.imshow(img, "gray", vmin=0, vmax=255)
    plt.subplot(212)
    plt.plot(hist)

    plt.show()


if __name__ == "__main__":
    main()
