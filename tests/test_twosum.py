import pytest
from leetcode.twosum import two_sum_brute

def test_two_sum_brute():
    A = [-2, 1, 2, 4, 7, 11]
    target = 13
    actual = two_sum_brute(A, target)
    expected = (2,11)
    assert actual == expected