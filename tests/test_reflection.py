import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from reflect import reflect_content

class TestReflection(unittest.TestCase):
    def test_reflection(self):
        test_content = "def example(): pass"
        test_history = [{"role": "user", "content": "Review this code"}]
        critique = reflect_content(test_content, test_history, model="llama3-70b-8192")
        self.assertIn("improvement", critique.lower())

if __name__ == "__main__":
    unittest.main()
