while True:
    num = str(input())
    if num == '0':
        break
    if len(num) % 2 == 0:
        left = num[:int(len(num)/2)]
        right = ''.join(reversed(num[int(len(num)/2):]))
    else:
        left = num[:int(len(num)/2)]
        right = ''.join(reversed(num[int(len(num)/2)+1:]))
    if left == right :
        print('yes')
    else:
        print('no')