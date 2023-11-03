import os
import argparse

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

def main():
    parser = argparse.ArgumentParser(prog='wc', description='A clone of the Linux tool wc')
    parser.add_argument('filename', type=str, help='File to process')
    parser.add_argument('-c', '--count', action='store_true', help='Count the bytes in the file')
    parser.add_argument('-l', '--lines', action='store_true', help='Count the lines in the file')

    args = parser.parse_args()

    byte_count, line_count = "", ""

    if args.count and byte_count != -1:
        byte_count = count_bytes(args.filename)
    if args.lines and line_count != -1:
        line_count = count_lines(args.filename)

    print(f"{line_count} {byte_count} {args.filename}")

if __name__ == "__main__":
    main()
