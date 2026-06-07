import pandas as pd

# Вместо загрузки из URL мы читаем локальный файл
local_df = pd.read_csv('tips_data.csv')
def copy_file(new_file, old_file):
    with open(old_file, 'r') as f:
        with open(new_file, 'w') as f2:
            for line in f:
                f2.write(line)
if __name__ == '__main__':
    copy_file('data.txt', 'tips_data.csv')