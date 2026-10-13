from flask import Flask, render_template, request
from PIL import Image
import numpy as np
import cv2
from clarity_analysis import blur_metric, sobel, robert, laplacian_check, roberts_check, sobel_check, score_check
from PIL import Image


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html', msg='')

    image = request.files['file']
    img = Image.open(image)
    img = np.array(img)
    img2 = np.mean(img, axis=2)

    laplace = cv2.Laplacian(img, cv2.CV_32F).var()
    fourier = blur_metric(img2)
    robert1 = robert(img2)
    sobel1 = sobel(img2)

    final_score = (laplacian_check(laplace) + roberts_check(robert1) + sobel_check(sobel1))/3
    rating = score_check(final_score)
    
    print(laplacian_check(laplace))
    print(roberts_check(robert1)) 
    print(sobel_check(sobel1))

    return render_template('index.html', msg='Your image has been uploaded', score = final_score, message = rating, test1 = laplace, test2 = fourier, test3 = robert1, test4 = sobel1)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)