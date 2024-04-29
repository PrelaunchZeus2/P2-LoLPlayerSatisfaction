import torch

cuda_available = torch.cuda.is_available()

print(cuda_available)