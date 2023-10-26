import os
import numpy as np
import cv2
from matplotlib import pyplot as plt


current_dir = os.path.dirname(os.path.realpath(__file__))


def main():
    # Load the image
    img = cv2.imread(current_dir + "/img.jpg", cv2.IMREAD_GRAYSCALE)

    plt.figure("Original Image", figsize=(6, 6))
    plt.subplot(211)
    plt.title("Original Image")
    plt.imshow(img, "gray", vmin=0, vmax=255)
    plt.subplot(212)
    hist_full = cv2.calcHist([img], [0], None, [256], [0, 256])
    plt.plot(hist_full)

    img_min = np.amin(img)
    img_max = np.amax(img)
    img_org = np.uint8(((img - img_min) / (img_max - img_min)) * (70 - 0) + 0)

    plt.figure("Shrunk Original Image", figsize=(6, 6))
    plt.subplot(211)
    plt.title("Shrunk Original Image")
    plt.imshow(img_org, "gray", vmin=0, vmax=255)
    plt.subplot(212)
    hist_full = cv2.calcHist([img_org], [0], None, [256], [0, 256])
    plt.plot(hist_full)

    img_min = np.amin(img_org)
    img_max = np.amax(img_org)
    img_shrunk = np.uint8(((img_org - img_min) / (img_max - img_min)) * (25 - 0) + 0)

    plt.figure("Shrunk of Shrunk Original Image", figsize=(6, 6))
    plt.subplot(211)
    plt.title("Shrunk of Shrunk Original Image")
    plt.imshow(img_shrunk, "gray", vmin=0, vmax=255)
    plt.subplot(212)
    hist_full = cv2.calcHist([img_shrunk], [0], None, [256], [0, 256])
    plt.plot(hist_full)

    img_min = np.amin(img_shrunk)
    img_max = np.amax(img_shrunk)
    img_stretch = np.uint8(
        ((img_shrunk - img_min) / (img_max - img_min)) * (150 - 0) + 0
    )

    plt.figure("Stretch of Shrunk of Shrunk Original Image", figsize=(6, 6))
    plt.subplot(211)
    plt.title("Stretch of Shrunk of Shrunk Original Image")
    plt.imshow(img_stretch, "gray", vmin=0, vmax=255)
    plt.subplot(212)
    hist_full = cv2.calcHist([img_stretch], [0], None, [256], [0, 256])
    plt.plot(hist_full)

    img_slide = img_stretch + 105

    plt.figure("Slide of Stretch of Shrunk of Shrunk Original Image", figsize=(6, 6))
    plt.subplot(211)
    plt.title("Slide of Stretch of Shrunk of Shrunk Original Image")
    plt.imshow(img_slide, "gray", vmin=0, vmax=255)
    plt.subplot(212)
    hist_full = cv2.calcHist([img_slide], [0], None, [256], [0, 256])
    plt.plot(hist_full)

    img_stretch_minus_img_org = img_stretch - img_org

    plt.figure(
        "Stretch of Shrunk of Shrunk Original Image Minus Shrunk Original Image",
        figsize=(6, 6),
    )
    plt.subplot(211)
    plt.title("Stretch of Shrunk of Shrunk Original Image Minus Shrunk Original Image")
    plt.imshow(img_stretch_minus_img_org, "gray", vmin=0, vmax=255)
    plt.subplot(212)
    hist_full = cv2.calcHist([img_stretch_minus_img_org], [0], None, [256], [0, 256])
    plt.plot(hist_full)

    img_org_minus_img_stretch = img_org - img_stretch

    plt.figure(
        "Shrunk Original Image Minus Stretch of Shrunk of Shrunk Original Image",
        figsize=(6, 6),
    )
    plt.subplot(211)
    plt.title("Shrunk Original Image Minus Stretch of Shrunk of Shrunk Original Image")
    plt.imshow(img_org_minus_img_stretch, "gray", vmin=0, vmax=255)
    plt.subplot(212)
    hist_full = cv2.calcHist([img_org_minus_img_stretch], [0], None, [256], [0, 256])
    plt.plot(hist_full)

    img_org_minus_img_shrunk = img_org - img_shrunk

    plt.figure(
        "Shrunk Original Image Minus Shrunk of Shrunk Original Image", figsize=(6, 6)
    )
    plt.subplot(211)
    plt.title("Shrunk Original Image Minus Shrunk of Shrunk Original Image")
    plt.imshow(img_org_minus_img_shrunk, "gray", vmin=0, vmax=255)
    plt.subplot(212)
    hist_full = cv2.calcHist([img_org_minus_img_shrunk], [0], None, [256], [0, 256])
    plt.plot(hist_full)

    plt.show()


if __name__ == "__main__":
    main()
