import sys
sys.path.append("../src")
#TODO make it with 'pip install -e'
from math_demo import(
    add,
    add_with_bug
)
def test_addition():
    assert add(2, 2) == 4
    print("Test BASIC ADDITION")
def test_addition_with_bug():
    assert add_with_bug(2, 2) == 4, "Function did not return 4"
    assert add_with_bug(0, 0) == 0, "Function did not return 0"
    print("Test BUGGED ADDITION PASSES(does it mean code ok?)")
    #assert add_with_bug(6, 7) == 13 #will fail here
def test_addition_duplicated():
    # is it real good test (relies on absense of + in add())
    assert add(2, 3) == 2 + 3

if __name__== "__main__":
    test_addition()
    test_addition_with_bug()