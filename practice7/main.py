from app.io.input import input_console, input_file_builtin, input_file_pandas
from app.io.output import output_console, output_file_builtin

def main():
    text_console = input_console()
    output_console(text_console)
    
    # Зчитуємо з файлу за допомогою вбудованих можливостей Python
    text_file_builtin = input_file_builtin("data/input.txt")
    output_file_builtin("data/output.txt", text_file_builtin)
    
    # Зчитуємо з файлу за допомогою pandas
    text_file_pandas = input_file_pandas("data/input.csv")
    output_file_builtin("data/output.csv", text_file_pandas)

if __name__ == "__main__":
    main()
