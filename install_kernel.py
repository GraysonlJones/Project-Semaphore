import sys
import zipfile
import shutil
from pathlib import Path
from jupyter_client.kernelspec import KernelSpecManager

def install_kernel():
    # Define paths
    zip_path = Path("jjava-1.0-a4-kernelspec.zip")
    extract_dir = Path("jjava-1.0-a4-kernelspec")
    
    # Check if the ZIP file exists
    if not zip_path.exists():
        print(f"Error: {zip_path} not found.")
        sys.exit(1)
    
    # Unzip the kernel specification
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall()
    
    # Verify extraction
    if not extract_dir.exists():
        print(f"Error: Failed to extract {zip_path}.")
        sys.exit(1)
    
    # Install the kernel
    km = KernelSpecManager()
    km.install_kernel_spec(str(extract_dir), user=True, name='java')
    print("Kernel installed successfully.")

if __name__ == "__main__":
    install_kernel()
