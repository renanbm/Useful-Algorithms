import os
from send2trash import send2trash
import hashlib

def remove_duplicates(dir):
    unique = []
    for filename in os.listdir(dir):
        fullPath = os.path.join(dir, filename)
        if os.path.isfile(fullPath):
            filehash = hashlib.md5(open(fullPath, 'rb').read()).hexdigest()
        if filehash not in unique:
            unique.append(filehash)
        else:
            print(fullPath)


if __name__ == "__main__":
    remove_duplicates(r"C:\Users\renan\Desktop\Daycoval - Segurança\\")