import pandas as pd

# Прямая ссылка на CSV-файл на GitHub
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

# Загрузка занимает одну строчку
df = pd.read_csv(url)

print(df) # Показывает первые 5 строк таблицы