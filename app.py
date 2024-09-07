import os
import cv2
import numpy as np
import easyocr

# Text removal function using EasyOCR and OpenCV
def remove_text_from_image(image_path, output_path):
    reader = easyocr.Reader(['en'], gpu=True)
    image = cv2.imread(image_path)
    results = reader.readtext(image)
    mask = np.zeros(image.shape[:2], dtype=np.uint8)
    
    # Create a mask for detected text areas
    for (bbox, text, prob) in results:
        (top_left, top_right, bottom_right, bottom_left) = bbox
        top_left = tuple(map(int, top_left))
        bottom_right = tuple(map(int, bottom_right))
        cv2.rectangle(mask, top_left, bottom_right, 255, -1)
    
    # Inpaint the text-removed areas
    result_image = cv2.inpaint(image, mask, inpaintRadius=7, flags=cv2.INPAINT_TELEA)
    
    # Save the result image
    cv2.imwrite(output_path, result_image)

# Utility function to get all folder names in a directory
def get_all_folder_names(directory_path):
    try:
        folder_names = [name for name in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, name))]
        return folder_names
    except FileNotFoundError:
        print(f"The directory '{directory_path}' does not exist.")
        return []
    except PermissionError:
        print(f"Permission denied for accessing the directory '{directory_path}'.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Utility function to list all files in a folder
def get_filenames_in_folder(folder_path):
    try:
        filenames = os.listdir(folder_path)
        file_list = [file for file in filenames if os.path.isfile(os.path.join(folder_path, file))]
        return file_list
    except FileNotFoundError:
        print(f"The folder '{folder_path}' does not exist.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Utility function to create a new folder if it doesn't exist
def create_folder(folder_name, folder_path):
    full_path = os.path.join(folder_path, folder_name)
    if not os.path.exists(full_path):
        os.makedirs(full_path)
        print(f"Folder created: {full_path}")
    else:
        print(f"Folder already exists: {full_path}")
    return full_path

# Main function to process the manga folder
def process_manga_folder(manga_folder_path, output_base_folder):
    manga_folder_name = os.path.basename(manga_folder_path)
    
    # Ask user for output folder
    output_manga_folder_path = create_folder(manga_folder_name, output_base_folder)  # Create folder with the manga folder's name in the specified output directory

    # Get all chapter folders inside the manga folder
    chapter_folders = get_all_folder_names(manga_folder_path)

    for chapter_folder in chapter_folders:
        chapter_folder_path = os.path.join(manga_folder_path, chapter_folder)
        
        # Create corresponding chapter folder in the output folder
        output_chapter_folder_path = create_folder(chapter_folder, output_manga_folder_path)

        # Get all image files in the chapter folder
        image_files = get_filenames_in_folder(chapter_folder_path)

        for image_file in image_files:
            image_file_path = os.path.join(chapter_folder_path, image_file)
            output_image_path = os.path.join(output_chapter_folder_path, image_file)
            
            # Remove text from the image and save it
            remove_text_from_image(image_file_path, output_image_path)
            print(f"Processed and saved: {output_image_path}")

# Example usage
if __name__ == "__main__":
    # Input manga folder path
    manga_folder = input("Enter the manga folder path: ")
    
    # Ask user for the output folder path
    output_folder = input("Enter the output folder path: ")
    
    process_manga_folder(manga_folder, output_folder)
