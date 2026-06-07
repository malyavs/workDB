from master import main


def test_clean(file):
    assert main.clean_file(file) == None
