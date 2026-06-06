import pandas as pd

# Вместо загрузки из URL мы читаем локальный файл
local_df = pd.read_csv('tips_data.csv')

# Теперь можно делать любые операции
print(local_df)