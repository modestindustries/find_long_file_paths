#!/usr/bin/python
#
# Takes a directory as an option, recursively checks the directory structure for files with a pathname with more than 1024 chars.
#
# Arg parsing code is courtesy of Greg Neagle.
#
#
# For later:
# 10.12 PATH_MAX = 1024 NAME_MAX = 255

import optparse
import os
import sys  

def walk_error_handler(exception_instance):
    '''Handle errors from os.walk()'''
    print("Error: Can't access {} ".format(exception_instance.filename))   

def main():
    '''Main'''
    usage = "usage: %prog [options]"
        
    file_path_too_long = 0
    total_files_checked = 0
    
    parser = optparse.OptionParser(usage=usage)

    optional_user_options = optparse.OptionGroup(
        parser, 'Options')
    optional_user_options.add_option(
        '--characters', '-c',
        help='Max file path characters. If this is not provided, the default of 1024 is used.')
    optional_user_options.add_option(
        '--filepath', '-f', help='File path to start at. Defaults to the current directory.')

    parser.add_option_group(optional_user_options)

    options, arguments = parser.parse_args()

    # verify options and arguments

    print options

    if options.characters:
        max_len = options.characters
    else:
        max_len = 1024
        
    if options.filepath:
        start_location = options.filepath
        os.chdir(start_location)
    else:
        start_location = os.getcwd()
    
    print ("Starting in {}".format(start_location))
    print ("Looking for file paths longer than {} characters.".format(max_len))

    for dirpath, dirs, files in os.walk(".", onerror=walk_error_handler):
        path_len = len(dirpath)
        total_files_checked += 1
        if (path_len >= max_len):
            print ("{}: {}".format(path_len, dirpath))
            file_path_too_long += 1
    
    # Tell me how many files were checked, and how many long file paths were found
    print ("Number of file paths checked: {}".format(total_files_checked))
    print ("Number of file paths longer than {} characters  : {}".format(max_len, file_path_too_long))




    
if __name__ == "__main__":
    main()
