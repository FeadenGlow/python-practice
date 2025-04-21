import unittest
import os
import pandas as pd
from app.io.input import input_file_builtin, input_file_pandas

class TestFileInputFunctions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Створимо тестовий CSV файл для обох функцій
        cls.test_file_path = "data/test_file.csv"
        data = {
            "Name": ["Alice", "Bob"],
            "Age": [25, 30]
        }
        cls.df = pd.DataFrame(data)
        cls.df.to_csv(cls.test_file_path, index=False)

    @classmethod
    def tearDownClass(cls):
        # Видалимо файл після завершення всіх тестів
        if os.path.exists(cls.test_file_path):
            os.remove(cls.test_file_path)

    # 🔹 Тести для input_file_builtin
    def test_builtin_read_content(self):
        expected = self.df.to_csv(index=False)
        result = input_file_builtin(self.test_file_path)
        self.assertEqual(result.strip(), expected.strip())

    def test_builtin_read_type(self):
        result = input_file_builtin(self.test_file_path)
        self.assertIsInstance(result, str)

    def test_builtin_read_not_empty(self):
        result = input_file_builtin(self.test_file_path)
        self.assertTrue(len(result) > 0)

    # 🔹 Тести для input_file_pandas
    def test_pandas_read_content(self):
        expected = self.df.to_string(index=False)
        result = input_file_pandas(self.test_file_path)
        self.assertEqual(result.strip(), expected.strip())

    def test_pandas_read_type(self):
        result = input_file_pandas(self.test_file_path)
        self.assertIsInstance(result, str)

    def test_pandas_read_contains_name_column(self):
        result = input_file_pandas(self.test_file_path)
        self.assertIn("Name", result)

if __name__ == '__main__':
    unittest.main()
