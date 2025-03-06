import pytest
import numbers
import decimal
from main import calculator

def test_calculator_empty():
    #given
    x = ""
    #when
    res = calculator(x)
    #then
    assert res == 0

def test_calculator_number():
    #given
    x = 100
    #when
    res = calculator(x)
    #then
    assert res == x and [isinstance(x, numbers.Number) for x in (0, 0.0, 0j, decimal.Decimal(0))]

def test_calculator_sum_comma():
    x = "1,2"

    res = calculator(x)

    assert res == 3


def test_calculator_sum_newline():
    x = "1\n2"

    res = calculator(x)

    assert res == 3


def test_calculator_sum_three_nums():
    x = "1\n2,3"

    res = calculator(x)

    assert res == 6


def test_calculator_negative_num_exception():
    x = "1\n-2,3"

    with pytest.raises(Exception):
        calculator(x)


def test_calculator_greater_than_thousand():
    x = "1001,1000\n0"

    res = calculator(x)

    assert res == 1000


def test_calculator_any_delimiter():
    x = "//#1#2"

    res = calculator(x)

    assert res == 3


def test_calculator_any_length_delimiter():
    x = "//[###]1###2###1001"

    res = calculator(x)

    assert res == 3


def test_calculator_any_multiple_delimiter():
    x = "//[##][$][***]1$2##2"

    res = calculator(x)

    assert res == 5