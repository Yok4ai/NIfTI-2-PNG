# NIfTI to PNG Converter
This is NIfTI to PNG converter with a GUI written in python.

# Setup

## Clone Repo
To get started, clone this repository and install the required dependencies. Make sure you have Python installed on your machine.

```bash
# Clone the repository
git clone https://github.com/Yok4ai/NIfTI-2-PNG.git
```
## Setting Up Virtual Environment 
### (Skip if using Conda or Python from a global installation)
```bash
cd NIfTI-2-PNG

#Create Python Virtual Environment
python3 -m venv venv

# Activate Virtual Environment
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```
## Requirements
```bash
# Install the required packages
pip3 install -r requirements.txt
```
Or manually install
```bash
pip3 install nibabel numpy pillow tkinterdnd2 matplotlib
```
## Usage

To use the NIfTI to PNG converter, follow these steps:

1. Ensure you have activated your virtual environment.
2. Run the `.py` files from the command line or your code editor.
3. Make sure to change the directories in the script as required.

For Example
```bash
python3 converter.py
```
To convert and delete the .nii files, run
```bash
python3 convertanddelete.py
```
To extract every slice of MRI images into PNG format, run
```bash
python3 extract-all-slices.py
```

## GUI (Linux-only)
Install the tkinter module
```bash
sudo apt install python3-tk
```
Run the script
```bash
python3 gui-converter.py
```
Drag and Drop the folder or Select the directory to convert the files inside. 
