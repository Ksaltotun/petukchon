num = input()
len = len(num)

if len > 5:
    print(int(num[0] + num[1:][::-1]))
else:
    print(int(num[::-1]))

