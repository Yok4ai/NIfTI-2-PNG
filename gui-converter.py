import os
import nibabel as nib
import numpy as np
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinterdnd2 import DND_FILES, TkinterDnD

def save_corrected_slices(nii_file):
    img = nib.load(nii_file)
    img_data = img.get_fdata()
    img_data = (img_data - np.min(img_data)) / (np.max(img_data) - np.min(img_data)) * 255
    img_data = img_data.astype(np.uint8)

    axial_slice_index = img_data.shape[2] // 2
    coronal_slice_index = img_data.shape[1] // 2
    sagittal_slice_index = img_data.shape[0] // 2

    axial_slice_data = img_data[:, :, axial_slice_index]
    axial_slice_data = np.rot90(axial_slice_data, k=1)
    axial_img = Image.fromarray(axial_slice_data)
    axial_img.save(os.path.join(os.path.dirname(nii_file), 'axial_slice.png'))

    coronal_slice_data = img_data[:, coronal_slice_index, :]
    coronal_slice_data = np.rot90(coronal_slice_data, k=2)
    coronal_img = Image.fromarray(np.transpose(coronal_slice_data))
    coronal_img.save(os.path.join(os.path.dirname(nii_file), 'coronal_slice.png'))

    sagittal_slice_data = img_data[sagittal_slice_index, :, :]
    sagittal_slice_data = np.rot90(sagittal_slice_data, k=2)
    sagittal_img = Image.fromarray(np.transpose(sagittal_slice_data))
    sagittal_img.save(os.path.join(os.path.dirname(nii_file), 'sagittal_slice.png'))

    os.remove(nii_file)

def process_patient_folder(patient_folder):
    for root, _, files in os.walk(patient_folder):
        for file in files:
            if file.endswith('.nii'):
                nii_file = os.path.join(root, file)
                save_corrected_slices(nii_file)
                print(f'Converted {nii_file} to PNG images and deleted the original NIfTI file.')

def process_all_patients(data_dir):
    for patient_folder in os.listdir(data_dir):
        full_patient_folder = os.path.join(data_dir, patient_folder)
        if os.path.isdir(full_patient_folder):
            process_patient_folder(full_patient_folder)

def select_directory():
    dir_path = filedialog.askdirectory()
    if dir_path:
        process_all_patients(dir_path)
        messagebox.showinfo("Success", "Processing complete! PNG images have been saved.")

def drop(event):
    folder_path = event.data.strip('{}')  # Clean up the dropped data
    if os.path.isdir(folder_path):
        process_all_patients(folder_path)
        messagebox.showinfo("Success", "Processing complete! PNG images have been saved.")
    else:
        messagebox.showerror("Error", "Please drop a valid folder.")

def create_gui():
    root = TkinterDnD.Tk()
    root.title("NIfTI File Processor")
    root.geometry("700x550")

    label = tk.Label(root, text="Drag and drop a folder or select a directory:")
    label.pack(pady=50)

    select_button = tk.Button(root, text="Select Directory", command=select_directory)
    select_button.pack(pady=20)

    root.drop_target_register(DND_FILES)  # Register the root window as a drop target
    root.dnd_bind('<<Drop>>', drop)  # Bind the drop event to the drop function

    exit_button = tk.Button(root, text="Exit", command=root.quit)
    exit_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
