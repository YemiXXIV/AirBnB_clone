#!/usr/bin/python3

"""
Unittests for review.py
"""
import unittest
from models.engine.file_storage import FileStorage


class TestReview(unittest.TestCase):
    """
    Test case for Review class
    """
    def test_review_obj(self):
        """
        Test if Review object can be created
        """
        from models.review import Review
        obj = Review()
        self.assertEqual(obj.text, "")
        self.assertEqual(obj.place_id, "")
        self.assertEqual(obj.user_id, "")
