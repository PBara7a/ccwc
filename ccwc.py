#!/usr/bin/env python3
import os
import sys
import argparse
import locale

def is_multibyte_encoding_supported() -> bool:
    locale_encoding = locale.getpreferredencoding()
    multibyte_encodings = ['utf-8', 'utf-16', 'utf-32']
    return any(encoding in locale_encoding.lower() for encoding in multibyte_encodings)

def count_bytes(data: str) -> int:
    """Function to count the bytes in a string."""
    return len(data.encode('utf-8'))
    
def count_lines(data: str) -> int:
    """Function to count the number of lines in a string."""
    return data.count('\n')
    
def count_words(data: str) -> int:
    """Function to count the number of words in a string."""
    return len(data.split())
    
def count_characters(data: str) -> int:
    """Function to count the number of characters in a file.
       If the current locale does not support multibyte characters,
       it returns a count of bytes instead."""
    if not is_multibyte_encoding_supported():
        return count_bytes(data)
    return len(data)

def read_from_stdin() -> str:
    return sys.stdin.read()

def read_from_file(filename: str) -> str:
    return open(filename, 'r').read()

def main():
    parser = argparse.ArgumentParser(prog='wc', description='A clone of the Linux tool wc')
    parser.add_argument('filename', nargs='?', type=str, help='File to process')
    parser.add_argument('-c', '--count', action='store_true', help='Count the bytes in the file')
    parser.add_argument('-l', '--lines', action='store_true', help='Count the lines in the file')
    parser.add_argument('-w', '--words', action='store_true', help='Count the words in the file')
    parser.add_argument('-m', '--multibyte', action='store_true', help='Count the multibyte characters in the file')
    args = parser.parse_args()

    filename, byte_count, line_count, word_count = '', '', '', ''
    flags_passed = any([args.count, args.lines, args.words, args.multibyte])

    data = None
    if args.filename:
        filename = args.filename
        data = read_from_file(args.filename)
    else:
        data = read_from_stdin()

    if not flags_passed:
        byte_count = count_bytes(data)
        line_count = count_lines(data)
        word_count = count_words(data)
    else:
        if args.count:
            byte_count = count_bytes(data) # The -c option cancels a prior usage of -m (not done yet)
        if args.lines:
            line_count = count_lines(data)
        if args.words:
            word_count = count_words(data)
        if args.multibyte:
            byte_count = count_characters(data)  # The -m option cancels a prior usage of -c

    print(f"{line_count} {word_count} {byte_count} {filename}")

if __name__ == '__main__':
    main()
