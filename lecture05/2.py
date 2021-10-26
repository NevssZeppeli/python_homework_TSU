from itertools import combinations

a = input("Введите строку формата NdM, где N - количество кубиков, а M - количество сторон каждого из них: ")
number = int(a[0])
count = int(a[2:])
cubes = [[x + 1 for x in range(count)] for _ in range(number)]
cub = [x for y in cubes for x in y]
print(cub)
