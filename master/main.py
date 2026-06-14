"""
    file for 
"""
def copy_file(new_file, old_file):
    """
    func for copying file
    :param new_file:
    :param old_file:
    :return:
    """
    try:
        with open(old_file, 'r',encoding="UTF-8") as f:
            with open(new_file, 'w',encoding="UTF-8") as f2:
                for line in f:
                    f2.write(line)
    except (FileNotFoundError, FileExistsError) as e1:
        raise ValueError(f"I don't have file {e1}") from e1
def clean_file(file):
    """
    cleaning file
    :param file:
    :return:
    """
    try:
        with open(file, 'w',encoding="UTF-8") as f:
            f.write('')
    except (FileNotFoundError, FileExistsError):
        raise ValueError(f"I don't have file {f}") from f
def main():
    """
    main function
    :return:
    """
    clean_file('info/data.txt')
    copy_file("info/data.txt","info/tips_data.csv")
if __name__ == '__main__':
    main()
