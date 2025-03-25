N, M = list(map(int, input().split()))

my_sum = 0

nums = list(map(int, input().split()))

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        for k in range(j+1, len(nums)):
            temp = nums[i] + nums[j] + nums[k]
            if (temp > my_sum) & (temp <= M):
                my_sum = temp

print(my_sum)