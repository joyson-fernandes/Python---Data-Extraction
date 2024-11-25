# Building a Python Script to Extract File Information


# What is Python?

Python is a high-level, interpreted programming language known for its readability and versatility. Key features include:

- **Ease of Learning**: Simple syntax that resembles natural language.
- **Interpreted Language**: Executes code line-by-line, facilitating quick testing and debugging.
- **Dynamic Typing**: Variables don’t need explicit declarations.
- **Versatile Use Cases**: Used in web development, data analysis, machine learning, automation, and more.
- **Rich Standard Library**: Comes with built-in modules for various tasks.
- **Strong Community Support**: A large, active community provides resources and libraries.
- **Cross-Platform Compatibility**: Runs on various operating systems without modification.

Python’s combination of simplicity and power makes it a popular choice among developers.

## Overview

In this topic, we will cover how to create a Python script to extract file information like name and size. We’ll start from foundational, advance to advanced tasks, and then tackle complex tasks as outlined below.

Get ready for some fun :)

### FOUNDATIONAL

Create a script that generates a list of dictionaries about files in the working directory. Then print the list.

#### Script: Foundational — `data_Extraction.py`

```python
import os  # Import the os module to interact with the operating system

def extract_file_info(directory):  # Define a function that takes a directory path as an argument
    for filename in os.listdir(directory):  # Iterate over each file in the specified directory
        if os.path.isfile(os.path.join(directory, filename)):  # Check if the path is a file and combining a directory path and a filename
            file_info = {  # Create a dictionary to hold file information
                'name': filename,  # Store the file name
                'size': os.path.getsize(os.path.join(directory, filename))  # Get and store the file size
            }
            print(file_info)  # Print each file's information on a separate line

if __name__ == "__main__":  # Check if the script is being run directly (not imported)
    current_directory = os.getcwd()  # Get the current working directory
    extract_file_info(current_directory)  # Call the function with the current directory

