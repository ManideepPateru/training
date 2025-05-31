nums = list(map(int, input("Enter list elements: ").split()))
start = 0
end = len(nums) - 1

while start < end:
    mid = (start + end) // 2
    if nums[mid] > nums[mid + 1]:
        end = mid
    else:
        start = mid + 1
print("Peak element index:", start)
print("Peak element value:", nums[start])
