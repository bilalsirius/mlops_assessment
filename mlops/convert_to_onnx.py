# from PIL import Image
# import onnx
# import torch
# import sys
# import os
# import traceback

# parent_dir = os.path.dirname(__file__)
# sys.path.append(parent_dir)
# from pytorch_model import Classifier, BasicBlock
# sys.path.remove(parent_dir)

# if __name__ == "__main__":
# 	try:
# 		# print("Path:", sys.argv[0])
# 		# if sys.argv[0]:
# 		mtailor = Classifier(BasicBlock, [2, 2, 2, 2])
# 		trained_model_path = os.path.join(".", "weights", "pytorch_model_weights_1.pth")
# 		mtailor.load_state_dict(torch.load(trained_model_path))
# 		mtailor.eval()
# 		print("model loaded!")
# 		img = Image.open(os.path.join(".", "..", "test_cases", "images", "n01667114_mud_turtle.jpeg"))
# 		dummy_data = mtailor.preprocess_numpy(img).unsqueeze(0)
# 		onnx_model_name = os.path.join(parent_dir, trained_model_path.split('/')[-1].split(".")[0] + ".onnx")
# 		torch.onnx.export(mtailor, dummy_data, onnx_model_name, verbose=True)
# 		onnx_model = onnx.load(onnx_model_name)
# 		print("Model Converted!!!!")
# 		#onnx.checker.check_model(onnx_model)
# 		# else:
# 		# 	print("no command line argument found!")
# 	except:
# 		print(traceback.print_exc())
		
