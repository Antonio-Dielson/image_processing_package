import cv2
import numpy as np

def find_differences(image_path1, image_path2, output_path):
    image1 = cv2.imread(image_path1)
    image2 = cv2.imread(image_path2)

    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    difference = cv2.absdiff(gray1, gray2)

    _, difference = cv2.threshold(difference, 30, 255, cv2.THRESH_BINARY)

    cv2.imwrite(output_path, difference)
    print(f"Imagem das diferenças salva em: {output_path}")
