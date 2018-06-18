#!/usr/bin/python

# Takes a directory as an option, recursively checks the directory structure for files with a pathname with more than 256 chars.

import os, sys  
    
def main():
    # print command line arguments
    #for arg in sys.argv[1:]:
    #    print arg
        
    long_file_path = 0
    total_files = 0

    arg = sys.argv[1]   
    os.chdir(arg)
    print ("Starting in {}".format(arg))

    for dirpath, dirs, files in os.walk("."):
        path_len = len(dirpath)
        total_files += 1
        if (path_len >= 256):
            print ("{}: {}".format(path_len, dirpath))
            long_file_path += 1
    
    # Tell me how many files were checked, and how many long file paths were found
    print ("Number of file paths checked: {}".format(total_files))
    print ("Number of file paths with more than 256 characters : {}".format(long_file_path))

if __name__ == "__main__":
    main()
