import sys

file = sys.argv[1]

with open(file, 'r', encoding='utf-8') as f:
    nums = [int(x) for x in f.read().split()]

nums.sort() 
median = nums[len(nums) // 2] 
count = sum(abs(num - median) for num in nums) 

if count > 20:
    print("20 ходов недостаточно для приведения всех элементов массива к одному числу")
else:
    print(count)
