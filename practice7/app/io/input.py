def input_console():
    """Функція для вводу тексту з консолі"""
    return input("Введіть текст: ")

def input_file_builtin(file_path):
    """Функція для зчитування з файлу за допомогою вбудованих можливостей Python"""
    with open(file_path, 'r') as file:
        return file.read()

import pandas as pd

def input_file_pandas(file_path):
    """Функція для зчитування з файлу за допомогою бібліотеки pandas"""
    return pd.read_csv(file_path).to_string(index=False)
