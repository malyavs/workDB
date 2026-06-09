import pandas as pd

# Вместо загрузки из URL мы читаем локальный файл
def copy_file(new_file, old_file):
    try:
        with open(old_file, 'r',encoding="UTF-8") as f:
            with open(new_file, 'w') as f2:
                for line in f:
                    f2.write(line)
    except (FileNotFoundError, FileExistsError) as e1:
        raise ValueError(f"I don't have file {e1}")
def clean_file(file):
    try:
        with open(file, 'w',encoding="UTF-8") as f:
            f.write('')
    except (FileNotFoundError, FileExistsError) as e:
        raise ValueError(f"I don't have file {e}")
def main():
    clean_file('info/data.txt')
    copy_file("info/data.txt","info/tips_data.csv")
if __name__ == '__main__':
    main()