import hashlib
import os
from tarfile import BLOCKSIZE
from unicodedata import name


def hashFile(filename):
    BLOCKSIZE = 65000    # Blocksize is taken so that we dont overflow the memory with larger data files
    hasher = hashlib.md5()
    with open(filename, 'rb') as file:
        buff = file.read(BLOCKSIZE)
        while(len(buff) > 0):
            hasher.update(buff)
            buff = file.read(BLOCKSIZE)
    return hasher.hexdigest


if __name__ == '__main__':
    hashMap = {}

    deletedFiles = []
    filelist = [f for f in os.listdir() if os.path.isfile(f)]
    for f in filelist:
        key = hashFile(f)
        if key in hashMap.keys():
            deletedFiles.append(f)
            os.remove(f)
        else:
            hashMap[key] = f
    if len(deletedFiles) != 0:
        print('Deleted Files')
        for i in deletedFiles:
            print(i)
    else:
        print('No duplicate files found.')