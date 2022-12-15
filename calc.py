new_str = input()
new_list = []
pos = 0
for index, item in enumerate(new_str): # тут я разбиваю выражение на список из чисел и знаков e.g. ['14', '/', '2']
    if item == 'x' or item == 'х':
        item = '*'
    if item == '*' or item == '/' or item == '+' or item == '-':
        new_list.append(new_str[pos:index])
        new_list.append(item)
        pos = index + 1
new_list.append(new_str[pos:])
  
# 4 функции для вычисления
def div(index, new_list): # деление
    new_list[index] = float(new_list[index - 1]) / float(new_list[index + 1])
    new_list.pop(index - 1)
    new_list.pop(index)
    return new_list

def mult(index, new_list): # умножение
    new_list[index] = float(new_list[index - 1]) * float(new_list[index + 1])
    new_list.pop(index - 1)
    new_list.pop(index)
    return new_list

def add(index, new_list): # сложение
    new_list[index] = float(new_list[index - 1]) + float(new_list[index + 1])
    new_list.pop(index - 1)
    new_list.pop(index)
    return new_list

def subtr(index, new_list): # вычитание
    new_list[index] = float(new_list[index - 1]) - float(new_list[index + 1])
    new_list.pop(index - 1)
    new_list.pop(index)
    return new_list

while len(new_list) != 1:
    if '*' in new_list:
        a = new_list.index('*')
        new_list = mult(a, new_list)
    if '/' in new_list:
        a = new_list.index('/')
        new_list = div(a, new_list)
    if '*' not in new_list and '/' not in new_list:
        if '+' in new_list:
            a = new_list.index('+')
            new_list = add(a, new_list)
        if '-' in new_list:
            a = new_list.index('-')
            new_list = subtr(a, new_list)
print('{0:g}'.format(new_list[0])) #это чтобы .0 отбрасывать в конце чисел
