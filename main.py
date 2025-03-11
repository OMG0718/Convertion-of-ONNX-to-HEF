import torch
import onnx
from ultralytics import YOLO  

model = YOLO("_your_file_name.pt")  #change to your actual file name

dummy_input = torch.randn(1, 3, 640, 640)  #(batch_size, channels, height, width)

# Export the model to ONNX with opset 12
onnx_path = "_export_file_name.onnx"  #change to a name you want
torch.onnx.export(
    model.model,           # Model
    dummy_input,           # Input tensor
    onnx_path,             # Save path
    export_params=True,    # Store trained weights
    opset_version=12,      # Use opset 12 for Hailo compatibility
    do_constant_folding=True,  # Optimize constant expressions
    input_names=["images"],  # Name input node
    output_names=["output"],  # Name output node
    dynamic_axes={"images": {0: "batch_size"}, "output": {0: "batch_size"}}  # Dynamic batch
)

print(f"Model exported successfully to {onnx_path}")

# Check if the exported ONNX model is valid
onnx_model = onnx.load(onnx_path)
onnx.checker.check_model(onnx_model)
print("ONNX model is valid!")
