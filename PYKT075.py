
def comp(x):
    ar = x.split(':')
    ar1 = ar[0].split(' ')
    return (ar1[2], ar1[1])

save = ''
a = []
st = ''
with open("SOTAY.txt", "r") as file:
    for i in file:
        if i.startswith('Ngay'): # ngay
            _, date = map(str, i.strip().split())
            save = date
        elif i.startswith('0') and len(i.strip()) == 10: #sdt
            st += i.strip() + ' ' + save
            a.append(st)
            st = ''
        else: # ten
            st += i.strip() + ': '
    a.sort(key = comp)
    with open ('DIENTHOAI.txt', "w") as f:
        for i in a:
            f.write(i + '\n')
    f.close()
    file.close()