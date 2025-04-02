nums = list(map(int, input().split()))

my_sum = 0
for num in nums:
    my_sum += num**2

print(my_sum%10)