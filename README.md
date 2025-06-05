# Color Detection

This project demonstrates real-time color detection using OpenCV and Python. It captures video from a webcam, detects a specified color (default: green), and highlights the detected region with a bounding box.

## Features

- Real-time video capture and processing
- HSV color space thresholding for robust color detection
- Bounding box visualization of detected color regions

## Requirements

See [requirements.txt](https://github.com/BenedictRaymond/Color-Detection-using-HSV/blob/master/requirements.txt) for dependencies:
- opencv-python
- Pillow
- numpy

Install dependencies with:
```sh
pip install -r requirements.txt
```


## Usage

Run the color detection script:

The script will open a webcam feed.
Press q to quit.

## Customization

To detect a different color, modify the color variable in color_detection.py (BGR format).

## Files
_color_detection.py:_ Main script for color detection.

_utils.py:_ Utility function for HSV color limits.

_requirements.txt:_ Python dependencies.

## License

This project is for educational purposes.
