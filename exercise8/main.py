import os
import numpy as np
import cv2
from matplotlib import pyplot as plt


current_dir = os.path.dirname(os.path.realpath(__file__))


def main():
    # Load the image
    img = cv2.imread(current_dir + "/img.png", cv2.IMREAD_GRAYSCALE)

    plt.figure("Original Image", figsize=(6, 6))
    laplacian = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    plt.subplot(111)
    plt.imshow(img, cmap="gray")

    result = cv2.filter2D(img, -1, kernel=laplacian)

    plt.figure("Laplacian Filters Results", figsize=(6, 6))
    plt.subplot(211)
    plt.imshow(laplacian, cmap="gray")

    plt.subplot(212)
    plt.imshow(result, cmap="gray")

    plt.show()


if __name__ == "__main__":
    main()
