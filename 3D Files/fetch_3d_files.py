from google.cloud import storage
import os

def download_gcs_file(bucket_name, source_blob_name, destination_file_name):
    """Downloads a file from Google Cloud Storage.
    
    Args:
        bucket_name: Name of the GCS bucket
        source_blob_name: Path to the file in GCS
        destination_file_name: Local path where the file should be downloaded
    """
    try:
        # Initialize the client
        storage_client = storage.Client()
        
        # Get the bucket
        bucket = storage_client.bucket(bucket_name)
        
        # Get the blob (file)
        blob = bucket.blob(source_blob_name)
        
        # Create the destination directory if it doesn't exist
        os.makedirs(os.path.dirname(destination_file_name), exist_ok=True)
        
        # Download the file
        blob.download_to_filename(destination_file_name)
        
        print(f"File {source_blob_name} downloaded to {destination_file_name} successfully.")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Configuration
bucket_name = "alpine-inkwell-325917.appspot.com"
source_blob_name = "models/iphone-13.gltf"
destination_file_name = "downloads/iphone-13.gltf"  # Local path where you want to save the file

# Before running this script, make sure to:
# 1. Install the required package: pip install google-cloud-storage
# 2. Set up authentication by setting the GOOGLE_APPLICATION_CREDENTIALS environment variable
#    pointing to your service account key JSON file

if __name__ == "__main__":
    download_gcs_file(bucket_name, source_blob_name, destination_file_name)