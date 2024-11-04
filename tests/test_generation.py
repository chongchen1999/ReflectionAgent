import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from generate import generate_response
from groq import Groq

from dotenv import load_dotenv
load_dotenv()

class TestGeneration(unittest.TestCase):
    def test_generation(self):
        # Mock client and history to test generate_response
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        model = "llama-3.1-70b-versatile"
        generation_history = [{"role": "user", "content": "Test message"}]

        # Call function
        response = generate_response(client, model, generation_history)

        # Assertions
        self.assertIsNotNone(response, "Generation response should not be None")
        self.assertIsInstance(response, str, "Generation response should be a string")

if __name__ == '__main__':
    unittest.main()