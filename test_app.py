import pytest
from app import app

# Example test: check if app runs without crashing
def test_app_exists():
    assert app is not None

# Example test: dummy always passes
def test_dummy():
    assert True

# If your app.py has a function, test it like this:
# Suppose app.py has:
# def add(a, b):
#     return a + b
#
# Then add this test:
def test_add_function():
    from app import add
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

  
