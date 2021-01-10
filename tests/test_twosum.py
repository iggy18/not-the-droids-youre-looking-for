import pytest
from leetcode.twosum import two_sum_brute, two_sum_hash

def test_two_sum_brute_import_works():
    assert two_sum_brute

def test_two_sum_hash_import():
    assert two_sum_hash

def test_two_sum_brute():
    A = [-2, 1, 2, 4, 7, 11]
    target = 13
    actual = two_sum_brute(A, target)
    expected = (2,11)
    assert actual == expected

def test_two_sum_brute_does_does_not_use_self():
    A = [-2, 3, 2, 4, 7, 11]
    target = 6
    actual = two_sum_brute(A, target)
    expected = (2,4)
    assert actual == expected

def test_two_sum_brute_only_uses_unique_numbers():
    A = [3, 2, 7, 11]
    target = 6
    actual = two_sum_brute(A, target)
    expected = False
    assert actual == expected

def test_two_sum_brute_works_with_negative_numbers():
    A = [-1, 3, 5, 4, 7, 11]
    target = 6
    actual = two_sum_brute(A, target)
    expected = (-1,7)
    assert actual == expected

def Test_two_sum_brute_returns_false_if_no_solution():
    A = [3, 4, 7, 11]
    target = 6
    actual = two_sum_brute(A, target)
    expected = False
    assert actual == expected

def test_two_sum_hash():
    A = [-2, 1, 2, 4, 7, 11]
    target = 13
    actual = two_sum_hash(A, target)
    expected = (2,11)
    assert actual == expected

def test_two_sum_hash_does_does_not_use_self():
    A = [-2, 3, 2, 4, 7, 11]
    target = 6
    actual = two_sum_hash(A, target)
    expected = (2,4)
    assert actual == expected

def test_two_sum_hash_only_uses_unique_numbers():
    A = [3, 2, 7, 11]
    target = 6
    actual = two_sum_hash(A, target)
    expected = False
    assert actual == expected

def test_two_sum_hash_works_with_negative_numbers():
    A = [-1, 3, 5, 4, 7, 11]
    target = 6
    actual = two_sum_hash(A, target)
    expected = (-1,7)
    assert actual == expected