from ndfl import calculate_ndfl_tax
def test_ndfl():
    assert calculate_ndfl_tax() == None
def test_ndfl_tier_1():
    assert calculate_ndfl_tax(500_000) == 65_000

def test_ndfl_tier_2():
    assert calculate_ndfl_tax(4_000_000) == 512_000

def test_ndfl_tier_3():
    assert calculate_ndfl_tax(15_000_000) == 1_602_000






