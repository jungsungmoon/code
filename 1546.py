N = int(input())

nums = list(map(int, input().split()))

max_score = max(nums)

print(sum([num/max_score*100 for num in nums])/len(nums))