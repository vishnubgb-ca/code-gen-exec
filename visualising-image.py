
import os
import shutil
import random

# Get the list of subfolders in the "Training" directory
training_dir = "Training"
subfolders = [f.path for f in os.scandir(training_dir) if f.is_dir()]

# For each subfolder
for subfolder in subfolders:
    print(f"Processing subfolder: {subfolder}")

    # Get the list of image files in the subfolder
    image_files = [f for f in os.listdir(subfolder) if f.endswith(".jpg") or f.endswith(".png") or f.endswith(".jpeg")]

    # If there are no image files in the subfolder, skip to the next subfolder
    if not image_files:
        print(f"No image files in {subfolder}, skipping...")
        continue

    # Select a random image file
    random_image = random.choice(image_files)

    # Construct the full path to the random image file
    random_image_path = os.path.join(subfolder, random_image)

    # Copy the random image file to the current working directory
    shutil.copy2(random_image_path, os.getcwd())

    print(f"Copied image: {random_image} from {subfolder} to {os.getcwd()}")

