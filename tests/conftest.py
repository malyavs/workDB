import pytest
from master import main


# Декоратор @pytest.fixture сообщает Pytest, что это фикстура
@pytest.fixture
def file():
    # Этот код выполнится перед каждым тестом, который запросит эту фикстуру
    print("Подготовка файла...")
    main.copy_file('info/data.txt', 'info/tips_data.csv')
    return 'info/data.txt' # Возвращаем имя файла, которое попадет в аргумент теста
