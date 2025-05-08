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
def for_loops_in_main():
    source = pathlib.Path("main.py").read_text()
    tree = ast.parse(source)
    return [node for node in ast.walk(tree) if isinstance(node, (ast.For, ast.AsyncFor))]

def test_sufficient_for_loop_count(for_loops_in_main):
    num_for_loops = len(for_loops_in_main)
    assert 2 <= num_for_loops < 25

def test_optimal_for_loop_count(for_loops_in_main):
    assert len(for_loops_in_main) == 2  
