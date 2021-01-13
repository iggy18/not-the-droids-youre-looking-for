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
# get values
def two_sum_hash(arr, tar):
    hash_table = dict()
    for i in range(len(arr)):
        if arr[i] in hash_table:
            return(hash_table[arr[i]], arr[i])
        else:
            hash_table[tar - arr[i]] = arr[i]
    return False

# get indices
def two_sum_index(nums, target):
    hash_table = dict()
    for i in range(len(nums)):
        if target - nums[i] in hash_table:
            return [hash_table[target - nums[i]],i]
        else:
            hash_table[nums[i]]=i