import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from reflect import reflect_on_response
from groq import Groq

from dotenv import load_dotenv
load_dotenv()

class TestReflection(unittest.TestCase):
    def test_reflection(self):
        # Mock client and history to test reflect_on_response
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        model = "llama-3.1-70b-versatile"
        reflection_history = [{"role": "user", "content": "Generated content"}]
        
        # Call function
        critique = reflect_on_response(client, model, reflection_history)
        
        # Assertions
        self.assertIsNotNone(critique, "Reflection response should not be None")
        self.assertIsInstance(critique, str, "Reflection response should be a string")

if __name__ == '__main__':
    unittest.main()