import unittest

from page_generator import extract_title

class TestPage(unittest.TestCase):
    def test_extract_title(self):
        md = '''# Tolkien Fan Club

![JRR Tolkien sitting](/images/tolkien.png)

Here's the deal, **I like Tolkien**.'''
        title = extract_title(md)
        self.assertEqual(
            title,
            "Tolkien Fan Club"
        )

    def test_extract_title2(self):
        md = '''

# Tolkien Fan Club

![JRR Tolkien sitting](/images/tolkien.png)

Here's the deal, **I like Tolkien**.'''
        title = extract_title(md)
        self.assertEqual(
            title,
            "Tolkien Fan Club"
        )