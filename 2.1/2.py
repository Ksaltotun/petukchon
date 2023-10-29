mass = int(input())
height = float(input())

imt = mass / (height * height)

if imt > 25:
    print('Избыточная масса')
elif imt < 18.5:
    print('Недостаточная масса')
else:
    print('Оптимальная масса')


