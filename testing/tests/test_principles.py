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
# def test_addition_overcomplicated():
#     # formally valid test but too slow
#     for i in range(0, 2 ** 32):
#         for j in range(0, 2 ** 32):
#             assert add(i, j) == sum([i, j]) #might violate duplicate principles
#             assert add(-i, j) == sum ([-i, j])
#             assert add(i, -j) == sum ([i, -j])
#             assert add(-i, -j) == sum ([-i, -j])
def test_addition_reasonable():
    assert add(2, 2) == 4
    assert add(0, 0) == 0
    assert add(6, 7) == 13
    assert add(-6, -7) == -13
    assert add(6, -7) == -1
    assert add(-6, 7) == 1
    assert add(-7, 0) == -7
    assert add(7, 0) == 7
    print("Test ADDITION REASONABLE PASS")
def test_addition_commutative():
    assert add(7, -6) == 1
    assert add(-6, 7) == 1



if __name__== "__main__":
    test_addition()
    test_addition_with_bug()
    test_addition_duplicated()
    # test_addition_overcomplicated() # too redundant run on your fear and risk
    test_addition_reasonable()
    test_addition_commutative()