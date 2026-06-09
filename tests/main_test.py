from master import main


def test_clean(file):
    with open(file, 'w',encoding="UTF-8") as f:
        f.write("test")
    with open(file,'r',encoding="UTF-8") as f:
        content = f.read()
    assert content == "test"
    assert main.clean_file(file) is None
