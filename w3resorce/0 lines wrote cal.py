#this i mad to calculate how many totel lines of code in this dir

#with open('w3resorce/readme.py','r') as file:
#    content = file.read()
#    lines=content.count('\n')+1
#    print(f"total lines is {lines}")

import os

def count_lines_and_characters_in_folder(folder_path):
    total_lines = 0
    total_characters = 0
    
    # Walk through the folder
    for root,dirs, files in os.walk(folder_path):
        for file in files:
            # Get the full path of the file
            file_path = os.path.join(root, file)

            # Open and read the file
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        total_lines += 1
                        total_characters += len(line)  # Count characters in each line
            except Exception as e:
                print(f"Could not read {file_path}: {e}")
    average=total_characters/total_lines
    return total_lines, total_characters,average

# Example usage
folder_path = 'w3resorce/'  # Replace with your folder path
total_lines, total_characters, average = count_lines_and_characters_in_folder("w3resorce")

print(f"Total lines in folder: {total_lines}")
print(f"Total characters in folder: {total_characters}")
print(f"this is the average car per line {average}")
