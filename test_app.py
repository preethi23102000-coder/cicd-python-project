import pytest
from app import add, greet

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_greet():
    assert greet("Preethi") == "Hello, Preethi!"
    assert greet("World") == "Hello, World!"
