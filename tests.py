import unittest
from markathon import Markathon


class TestBase(unittest.TestCase):
    def setUp(self):
        """Register the tag needed for the tests."""
        Markathon.register_tag(globals(), 'test_tag')

    def test_emptytag(self):
        """Test a single empty tag."""
        empty_tag = test_tag()
        self.assertEqual(str(empty_tag), '<test_tag/>')

    def test_tag_with_content(self):
        """Test a single tag with content."""
        tag_with_content = test_tag('content')
        self.assertEqual(str(tag_with_content),
                         '<test_tag>content</test_tag>')

    def test_nested_tags(self):
        """Test a tag in another tag."""
        nested_tags = test_tag(test_tag())
        self.assertEqual(str(nested_tags), '<test_tag><test_tag/></test_tag>')

    def test_attribute(self):
        """Test a tag with one attribute"""
        tag_with_attribute = test_tag(attr="hello")
        self.assertEqual(str(tag_with_attribute), '<test_tag attr="hello"/>')

    def test_duplication(self):
        """A broken tag-registration mechanism can append each tag's content
        to the previous same tag instead of creating a new one."""
        test_tag("hello")
        tag = test_tag("world")
        self.assertEqual(str(tag), '<test_tag>world</test_tag>')

    def test_tag_and_str(self):
        """Test string + markathon concatenation."""
        self.assertEqual(str(test_tag()+'after'), '<test_tag/>after')
        self.assertEqual('before'+str(test_tag()), 'before<test_tag/>')

    # TODO: Test 'before tag' and 'after tag'


from xhtml import *


class TestXHTML(unittest.TestCase):
    def setUp(self):
        """Define the XHTML DTD string."""
        DTD = ('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"'
               ' "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n')

    def test_html_tag(self):
        """Test the HTML tag, ensure that the DTD is added."""
        self.assertEqual(str(html()),
                         DTD+'<html xmlns="http://www.w3.org/1999/xhtml"/>')


if __name__ == '__main__':
    unittest.main()
