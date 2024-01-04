import os
import shutil
from sklearn.model_selection import train_test_split

def split_data(source_folder, destination_folder):
    # Create train, test, and validation folders
    train_folder = os.path.join(destination_folder, 'train')
    test_folder = os.path.join(destination_folder, 'test')
    validation_folder = os.path.join(destination_folder, 'validation')

    os.makedirs(train_folder, exist_ok=True)
    os.makedirs(test_folder, exist_ok=True)
    os.makedirs(validation_folder, exist_ok=True)

    # Create subfolders for images and labels within train, test, and validation folders
    for folder in [train_folder, test_folder, validation_folder]:
        os.makedirs(os.path.join(folder, 'images'), exist_ok=True)
        os.makedirs(os.path.join(folder, 'labels'), exist_ok=True)

    # Function to move files to their respective folders
    def move_files(files, source, destination_images, destination_labels):
        os.makedirs(destination_images, exist_ok=True)
        os.makedirs(destination_labels, exist_ok=True)

        for file in files:
            shutil.move(os.path.join(source, 'images', file), os.path.join(destination_images, file))
            base_name, ext = os.path.splitext(file)
            text_file = base_name + '.txt'
            text_file_path = os.path.join(source, 'labels', text_file)

            if os.path.exists(text_file_path):
                shutil.move(text_file_path, os.path.join(destination_labels, text_file))

    # Get the list of image files in the images folder
    image_files = [f for f in os.listdir(os.path.join(source_folder, 'images')) if f.endswith('.jpg') or f.endswith('.png')]

    # Split the files into train, test, and validation sets
    train_files, test_validation_files = train_test_split(image_files, test_size=0.4, random_state=42)
    test_files, validation_files = train_test_split(test_validation_files, test_size=0.5, random_state=42)

    # Move image and text files to their respective folders
    move_files(train_files, source_folder, os.path.join(train_folder, 'images'), os.path.join(train_folder, 'labels'))
    move_files(test_files, source_folder, os.path.join(test_folder, 'images'), os.path.join(test_folder, 'labels'))
    move_files(validation_files, source_folder, os.path.join(validation_folder, 'images'), os.path.join(validation_folder, 'labels'))

if __name__ == "__main__":
    # Set the path to the SampleImages folder
    source_images_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'SampleImages')

    # Set the path to the destination folder
    destination_folder = os.path.join(source_images_folder, 'split_data')

    # Call the split_data function
    split_data(source_images_folder, destination_folder)
