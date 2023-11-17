import os
import numpy as np
import cv2
from matplotlib import pyplot as plt


current_dir = os.path.dirname(os.path.realpath(__file__))


def main():
    # Load the image
    img1 = cv2.imread(current_dir + "/1.png", cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(current_dir + "/2.png", cv2.IMREAD_GRAYSCALE)
    img3 = cv2.imread(current_dir + "/3.png", cv2.IMREAD_GRAYSCALE)

    plt.figure("First Image", figsize=(6, 6))
    plt.subplot(211)
    plt.title("Original Image")
    plt.imshow(img1, "gray", vmin=0, vmax=255)
    plt.subplot(212)
    img1_fourier = np.fft.fftshift(np.fft.fft2(img1))
    plt.imshow(np.log(abs(img1_fourier)), cmap="gray")

    plt.figure("Second Image", figsize=(6, 6))
    plt.subplot(211)
    plt.title("Original Image")
    plt.imshow(img2, "gray", vmin=0, vmax=255)
    plt.subplot(212)
    img2_fourier = np.fft.fftshift(np.fft.fft2(img2))
    plt.imshow(np.log(abs(img2_fourier)), cmap="gray")

    plt.figure("Third Image", figsize=(6, 6))
    plt.subplot(211)
    plt.title("Original Image")
    plt.imshow(img3, "gray", vmin=0, vmax=255)
    plt.subplot(212)
    img3_fourier = np.fft.fftshift(np.fft.fft2(img3))
    plt.imshow(np.log(abs(img3_fourier)), cmap="gray")

    plt.show()


if __name__ == "__main__":
    main()
