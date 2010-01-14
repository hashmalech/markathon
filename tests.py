import unittest
from markathon import *


class TestTagBehaviors(unittest.TestCase):

    def setUp(self):
        pass

    def test_simpletag(self):
        simple_tag = str(b())
        self.assertEqual(simple_tag, '<b />')

    def test_nested_tags(self):
        nested_tags = str(p(b()))
        self.assertEqual(nested_tags, '<p><b /></p>')


if __name__ == '__main__':
    unittest.main()