import telebot
import json

token = "тут был токен"
bot = telebot.TeleBot(token)

# хэндлер для яндекс клауда
def handler(event,context):
    body = json.loads(event['body'])
    update = telebot.types.Update.de_json(body)
    bot.process_new_updates([update])

def calc(new_str):
    new_str = str(new_str)
    new_list = []
    steps = [] # сюда буду записывать последовательность действий
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
  
    # а тут цикл с вычиcлением; гоняет список по функциям сверху пока не придёт к ответу
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
        
    return '{0:g}'.format(new_list[0]) #это чтобы .0 отбрасывать в конце чисел

def listener(messages):
    for m in messages:
        chatid = m.chat.id
        if m.content_type == 'text':
            text = m.text
            bot.send_message(chatid, calc(text))

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '''Привет!
    Это бот-калькулятор для тестового задания в Saber Interactive. Калькулятор может делать самые простые вычисления: сложение, вычитание, умножение, деление. Просто отправь любое выражение в чат после этого текста, специальные команды не нужны. Пример: 14+6/2*5*2-4''')

bot.set_update_listener(listener)

# бесконечный цикл получения новых записей со стороны Telegram

if __name__ == '__main__':
    bot.infinity_polling()
