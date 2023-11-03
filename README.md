# ccwc - command-line tool

`ccwc` is a command-line tool written in Python that provides word counting functionalities similar to the Unix `wc` command. It can count bytes, lines, words, and characters in a text file or from standard input.

## Table of Contents

- [Features](#features)
- [Usage](#usage)
- [Installation](#installation)
- [Examples](#examples)

## Features

- Count bytes (`-c` or `--count`)
- Count lines (`-l` or `--lines`)
- Count words (`-w` or `--words`)
- Count characters (`-m` or `--multibytes`)
- Default mode: Counts bytes, lines, and words if no options are provided
- Reads from standard input if no filename is specified

## Usage

ccwc [OPTION] [FILE]

- `OPTIONS` can include:
  - `-c`: Count bytes
  - `-l`: Count lines
  - `-w`: Count words
  - `-m`: Count characters (multibyte-aware if locale supports it)
- `FILE` is the path to the file to be analyzed. If not provided, `ccwc` reads from standard input.

## Installation

1. Clone this repository:

   ```bash
   git clone git@github.com:PBara7a/ccwc.git
   ```

2. Navigate to the `ccwc` directory:

   ```bash
   cd ccwc
   ```

3. Give the file permission to be executed:

   ```bash
   chmod +x ccwc.py
   ```

4. Run `ccwc`:

   a. Read from file

   ```bash
   ./ccwc.py [OPTION] [FILE]
   ```

   b. Read from standard input

   ```bash
   cat [FILE] | ./ccwc.py [OPTION]
   ```

## Examples

```bash
->~ ./ccwc.py test.txt
    7144   58164  335041 test.txt
```

```bash
->~ ./ccwc.py -c test.txt
    335041 test.txt
```

```bash
->~ ./ccwc.py -cl test.txt
    7144  335041 test.txt
```

```bash
->~ cat test.txt | ./ccwc.py -m
    332145
```

```bash
->~ cat test.txt | ./ccwc.py
    7144   58164  335041
```
