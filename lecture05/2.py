k = input("Введите строку формата NdM, где N - количество кубиков, а M - количество сторон каждого из них: ")
number = int(k[0])
count = int(k[2:])
cubes = [[x + 1 for x in range(count)] for _ in range(number)]


s = [0]
for i in range(len(cubes)):
    pair = ''.join(str(y) for y in cubes[i])
    cmb = [int(a) + int(b) for a in s for b in pair]
    for x in cmb:
        s = [x for x in cmb]


for x in sorted((set(s))):
    print(x, '=', round(s.count(x)/len(s) * 100, 2), "%")
    # print(x, '=', s.count(x) / len(s) * 100, "%")
    # но если не сделать округление, что-то идёт не так, то ли это тонкость задачи, то ли я где-то напортачил...
