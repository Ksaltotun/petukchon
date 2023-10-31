num = input()

len = len(num)

if len < 4:
    print(num)
else:
    newStr = ''
    for i in range(len):
        newStr += num[::-1][i]
        if (i + 1) % 3 == 0 and i != len - 1:
            newStr += ','
    print(newStr[::-1])
