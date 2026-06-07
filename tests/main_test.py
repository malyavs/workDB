import main
import pytest
def test_clean(file):
    assert main.clean_file(file) == None
