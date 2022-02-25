from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from yolov5.detect import run
app = Flask(__name__)

#업로드 HTML 렌더링
@app.route('/upload')
def render_file():
    return render_template('upload.html')


#파일 업로드 처리
@app.route('/fileUpload', methods = ['GET', 'POST'])
def upload_file():

    if request.method == 'POST':
          f = request.files['file']
          f.save('static/food/' + secure_filename(f.filename))
          files = os.listdir("static")
          run(weights= 'best.pt',
          source = 'static/food/' + f.filename,
          imgsz= (512, 512),
          project='static/detect-output',
          name = 'exp',
          exist_ok=True)
          return render_template('view.html', img=f.filename)

if __name__ == '__main__':
    #서버 실행
    app.run(host = "127.0.0.1", port = "5000", debug = True)
