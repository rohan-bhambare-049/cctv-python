# Real-time Face and Body Detection with Video Recording

This project implements a real-time face and full body detection system using OpenCV. When it detects a face or body via webcam input, it starts recording video footage automatically and saves it with timestamped filenames.

# Mini - Project Made by Rohan Bhambare

## Features

- Real-time face and full body detection using Haar cascades
- Video recording starts automatically on detection
- Recording stops after a configurable delay once detection stops
- Saves recorded videos with timestamped filenames
- Displays live webcam feed with detection rectangles overlayed

## Requirements

- Python 3.x
- OpenCV library (`cv2`)

## Installation

1. Install Python 3 from [python.org](https://python.org)
2. Install OpenCV via pip: pip install opencv-python

## Usage

1. Run the script: python cam.py
2. The webcam feed will open in a window.
3. When faces or bodies are detected, recording starts automatically.
4. Recording stops 5 seconds after the last detection.
5. Press the `q` key to quit the program.

## Configuration

- The delay before stopping recording after detection ends is set to 5 seconds by default and can be adjusted by changing the `SEC` variable in the script.
