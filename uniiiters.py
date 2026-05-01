import unittest
from main import count_m
class count_test(unittest.TestCase):
    def simple_tets(self):
        s = "milad make every things remarkable"
        c = "m"
        result = 1
        self.assertEqual(count_m(s,c),result)