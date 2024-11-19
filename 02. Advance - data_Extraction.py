import os

def extract_file_info(directory=os.getcwd()):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_info = {
                'name': filename,
                'size': os.path.getsize(os.path.join(root, filename))
            }
            print(file_info)  # Print each file info on a separate line

if __name__ == "__main__":
    # You can pass a specific directory here if desired
    extract_file_info()  # Defaults to current working directory
