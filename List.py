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
# problem remove duplicates
def remove_duplicates(nums):
    unique_nums = []
    for num in nums:
        if num not in unique_nums:
            unique_nums.append(num)
    return unique_nums
# print(remove_duplicates([1,2,3,3,4]))
# problem3: sum of all evens
def sum_of_evens(nums):
    sum = 0
    for num in nums:
        if num % 2 == 0:
            sum += num
    return sum
# print(sum_of_evens([1,2,3,4]))