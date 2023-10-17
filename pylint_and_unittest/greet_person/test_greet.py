import unittest
import greet

class TestGreet(unittest.TestCase):
    def test_greet_vahram(self):
        text = greet.greet_person('Vahram')
        self.assertEqual(text,'Hello, Dear Vahram')
    
    def test_greet_beautiful_world(self):
        text = greet.greet_person('beautiful world!')
        self.assertEqual(text,'Hello, Dear beautiful world!')

if __name__ == '__main__':
    unittest.main()