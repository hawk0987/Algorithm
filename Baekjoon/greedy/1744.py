N = int(input())
positive_nums = []
negative_nums = []
one_nums = []
total = 0

for _ in range(N) :
    num = int(input())
    if num > 1 :
        positive_nums.append(num)
    elif num <= 0 :
        negative_nums.append(num)
    else :
        one_nums.append(num)

positive_nums.sort(reverse=True)
negative_nums.sort()

# 양수 계산
if len(positive_nums)%2 == 0 :
    for i in range(0, len(positive_nums), 2) :
        total += positive_nums[i] * positive_nums[i+1]
else :
    for i in range(0, len(positive_nums)-1, 2) :
        total += positive_nums[i] * positive_nums[i+1]
    total += positive_nums[-1]

# 음수 계산
if len(negative_nums)%2 == 0 :
    for i in range(0, len(negative_nums), 2) :
        total += negative_nums[i] * negative_nums[i+1]
else :
    for i in range(0, len(negative_nums)-1, 2) :
        total += negative_nums[i] * negative_nums[i+1]
    total += negative_nums[-1]

# 1 계산
total += sum(one_nums)

print(total)
