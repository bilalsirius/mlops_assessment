import banana_dev as banana
import json
import base64
from io import BytesIO
from PIL import Image



api_key = "610bf20c-edd9-46dd-b451-837860afbcb5"
model_key = "3ba37889-e950-4650-954f-1526431a7832"
image_bytes = open("./test_cases/images/turtle.jpeg","rb").read()
image_bytes = base64.b64encode(image_bytes)
model_inputs = json.dumps({"image":image_bytes.decode('utf-8')}) # anything you want to send to your model
# print(model_inputs)
model_inputs = json.loads(model_inputs)
# print(Image.open(BytesIO(base64.b64decode(model_inputs["image"].encode('utf-8')))))

out = banana.run(api_key, model_key, model_inputs)
print(out)