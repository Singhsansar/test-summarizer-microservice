import gdown
import zipfile
import os

# Replace 'your_file_id' with the actual file ID from the provided link
file_id = '1-1IBOAx3NEc0qDiHyLJcCvIs9SM2RIEo'
file_url = f'https://drive.google.com/uc?id={file_id}'
downloaded_file = 'downloaded_file.zip'
extracted_folder = 'model'

gdown.download(file_url, downloaded_file, quiet=False)

if not zipfile.is_zipfile(downloaded_file):
    raise ValueError(f"The downloaded file '{downloaded_file}' is not a zip file.")

if not os.path.exists(extracted_folder):
    os.makedirs(extracted_folder)

with zipfile.ZipFile(downloaded_file, 'r') as zip_ref:
    zip_ref.extractall(extracted_folder)

os.remove(downloaded_file)

print(f"File downloaded and extracted to '{extracted_folder}'.")
