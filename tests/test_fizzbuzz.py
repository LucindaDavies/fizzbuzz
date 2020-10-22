import unittest
from src.fizzbuzz import *

class TestFizzBuzz(unittest.TestCase):
    
    def test_fizzbuzz_returns_fizz_number_is_divisible_by_three(self):
        self.assertEqual("fizz", fizzbuzz(3))
        self.assertEqual("fizz", fizzbuzz(9))


    def test_fizzbuzz_returns_buzz_number_is_divisible_by_five(self):
        self.assertEqual("buzz", fizzbuzz(5))
        self.assertEqual("buzz", fizzbuzz(10))


    def test_fizzbuzz_returns_fizzbuzz_number_is_divisible_by_three_and_five(self):
        self.assertEqual("fizzbuzz", fizzbuzz(15))
        self.assertEqual("fizzbuzz", fizzbuzz(30))


    def test_fizzbuzz_returns_the_number_if_the_number_is_not_divisible_by_three_or_five(self):
        self.assertEqual("2", fizzbuzz(2))