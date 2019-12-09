def test_read_global(shared_datadir):
    contents = (shared_datadir / 'hello.txt').read_text()
    print(shared_datadir)  # C:\Users\yangkai420\AppData\Local\Temp\pytest-of-yangkai420\pytest-121\test_read_global0\data, 保存在了临时文件中, 运行期间修改data/hello.txt不会导致数据变化
    assert contents == 'Hello World!\n'
