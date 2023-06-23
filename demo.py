import pytest

@pytest.fixture
def example():
    return 1

def test_with_fix(example):
    assert example == 1