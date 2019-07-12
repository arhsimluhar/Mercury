# content of test_sample.py
# dummy testcase to test pytest functionality
def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4
