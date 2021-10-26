from string import digits, punctuation

try:
    msg = input("Введите строку формата 'СлОВо сЛоВо'. Регистр у каждой буквы любой: ")
    first, second = msg.split()
except ValueError as e:
    if len(msg.split()) > 2:
        print("Вы ввели слишком много слов. Введите два слова.")
    if len(msg.split()) <= 1:
        print("Вы ввели слишком мало слов или пробел. Введите два слова.")
    exit(1)

for x in msg:
    if x in digits or x in punctuation:
        msg = msg.replace(x, '')

res = set()
for x in first:
    for y in second:
        if x.upper() == y.upper():
            res.add(x.lower())

print(*sorted(res))


