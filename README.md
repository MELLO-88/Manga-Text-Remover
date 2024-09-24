# Manga Text Removal App

## Overview
This application allows you to remove text from images (e.g., manga pages) using EasyOCR and OpenCV. It processes an entire manga folder by detecting and removing text from images within subfolders (chapters) and saves the output in a specified directory.


## Prerequisites
- Python 3.x
- Required libraries:
  - `opencv-python`
  - `numpy`
  - `easyocr`
  - `os` (standard Python library)

### Install Dependencies

Run the following command to install the necessary dependencies:

```bash
pip install opencv-python numpy easyocr
```

## How It Works

1. **Input Folder**: The app takes a path to a folder containing manga chapters. Each chapter should be a subfolder containing image files.
2. **Text Removal**: The app detects text on each image in the folder, creates a mask over the detected text areas, and removes the text using inpainting techniques.
3. **Output Folder**: The processed images are saved in a newly created output folder, preserving the structure of the original input folder.

## Folder Structure

### Input Folder

```
manga_folder/
    ├── chapter1/
    │   ├── page1.jpg
    │   ├── page2.jpg
    │   └── ...
    └── chapter2/
        ├── page1.jpg
        └── ...
```

### Output Folder

The output folder will have a similar structure to the input folder but will contain the processed images with text removed:

```
output_folder/
    ├── chapter1/
    │   ├── page1.jpg
    │   ├── page2.jpg
    │   └── ...
    └── chapter2/
        ├── page1.jpg
        └── ...
```

## Usage

### Run the App

You can run the app by executing the following commands in your terminal:

```bash
python app.py
```

1. **Enter the Manga Folder Path**: The path to the folder containing your manga (with chapters as subfolders).
2. **Enter the Output Folder Path**: The folder where the processed images (with text removed) will be saved.

The app will process each chapter folder in the input manga folder and save the images with text removed in the corresponding output folder.

### Example Input/Output

- **Input**: 
  - Manga folder: `/path/to/manga`
  - Chapter folders: `/path/to/manga/chapter1/`, `/path/to/manga/chapter2/`, etc.
  
- **Output**: 
  - Processed images will be saved to `/path/to/output/chapter1/`, `/path/to/output/chapter2/`, etc.

## License
This project is open-source and free to use for non-commercial purposes.

## Author
Kaung Thant Tun - Developer of the Manga Text Removal App

---

This README provides a brief overview and usage instructions for running the manga text removal app.
