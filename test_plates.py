from plates import is_valid

def main():
    test_is_valid_length_short()
    test_is_valid_length_long()
    test_is_valid_number_middle()
    test_is_valid_first_number()
    test_punctuation()
    test_alph_start()

def test_is_valid_length_short():
    assert is_valid("A") == False
    assert is_valid("AA") == True

def test_is_valid_length_long():
    assert is_valid("AB12345") == False
    assert is_valid("AAAAAA") == True

def test_is_valid_number_middle():
    assert is_valid("AAA22A") == False
    assert is_valid("AAA222") == True

def test_is_valid_first_number():
    assert is_valid("AAA022") == False
    assert is_valid("AAA202") == True

def test_punctuation():
    assert is_valid("PI3.14") == False
    assert is_valid("PI3!14") == False

def test_alph_start():
    assert is_valid("123456") == False
    assert is_valid("AB1234") == True

if __name__ == "__main__":
    main()