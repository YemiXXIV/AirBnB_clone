#!/usr/bin/python3

"""
Unittest for state.py
"""

#!/usr/bin/python3
"""Test module for state class"""

import models
import unittest
from datetime import datetime
from models.state import State
from models.base_model import BaseModel


class TestState_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the State class."""

    def test_no_args_instantiates(self):
        self.assertEqual(State, type(State()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(State(), models.storage.all().values())



if __name__ == "__main__":
    unittest.main()
