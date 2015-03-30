import os

def getImlist(path):
    """Returns a list of filenames for all images in a directory."""
        
    return [os.path.join(path,f) for f in os.listdir(path)]