from flask import Flask, request, jsonify
import os 
import sys

app = Flask(__name__)

parent_dir = os.path.dirname(__file__)
sys.path.append(parent_dir)
from mlops.model import Onnx
sys.path.remove(parent_dir)
onnx_model = Onnx()

print("app file chali")

def runf():
    print("ye chala?")
@app.route('/predict', methods=['POST'])
def predict():
    print(request.files["image"])
    img_bytes = request.files['image'].read()
    # Preprocess the image data if necessary
    prediction = onnx_model.prediction(img_bytes)
    return jsonify(prediction)

if __name__ == '__main__':
    runf()
    app.run(host='0.0.0.0', port=8080, debug=True)