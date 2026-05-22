from linecache import clearcache

import pytest

@pytest.fixture
def before_after () :
    print('\n before')
    yield
    print ('\n after')



def test_test1 (before_after) :
    assert 1==1

def test_test2 (before_after) :
        assert 2==2

def test_test3(before_after):
    assert 3 == 3
