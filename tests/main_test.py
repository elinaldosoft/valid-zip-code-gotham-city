from app.main import valid_zip_code, valid_zip_code_alg_2


def test_valid_zip_code():
    assert valid_zip_code('10000') is False
    assert valid_zip_code('100--00--a-aaa') is False
    assert valid_zip_code('999999') is False
    assert valid_zip_code('1000000') is False
    assert valid_zip_code('121426') is False
    assert valid_zip_code('523563') is True
    assert valid_zip_code('552523') is False
    assert valid_zip_code('123456') is True
    assert valid_zip_code('123412') is True


def test_valid_zip_code_alg_2():
    assert valid_zip_code_alg_2('10000') is False
    assert valid_zip_code_alg_2('100--00--a-aaa') is False
    assert valid_zip_code_alg_2('999999') is False
    assert valid_zip_code_alg_2('1000000') is False
    assert valid_zip_code_alg_2('121426') is False
    assert valid_zip_code_alg_2('523563') is True
    assert valid_zip_code_alg_2('552523') is False
    assert valid_zip_code_alg_2('123456') is True
    assert valid_zip_code_alg_2('123412') is True
