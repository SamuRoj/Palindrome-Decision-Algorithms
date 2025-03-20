import unittest
from palindrome import data_generator
from palindrome import constants


class DataGeneratorTest(unittest.TestCase):
    def test_data_generator_with_empty_list(self):
        N = 0
        random_list = data_generator.get_random_list(N)
        self.assertTrue(N == len(random_list))
        pass

    def test_data_generator_with_1(self):
        N = 1
        random_list = data_generator.get_random_list(N)
        self.assertTrue(N == len(random_list))
        pass

    def test_data_generator_with_2(self):
        N = 2
        random_list = data_generator.get_random_list(N)
        self.assertTrue(N == len(random_list))
        pass

    def test_data_generator_with_1000(self):
        N = 1000
        random_list = data_generator.get_random_list(N)
        self.assertTrue(N == len(random_list))
        for number in random_list:
            self.assertTrue(number <= constants.MAX_VALUE)
            self.assertTrue(number > 0)
        pass

    def test_data_generator_random_string(self):
        N = 1000
        random_string = data_generator.generate_random_string(N)
        self.assertTrue(N == len(random_string))

    def test_data_generator_generate_palindrome(self):
        N = 1000
        samples = 15
        random_palindromes = data_generator.generate_palindromes(N, samples, True)
        self.assertTrue(len(random_palindromes) == samples)
        for i in random_palindromes:
            self.assertTrue(len(i) == N or len(i) == N + 1)

    def test_data_generator_generate_palindrome_and_non_palindrome(self):
        N = 1000
        samples = 15
        random_palindromes = data_generator.generate_palindromes_and_non_palindromes(N, samples)
        self.assertTrue(len(random_palindromes) == samples)
        for i in random_palindromes:
            self.assertTrue(len(i) == N or len(i) == N + 1)

if __name__ == "__main__":
    unittest.main()
