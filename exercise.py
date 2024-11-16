def maximum(nums):
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num
# print(maximum([1,2,3,4,5]))
def printer():
    total = 0
    count = 0
    try:
        while True:
            inputNum = int(input("Enter number:"))
            if inputNum == "Done":
                break
            total += inputNum
            count += 1
    except:
        print("Invalid input")
    print("Count " + str(count),"Total " + str(total),"Average " + str(total / count))
# printer()
def binarySearch(nums,target):
    n = len(nums)
    left = 0
    right = n - 1
    while right >= left:
        mid = (right + left) // 2
        if nums[mid] == target:
            return True
        else:
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
    return False
# print(binarySearch([1,2,3,4,5,6],9))
# string
str = 'X-DSPAM-Confidence:0.8475'
colonIndex = str.find(':')
num = str[colonIndex + 1:]
# print(float(num))
