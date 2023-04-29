 
import os

# Define the root directory of the ETL project
root_dir = "ETL_Project"

# Define subdirectories for extraction, transformation, and loading
extract_dir = "1_extract_data"
transform_dir = "2_transform_data"
load_dir = "3_load_data"

# Create the root directory and subdirectories if they do not already exist
if not os.path.exists(root_dir):
    os.mkdir(root_dir)

if not os.path.exists(os.path.join(root_dir, extract_dir)):
    os.mkdir(os.path.join(root_dir, extract_dir))

if not os.path.exists(os.path.join(root_dir, transform_dir)):
    os.mkdir(os.path.join(root_dir, transform_dir))

if not os.path.exists(os.path.join(root_dir, load_dir)):
    os.mkdir(os.path.join(root_dir, load_dir))

# Define file names for the empty files to be created
extract_file = "data_extract.csv"
transform_file = "data_transform.csv"
load_file = "data_load.csv"

# Create empty files in the respective subdirectories
open(os.path.join(root_dir, extract_dir, extract_file), 'a').close()
open(os.path.join(root_dir, transform_dir, transform_file), 'a').close()
open(os.path.join(root_dir, load_dir, load_file), 'a').close()

