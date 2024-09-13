from flask import Flask, render_template,request, redirect, url_for
import os
from PIL import Image
app = Flask(__name__)

ficFlolder = os.path.join('static', 'displayData')

@app.route('/', methods = ['GET'])
def hello_world():
    imagelist = os.listdir('static/displayData')
    
    imagelist = ['displayData/' + image for image in imagelist]
    
    return render_template('b.html', imageList = imagelist)
    
@app.route('/', methods = ['POST'])
def predict_image():
    imagelist = os.listdir('static/displayData')
    imagelist = ['displayData/' + image for image in imagelist]
    # imagefile = request.files['imageperson']
    
    # image_path = 'images/' + imagefile.filename
    
    # imagefile.save(image_path)
    # l = request.form['imageclothes02']
    # if len(l)<1:
    #     imagefileclothe = request.files['imageclothes01']
    #     image_path = 'images/clothes.jpg'
    #     imagefileclothe.save(image_path)
    # else:
    #     imagefileclothe = request.form['imageclothes02']
    #     imagefileclothe = imagefileclothe.replace('http://127.0.0.1:5000/','')
    #     img = Image.open(imagefileclothe)
    #     img.save('images/clothes.jpg')

    # return render_template('b.html', imageList = imagelist)
    return redirect(url_for('process'))

@app.route('/process', methods = ['GET'])
def process():
    path1 = "static/displayData/aaa.jpg"
    path2 = "static/displayData/bbb.jpg"
    
    return render_template('process.html', item01 = path1, item02 = path2, item03 = path2)

@app.route('/process', methods = ['POST'])
def back():
    return redirect(url_for('hello_world'))
    
    
if __name__ == "__main__":
    app.run()