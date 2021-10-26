import collections

msg = input("Введите строку: ")
res = dict(collections.Counter(msg))
for key in sorted(res):
    print(key, '=', res[key])