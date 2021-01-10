#time complexity of O(n^2) because two for loops
#space complexity of O()
def two_sum_brute(arr, tar):
    for first_num in range(len(arr)-1):
        for second_num in range(first_num+1, len(arr)):                
            if arr[first_num] + arr[second_num] == tar:
                return (arr[first_num], arr[second_num])
    return False

# time complexity of O(n)
# space complexity of O(n)
def two_sum_hash(arr, tar):
    hash_table = dict()
    for i in range(len(arr)):
        if arr[i] in hash_table:
            return(hash_table[arr[i]], arr[i])
        else:
            hash_table[tar - arr[i]] = arr[i]
    return False
