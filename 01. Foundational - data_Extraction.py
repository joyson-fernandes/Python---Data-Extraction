import os

def extract_file_info(directory):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_info = {
                'name': filename,
                'size': os.path.getsize(os.path.join(directory, filename))
            }
            print(file_info)  # Print each file info on a separate line

if __name__ == "__main__":
    current_directory = os.getcwd()
    extract_file_info(current_directory)
