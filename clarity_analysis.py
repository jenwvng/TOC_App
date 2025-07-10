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


def laplacian_check(value):
    good = 250
    mid = 120
    bad = 40

    mid_score = 5
    bad_score = 3

    if value >= good:
        score = 10
    elif value < good and value >= mid:
        a = value - mid
        b = good - mid
        c = a / b
        score = c + 5
    elif value < mid and value >= bad:
        score = (value - bad) * ((mid_score-bad_score)/(mid-bad)) + bad_score
    elif value < bad:
        score = value * bad_score/bad
    return score


def roberts_check(value1):
    good = 700
    mid = 50
    bad = 75

    mid_score = 5
    bad_score = 3

    if value1 >= good:
        score = 10
    elif value1 < good and value1 >= mid:
        a = value1 - mid
        b = good - mid
        c = a / b
        score = c + 5
    elif value1 < mid and value1 >= bad:
        score = (value1 - bad) * ((mid_score-bad_score)/(mid-bad)) + bad_score
    elif value1 < bad:
        score = value1 * bad_score/bad
    return score


def sobel_check(value2):
    good = 750000
    mid = 50000
    bad = 25000

    mid_score = 5
    bad_score = 3

    if value2 >= good:
        score = 10
    elif value2 < good and value2 >= bad:
        a = value2 - mid
        b = good - mid
        c = a / b
        score = c + 5
    elif value2 < mid and value2 >= bad:
        score = (value2 - bad) * ((mid_score-bad_score)/(mid-bad)) + bad_score
    elif value2 < bad:
        score = value2 * bad_score/bad
    return score


def score_check(value3):
    msg = ""
    if value3 >= 10:
        msg = "The clarity is amazing"
    elif value3 < 10 and value3 >= 6:
        msg = "The clarity is good"
    elif value3 < 6 and value3 >= 3:
        msg = "The clarity is subpar"
    elif value3 < 3:
        msg = "The clarity is terrible"
    return msg


print(roberts_check(120))