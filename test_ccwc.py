import unittest
import subprocess
from ccwc import count_bytes, main

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

if __name__ == '__main__':
    unittest.main()
