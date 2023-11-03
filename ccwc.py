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

def main():
    parser = argparse.ArgumentParser(prog='wc', description='A clone of the Linux tool wc')
    parser.add_argument('filename', type=str, help='File to process')
    parser.add_argument('-c', '--count', action='store_true', help='Count the bytes in the file')

    args = parser.parse_args()

    if args.count:
        byte_count = count_bytes(args.filename)
        if byte_count != -1:
            print(f"  {byte_count} {args.filename}")
    else:
        print("No arguments passed")

if __name__ == "__main__":
    main()
