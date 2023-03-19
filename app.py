import time
import base64
import json
from urllib.parse import urlparse
import os
import requests

def is_url_or_path(string):
    # Parse the string and check if it has a valid scheme
    parsed_url = urlparse(string)
    if parsed_url.scheme:
        return True
    
    return False

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
    try:
        if "image" in model_inputs:
            img_p = model_inputs["image"]
            if is_url_or_path(img_p):
                img = requests.get(img_p) 
                img = base64.b64decode(img)
            else:
                img = open(f".{img_p}", "rb").read()
            img = model.preprocess_cv2(img)
            pred = model.prediction(img)
            return pred
        if "test" in model_inputs:
            res = {}
            for img_p in model_inputs["test"]:
                if is_url_or_path(img_p):
                    img = requests.get(img_p) 
                    img = base64.b64decode(img)
                else:
                    img = open(f".{img_p}", "rb").read()
                img = model.preprocess_cv2(img)
                pred = model.prediction(img)
                res[img_p.split('/')[-1]] = pred
            return res
    except:
        import traceback
        return {"error":traceback.print_ex()}
