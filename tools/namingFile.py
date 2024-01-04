import os

# Specify the directory containing the images
directory_path = r'u:\Atit\Coding\AI\CustomData\Machinemodels\RequiredModels\test sample jpeg'

# Ensure the directory path is correct
if not os.path.exists(directory_path):
    print(f"Directory '{directory_path}' does not exist.")
    exit()

# List all files in the directory
file_list = os.listdir(directory_path)

# Sort the files alphabetically
file_list.sort()

# Number of images
num_images = len(file_list)

# Iterate through the files and rename them with sequential numbers
for count, old_name in enumerate(file_list, start=1):
    # Construct the new name with counting number
    new_name = f"{count}"  # No leading zero in the first place
    new_path = os.path.join(directory_path, f"{new_name}.jpg")  # Assuming images have a .jpg extension
    
    # Construct the old path
    old_path = os.path.join(directory_path, old_name)
    
    # Check if the file exists before renaming
    if os.path.exists(old_path):
        # Rename the file
        os.rename(old_path, new_path)
        print(f"Renamed: {old_name} -> {new_name}.jpg")
    else:
        print(f"File not found: {old_path}")

print(f"Successfully renamed {num_images} images.")
