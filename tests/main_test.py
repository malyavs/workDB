from master import main



def test_clean(two_temp_files):
    src_file, dst_file = two_temp_files
    with open(src_file,'r',encoding="UTF-8") as f1:
        old_content1 = f1.read()
    with open(dst_file,'w',encoding="UTF-8") as f:
        f.write("ZEBRA")
    with open(dst_file,'r',encoding="UTF-8") as f2:
        old_content2 = f2.read()
    assert old_content2 == "ZEBRA"
    assert main.clean_file(dst_file) == None
    main.copy_file(dst_file,src_file)
    with open(dst_file,'r',encoding="UTF-8") as f1:
        assert old_content1 == f1.read()
        main.clean_file(dst_file)

"""def test_copy(new_file, old_file):
    with open(new_file,'r',encoding="UTF-8") as f:
        content = f.read()
    with open(old_file,'r',encoding="UTF-8") as f:
        content2 = f.read()
    if content != content2:
        main.copy_file("data.txt","tips_data.txt")
    with open(new_file,'r',encoding="UTF-8") as f:
        new_content = f.read()
        assert new_content == content2
"""