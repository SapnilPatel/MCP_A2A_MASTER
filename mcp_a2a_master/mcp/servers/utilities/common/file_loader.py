import os

def load_instructions_file(filename: str, default: str = "") -> str:
    """
    Loads the content of a text file containing instructions for an agent. If fiel does not exist, return the default instructions.
    
    Args:
        filename (str): The name of the file to load, relative to the current directory.
        default (str, optional): The default content to return if the file cannot be loaded. Defaults to an empty string.
        
    Returns:
        str: The content of the file if it exists, otherwise the default string.
    """

    if os.path.isfile(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    return default