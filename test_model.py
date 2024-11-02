import torch
from models.yolo import YOLOv5

# Load the trained model
model = YOLOv5.load_from_checkpoint("model/best_model.ckpt")

# Test with an example image
img_path = "path/to/test/image.jpg"  # Change this to your test image path
results = model.predict(img_path)
print(results)
