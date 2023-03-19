import time
import base64
import json

def init():
    global model
    from mlops.model import Onnx
    model = Onnx()
    print("model loaded!!")

def inference(model_inputs:dict) -> dict:
    global model
    try:
        model_inputs = json.loads(model_inputs)
    except:
        pass
    img = base64.b64decode(model_inputs["image"].encode('utf-8'))
    img = model.preprocess_cv2(img)
    pred = model.prediction(img)
    return pred
