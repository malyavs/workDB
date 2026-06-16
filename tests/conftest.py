from fileinput import close
from os import remove
import pytest
from master import main

# Декоратор @pytest.fixture сообщает Pytest, что это фикстура
@pytest.fixture
def two_temp_files():
    with open('info/tips_data.csv', 'r') as f:
        content = f.read()
    file="first_file_with_text.txt"
    second_file="second_file_without_text.txt"
    with open(file, "w") as f:
        f.write(content)
    with open(second_file, 'w') as f:
        f.write("")
    yield file, second_file
    remove(file)
    remove(second_file)
