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
    imagefile = request.files['imageperson']
    
    image_path = 'static/UploadImage/person.jpg'
    
    imagefile.save(image_path)
    action = request.form['submit_action']
    if(action == 'Gợi ý mẫu áo phù hợp'):
        imagelist2 = os.listdir('static/recommentData/type0')
        imagelist2 = ['recommentData/type0/' + image for image in imagelist2]
        url = image_path
        return  render_template('b.html', imageList = imagelist, imageList2 = imagelist2, image_url = url, DL = 'Flex')
    else:
        return "HELLO"
    
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
    # return redirect(url_for('process'))
    return "HELLO"






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