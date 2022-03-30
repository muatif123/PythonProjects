"""A Simple Backup Script which creates the root structure in another folder
and syncs everything which recursively lies within one of the source folders.
For files bigger than a given threshold , they are first zipped."""

# Importing the required libraries
import argparse
import gzip
import os
import shutil
import sys
import threading


# Defining the function to parse the input
def parse_input():
    parser = argparse.ArgumentParser()      # Parser function for parsing CLI which returns parse_args()
    parser.add_argument('-t', '--target', nargs = 1, required = True, help = 'Target Backup Folder')
    parser.add_argument('-s', '--source', nargs = '+', required = True, help = 'Source files to be added')
    parser.add_argument('-c', '--compress', nargs = 1, type = int, help = 'Gzip thereshold in bytes, Default is 2MB', default = [2048000])

    # Help Section will be triggered when no input is provided
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    
    return parser.parse_args()


# Defining the fucntion to inform the user of the new size
def size_if_newer(source, target):                  # If there is a change in file size, the program will report it to the user
    src_stat = os.stat(source)
    try:
        target_ts = os.stat(target).st_mtime
    except FileNotFoundError:
        try:
            target_ts = os.stat(target + '.gz').st_mtime
        except FileNotFoundError:
            target_ts = 0

    return src_stat.st_size if (src_stat.st_mtime - target_ts > 1) else False

# Defining the function for multithreading sync files and the compression threshold
def threaded_sync_file(source, target, compress):
    size = size_if_newer(source, target)

    if size:
        transfer_file(source, target, size > compress)

# Defining the function to transfer the files
def transfer_file(source, target, compress):
    try:
        if compress:
            with gzip.open(target, '.gz', 'wb') as target_fid:
                with open(source, 'rb') as source_fid:
                    target_fid.writelines(source_fid)
            print('Compress {}'.format(source))
        else:
            shutil.copy2(source, target)
            print('Copy {}'.format(source))
    except FileNotFoundError:
        os.makedirs(os.path.dirname(target))
        transfer_file(source, target, compress)


# Defining the function to synchronize with the Target folder
def sync_target(root, arg):
    target = arg.target[0]
    compress = arg.compress[0]
    threads = []

    for path, _, files in os.walk(root):
        for source in files:
            source  = path + '/' + source
            threads.append(threaded_sync_file(source, target, compress))
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    arg = parse_input()
    print('Start Copying')
    for root in arg.source:
        sync_target(root, arg)
    print('Done')




    
