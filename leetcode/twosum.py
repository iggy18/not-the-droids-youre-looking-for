A = [-2, 1, 2, 4, 7, 11]
target = 13

def two_sum_brute(arr, tar):
    for first_num in set(arr):
        for second_num in set(arr):
            if first_num + second_num == tar:
                return (first_num, second_num)

two_sum_brute(A, target)