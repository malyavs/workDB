import pandas as pd

# Вместо загрузки из URL мы читаем локальный файл
def copy_file(new_file, old_file):
    with open(old_file, 'r') as f:
        with open(new_file, 'w') as f2:
            for line in f:
                f2.write(line)
def clean_file(file):
    with open(file, 'w') as f:
        with open(file, 'r') as f2:
            for line in f2:
                line=""
if __name__ == '__main__':
    copy_file('info/data.txt', 'info/tips_data.csv')
