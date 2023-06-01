import numpy as np
import tensorflow as tf
from PIL import Image
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__, static_folder='static', template_folder='templates')
model = tf.keras.models.load_model('keras_model.h5')

class_names = ['결막염', '정상']  # 클래스 이름 리스트


@app.route('/')
def dsf():
    return render_template('main.html')


# 업로드 HTML 렌더링

@app.route('/upload')
def render_file():
    return render_template('upload.html')


# 파일 업로드 처리
@app.route('/fileUpload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        # 저장할 경로 + 파일명
        f.save(secure_filename(f.filename))

        # 예측할 이미지를 읽어오고 전처리 작업 수행
        image = Image.open(f)
        image = image.resize((224, 224))
        image = np.expand_dims(image, axis=0)
        image = tf.keras.applications.mobilenet_v2.preprocess_input(image)

        # 예측 수행
        prediction = model.predict(image)
        class_index = np.argmax(prediction)  # 가장 높은 확률 값을 가진 클래스의 인덱스
        class_name = class_names[class_index]  # 클래스 이름
        result = {'class_name': class_name}  # 클래스 이름 반환

        # 결과를 result.html 템플릿에 전달하여 렌더링
        return render_template('result.html', result=result['class_name'])


if __name__ == '__main__':
    # 서버 실행
    app.run(debug=True)
