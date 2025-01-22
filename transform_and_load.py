
import os
import torch
from torchvision import datasets, transforms
import pickle

# Define the transformations
transform = transforms.Compose([
    transforms.Resize((224, 224)),  # Resize the image to 224x224 pixels
    transforms.RandomHorizontalFlip(),  # Randomly flip the image horizontally
    transforms.RandomVerticalFlip(),  # Randomly flip the image vertically
    transforms.RandomRotation(10),  # Randomly rotate the image by up to 10 degrees
    transforms.ToTensor(),  # Convert the image to PyTorch Tensor data type
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  # Normalize the image
])

# Load the images from the "Training" folder
dataset = datasets.ImageFolder(root="Training", transform=transform)

# Create a data loader
dataloader = torch.utils.data.DataLoader(dataset, batch_size=32, shuffle=True)

# Print a success message
print("Successfully loaded and transformed the images using torch dataloader.")

# Store the transformed data loader object using pickle
with open("model_dataset.pkl", "wb") as f:
    pickle.dump(dataloader, f)

# Print a success message
print("Successfully stored the transformed data loader object using pickle.")

