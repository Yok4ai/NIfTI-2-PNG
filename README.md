# NIfTI to PNG Converter
This is a Python script that processes NIfTI (Neuroimaging Informatics Technology Initiative) files and converts selected slices into PNG images. It uses the `nibabel`, `numpy`, and `Pillow` libraries to handle medical imaging data.

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
pip3 install nibabel numpy pillow
```
## Usage

To use the NIfTI to PNG converter, follow these steps:

1. Ensure you have activated your virtual environment.
2. Run the `converter.py` file from the command line or your code editor.

```bash
python3 converter.py
