import sys
correct_set = [1,1,2,2,2,8]
result = []
found_set = list(map(int, sys.stdin.readline().split()))
for i in range(6):
    difference = correct_set[i]-found_set[i]
    result.append(difference)
print(*result)
