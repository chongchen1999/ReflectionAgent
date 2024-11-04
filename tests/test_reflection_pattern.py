import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from reflection_agent import ReflectionAgent

class TestReflectionPattern(unittest.TestCase):
    def test_full_loop(self):
        agent = ReflectionAgent()
        result = agent.run(
            user_msg="Generate a bubble sort implementation",
            generation_system_prompt="You are a Python programmer tasked with generating high-quality Python code.",
            reflection_system_prompt="You are an experienced code reviewer. Provide detailed feedback for improving the code.",
            n_steps=2
        )
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)

if __name__ == "__main__":
    unittest.main()
