import unittest
from src.data.preprocessing import clean_data, encode_categorical

class TestPreprocessing(unittest.TestCase):

    def test_clean_data(self):
        # Test case for cleaning data
        input_data = {
            'column1': [1, 2, None, 4],
            'column2': ['A', 'B', 'C', None]
        }
        expected_output = {
            'column1': [1, 2, 4],
            'column2': ['A', 'B', 'C']
        }
        cleaned_data = clean_data(input_data)
        self.assertEqual(cleaned_data, expected_output)

    def test_encode_categorical(self):
        # Test case for encoding categorical variables
        input_data = {
            'column1': ['A', 'B', 'A', 'C'],
        }
        expected_output = {
            'column1': [0, 1, 0, 2]
        }
        encoded_data = encode_categorical(input_data)
        self.assertEqual(encoded_data, expected_output)

if __name__ == '__main__':
    unittest.main()