#time complexity of O(n^2) because two for loops
#space complexity of O()
def two_sum_brute(arr, tar):
    for first_num in range(len(arr)-1):
        for second_num in range(first_num+1, len(arr)):                
            if arr[first_num] + arr[second_num] == tar:
                return (arr[first_num], arr[second_num])
    return False


