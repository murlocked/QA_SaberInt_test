new_str = input()
new_list = []
steps = []
pos = 0
for index, item in enumerate(new_str): # тут я разбиваю выражение на список из чисел и знаков e.g. ['14', '/', '2']
    if item == 'x' or item == 'х':
        item = '*'
    if item == '*' or item == '/' or item == '+' or item == '-':
        steps.append(item)
        new_list.append(new_str[pos:index])
        new_list.append(item)
        pos = index + 1
new_list.append(new_str[pos:])
  
# 4 функции для вычисления
def div(index): # деление
    new_list[index] = float(new_list[index - 1]) / float(new_list[index + 1])
    new_list.pop(index - 1)
    new_list.pop(index)
    return new_list

def mult(index): # умножение
    new_list[index] = float(new_list[index - 1]) * float(new_list[index + 1])
    new_list.pop(index - 1)
    new_list.pop(index)
    return new_list

def add(index): # сложение
    new_list[index] = float(new_list[index - 1]) + float(new_list[index + 1])
    new_list.pop(index - 1)
    new_list.pop(index)
    return new_list

def subtr(index): # вычитание
    new_list[index] = float(new_list[index - 1]) - float(new_list[index + 1])
    new_list.pop(index - 1)
    new_list.pop(index)
    return new_list

while len(new_list) != 1:
    for index, step in enumerate(steps):
        a = new_list.index(step)
        if step == '*':
            new_list = mult(a)
            steps.pop(index)
        if step == '/':
            new_list = div(a)
            steps.pop(index)
        if '*' not in steps and '/' not in steps:
            if step == '+':
                new_list = add(a)
            if step == '-':
                new_list = subtr(a)
print('{0:g}'.format(new_list[0])) #это чтобы .0 отбрасывать в конце чисел
