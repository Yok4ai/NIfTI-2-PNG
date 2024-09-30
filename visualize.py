import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt

# Function to load NIfTI image
def load_nifti_image(file_path):
    img = nib.load(file_path)
    img_data = img.get_fdata()
    return img_data

# Function to normalize the image data
def normalize_image(img_data):
    img_data_normalized = (img_data - np.min(img_data)) / (np.max(img_data) - np.min(img_data))
    return img_data_normalized

# Function to visualize a specific slice of the MRI
def visualize_slice(img_data, slice_index):
    plt.imshow(img_data[:, :, slice_index], cmap='gray')
    plt.title(f'Slice {slice_index}')
    plt.axis('off')
    plt.show()

# Function to process and prepare data for neural network input
def prepare_data_for_model(img_data):
    # Reshape or transform if necessary (e.g., add a channel dimension)
    img_data_expanded = np.expand_dims(img_data, axis=-1)  # Add channel dimension
    return img_data_expanded

# Main script execution
if __name__ == "__main__":
    # Path to the NIfTI file
    nii_file_path = 'path_to_your_file.nii'  # Change this to your file path
    nii_file_path = '/mnt/Data 1/Dataset-backup/data/TrainingData/BraTS-GLI-00000-000/BraTS-GLI-00000-000-t1c.nii/00000057_brain_t1ce.nii'
    

    # Load the NIfTI image
    img_data = load_nifti_image(nii_file_path)
    print(f"Original Image Shape: {img_data.shape}")

    # Normalize the image data
    img_data_normalized = normalize_image(img_data)
    print(f"Normalized Image Shape: {img_data_normalized.shape}")

    # Visualize a middle slice of the MRI
    slice_index = img_data_normalized.shape[2] // 2  # Get the middle slice index
    visualize_slice(img_data_normalized, slice_index)

    # Prepare data for model input
    img_data_for_model = prepare_data_for_model(img_data_normalized)
    print(f"Model Input Shape: {img_data_for_model.shape}")

    # Save the prepared data or use it for your model here
    # For example: model.predict(img_data_for_model)
