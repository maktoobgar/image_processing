import os
import random
import numpy as np
import cv2
from matplotlib import pyplot as plt
from scipy.stats import gaussian_kde


current_dir = os.path.dirname(os.path.realpath(__file__))


def sp_noise(image, prob):
    """
    Add salt and pepper noise to image
    prob: Probability of the noise
    """
    output = np.zeros(image.shape, np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output


def main():
    # Load the image
    img = cv2.imread(current_dir + "/img.jpeg", cv2.IMREAD_GRAYSCALE)

    plt.figure("Original Image", figsize=(6, 6))
    plt.subplot(211)
    plt.title("Original Image")
    plt.imshow(img, "gray", vmin=0, vmax=255)
    plt.subplot(212)
    hist_full = cv2.calcHist([img], [0], None, [256], [0, 256])
    plt.plot(hist_full)

    mean = 0
    var = 0.01
    sigma = np.sqrt(var)
    gaussian_noise = np.random.normal(loc=mean, scale=sigma, size=img.shape) * 60

    gaussian_img = np.uint8(img + gaussian_noise)
    plt.figure("Gaussian Noised Image", figsize=(6, 6))
    plt.subplot(211)
    plt.title("Gaussian Noised Image")
    plt.imshow(gaussian_img, "gray", vmin=0, vmax=255)
    plt.subplot(212)
    hist_full = cv2.calcHist([gaussian_img], [0], None, [256], [0, 256])
    plt.plot(hist_full)

    image = img.astype(np.float64)
    noise_std = 0.2
    noise = np.random.rayleigh(noise_std, img.shape)

    rayleigh_img = cv2.addWeighted(image, 1, noise, 70, 0.0).astype(np.uint8)
    plt.figure("Rayleigh Noised Image", figsize=(6, 6))
    plt.subplot(211)
    plt.title("Rayleigh Noised Image")
    plt.imshow(rayleigh_img, "gray", vmin=0, vmax=255)
    plt.subplot(212)
    hist_full = cv2.calcHist([rayleigh_img], [0], None, [256], [0, 256])
    plt.plot(hist_full)

    shape, scale = 0.5, 1
    gamma_noise = np.random.gamma(shape, scale, size=img.shape)

    gamma_img = cv2.addWeighted(image, 1, gamma_noise, 70, 0.0).astype(np.uint8)
    plt.figure("Gamma Noised Image", figsize=(6, 6))
    plt.subplot(211)
    plt.title("Gamma Noised Image")
    plt.imshow(gamma_img, "gray", vmin=0, vmax=255)
    plt.subplot(212)
    hist_full = cv2.calcHist([gamma_img], [0], None, [256], [0, 256])
    plt.plot(hist_full)

    exponential_noise = np.random.exponential(5, size=img.shape)

    exponential_img = cv2.addWeighted(image, 1, exponential_noise, 5, 0.0).astype(
        np.uint8
    )
    plt.figure("Exponential Noised Image", figsize=(6, 6))
    plt.subplot(211)
    plt.title("Exponential Noised Image")
    plt.imshow(exponential_img, "gray", vmin=0, vmax=255)
    plt.subplot(212)
    hist_full = cv2.calcHist([exponential_img], [0], None, [256], [0, 256])
    plt.plot(hist_full)

    lower_limit = -2
    upper_limit = 3

    uniform_noise = np.random.uniform(lower_limit, upper_limit, size=img.shape)
    uniform_img = cv2.addWeighted(image, 1, uniform_noise, 5, 0.0).astype(np.uint8)
    plt.figure("Uniform Noised Image", figsize=(6, 6))
    plt.subplot(211)
    plt.title("Uniform Noised Image")
    plt.imshow(uniform_img, "gray", vmin=0, vmax=255)
    plt.subplot(212)
    hist_full = cv2.calcHist([uniform_img], [0], None, [256], [0, 256])
    plt.plot(hist_full)

    sp_noise_img = sp_noise(image, 0.05)
    plt.figure("Salt And Pepper Noised Image", figsize=(6, 6))
    plt.subplot(211)
    plt.title("Salt And Pepper Noised Image")
    plt.imshow(sp_noise_img, "gray", vmin=0, vmax=255)
    plt.subplot(212)
    hist_full = cv2.calcHist([sp_noise_img], [0], None, [256], [0, 256])
    plt.plot(hist_full)

    plt.show()


if __name__ == "__main__":
    main()
