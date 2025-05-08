# test_main.py

import io
import sys
import importlib
import re
import pytest
import ast
import pathlib

@pytest.fixture(scope="module")
def captured_output_once():
    old_stdout = sys.stdout
    sys.stdout = buffer = io.StringIO()
    try:
        if "main" in sys.modules:
            importlib.reload(sys.modules["main"])
        else:
            import main  # noqa: F401
    finally:
        sys.stdout = old_stdout
    return buffer.getvalue()

def test_response_count(captured_output_once):
    responses = re.findall(r"Response \d+: ", captured_output_once)
    assert len(responses) == 25

def test_temperature_headers(captured_output_once):
    headers = re.findall(r"### Temperature \d\.0", captured_output_once)
    assert len(headers) == 5

@pytest.fixture(scope="module")
def ast_tree_main():
    source = pathlib.Path("main.py").read_text()
    tree = ast.parse(source)
    return tree
    return 

def test_sufficient_for_loop_count(ast_tree_main):    
    num_for_loops = len([node for node in ast.walk(ast_tree_main) if isinstance(node, (ast.For, ast.AsyncFor))])
    assert 2 <= num_for_loops < 25

def test_optimal_for_loop_count(ast_tree_main):
    num_for_loops = len([node for node in ast.walk(ast_tree_main) if isinstance(node, (ast.For, ast.AsyncFor))])
    assert num_for_loops == 2  

def test_no_f_string(ast_tree_main):
    # Check for f-strings in the abstract syntax tree
    f_strings = [node for node in ast.walk(ast_tree_main) if isinstance(node, ast.JoinedStr)]
    assert len(f_strings) == 0, "Unauthorized feature usage detected in the code"
