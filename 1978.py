N = int(input())

nums = list(map(int, input().split()))

def check_prime(num:int):
    if num == 1:
        return 0
    else:
        for n in range(2, int(num**0.5) +1):
            if num % n == 0:
                return 0
    return 1

print(sum(list(map(check_prime, nums))))