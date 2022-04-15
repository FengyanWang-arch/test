import pytest
def div(a,b):
    return a/b


class TestDiv:
    def test_div(self):
        assert 1==div(1,1)

if __name__=='__main__':
    pytest.main(["div_test.py::TestDiv::test_div","-vs"])