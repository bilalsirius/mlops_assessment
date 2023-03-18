import banana_dev as banana
import json

api_key = "c18de9da-b28e-4681-9ddf-0ed4e929a237"
model_key = "fc518ead-5511-4b36-9f7d-8face6b1ca60"
model_inputs = json.dumps({"image":"abc"}) # anything you want to send to your model

out = banana.run(api_key, model_key, model_inputs)