import json
import numpy as np

from flask import Flask
from flask import request
from PIL import Image
from keras.models import load_model
from keras.applications.xception import preprocess_input



MODEL = load_model('models/Xception_best.h5')


app = Flask("Kitchenware Classification")


@app.route('/classify_img', methods=['POST'])
def classifier():
    input_img = request.get_json()

    # im = Image.open(requests.get(inputImg['im'], stream=True).raw)
    picture = Image.open(f'{input_img["img_name"]}')
    picture = picture.resize((299, 299))

    arr = np.array(picture)
    arr = np.expand_dims(arr, axis=0)
    arr = preprocess_input(arr)

    prediction = MODEL.predict([arr])
    classes = {'cup': 0, 'fork': 1, 'glass': 2, 'knife': 3, 'plate': 4, 'spoon': 5}
    label = prediction[0]
    results = {i: round(float(j), 2) for i, j in zip(classes.keys(), label)}
    return json.dumps(results)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5050)
