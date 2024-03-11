#!/usr/bin/python3

"""
Unittest for state.py
"""
import unittest
from models.engine.file_storage import FileStorage


class TestState(unittest.TestCase):
    """
    Test case for State class
    """
    def test_state_obj(self):
        """
        Test if State object can be created
        """
        from models.state import State
        obj = State()
        self.assertEqual(obj.name, "")

if __name__ == "__main__":
    unittest.main()
