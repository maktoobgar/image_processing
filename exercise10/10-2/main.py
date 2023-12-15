import os
import numpy as np
import cv2
from matplotlib import pyplot as plt


current_dir = os.path.dirname(os.path.realpath(__file__))


def calculate_snr(noisy_image, original_image):
    original = np.int32(original_image)
    noisy = np.int32(noisy_image)

    noisy_to_power_two = noisy * noisy
    sum_of_noisy_to_power_two = np.sum(noisy_to_power_two)

    diff = noisy - original
    diff_to_power_two = diff * diff
    sum_of_diff_to_power_two = np.sum(diff_to_power_two)

    snr = sum_of_noisy_to_power_two / sum_of_diff_to_power_two

    return snr


def main():
    # Load the image
    img = cv2.imread(current_dir + "/img.jpg", cv2.IMREAD_GRAYSCALE)

    snr = calculate_snr(img, img)
    plt.figure("Original Image", figsize=(6, 6))
    plt.subplot(211)
    plt.title("snr = " + str(snr))
    plt.imshow(img, "gray", vmin=0, vmax=255)
    plt.subplot(212)
    cosine_transform = cv2.dct(np.float32(img), cv2.DCT_INVERSE)
    plt.imshow(np.log(abs(cosine_transform) + 1), cmap="gray")
    xlen = len(cosine_transform[0])
    ylen = len(cosine_transform)

    for j in range(ylen):
        for i in range(xlen):
            if ((-1.3328125 * i) + 853 - j) < 0:
                cosine_transform[j][i] = 0

    reconstructed_image = cv2.idct(cosine_transform)
    snr = calculate_snr(reconstructed_image, img)
    plt.figure("Half High Freq Removed Image", figsize=(6, 6))
    plt.subplot(211)
    plt.title("snr = " + str(snr))
    plt.imshow(reconstructed_image, "gray", vmin=0, vmax=255)
    plt.subplot(212)
    plt.imshow(np.log(abs(cosine_transform) + 1), cmap="gray")

    for j in range(ylen):
        for i in range(xlen):
            if ((-1.090415913 * i) + 603 - j) < 0:
                cosine_transform[j][i] = 0

    reconstructed_image = cv2.idct(cosine_transform)
    snr = calculate_snr(reconstructed_image, img)
    plt.figure("75% High Freq Removed Image", figsize=(6, 6))
    plt.subplot(211)
    plt.title("snr = " + str(snr))
    plt.imshow(reconstructed_image, "gray", vmin=0, vmax=255)
    plt.subplot(212)
    plt.imshow(np.log(abs(cosine_transform) + 1), cmap="gray")

    for j in range(ylen):
        for i in range(xlen):
            if ((-1.332167832 * i) + 381 - j) < 0:
                cosine_transform[j][i] = 0

    reconstructed_image = cv2.idct(cosine_transform)
    snr = calculate_snr(reconstructed_image, img)
    plt.figure("90% High Freq Removed Image", figsize=(6, 6))
    plt.subplot(211)
    plt.title("snr = " + str(snr))
    plt.imshow(reconstructed_image, "gray", vmin=0, vmax=255)
    plt.subplot(212)
    plt.imshow(np.log(abs(cosine_transform) + 1), cmap="gray")

    plt.show()


if __name__ == "__main__":
    main()
