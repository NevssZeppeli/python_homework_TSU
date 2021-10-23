import random

cubes = []

a = input("Введите строку формата NdM, где N - количество кубиков, а M - количество сторон каждого из них: ")
cubes = [[x + 1 for x in range(int(a[2:]))] for _ in range(int(a[0]))]

print(cubes)
