from ndfl import calculate_ndfl_tax
def test_ndfl_tier_1():
    assert calculate_ndfl_tax(500_000) == 65_000

def test_ndfl_tier_2():
    assert calculate_ndfl_tax(4_000_000) == 552_000

def test_ndfl_tier_3():
    assert calculate_ndfl_tax(10_000_000) == 1_602_000

def test_ndfl_tier_4():
    assert calculate_ndfl_tax(25_000_000) == 4_402_000

def test_ndfl_tier_5():
    assert calculate_ndfl_tax(75_000_000) == 14_902_000







