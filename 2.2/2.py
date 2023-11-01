numbers = input().split(' ')
count = 0

for i in range(1, len(numbers)):
    if (int(numbers[i - 1]) < int(numbers[i])):
            count += 1

print(count)