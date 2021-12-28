from python_final.pythonisms import add_2,convert_to,timer

def test_add_2():
    expected = [3,4,5,6]
    actual = add_2([1,2,3,4])
    assert actual == expected

def test_convert_to():
    expected = {1,2,3,4}
    actual = convert_to([1,2,3,4],"set")
    assert expected == actual
