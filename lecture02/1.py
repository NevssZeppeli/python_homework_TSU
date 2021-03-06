from string import digits

number = input("Введите число от 0 до 99: ").strip() #вводим строку, убираем пустые символы

result = ''

#фильтр чисел, без массивов, решил использовать string.digits, если будет нельзя - то уже даже не знаю, как тут быть
if (len(number) == 0 or len(number) > 2) or (number[0] not in digits) or (len(number) == 2 and number[1] not in digits):
    print('Неправильный ввод. '
          'Запустите программу снова и введите число от 0 до 99')
    exit()

#сначала мы смотрим последнюю цифру (или единственную, если число однозначное, тут это не имеет значения, но ноль особенный!)
if number[-1] == '0' and len(number) == 1:
    result = "ноль"
if number[-1] == '1':
    result = 'один'
if number[-1] == '2':
    result = "два"
if number[-1] == '3':
    result = "три"
if number[-1] == '4':
    result = "четыре"
if number[-1] == '5':
    result = "пять"
if number[-1] == '6':
    result = "шесть"
if number[-1] == '7':
    result = "семь"
if number[-1] == '8':
    result = "восемь"
if number[-1] == '9':
    result = "9"

#здесь мы работаем с двухзначными числами
if len(number) == 2:
    #второй десяток особенный, потому нужно расписать его целиком + есть проблема,
    #ибо result перезаписывается 2 раза в случае работы с первым десятком (ноль -> десять), но я её решил
    if number == '10':
        result = 'десять'
    if number == '11':
        result = 'одиннадцать'
    if number == '12':
        result = 'двенадцать'
    if number == '13':
        result = 'тринадцать'
    if number == '14':
        result = 'четырнадцать'
    if number == '15':
        result = 'пятнадцать'
    if number == '16':
        result = 'шестнадцать'
    if number == '17':
        result = 'семнадцать'
    if number == '18':
        result = 'восемнадцать'
    if number == '19':
        result = 'девятнадцать'

    #оставшиеся десятки
    if number[0] == '2':
        result = "двадцать " + result
    if number[0] == '3':
        result = "тридцать " + result
    if number[0] == '4':
        result = "сорок " + result
    if number[0] == '5':
        result = "пятьдесят " + result
    if number[0] == '6':
        result = "шестьдесят " + result
    if number[0] == '7':
        result = "семьдесят " + result
    if number[0] == '8':
        result = "восемьдесят " + result
    if number[0] == '9':
        result = "девяноста " + result

print(result)