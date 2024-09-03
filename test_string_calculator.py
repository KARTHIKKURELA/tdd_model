#This is the file where test cases for production code is written
def test_add():
    assert add("") == 0
    assert add("1") == 1

test_add()
