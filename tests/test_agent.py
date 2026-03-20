import unittest
from ai_agent.agent import AIAgent

class TestAIAgent(unittest.TestCase):
    def test_respond(self):
        agent = AIAgent()
        self.assertEqual(agent.respond('hello'), 'You said: hello')

if __name__ == '__main__':
    unittest.main()
