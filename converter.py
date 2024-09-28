import os  # Import the os module for interacting with the operating system, such as file and directory manipulation.
import nibabel as nib  # Import the nibabel library for reading and writing NIfTI files (medical imaging format).
import numpy as np  # Import NumPy for numerical operations, especially with arrays.
from PIL import Image  # Import the Image class from the PIL (Pillow) library to handle image processing.

def save_corrected_slices(nii_file, output_dir):
    # Load the NIfTI file using nibabel
    img = nib.load(nii_file)  # Load the NIfTI file and create an image object.
    img_data = img.get_fdata()  # Get the image data as a NumPy array.

    # Normalize the data to the range [0, 255] for image representation
    img_data = (img_data - np.min(img_data)) / (np.max(img_data) - np.min(img_data)) * 255  # Normalize data.
    img_data = img_data.astype(np.uint8)  # Convert the data type to unsigned 8-bit integer (0-255).

    # Get the middle slice indices for each anatomical plane
    axial_slice_index = img_data.shape[2] // 2   # Calculate the index for the middle axial slice (Z-plane).
    coronal_slice_index = img_data.shape[1] // 2  # Calculate the index for the middle coronal slice (Y-plane).
    sagittal_slice_index = img_data.shape[0] // 2  # Calculate the index for the middle sagittal slice (X-plane).

    # Save the axial slice and rotate it by 90 degrees
    axial_slice_data = img_data[:, :, axial_slice_index]  # Extract the middle axial slice.
    axial_slice_data = np.rot90(axial_slice_data, k=1)  # Rotate the axial slice 90 degrees counter-clockwise.
    axial_img = Image.fromarray(axial_slice_data)  # Convert the NumPy array to a PIL Image object.
    axial_img.save(os.path.join(output_dir, f'axial_slice.png'))  # Save the axial slice image as PNG.

    # Save the coronal slice and rotate it by 90 degrees
    coronal_slice_data = img_data[:, coronal_slice_index, :]  # Extract the middle coronal slice.
    coronal_slice_data = np.rot90(coronal_slice_data, k=2)  # Rotate the coronal slice 180 degrees (2 times 90 degrees).
    coronal_img = Image.fromarray(np.transpose(coronal_slice_data))  # Transpose the data for proper orientation and convert to PIL Image.
    coronal_img.save(os.path.join(output_dir, f'coronal_slice.png'))  # Save the coronal slice image as PNG.

    # Save the sagittal slice and rotate it by 90 degrees
    sagittal_slice_data = img_data[sagittal_slice_index, :, :]  # Extract the middle sagittal slice.
    sagittal_slice_data = np.rot90(sagittal_slice_data, k=2)  # Rotate the sagittal slice 180 degrees.
    sagittal_img = Image.fromarray(np.transpose(sagittal_slice_data))  # Transpose the data and convert to PIL Image.
    sagittal_img.save(os.path.join(output_dir, f'sagittal_slice.png'))  # Save the sagittal slice image as PNG.

def process_patient_folder(patient_folder):
    # Iterate over all files in the patient folder
    for root, _, files in os.walk(patient_folder):  # Walk through the directory, returning root, directories, and files.
        for file in files:  # Loop through the list of files
            if file.endswith('.nii'):  # Check if the file is a NIfTI file
                nii_file = os.path.join(root, file)  # Create the full path to the NIfTI file.
                output_dir = os.path.join(root, 'converted_png')  # Define the output directory for converted images.
                if not os.path.exists(output_dir):  # Check if the output directory exists.
                    os.makedirs(output_dir)  # Create the output directory if it doesn't exist.
                save_corrected_slices(nii_file, output_dir)  # Call the function to process and save slices from the NIfTI file.
                print(f'Converted {nii_file} to PNG images in {output_dir}')  # Print a message indicating the conversion.

def process_all_patients(data_dir):
    # Iterate over each patient folder in the data directory
    for patient_folder in os.listdir(data_dir):  # List all items in the data directory
        full_patient_folder = os.path.join(data_dir, patient_folder)  # Create the full path to the patient folder.
        if os.path.isdir(full_patient_folder):  # Check if the item is a directory (patient folder)
            process_patient_folder(full_patient_folder)  # Process the patient folder.

# Example usage
data_dir = '/home/whatever/Documents/CSE499/BraTS-GLI-00000-000'  # Define the path to the main data directory containing patient folders.
process_all_patients(data_dir)  # Call the function to process all patient folders in the specified data directory.
