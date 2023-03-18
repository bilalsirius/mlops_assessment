from PIL import Image
import onnx
import torch
import sys
import os
import traceback

parent_dir = os.path.dirname(__file__)
sys.path.append(parent_dir)
from pytorch_model import Classifier, BasicBlock
sys.path.remove(parent_dir)

def convert_model(path, des, img_pil):
	try:
		mtailor = Classifier(BasicBlock, [2, 2, 2, 2])
		mtailor.load_state_dict(torch.load(path))
		mtailor.eval()
		print("model loaded!")
		dummy_data = mtailor.preprocess_numpy(img_pil).unsqueeze(0)
		torch.onnx.export(mtailor, dummy_data, des, verbose=True)
		# onnx_model = onnx.load(des)
		# onnx.checker.check_model(onnx_model)
		print("Model Converted!!!!")
	except:
		import traceback
		print(traceback.print_exc())

# if __name__ == "__main__":
# 	try:
# 		trained_model_path = "./weights/pytorch_model_weights_1.pth"
		img_pil = Image.open("./../test_cases/images/n01667114_mud_turtle.jpeg")
# 		onnx_model_name = parent_dir + "/" + trained_model_path.split('/')[-1].split(".")[0] + ".onnx"
# 		convert_model(trained_model_path, onnx_model_name, img_pil)
# 	except:
# 		print(traceback.print_exc())
		
