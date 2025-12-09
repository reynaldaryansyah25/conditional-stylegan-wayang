import torch
import cv2
import skimage
import albumentations
import sklearn
import torch_fidelity

print("Torch CUDA:", torch.cuda.is_available())
print("OpenCV:", cv2.__version__)
print("Skimage:", skimage.__version__)
print("Albumentations:", albumentations.__version__)
