from string import digits, punctuation
msg = input("Введите строку для подсчета верхнего и нижнего регистра: ")

for x in msg:
    if x in digits or x in punctuation or x == " ":
        msg = msg.replace(x, '')

count_upper = sum(1 for c in msg if c.isupper())
count_lower = sum(1 for c in msg if not c.isupper())

print("Lower case:", count_lower, "Upper case:", count_upper)
