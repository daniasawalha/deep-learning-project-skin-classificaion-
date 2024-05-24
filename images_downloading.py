#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import requests
import pandas as pd

# Set the working path for images
download_path = '/fitzpatrick17k/images/all/'

# Ensure the directory exists or create it
os.makedirs(download_path, exist_ok=True)

# Load the CSV file with Fitzpatrick annotations
csv_file_path = 'fitzpatrick17k.csv'
df = pd.read_csv(csv_file_path)

# Iterate through each row and download the image
for index, row in df.iterrows():
    image_url = row['url']
    image_filename = f"{row['md5hash']}.jpg"  # Assuming the filename is derived from the md5hash
    image_path = os.path.join(download_path, image_filename)

    try:
        # Download the image
        response = requests.get(image_url, stream=True)
        with open(image_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)

        print(f"Downloaded: {image_filename}")

    except Exception as e:
        print(f"Error downloading {image_filename}: {str(e)}")

print("Download process completed.")


# In[7]:


print("Current Working Directory:", os.getcwd())


# In[6]:


# Set the working path for images
download_path = '/fitzpatrick17k/images/all/'

# Ensure the directory exists or create it
os.makedirs(download_path, exist_ok=True)


# In[10]:


import os
import requests
import pandas as pd

# Set the working path for images
download_path = '/fitzpatrick17/all/'

# Ensure the directory exists or create it
os.makedirs(download_path, exist_ok=True)

# Load the CSV file with Fitzpatrick annotations
csv_file_path = 'fitzpatrick17k.csv'
df = pd.read_csv(csv_file_path)

# Counter for downloaded images
downloaded_images_count = 0

# Iterate through each row and download the image
for index, row in df.iterrows():
    image_url = row['url']
    image_filename = f"{row['md5hash']}.jpg"
    label = row['label']

    label_path = os.path.join(download_path, str(label))
    os.makedirs(label_path, exist_ok=True)

    image_path = os.path.join(label_path, image_filename)

    try:
        # Download the image
        response = requests.get(image_url, stream=True)
        with open(image_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)

        print(f"Downloaded: {image_filename} to {label_path}")
        downloaded_images_count += 1

    except Exception as e:
        print(f"Error downloading {image_filename}: {str(e)}")

print(f"Total {downloaded_images_count} images downloaded.")
print("Download process completed.")


# In[11]:


import os
print(os.getcwd())


# In[1]:


import os
import pandas as pd
from PIL import Image
from shutil import copyfile

# Path to CSV file and image directory
csv_path = 'fitzpatrick17k.csv'
image_dir = 'D:\\pr\\fitzpatrick17k\\images\\all\\'
output_dir = 'D:\\pr\\fitzpatrick17k\\images\\labeled\\'
updated_csv_path = 'fitzpatrick17k_updated.csv'

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

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
valid_image_names = [name[:-4] for name in os.listdir(image_dir) if name.endswith('.jpg')]
df = df[df['md5hash'].isin(valid_image_names)]

# Save each label to a separate path
for label in df['label'].unique():
    label_df = df[df['label'] == label]
    label_output_dir = os.path.join(output_dir, label)
    os.makedirs(label_output_dir, exist_ok=True)

    # Copy images to the label-specific directory
    for _, row in label_df.iterrows():
        image_name = row['md5hash'] + '.jpg'
        source_path = os.path.join(image_dir, image_name)
        dest_path = os.path.join(label_output_dir, image_name)
        copyfile(source_path, dest_path)

# Save the updated DataFrame to a new CSV file
df.to_csv(updated_csv_path, index=False)

# Print the number of valid records
num_valid_records = len(df)
print(f"Number of valid records: {num_valid_records}")

# Step 3: Remove records with frequency less than 30 from 'label' column
label_counts = df['label'].value_counts()
selected_labels = label_counts[label_counts >= 80].index
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
print("labels:", df_filtered)


# In[14]:


import os

root_path = os.path.abspath(os.sep)
print(f"The root path is: {root_path}")


# In[ ]:




