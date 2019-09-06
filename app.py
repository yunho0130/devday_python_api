from flask import Flask, request, jsonify
from flask.json import JSONEncoder
import keras
import numpy as np

app = Flask(__name__)

@app.route("/hello", methods=['GET']) 
def hello():
    return "hello world", 200

@app.route("/predict_price", methods=['POST']) 
def model1():
    payload = request.json
    input_features = np.array([list(payload['features'])])
    model = keras.models.load_model('keras_house_price_model_v1.h5')
    result = {
	    'model name': 'house price predict model', 
	    'api ver': '1.2',
	    'predict result': str(model.predict(input_features[0:1])[0][0])
    }
    return jsonify(result), 200