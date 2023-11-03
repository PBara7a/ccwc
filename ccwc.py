import os
import argparse
import locale

def is_multibyte_encoding_supported() -> bool:
    locale_encoding = locale.getpreferredencoding()
    multibyte_encodings = ['utf-8', 'utf-16', 'utf-32']
    return any(encoding in locale_encoding.lower() for encoding in multibyte_encodings)

def count_bytes(filename: str) -> int:
    """Function to count the bytes in a file."""
    try:
        return os.path.getsize(filename)
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
        return -1
    except OSError as e:
        print(f"An error occurred: {e}")
        return -1
    
def count_lines(filename: str) -> int:
    """Function to count the number of lines in a file."""
    try:
        with open(filename, 'r') as file:
            return sum(1 for line in file)
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
        return -1
    except OSError as e:
        print(f"An error occurred: {e}")
        return -1
    
def count_words(filename: str) -> int:
    """Function to count the number of words in a file."""
    try:
        with open(filename, 'r') as file:
            return sum(len(line.split()) for line in file)
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
        return -1
    except OSError as e:
        print(f"An error occurred: {e}")
        return -1
    
def count_characters(filename: str) -> int:
    """Function to count the number of characters in a file.
       If the current locale does not support multibyte characters,
       it returns a count of bytes instead."""
    if not is_multibyte_encoding_supported():
        return count_bytes(filename)
    try:
        with open(filename, 'r') as file:
            return sum(len(line) for line in file)
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
        return -1
    except OSError as e:
        print(f"An error occurred: {e}")
        return -1

def main():
    parser = argparse.ArgumentParser(prog='wc', description='A clone of the Linux tool wc')
    parser.add_argument('filename', type=str, help='File to process')
    parser.add_argument('-c', '--count', action='store_true', help='Count the bytes in the file')
    parser.add_argument('-l', '--lines', action='store_true', help='Count the lines in the file')
    parser.add_argument('-w', '--words', action='store_true', help='Count the words in the file')
    parser.add_argument('-m', '--multibyte', action='store_true', help='Count the multibyte characters in the file')

    args = parser.parse_args()

    byte_count, line_count, word_count, multibyte_count = '', '', '', ''

    if args.count and byte_count != -1:
        byte_count = count_bytes(args.filename)
    if args.lines and line_count != -1:
        line_count = count_lines(args.filename)
    if args.words and word_count != -1:
        word_count = count_words(args.filename)
    if args.multibyte and multibyte_count != -1:
        byte_count = count_characters(args.filename) # The -m option cancels a prior usage of -c

    print(f"{line_count} {word_count} {byte_count} {args.filename}")

if __name__ == '__main__':
    main()
