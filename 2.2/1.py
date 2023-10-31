num = int(input())
arr = [ input().split(' ') for i in range(num) ]

first = 0
second = 0
third = 0
fourth = 0

def whatQuart (pair):
    first = 0
    second = 0
    third = 0
    fourth = 0
    if int(pair[0]) > 0 and int(pair[1]) > 0:
        first += 1
    elif int(pair[0]) < 0 and int(pair[1]) > 0:
        second += 1
    elif int(pair[0]) < 0 and int(pair[1]) < 0:
        third += 1
    elif int(pair[0]) > 0 and int(pair[1]) < 0:    
        fourth += 1
    return [first, second, third, fourth]
for i in arr:
    first += whatQuart(i)[0]
    second += whatQuart(i)[1]
    third += whatQuart(i)[2]
    fourth += whatQuart(i)[3]



print('Первая четверть:', first)
print('Вторая четверть:', second)
print('Третья четверть:', third)
print('Четвертая четверть:', fourth)