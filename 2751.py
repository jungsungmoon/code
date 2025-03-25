import sys
N = int(input())

nums = []
for n in range(N):
    nums.append(int(sys.stdin.readline()))
nums.sort()
for num in nums:
    print(num)