import cv2
import numpy as np


def variance_of_laplacian(image_path):
    image = cv2.imread(image_path)
    grayscale = cv2.cvtColor(image, cv2.CV_64F)
    return float(cv2.Laplacian(grayscale, cv2.CV_64F).var())

def blur_metric(image_path):
    fft_image = np.fft.fft2(image_path)
    return float(np.mean(np.log(np.abs(fft_image))))

def sobel(image_path):
    sobelx = cv2.Sobel(image_path, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(image_path, cv2.CV_64F, 0, 1, ksize=5)
    sobelxy = cv2.add(sobelx, sobely)
    return float(sobelxy.var())


def robert(image_path):
    kernelx = np.array([[1, 0], [0, -1]])
    kernely = np.array([[0, 1], [-1, 0]])
    img_robertx = cv2.filter2D(image_path, -1, kernelx)
    img_roberty = cv2.filter2D(image_path, -1, kernely)
    robert_cross = cv2.add(img_robertx, img_roberty)
    return float(robert_cross.var())
