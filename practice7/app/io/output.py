def output_console(text):
    """Функція для виводу тексту в консоль"""
    print(text)

def output_file_builtin(file_path, text):
    """Функція для запису тексту до файлу за допомогою вбудованих можливостей Python"""
    with open(file_path, 'w') as file:
        file.write(text)

