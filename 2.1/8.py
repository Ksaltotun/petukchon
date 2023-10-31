total = int(input())
counter = int(input())

current = 0
alive = [i + 1 for i in range(total)]


i = 0
while len(alive) > 1:
    i = (i + counter - 1) % total
    alive.pop(i)
    total -= 1
print(alive[0])
