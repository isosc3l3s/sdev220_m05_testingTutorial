import unittest

from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()
    
Print("This is my response for the end of the notebook. The test Ran in 0.01 seconds. I was worried for a while since I was not getting the functionality of code that I am used to expecting. I am relieved to see that it has worked. I understand the point of testing is a part of debugging and rounding code down to efficiency.")