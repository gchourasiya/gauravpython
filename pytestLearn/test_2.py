def test_upperCase():
    assert "loud noises".upper() == "LOUD NOISES"

def test_reversed():
    assert list(reversed([1,2,3,4])) == [4,3,2,1]

def test_some_primes():
    assert 37 in [num for num in range(1,100) if num!=1 and not any ([div for div in range(2,num) if num%div==0])]
