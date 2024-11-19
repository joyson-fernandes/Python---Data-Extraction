import os

def extract_file_info(directory=os.getcwd()):
    file_info_dict = {}
    
    for root, dirs, files in os.walk(directory):
        for filename in files:
            # Create a dictionary entry with file path as key
            file_info_dict[os.path.join(root, filename)] = {
                'name': filename,
                'size': os.path.getsize(os.path.join(root, filename))
            }
    
    # Print each file's information on a separate line
    for file_path, info in file_info_dict.items():
        print({file_path: info})  # Print as a dictionary on a separate line

if __name__ == "__main__":
    extract_file_info()  # Defaults to current working directory
