import unittest
import sys
import io
from main_virtual_machine import VirtualMachine  # Assuming this is your VM class

class TestVirtualMachine(unittest.TestCase):
    def setUp(self):
        self.captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = self.captured_output  # and redirect stdout.

    def tearDown(self):
        sys.stdout = sys.__stdout__  # Reset redirect.

    def test_jmp(self, filename="inputs/testing"):
        self.vm = VirtualMachine(filename)
        self.vm.load_instructions(filename)
        self.vm.run()
        output = self.captured_output.getvalue().strip()  # Get stdout output
        self.assertNotIn("should not be printed", output)
        self.assertIn("JMP successful", output)

    def test_fjmp(self, filename="inputs/testing"):
        self.vm = VirtualMachine(filename)
        self.vm.load_instructions(filename)
        self.vm.run()
        output = self.captured_output.getvalue().strip()  # Get stdout output
        self.assertNotIn("should not be printed", output)
        self.assertIn("FJMP successful", output)

if __name__ == '__main__':
    unittest.main()