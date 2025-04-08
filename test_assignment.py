import pytest
import ast
import importlib

# Test to check for file docstring
def test_file_docstring():
    with open('assignment.py', 'r') as file:
        tree = ast.parse(file.read())
    docstring = ast.get_docstring(tree)
    assert docstring is not None, "DMACC Student, there does not appear to be a docstring at the top of your file. Please add a docstring explaining what your code does."

# Test to check the return value of main
def test_main_return_value():
    from assignment import main

    total_population = main()
    expected_values = [3046355, 3046355.0, "3046355", "3,046,355"]
    assert total_population in expected_values, "DMACC Student, the return value of main should be one of the following: 3046355, '3046355', or '3,046,355'. Recieved " + str(total_population)

if __name__ == "__main__":
    pytest.main()