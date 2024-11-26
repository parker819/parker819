import torch

# 检查 PyTorch 版本
print("PyTorch 版本:", torch.__version__)

# 检查 CUDA 是否可用（如果使用 GPU 版本）
print("CUDA 是否可用:", torch.cuda.is_available())

x=torch.tensor([1, 2, 3])
x.device
