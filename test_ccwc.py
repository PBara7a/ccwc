import unittest
import subprocess
from ccwc import count_bytes, count_lines, count_words

class TestSPC(unittest.TestCase):
    """Tests will be done against wc, the Linux tool"""

    def test_byte_count(self):
        filename = 'test.txt'
        
        # Get the byte count from my application
        ccwc_byte_count = count_bytes(filename)
        
        # Get the byte count from wc
        wc_output = subprocess.check_output(['wc', '-c', filename]).decode('utf-8')
        wc_byte_count = int(wc_output.strip().split()[0])
        
        self.assertEqual(ccwc_byte_count, wc_byte_count, "Byte count does not match wc's output")

    def test_byte_count_missing_file(self):
        filename = 'missing.txt'
        ccwc_byte_count = count_bytes(filename)
        expected_count = -1
        self.assertEqual(ccwc_byte_count, expected_count, "Byte count does not match expected")

    def test_line_count(self):
        filename = 'test.txt'
        
        ccwc_line_count = count_lines(filename)
        
        wc_output = subprocess.check_output(['wc', '-l', filename]).decode('utf-8')
        wc_byte_count = int(wc_output.strip().split()[0])
        
        self.assertEqual(ccwc_line_count, wc_byte_count, "Line count does not match wc's output")

    def test_word_count(self):
        filename = 'test.txt'
        
        ccwc_word_count = count_words(filename)
        
        wc_output = subprocess.check_output(['wc', '-w', filename]).decode('utf-8')
        wc_byte_count = int(wc_output.strip().split()[0])
        
        self.assertEqual(ccwc_word_count, wc_byte_count, "Word count does not match wc's output")

if __name__ == '__main__':
    unittest.main()
