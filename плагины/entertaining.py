import os
import random

users_dir = os.path.join(r"users/")

def choiceWord(sourceText):
    messages_choiceword = ['естественно - ', 'нет ничего лучше чем - ', '100% намного лучше - ']
    commandAndDelim = ['выбери', ' или ']
    command = commandAndDelim[0]
    delim = commandAndDelim[1]
    quantity = random.choice(messages_choiceword)
    if sourceText != '':
        if command == sourceText.split()[0].lower():
            if len(sourceText.split()) > 1:
                if delim in sourceText:
                    sourceText = ' '.join(sourceText.split()[1:])
                    return ', ' + str(quantity) + random.choice(sourceText.split(delim)) + ' 🙂'
                else:
                    return ', правильнее будет - Выбери [фраза] или [фраза2]'
            else:
                return ', команда выбери, выберет из двух вариантов ответов - один!\n📠 Использование: Выбери [фраза] или [фраза2]'
        return None
    return None

def choiceBall(sourceText):
    messages_ball = ['да', 'нет', 'сейчас нельзя предсказать! 🔮', 'знаки говорят - "да". 🔮', 'весьма сомнительно. 🔮',
                     'определённо да. 🔮', 'мой ответ - "да" 🔮', 'предрешено! 🔮', 'никаких сомнений! 🔮',
                     'знаки говорят - "нет". 🔮', 'можешь быть уверен в этом! 🔮', 'лучше не рассказывать! 🔮']

    command = 'шар'
    quantity = random.choice(messages_ball)
    if sourceText != '':
        if command == sourceText.split()[0].lower():
            if len(sourceText.split()) > 1:
                return ', ' + str(quantity)
            else:
                return ', шар даст ответ на ваш вопрос в виде предсказания!\n🔮 Использование: Шар [текст]'
        else:
            return None
    return None


def infaWord(sourceText):
    messages_infa = ['шанс этого - ', 'мне кажется около - ', 'вероятность - ']

    command = 'инфа'
    quantity = random.choice(messages_infa)
    interest = random.randint(0, 100)
    if sourceText != '':
        if command == sourceText.split()[0].lower():
            if len(sourceText.split()) > 1:
                return ', ' + str(quantity) + str(interest) + '%'
            else:
                return ', инфа даст ответ на ваш вопрос в виде процентов!\n📊 Использование: Инфа [текст]'
        else:
            return None
    return None