import time

def init():
    global model
    from mlops.model import Onnx
    model = Onnx()

def inference(model_inputs:dict) -> dict:
    global model
    img = model_inputs["image"]
    img = model.preprocess_cv2(img)
    pred = model.prediction(img)
    return pred
