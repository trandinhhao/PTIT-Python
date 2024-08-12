
if __name__ == '__main__':
    s = input()
    a = ['4', '7']
    cnt = 0
    for x in s:
        if x in a:
            cnt += 1
    if cnt==7 or cnt == 4:
        print('YES')
    else:
        print('NO')