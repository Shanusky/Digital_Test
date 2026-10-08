# Your testing code
from src.my_math import add_numbers, substract_numbers, multiply_numbers

def test_add_numbers():
    assert add_numbers(1,2) == 3

def test_substract_numbers():
    assert substract_numbers(5,10) == -5

def test_multiply_numbers():
    assert multiply_numbers(2,2) == 4

    
