import os
import pandas as pd
from PIL import Image
from shutil import copyfile

# Path to CSV file and image directory
csv_path = 'fitzpatrick17k.csv'
image_dir = 'D:\\pr\\fitzpatrick17k\\images\\all\\'
updated_csv_path = 'fitzpatrick17k_updated.csv'

# Step 1: Remove corrupted images from the image directory
corrupted_images = []
for image_name in os.listdir(image_dir):
    image_path = os.path.join(image_dir, image_name)
    try:
        with Image.open(image_path):
            pass
    except (OSError, IOError):
        print(f"Removing corrupted image: {image_name}")
        corrupted_images.append(image_name)
        os.remove(image_path)

# Step 2: Read CSV file and filter records based on valid images
df = pd.read_csv(csv_path)

# Filter the DataFrame to include only rows with valid images
df = df[df['md5hash'].isin([name[:-4] for name in os.listdir(image_dir) if name.endswith('.jpg')])]

# Save the updated DataFrame to a new CSV file
df.to_csv(updated_csv_path, index=False)

# Print the number of valid records
num_valid_records = len(df)
print(f"Number of valid records: {num_valid_records}")

# Step 3: Remove records with frequency less than 30 from 'label' column
label_counts = df['label'].value_counts()
selected_labels = label_counts[(label_counts >= 100) & (label_counts <= 200)].index

df_filtered = df[df['label'].isin(selected_labels)]

# Save the filtered DataFrame to the same CSV file
df_filtered.to_csv(updated_csv_path, index=False)

# Print the number of filtered records
num_filtered_records = len(df_filtered)
print(f"Number of filtered records: {num_filtered_records}")

# Step 4: Remove images that are not in the 'md5hash' column
valid_images_set = set(df_filtered['md5hash'])
for image_name in os.listdir(image_dir):
    if image_name[:-4] not in valid_images_set:
        print(f"Removing image not in 'md5hash': {image_name}")
        os.remove(os.path.join(image_dir, image_name))

# Print the final number of valid records and images
num_final_records = len(df_filtered)
num_final_images = len([name for name in os.listdir(image_dir) if name.endswith('.jpg')])
print(f"Final number of valid records: {num_final_records}")
print(f"Final number of valid images: {num_final_images}")
print("labels:",df_filtered)
