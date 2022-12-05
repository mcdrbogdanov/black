import os
import random

users_dir = os.path.join(r"users/")

def choiceWord(sourceText):
    messages_choiceword = ['�֧��֧��ӧ֧ߧߧ� - ', '�ߧ֧� �ߧڧ�֧ԧ� �ݧ���� ��֧� - ', '100% �ߧѧާߧ�ԧ� �ݧ���� - ']
    commandAndDelim = ['�ӧ�ҧ֧��', ' �ڧݧ� ']
    command = commandAndDelim[0]
    delim = commandAndDelim[1]
    quantity = random.choice(messages_choiceword)
    if sourceText != '':
        if command == sourceText.split()[0].lower():
            if len(sourceText.split()) > 1:
                if delim in sourceText:
                    sourceText = ' '.join(sourceText.split()[1:])
                    return ', ' + str(quantity) + random.choice(sourceText.split(delim)) + ' �0�2'
                else:
                    return ', ���ѧӧڧݧ�ߧ֧� �ҧ�է֧� - ����ҧ֧�� [���ѧ٧�] �ڧݧ� [���ѧ٧�2]'
            else:
                return ', �ܧ�ާѧߧէ� �ӧ�ҧ֧��, �ӧ�ҧ֧�֧� �ڧ� �էӧ�� �ӧѧ�ڧѧߧ��� ���ӧ֧��� - ��էڧ�!\n�9�8 ������ݧ�٧�ӧѧߧڧ�: ����ҧ֧�� [���ѧ٧�] �ڧݧ� [���ѧ٧�2]'
        return None
    return None

def choiceBall(sourceText):
    messages_ball = ['�է�', '�ߧ֧�', '��֧ۧ�ѧ� �ߧ֧ݧ�٧� ���֧է�ܧѧ٧ѧ��! �9�6', '�٧ߧѧܧ� �ԧ�ӧ���� - "�է�". �9�6', '�ӧ֧��ާ� ���ާߧڧ�֧ݧ�ߧ�. �9�6',
                     '����֧է֧ݧקߧߧ� �է�. �9�6', '�ާ�� ���ӧ֧� - "�է�" �9�6', '���֧է�֧�֧ߧ�! �9�6', '�ߧڧܧѧܧڧ� ���ާߧ֧ߧڧ�! �9�6',
                     '�٧ߧѧܧ� �ԧ�ӧ���� - "�ߧ֧�". �9�6', '�ާ�ا֧�� �ҧ��� ��ӧ֧�֧� �� �����! �9�6', '�ݧ���� �ߧ� ��ѧ��ܧѧ٧�ӧѧ��! �9�6']

    command = '��ѧ�'
    quantity = random.choice(messages_ball)
    if sourceText != '':
        if command == sourceText.split()[0].lower():
            if len(sourceText.split()) > 1:
                return ', ' + str(quantity)
            else:
                return ', ��ѧ� �էѧ�� ���ӧ֧� �ߧ� �ӧѧ� �ӧ����� �� �ӧڧէ� ���֧է�ܧѧ٧ѧߧڧ�!\n�9�6 ������ݧ�٧�ӧѧߧڧ�: ���ѧ� [��֧ܧ��]'
        else:
            return None
    return None


def infaWord(sourceText):
    messages_infa = ['��ѧߧ� ����ԧ� - ', '�ާߧ� �ܧѧا֧��� ��ܧ�ݧ� - ', '�ӧ֧����ߧ���� - ']

    command = '�ڧߧ��'
    quantity = random.choice(messages_infa)
    interest = random.randint(0, 100)
    if sourceText != '':
        if command == sourceText.split()[0].lower():
            if len(sourceText.split()) > 1:
                return ', ' + str(quantity) + str(interest) + '%'
            else:
                return ', �ڧߧ�� �էѧ�� ���ӧ֧� �ߧ� �ӧѧ� �ӧ����� �� �ӧڧէ� �����֧ߧ���!\n�9�6 ������ݧ�٧�ӧѧߧڧ�: ���ߧ�� [��֧ܧ��]'
        else:
            return None
    return None