from PIL import Image
import numpy as np
import os
import io
import onnxruntime
import traceback

parent_dir = os.path.dirname(__file__)

weight_path = os.path.join(parent_dir, "weights", "pytorch_model_weights_1.onnx")

class Onnx:
  def __init__(self):
    self.model = onnxruntime.InferenceSession(weight_path) # Load the ONNX model
    self.input_name = self.model.get_inputs()[0].name
    self.output_name = self.model.get_outputs()[0].name

  def preprocess_cv2(self, img):
      img = img.resize((224, 224)) # resize image to 224x224
      # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # convert BGR to RGB
      img = np.array(img)[:,:,:3]
      img = np.float32(img) / 255.0 # normalize pixel values to [0,1]
      mean = np.array([0.485, 0.456, 0.406])
      std = np.array([0.229, 0.224, 0.225]) 
      img[:,:,0] = (img[:,:,0] - mean[0]) / std[0]
      img[:,:,1] = (img[:,:,1] - mean[1]) / std[1]
      img[:,:,2] = (img[:,:,2] - mean[2]) / std[2]
      img = np.transpose(img, (2, 0, 1)) # convert HxWxC to CxHxW
      # img = np.moveaxis(img*255, 0, -1)
      # img = img.astype(np.uint8)
      return img

    
  def prediction(self, img_byte):
    try:
    
      img = Image.open(io.BytesIO(img_byte)) # open image in pil
      img = self.preprocess_cv2(img) # return preprocess image
      img = np.expand_dims(img, axis=0) # add shape 
      preds = self.model.run([self.output_name], {self.input_name: img})
      if preds:
        return {"label":str(np.argmax(preds[0]))}
      else:
        return {"label":""}
    except:
      print(traceback.print_exc())
      return {"label":""}
    
    