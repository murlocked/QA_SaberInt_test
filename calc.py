new_str = input()
new_list = []
pos = 0
for index, item in enumerate(new_str): # тут я разбиваю выражение на список из чисел и знаков e.g. ['14', '/', '2']
    if item == '*' or item == '/' or item == '+' or item == '-':
        new_list.append(new_str[pos:index])
        new_list.append(item)
        pos = index + 1
new_list.append(new_str[pos:])
  
# 4 функции для вычисления
def div(index): # деление
    new_list[index] = int(new_list[index - 1]) / int(new_list[index + 1])
    new_list.pop(index - 1)
    new_list.pop(index)
    return new_list

def mult(index): # умножение
    new_list[index] = int(new_list[index - 1]) * int(new_list[index + 1])
    new_list.pop(index - 1)
    new_list.pop(index)
    return new_list

def add(index): # сложение
    new_list[index] = int(new_list[index - 1]) + int(new_list[index + 1])
    new_list.pop(index - 1)
    new_list.pop(index)
    return new_list

def subtr(index): # вычитание
    new_list[index] = int(new_list[index - 1]) - int(new_list[index + 1])
    new_list.pop(index - 1)
    new_list.pop(index)
    return new_list

# а тут цикл с вычилением; гоняет список по функциям сверху пока не придёт к ответу
while len(new_list) != 1: 
    for index, item in enumerate(new_list):
        if item == '*':
            new_list = mult(index)
        if item == '/':
            new_list = div(index)
        if '*' not in new_list and '/' not in new_list:
            if item == '+':
                new_list = add(index)
            if item == '-':
                new_list = subtr(index)

print('{0:g}'.format(new_list[0])) #это чтобы .0 отбрасывать в конце чисел
