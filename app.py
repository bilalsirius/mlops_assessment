import time
import base64

def init():
    global model
    from mlops.model import Onnx
    model = Onnx()
    print("model loaded!!")

def inference(model_inputs:dict) -> dict:
    global model
    img = base64.b64decode(model_inputs["image"].encode('utf-8'))
    img = model.preprocess_cv2(img)
    pred = model.prediction(img)
    return pred
