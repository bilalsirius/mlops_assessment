import unittest
import sys
import os
import glob
import json

from mlops.model import Onnx
# Define the function to be tested

parent_dir = os.path.dirname(__file__)
img_paths = glob.glob(os.path.join(parent_dir, "images", "*g"))
response = json.load(open(os.path.join(parent_dir, "groundtruth.json")))
mltailor = Onnx()

# Define the test class
class OnnxTest(unittest.TestCase):

    # Define a test method
    def test_invalid_input(self):
        result = mltailor.prediction(None)
        self.assertEqual(result["label"], "")

    # Define another test method
    def test_valid_outputs(self):
        for img in img_paths:
            self.assertEqual(mltailor.prediction(img), response[img.split('/')[-1]["label"]])

# Run the tests
if __name__ == '__main__':
    unittest.main()