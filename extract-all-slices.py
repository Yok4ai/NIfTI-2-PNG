import os
import nibabel as nib
import numpy as np
from PIL import Image

def save_all_slices(nii_file):
    # Load the NIfTI file using nibabel
    img = nib.load(nii_file)
    img_data = img.get_fdata()

    # Normalize the data to the range [0, 255] for image representation
    img_data = (img_data - np.min(img_data)) / (np.max(img_data) - np.min(img_data)) * 255
    img_data = img_data.astype(np.uint8)

    # Define the output directory for slices
    output_dir = os.path.dirname(nii_file)
    
    # Save all axial slices
    for i in range(img_data.shape[2]):
        axial_slice_data = img_data[:, :, i]
        axial_slice_data = np.rot90(axial_slice_data, k=1)
        axial_img = Image.fromarray(axial_slice_data)
        axial_img.save(os.path.join(output_dir, f'axial_slice_{i:03d}.png'))

    # Save all coronal slices
    for i in range(img_data.shape[1]):
        coronal_slice_data = img_data[:, i, :]
        coronal_slice_data = np.rot90(coronal_slice_data, k=2)
        coronal_img = Image.fromarray(np.transpose(coronal_slice_data))
        coronal_img.save(os.path.join(output_dir, f'coronal_slice_{i:03d}.png'))

    # Save all sagittal slices
    for i in range(img_data.shape[0]):
        sagittal_slice_data = img_data[i, :, :]
        sagittal_slice_data = np.rot90(sagittal_slice_data, k=2)
        sagittal_img = Image.fromarray(np.transpose(sagittal_slice_data))
        sagittal_img.save(os.path.join(output_dir, f'sagittal_slice_{i:03d}.png'))

def process_patient_folder(patient_folder):
    # Iterate over all files in the patient folder
    for root, _, files in os.walk(patient_folder):
        for file in files:
            if file.endswith('.nii'):
                nii_file = os.path.join(root, file)
                save_all_slices(nii_file)
                print(f'Converted {nii_file} to PNG images.')

def process_all_patients(data_dir):
    # Iterate over each patient folder in the data directory
    for patient_folder in os.listdir(data_dir):
        full_patient_folder = os.path.join(data_dir, patient_folder)
        if os.path.isdir(full_patient_folder):
            process_patient_folder(full_patient_folder)

# Example usage
data_dir = '/home/whatever/Documents/Github/NIfTI-2-PNG/data/Example/BraTS-GLI-00000-000'
process_all_patients(data_dir)
