# practicing list comprehension
nums = [1,2,3,4,5,6,7,8]
even = [x for x in nums if x % 2 == 0]
# print(even)
# problem 1: find the second largest element
def second_largest(nums):
    unique_nums = set(nums)
    n = len(unique_nums)
    # if less than two unique elements
    if n < 2:
        return None
    sorted_nums = sorted(unique_nums,reverse=True)
    # return the second largest element
    return sorted_nums[1]
# print(second_largest([1,2,3,4,5]))