units = {"1": "один", "2": "два", "3": "три", "4": "четыре", "5": "пять", "6": "шесть", "7": "семь",
         "8": "восемь", "9": "девять"}
second_dozen = {"10": "десять", "11": "одиннадцать", "12": "двенадцать", "13": "тринадцать", "14": "четырнадцать",
                "15": "пятнадцать","16": "шестнадцать", "17": "семнадцать", "18": "восемнадцать", "19": "девятнадцать"}
dozens = {"2": "двадцать", "3": "тридцать", "4": "сорок", "5": "пятьдесят", "6": "шестьдесят", "7": "семьдесят",
          "8": "восемьдесят", "9": "девяноста"}


def number_to_word(n) -> str:

    if len(n) == 0 or len(n) > 2 or not n.isdigit():
        print("Ошибка ввода. Введите число от 0 до 99")
        exit(1)

    result = ''

    if n[-1] == '0' and len(n) == 1:
        return "ноль"
    if n[-1] == '0' and len(n) == 2:
        pass
    else:
        result = str(units.get(n[-1]))
    if len(n) == 2:
        if n in [*second_dozen]:
            result = second_dozen.get(n)
        if n[0] in [*dozens]:
            result = dozens.get(n[0]) + ' ' + result
    return result


print(number_to_word(n=input("Введите число от 0 до 99: ")))