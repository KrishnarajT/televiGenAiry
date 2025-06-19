import os

def change_extension(root_folder, old_ext='.srt', new_ext='.txt'):
    """
    Recursively change file extensions from old_ext to new_ext in the given root_folder.

    :param root_folder: Path to the root directory
    :param old_ext: The current file extension to be changed
    :param new_ext: The new file extension to be applied
    """
    for dirpath, _, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith(old_ext):
                # Construct full file path
                old_file = os.path.join(dirpath, filename)
                # Construct new file path with the new extension
                new_file = os.path.join(dirpath, filename[:-len(old_ext)] + new_ext)
                # Rename the file

                try: 
                    os.rename(old_file, new_file)
                    print(f'Renamed: {old_file} to {new_file}')
                except Exception as e:
                    print(e)
if __name__ == "__main__":
    # Get the root folder path from the user
    root_folder = input("Enter the path of the root folder: ")
    change_extension(root_folder)