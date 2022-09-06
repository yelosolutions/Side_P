#!/usr/bin/python3
"""to convert data sizes to human
readable form
"""


suffixes = {1024: ['KiB', 'MiB', 'GiB', 'TiB', 'EiB', 'ZiB'],
            1000: ['KB', 'MB', 'GB', 'TB', 'EB', 'ZB']}


def file_size(size, kilobyte_is_1000_bytes = True):
    """converts file size to human readable form
        arguments: 
            size -> size of data in bytes
            kilobyte_is_1000_bytes -> condition for divider  
        returns:
            key-worded string


    """
    if size < 0:
        raise ValueError("Size must be non-negative")
    divider = 1000 if kilobyte_is_1000_bytes else 1024

    for suffix in suffixes[divider]:
        size /= divider

        if size < divider:
            return '{0:.1f} {1} '.format(size, suffix)
        
    raise ValueError("Size too large")

if __name__ == '__main__':
    print(file_size(int(input("Enter file size: "))))
