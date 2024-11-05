import unittest
import os
import sys
from unittest.mock import patch
from colorama import Fore

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from reflection_agent import ReflectionAgent, BASE_GENERATION_SYSTEM_PROMPT, BASE_REFLECTION_SYSTEM_PROMPT
from generate import generate_response
from reflect import reflect_on_response
from utils import FixedFirstChatHistory, build_prompt_structure

class TestReflectionAgent(unittest.TestCase):
    def setUp(self):
        self.agent = ReflectionAgent(model="llama-3.1-70b-versatile")

    #  Basic Functionality
    def test_successful_reflection_loop(self):
        user_msg = "Can you write a short story about a cat?"
        result = self.agent.run(user_msg, verbose=0)
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    # Stop Sequence Detection
    def test_stop_sequence_in_reflection(self):
        user_msg = "Can you write a short story about a dog?"
        with patch('builtins.print') as mock_print:
            result = self.agent.run(user_msg, verbose=0)
            mock_print.assert_called_with(Fore.RED, '\n\nStop Sequence found. Stopping the reflection loop ... \n\n')
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    # empty message
    def test_empty_user_message(self):
        user_msg = ""
        with self.assertRaises(ValueError):
            self.agent.run(user_msg, verbose=0)

    # long message
    def test_long_user_message(self):
        user_msg = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus eu risus ac odio bibendum malesuada. Nulla facilisi. Sed quis eros sed magna commodo varius. Fusce vel mauris et eros rhoncus faucibus. Nullam posuere, massa vel efficitur faucibus, mi mi commodo dui, vel ultricies magna mi vel mauris. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Morbi vel commodo urna. Nullam vel magna eget mi pretium fermentum. Proin faucibus, eros vel efficitur lobortis, mi mi commodo dui, vel ultricies magna mi vel mauris."
        result = self.agent.run(user_msg, verbose=0)
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    # Verbosity Levels
    def test_high_verbosity(self):
        user_msg = "Can you write a short story about a bird?"
        with patch('builtins.print') as mock_print:
            result = self.agent.run(user_msg, verbose=2)
            self.assertEqual(mock_print.call_count, 22)
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    # Custom Prompts
    def test_custom_system_prompts(self):
        user_msg = "Can you write a short poem about the moon?"
        custom_generation_prompt = "Write the most beautiful and poetic description of the moon you can."
        custom_reflection_prompt = "Analyze the poem and provide feedback on how to improve it."
        result = self.agent.run(
            user_msg,
            generation_system_prompt=custom_generation_prompt,
            reflection_system_prompt=custom_reflection_prompt,
            verbose=0
        )
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    # high step count
    def test_high_step_count(self):
        user_msg = "Can you write a short story about a unicorn?"
        result = self.agent.run(user_msg, n_steps=10, verbose=0)
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    # low step count
    def test_low_step_count(self):
        user_msg = "Can you write a short story about a dragon?"
        result = self.agent.run(user_msg, n_steps=2, verbose=0)
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

if __name__ == '__main__':
    unittest.main()