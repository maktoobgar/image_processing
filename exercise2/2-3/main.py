import os
import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt


current_dir = os.path.dirname(os.path.realpath(__file__))


class FileManager:
    __content = list[int]
    __content_size = 0
    __current_byte = 0
    __current_two_bits = 0

    def __init__(self, content: list[int]) -> None:
        self.__content = content
        self.__content_size = len(content)
        self.__current_byte = 0
        self.__current_two_bits = 0

    def get_two_bits(self) -> list:
        if self.__current_byte >= self.__content_size:
            return [0, 0]

        filter = -1
        shift_amount = -1
        match self.__current_two_bits:
            case 0:
                filter = 0b11000000
                shift_amount = 6
            case 1:
                filter = 0b00110000
                shift_amount = 4
            case 2:
                filter = 0b00001100
                shift_amount = 2
            case 3:
                filter = 0b00000011
                shift_amount = 0

        output = (filter & self.__content[self.__current_byte]) >> shift_amount

        self.__current_two_bits += 1
        if self.__current_two_bits > 3:
            self.__current_two_bits = 0
            self.__current_byte += 1

        return [1, output]

    def save_two_bits(self, byte: int) -> None:
        if len(self.__content) == 0:
            self.__content.append(0)

        filter = 0b00000011
        shift_amount = -1
        match self.__current_two_bits:
            case 0:
                shift_amount = 6
            case 1:
                shift_amount = 4
            case 2:
                shift_amount = 2
            case 3:
                shift_amount = 0

        self.__content[self.__current_byte] = self.__content[self.__current_byte] | (
            (filter & byte) << shift_amount
        )

        self.__current_two_bits += 1
        if self.__current_two_bits > 3:
            self.__current_two_bits = 0
            self.__current_byte += 1
            self.__content.append(0)

        return filter & byte

    def content(self) -> list[int]:
        return self.__content


def encrypt() -> None:
    # Load the image
    img = cv2.imread(current_dir + "/img.jpg", cv2.IMREAD_GRAYSCALE)

    modified_img = img & 0b11111100

    # Load file
    file = open(current_dir + "/text.txt", "rb")
    byte_list = list(file.read())
    file.close()

    # Load the file into FileManager and then do encryption
    content = FileManager(byte_list)
    for i in range(len(img)):
        for j in range(len(img[i])):
            data = content.get_two_bits()
            if data[0] == 0:
                break
            modified_img[i][j] = modified_img[i][j] | data[1]

    plt.figure("Original Image", figsize=(6, 6))
    plt.subplot(121)
    plt.title("Original Image")
    plt.imshow(img, "gray")
    plt.subplot(122)
    plt.title("Embeded Image")
    plt.imshow(modified_img, "gray")
    plt.show()


# def decrypt() -> None:
#     # Load the image
#     img = cv2.imread(current_dir + "/encrypted.jpg", cv2.IMREAD_GRAYSCALE)

#     content = FileManager([])
#     for i in range(len(img)):
#         for j in range(len(img[i])):
#             bits = content.save_two_bits(img[i][j])

#     file = open(current_dir + "/decrypt.txt", "wb")
#     file.write(bytes(content.content()))
#     file.close()


if __name__ == "__main__":
    encrypt()
    # if len(sys.argv) > 1:
    #     if sys.argv[1] == "encrypt":
    #         encrypt()
    #     elif sys.argv[1] == "decrypt":
    #         decrypt()
