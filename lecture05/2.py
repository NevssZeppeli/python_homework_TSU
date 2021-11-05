class d_exception(Exception): # тут я делаю робкую попытку сделать свой эксепшн
    def __init__(self, text):
        self.txt = text


while True:
    try:
        k = input("Введите строку формата NdM, где N - количество кубиков, а M - количество сторон каждого из них: ")
        if 'd' not in k:
            raise d_exception()
        number = int(k[0])
        count = int(k[2:])
        cubes = [[x + 1 for x in range(count)] for _ in range(number)]
        break
    except Exception as e:
        print("Неправильный ввод, введите строку снова")


s = [0]
for i in range(len(cubes)):
    pair = ''.join(str(y) for y in cubes[i])
    cmb = [int(a) + int(b) for a in s for b in pair]
    s = [x for x in cmb]


for x in sorted((set(s))):
    print(x, '=', round(s.count(x)/len(s) * 100, 2), "%")
    # print(x, '=', s.count(x) / len(s) * 100, "%")
    # но если не сделать округление, что-то идёт не так, то ли это тонкость задачи, то ли я где-то напортачил...
