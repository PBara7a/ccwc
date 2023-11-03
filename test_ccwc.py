import unittest
import subprocess
from unittest.mock import patch
from ccwc import count_bytes, count_lines, count_words, count_characters

filename = 'test.txt'
data = open(filename, 'r').read()
data_from_stdin = subprocess.check_output(['cat', filename]).decode('utf-8')

class TestSPC(unittest.TestCase):
    """Tests will be done against wc, the Linux tool"""

    def test_byte_count(self):
        # Get the byte count from my application
        ccwc_byte_count = count_bytes(data)
        ccwc_stdin_byte_count = count_bytes(data_from_stdin)
        
        # Get the byte count from wc
        wc_output = subprocess.check_output(['wc', '-c', filename]).decode('utf-8')
        wc_byte_count = int(wc_output.strip().split()[0])
        
        self.assertEqual(ccwc_byte_count, wc_byte_count, "(File) Byte count does not match wc's output")
        self.assertEqual(ccwc_stdin_byte_count, wc_byte_count, "(stdin) Byte count does not match wc's output")

    def test_line_count(self):
        ccwc_line_count = count_lines(data)
        ccwc_stdin_line_count = count_lines(data_from_stdin)
        
        wc_output = subprocess.check_output(['wc', '-l', filename]).decode('utf-8')
        wc_byte_count = int(wc_output.strip().split()[0])
        
        self.assertEqual(ccwc_line_count, wc_byte_count, "(File) Line count does not match wc's output")
        self.assertEqual(ccwc_stdin_line_count, wc_byte_count, "(stdin) Line count does not match wc's output")

    def test_word_count(self):
        ccwc_word_count = count_words(data)
        ccwc_stdin_word_count = count_words(data_from_stdin)
        
        wc_output = subprocess.check_output(['wc', '-w', filename]).decode('utf-8')
        wc_byte_count = int(wc_output.strip().split()[0])
        
        self.assertEqual(ccwc_word_count, wc_byte_count, "(File) Word count does not match wc's output")
        self.assertEqual(ccwc_stdin_word_count, wc_byte_count, "(stdin) Word count does not match wc's output")

    def test_character_count(self):
        ccwc_character_count = count_characters(data)
        ccwc_stdin_character_count = count_characters(data_from_stdin)
        
        wc_output = subprocess.check_output(['wc', '-m', filename]).decode('utf-8')
        wc_byte_count = int(wc_output.strip().split()[0])
        
        self.assertEqual(ccwc_character_count, wc_byte_count, "(File) Character count does not match wc's output")
        self.assertEqual(ccwc_stdin_character_count, wc_byte_count, "(stdin) Character count does not match wc's output")

    @patch('locale.getpreferredencoding')
    def test_character_count_multibyte_not_supported(self, mock_getpreferredencoding):
        mock_getpreferredencoding.return_value = 'nope'

        ccwc_character_count = count_characters(data)
        ccwc_stdin_character_count = count_characters(data_from_stdin)
        
        # It should match the byte count instead
        wc_output = subprocess.check_output(['wc', '-c', filename]).decode('utf-8')
        wc_byte_count = int(wc_output.strip().split()[0])
        
        self.assertEqual(ccwc_character_count, wc_byte_count, "(File) Character count does not match wc's output")
        self.assertEqual(ccwc_stdin_character_count, wc_byte_count, "(stdin) Character count does not match wc's output")

if __name__ == '__main__':
    unittest.main()
