import random
import json
import os
from plugins import gf

users_dir = os.path.join(r"users/")

casinoHelp = ', ���ާ��� ��� �ڧԧ�ѧ�:\n\n�7�4�7�4�0�4 ���ѧ٧ڧߧ� Platinum �C ��ѧ٧ӧݧ֧ܧѧ�֧ݧ�ߧ�� ��֧ߧ��, �ԧ���ӧ�� ���ڧߧ��� �ӧ�֧�. �� ��֧���ߧѧݧ� Platinum ��էߧ� �٧ѧҧ���: ��է֧ݧѧ�� ��ѧ�, ����ҧ� �ԧ���� ������� ����ӧ֧ݧ� �ӧ�֧ާ�. Platinum ��է�ӧݧ֧�ӧ��ڧ� �ݧ�ҧ�� �ӧѧ� �ܧѧ��ڧ�. �9�5\n\n�7�1 ����ާ���:\n�7�4�7�4�9�4 ���ѧ٧ڧߧ� [���ާާ�/�ӧ��]\n�7�4�7�4�9�4 ����֧ۧ� [�ӧӧ֧��/�ӧߧڧ�] [���ާާ�]\n�7�4�7�4�9�6 ����ҧڧ� [��ڧ�ݧ� 1-6]\n�7�4�7�4�0�5 ����ѧܧѧߧ�ڧ� [1-3] [���ާާ�]\n�7�4�7�4�9�4 ����ߧ֧�ܧ� [���֧�/��֧�ܧ�]'
casinoHelp2 = '�7�4�0�4 ���ѧ٧ڧߧ� Platinum �C ��ѧ٧ӧݧ֧ܧѧ�֧ݧ�ߧ�� ��֧ߧ��, �ԧ���ӧ�� ���ڧߧ��� �ӧ�֧�. �� ��֧���ߧѧݧ� Platinum ��էߧ� �٧ѧҧ���: ��է֧ݧѧ�� ��ѧ�, ����ҧ� �ԧ���� ������� ����ӧ֧ݧ� �ӧ�֧ާ�. Platinum ��է�ӧݧ֧�ӧ��ڧ� �ݧ�ҧ�� �ӧѧ� �ܧѧ��ڧ�. �9�5\n\n�7�1 ����ާ���:\n�7�4�7�4�9�4 ���ѧ٧ڧߧ� [���ާާ�/�ӧ��]\n�7�4�7�4�9�4 ����֧ۧ� [�ӧӧ֧��/�ӧߧڧ�] [���ާާ�]\n�7�4�7�4�9�6 ����ҧڧ� [��ڧ�ݧ� 1-6]\n�7�4�7�4�0�5 ����ѧܧѧߧ�ڧ� [1-3] [���ާާ�]\n�7�4�7�4�9�4 ����ߧ֧�ܧ� [���֧�/��֧�ܧ�]'

def casino(sourceText, id):
    get_data = gf.loadjson(users_dir + str(id) + ".json")
    if '�ܧѧ٧ڧߧ�' == sourceText.split()[0].lower():
        if len(sourceText.split()) > 1:
            summa = sourceText.split()[1].lower()
            if summa.isdigit():
                if int(summa) >= 1:
                    if int(summa) <= int(get_data['balance']):
                        if int(get_data['balance']) > 0:
                            if summa.isdigit():
                                casino_win = gf.check_casino_win(id)
                                if str(casino_win) == '1':
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    balance_do = int(get_data['balance'])
                                    user_balance = int(get_data['balance']) + int(summa)
                                    balance_posle = user_balance - balance_do
                                    get_data.update({"balance": '{}'.format(str(user_balance))})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    message_1 = ', �ӧ� �ӧ�ڧԧ�ѧݧ�: ' + str(balance_posle) + '�� �0�3\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(user_balance) + '��'
                                    return message_1
                                elif str(casino_win) == '2':
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    balance_do = int(get_data['balance'])
                                    user_balance = int(get_data['balance']) - int(summa)
                                    balance_posle = balance_do - user_balance
                                    get_data.update({"balance": '{}'.format(str(user_balance))})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    message_2 = ', �ӧ� ����ڧԧ�ѧݧ�: ' + str(balance_posle) + '�� �9�6\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(user_balance) + '��'
                                    return message_2
                                else:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    user_balance = int(get_data['balance'])
                                    message_3 = ', �է֧ߧ�ԧ� ����ѧ���� ���� ���ѧ�! �7�2\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(user_balance) + '��'
                                    return message_3
                            else:
                                return ', �ҧ�ܧӧ� �� ��ڧާӧ�ݧ� �٧ѧ��֧�֧ߧ�, ������ݧ�٧�ۧ�� ��ڧ���! �9�7'
                        else:
                            return ', �ӧѧ� �ҧѧݧѧߧ� ��ѧӧ֧� 0 ���ҧݧ֧�! �9�7'
                    else:
                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                        user_balance = get_data['balance']
                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�, ���ѧӧܧ� �ӧ��� ��֧� �է֧ߧ֧� �� �ӧѧ� �ߧ� �ҧѧݧѧߧ��! �9�6\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(user_balance) + '��'
                else:
                    return ', ���ѧӧܧ� �է�ݧاߧ� �ҧ��� �ҧ�ݧ��� 0! �9�6'

            elif sourceText.split()[1].lower() == '�ӧ��':
                user_balance = int(get_data['balance'])
                if user_balance >= 1:
                    casino_win = gf.check_casino_win(id)
                    if str(casino_win) == '1':
                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                        summa = int(get_data['balance'])
                        user_balance = int(get_data['balance']) + int(user_balance)
                        get_data.update({"balance": '{}'.format(str(user_balance))})
                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                        message_1 = ', �ӧ� �ӧ�ڧԧ�ѧݧ�: ' + str(summa) + '�� �0�3\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(user_balance) + '��'
                        return message_1
                    elif str(casino_win) == '2':
                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                        summa = int(get_data['balance'])
                        user_balance = int(get_data['balance']) - int(user_balance)
                        balance_posle = user_balance - user_balance
                        get_data.update({"balance": '{}'.format(str(user_balance))})
                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                        message_2 = ', �ӧ� ����ڧԧ�ѧݧ�: ' + str(summa) + '�� �9�6\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(balance_posle) + '��'
                        return message_2
                    else:
                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                        user_balance = int(get_data['balance'])
                        message_3 = ', �է֧ߧ�ԧ� ����ѧ���� ���� ���ѧ�! �7�2\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(user_balance) + '��'
                        return message_3
                else:
                    return ', �ӧѧ� �ҧѧݧѧߧ� ��ѧӧ֧� 0 ���ҧݧ֧�! �9�7'
            else:
                return ', �ҧ�ܧӧ� �� ��ڧާӧ�ݧ� �٧ѧ��֧�֧ߧ�! �9�7'
        else:
            return casinoHelp
    elif '�ܧ�ҧڧ�' == sourceText.split()[0].lower():
        if len(sourceText.split()) > 1:
            chislo = sourceText.split()[1].lower()
            if chislo.isdigit():
                get_data = gf.loadjson(users_dir + str(id) + ".json")
                group = str(get_data['group'])
                cubic_win = random.randint(1, 6)
                if int(chislo) <= 6:
                    if str(chislo) == '0': return ', ��ݧڧ�ܧ�� �ާѧݧ֧ߧ�ܧ�� ��ڧ�ݧ�! ������ݧ�٧�ۧ�� (��ڧ�ݧ� ��� 1 �է� 6) �9�7'
                    chislo = int(chislo)
                    if chislo != cubic_win:
                        if group == 'VIP':
                            pass_count = 4
                            while pass_count and cubic_win != chislo:
                                cubic_win = random.randint(1, 6)
                                pass_count -= 1
                        elif group == 'Premium':
                            pass_count = 3
                            while pass_count and cubic_win != chislo:
                                cubic_win = random.randint(1, 6)
                                pass_count -= 1
                        else:
                            pass_count = 1
                            while pass_count and cubic_win != chislo:
                                cubic_win = random.randint(1, 6)
                                pass_count -= 1

                    if str(chislo) == str(cubic_win):
                        with open(users_dir + str(id) + ".json", "r", encoding='utf-8') as user_profile:
                            get_data = json.load(user_profile, encoding='utf-8')
                            user_balance = int(get_data['balance']) + int(2000)
                            get_data.update({"balance": '{}'.format(str(user_balance))})
                        with open(users_dir + str(id) + ".json", "w", encoding='utf-8') as write_file:
                            json.dump(get_data, write_file, ensure_ascii=False)
                        message_1 = ', �ӧ� ��ԧѧէѧݧ�! ���ѧ� �ӧ�ڧԧ��� +2.000�� �0�5'
                        return message_1
                    else:
                        message_2 = ', �ӧ� ����ڧԧ�ѧݧ�! �����ѧݧ� ��ڧ�ݧ�: ' + str(cubic_win) + ' �9�6'
                        return message_2
                else:
                    return ', ��ݧڧ�ܧ�� �ҧ�ݧ���� ��ڧ�ݧ�! ������ݧ�٧�ۧ�� (��ڧ�ݧ� ��� 1 �է� 6) �9�7'
            else:
                return ', �ҧ�ܧӧ� �� ��ڧާӧ�ݧ� �٧ѧ��֧�֧ߧ�! ������ݧ�٧�ۧ�� (��ڧ�ݧ� ��� 1 �է� 6) �9�7'
        else:
            return casinoHelp
    elif '�ާ�ߧ֧�ܧ�' == sourceText.split()[0].lower():
        if len(sourceText.split()) == 2:
            get_data = gf.loadjson(users_dir + str(id) + ".json")
            group = str(get_data['group'])
            chislo = sourceText.split()[1].lower()
            summa = 2000
            monetka_win = random.randint(1, 2)
            if chislo.isalpha() and chislo in ['���ק�', '���֧�', '��֧�ܧ�']:
                chislo = gf.check_word_monetka(chislo)
                if chislo != monetka_win:
                    if group == 'Premium':
                        pass_count = 2
                        while pass_count and monetka_win != chislo:
                            monetka_win = random.randint(1, 2)
                            pass_count -= 1
                    elif group == 'VIP':
                        pass_count = 1
                        while pass_count and monetka_win != chislo:
                            monetka_win = random.randint(1, 2)
                            pass_count -= 1
                    else:
                        pass_count = 0
                        while pass_count and monetka_win != chislo:
                            monetka_win = random.randint(1, 2)
                            pass_count -= 1

                if int(chislo) == int(monetka_win):
                    with open(users_dir + str(id) + ".json", "r", encoding='utf-8') as user_profile:
                        get_data = json.load(user_profile, encoding='utf-8')
                        user_balance = int(get_data['balance']) + int(summa)
                        get_data.update({"balance": '{}'.format(str(user_balance))})
                    with open(users_dir + str(id) + ".json", "w", encoding='utf-8') as write_file:
                        json.dump(get_data, write_file, ensure_ascii=False)
                    message_1 = ', �ӧ� ��ԧѧէѧݧ�! �9�9 ���ѧ� ���ڧ�: +2.000�� �0�1\n�9�0 �� �ܧ��֧ݧ�ܧ�: ' + str(user_balance) + '��'
                    gen_chislo = random.randint(1, 2)
                    if int(gen_chislo) == 1:
                        return message_1
                    else:
                        return message_1
                else:
                    message_2 = ', �ӧ� �ߧ� ��ԧѧէѧݧ�! �0�1 ' + str(gf.convert_win_monetka(monetka_win)) + '. �9�6'
                    gen_chislo = random.randint(1, 2)
                    if int(gen_chislo) == 1:
                        return message_2
                    else:
                        return message_2
            else:
                return ', �ڧ���ݧ�٧�ӧѧߧڧ�: �0�0����ߧ֧�ܧ� [���֧�/��֧�ܧ�]�0�3'
        elif len(sourceText.split()) >= 3:
            return casinoHelp
        else:
            return casinoHelp

    elif '���֧ۧ�' == sourceText.split()[0].lower():
        if len(sourceText.split()) == 3:
            get_data = gf.loadjson(users_dir + str(id) + ".json")
            group = str(get_data['group'])
            word = sourceText.split()[1].lower()
            traid_win = random.randint(1, 2)
            summa = sourceText.split()[2].lower()
            if word.isalpha() and word in ['�ӧӧ֧��', '�ӧߧڧ�']:
                user_balance = int(get_data['balance'])
                if user_balance >= 1:
                    if summa.isdigit():
                        chislo = gf.check_word_traid(word)
                        if chislo != traid_win:
                            if group == 'Premium':
                                pass_count = 2
                                while pass_count and traid_win != chislo:
                                    traid_win = random.randint(1, 2)
                                    pass_count -= 1
                            elif group == 'VIP':
                                pass_count = 1
                                while pass_count and traid_win != chislo:
                                    traid_win = random.randint(1, 2)
                                    pass_count -= 1
                            else:
                                pass_count = 0
                                while pass_count and traid_win != chislo:
                                    traid_win = random.randint(1, 2)
                                    pass_count -= 1

                        if int(chislo) == int(traid_win):
                            gen_traid = random.randint(5, 45)
                            trade_wins = random.randint(200, 500)
                            with open(users_dir + str(id) + ".json", "r", encoding='utf-8') as user_profile:
                                get_data = json.load(user_profile, encoding='utf-8')
                                user_balance = int(get_data['balance']) + int(trade_wins)
                                get_data.update({"balance": '{}'.format(str(user_balance))})
                            with open(users_dir + str(id) + ".json", "w", encoding='utf-8') as write_file:
                                json.dump(get_data, write_file, ensure_ascii=False)
                            message_1 = ', �ܧ��� ���էߧ�ݧ��7�2 �ߧ� ' + str(gen_traid) + '��\n�7�3 ���� �٧ѧ�ѧҧ��ѧݧ� +' + str(trade_wins) + '��\n�9�0 �� �ܧ��֧ݧ�ܧ�: ' + str(user_balance) + '��'
                            message_2 = ', �ܧ��� ���ѧ݁7�3 �ߧ� ' + str(gen_traid) + '��\n�7�3 ���� �٧ѧ�ѧҧ��ѧݧ� +' + str(trade_wins) + '��\n�9�0 �� �ܧ��֧ݧ�ܧ�: ' + str(user_balance) + '��'
                            gen_chislo = random.randint(1, 2)
                            if int(gen_chislo) == 1:
                                return message_1
                            else:
                                return message_2
                        else:
                            gen_traid = random.randint(5, 45)
                            with open(users_dir + str(id) + ".json", "r", encoding='utf-8') as user_profile:
                                get_data = json.load(user_profile, encoding='utf-8')
                                user_balance = int(get_data['balance']) - int(summa)
                                get_data.update({"balance": '{}'.format(str(user_balance))})
                            with open(users_dir + str(id) + ".json", "w", encoding='utf-8') as write_file:
                                json.dump(get_data, write_file, ensure_ascii=False)

                            gen_chislo = random.randint(1, 2)
                            message_1 = ', �ܧ��� ���էߧ�ݧ��7�2 �ߧ� ' + str(gen_traid) + '��\n�7�4 ���� ����֧��ݧ�: ' + str(summa) + '��\n�9�0 �� �ܧ��֧ݧ�ܧ�: ' + str(user_balance) + '��'
                            message_2 = ', �ܧ��� ���ѧ݁7�3 �ߧ� ' + str(gen_traid) + '��\n�7�4 ���� ����֧��ݧ�: ' + str(summa) + '��\n�9�0 �� �ܧ��֧ݧ�ܧ�: ' + str(user_balance) + '��'
                            if int(gen_chislo) == 1:
                                return message_1
                            else:
                                return message_2
                    else:
                        return ', �ڧ���ݧ�٧�ӧѧߧڧ�: �0�0����֧ۧ� [�ӧӧ֧��/�ӧߧڧ�] [���ާާ�]�0�3'
                else:
                    return ', �ӧѧ� �ҧѧݧѧߧ� ��ѧӧ֧� 0 ���ҧݧ֧�! �9�7'
            else:
                return ', �ڧ���ݧ�٧�ӧѧߧڧ�: �0�0����֧ۧ� [�ӧӧ֧��/�ӧߧڧ�] [���ާާ�]�0�3'
        elif len(sourceText.split()) >= 3:
            return casinoHelp
        else:
            return casinoHelp

    elif '���ѧܧѧߧ�ڧ�' == sourceText.split()[0].lower():
        if len(sourceText.split()) > 2:
            get_data = gf.loadjson(users_dir + str(id) + ".json")
            group = str(get_data['group'])
            user_balance = get_data['balance']
            chislo = sourceText.split()[1].lower()
            summa = sourceText.split()[2].lower()
            if chislo.isdigit() and summa.isdigit():
                if int(summa) <= int(user_balance):
                    if int(get_data['balance']) > 0:
                          import random
import json
import os
from plugins import gf

users_dir = os.path.join(r"users/")

casinoHelp = ', ���ާ��� ��� �ڧԧ�ѧ�:\n\n�7�4�7�4�0�4 ���ѧ٧ڧߧ� Platinum �C ��ѧ٧ӧݧ֧ܧѧ�֧ݧ�ߧ�� ��֧ߧ��, �ԧ���ӧ�� ���ڧߧ��� �ӧ�֧�. �� ��֧���ߧѧݧ� Platinum ��էߧ� �٧ѧҧ���: ��է֧ݧѧ�� ��ѧ�, ����ҧ� �ԧ���� ������� ����ӧ֧ݧ� �ӧ�֧ާ�. Platinum ��է�ӧݧ֧�ӧ��ڧ� �ݧ�ҧ�� �ӧѧ� �ܧѧ��ڧ�. �9�5\n\n�7�1 ����ާ���:\n�7�4�7�4�9�4 ���ѧ٧ڧߧ� [���ާާ�/�ӧ��]\n�7�4�7�4�9�4 ����֧ۧ� [�ӧӧ֧��/�ӧߧڧ�] [���ާާ�]\n�7�4�7�4�9�6 ����ҧڧ� [��ڧ�ݧ� 1-6]\n�7�4�7�4�0�5 ����ѧܧѧߧ�ڧ� [1-3] [���ާާ�]\n�7�4�7�4�9�4 ����ߧ֧�ܧ� [���֧�/��֧�ܧ�]'
casinoHelp2 = '�7�4�0�4 ���ѧ٧ڧߧ� Platinum �C ��ѧ٧ӧݧ֧ܧѧ�֧ݧ�ߧ�� ��֧ߧ��, �ԧ���ӧ�� ���ڧߧ��� �ӧ�֧�. �� ��֧���ߧѧݧ� Platinum ��էߧ� �٧ѧҧ���: ��է֧ݧѧ�� ��ѧ�, ����ҧ� �ԧ���� ������� ����ӧ֧ݧ� �ӧ�֧ާ�. Platinum ��է�ӧݧ֧�ӧ��ڧ� �ݧ�ҧ�� �ӧѧ� �ܧѧ��ڧ�. �9�5\n\n�7�1 ����ާ���:\n�7�4�7�4�9�4 ���ѧ٧ڧߧ� [���ާާ�/�ӧ��]\n�7�4�7�4�9�4 ����֧ۧ� [�ӧӧ֧��/�ӧߧڧ�] [���ާާ�]\n�7�4�7�4�9�6 ����ҧڧ� [��ڧ�ݧ� 1-6]\n�7�4�7�4�0�5 ����ѧܧѧߧ�ڧ� [1-3] [���ާާ�]\n�7�4�7�4�9�4 ����ߧ֧�ܧ� [���֧�/��֧�ܧ�]'

def casino(sourceText, id):
    get_data = gf.loadjson(users_dir + str(id) + ".json")
    if '�ܧѧ٧ڧߧ�' == sourceText.split()[0].lower():
        if len(sourceText.split()) > 1:
            summa = sourceText.split()[1].lower()
            if summa.isdigit():
                if int(summa) >= 1:
                    if int(summa) <= int(get_data['balance']):
                        if int(get_data['balance']) > 0:
                            if summa.isdigit():
                                casino_win = gf.check_casino_win(id)
                                if str(casino_win) == '1':
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    balance_do = int(get_data['balance'])
                                    user_balance = int(get_data['balance']) + int(summa)
                                    balance_posle = user_balance - balance_do
                                    get_data.update({"balance": '{}'.format(str(user_balance))})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    message_1 = ', �ӧ� �ӧ�ڧԧ�ѧݧ�: ' + str(balance_posle) + '�� �0�3\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(user_balance) + '��'
                                    return message_1
                                elif str(casino_win) == '2':
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    balance_do = int(get_data['balance'])
                                    user_balance = int(get_data['balance']) - int(summa)
                                    balance_posle = balance_do - user_balance
                                    get_data.update({"balance": '{}'.format(str(user_balance))})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    message_2 = ', �ӧ� ����ڧԧ�ѧݧ�: ' + str(balance_posle) + '�� �9�6\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(user_balance) + '��'
                                    return message_2
                                else:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    user_balance = int(get_data['balance'])
                                    message_3 = ', �է֧ߧ�ԧ� ����ѧ���� ���� ���ѧ�! �7�2\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(user_balance) + '��'
                                    return message_3
                            else:
                                return ', �ҧ�ܧӧ� �� ��ڧާӧ�ݧ� �٧ѧ��֧�֧ߧ�, ������ݧ�٧�ۧ�� ��ڧ���! �9�7'
                        else:
                            return ', �ӧѧ� �ҧѧݧѧߧ� ��ѧӧ֧� 0 ���ҧݧ֧�! �9�7'
                    else:
                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                        user_balance = get_data['balance']
                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�, ���ѧӧܧ� �ӧ��� ��֧� �է֧ߧ֧� �� �ӧѧ� �ߧ� �ҧѧݧѧߧ��! �9�6\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(user_balance) + '��'
                else:
                    return ', ���ѧӧܧ� �է�ݧاߧ� �ҧ��� �ҧ�ݧ��� 0! �9�6'

            elif sourceText.split()[1].lower() == '�ӧ��':
                user_balance = int(get_data['balance'])
                if user_balance >= 1:
                    casino_win = gf.check_casino_win(id)
                    if str(casino_win) == '1':
                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                        summa = int(get_data['balance'])
                        user_balance = int(get_data['balance']) + int(user_balance)
                        get_data.update({"balance": '{}'.format(str(user_balance))})
                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                        message_1 = ', �ӧ� �ӧ�ڧԧ�ѧݧ�: ' + str(summa) + '�� �0�3\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(user_balance) + '��'
                        return message_1
                    elif str(casino_win) == '2':
                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                        summa = int(get_data['balance'])
                        user_balance = int(get_data['balance']) - int(user_balance)
                        balance_posle = user_balance - user_balance
                        get_data.update({"balance": '{}'.format(str(user_balance))})
                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                        message_2 = ', �ӧ� ����ڧԧ�ѧݧ�: ' + str(summa) + '�� �9�6\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(balance_posle) + '��'
                        return message_2
                    else:
                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                        user_balance = int(get_data['balance'])
                        message_3 = ', �է֧ߧ�ԧ� ����ѧ���� ���� ���ѧ�! �7�2\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(user_balance) + '��'
                        return message_3
                else:
                    return ', �ӧѧ� �ҧѧݧѧߧ� ��ѧӧ֧� 0 ���ҧݧ֧�! �9�7'
            else:
                return ', �ҧ�ܧӧ� �� ��ڧާӧ�ݧ� �٧ѧ��֧�֧ߧ�! �9�7'
        else:
            return casinoHelp
    elif '�ܧ�ҧڧ�' == sourceText.split()[0].lower():
        if len(sourceText.split()) > 1:
            chislo = sourceText.split()[1].lower()
            if chislo.isdigit():
                get_data = gf.loadjson(users_dir + str(id) + ".json")
                group = str(get_data['group'])
                cubic_win = random.randint(1, 6)
                if int(chislo) <= 6:
                    if str(chislo) == '0': return ', ��ݧڧ�ܧ�� �ާѧݧ֧ߧ�ܧ�� ��ڧ�ݧ�! ������ݧ�٧�ۧ�� (��ڧ�ݧ� ��� 1 �է� 6) �9�7'
                    chislo = int(chislo)
                    if chislo != cubic_win:
                        if group == 'VIP':
                            pass_count = 4
                            while pass_count and cubic_win != chislo:
                                cubic_win = random.randint(1, 6)
                                pass_count -= 1
                        elif group == 'Premium':
                            pass_count = 3
                            while pass_count and cubic_win != chislo:
                                cubic_win = random.randint(1, 6)
                                pass_count -= 1
                        else:
                            pass_count = 1
                            while pass_count and cubic_win != chislo:
                                cubic_win = random.randint(1, 6)
                                pass_count -= 1

                    if str(chislo) == str(cubic_win):
                        with open(users_dir + str(id) + ".json", "r", encoding='utf-8') as user_profile:
                            get_data = json.load(user_profile, encoding='utf-8')
                            user_balance = int(get_data['balance']) + int(2000)
                            get_data.update({"balance": '{}'.format(str(user_balance))})
                        with open(users_dir + str(id) + ".json", "w", encoding='utf-8') as write_file:
                            json.dump(get_data, write_file, ensure_ascii=False)
                        message_1 = ', �ӧ� ��ԧѧէѧݧ�! ���ѧ� �ӧ�ڧԧ��� +2.000�� �0�5'
                        return message_1
                    else:
                        message_2 = ', �ӧ� ����ڧԧ�ѧݧ�! �����ѧݧ� ��ڧ�ݧ�: ' + str(cubic_win) + ' �9�6'
                        return message_2
                else:
                    return ', ��ݧڧ�ܧ�� �ҧ�ݧ���� ��ڧ�ݧ�! ������ݧ�٧�ۧ�� (��ڧ�ݧ� ��� 1 �է� 6) �9�7'
            else:
                return ', �ҧ�ܧӧ� �� ��ڧާӧ�ݧ� �٧ѧ��֧�֧ߧ�! ������ݧ�٧�ۧ�� (��ڧ�ݧ� ��� 1 �է� 6) �9�7'
        else:
            return casinoHelp
    elif '�ާ�ߧ֧�ܧ�' == sourceText.split()[0].lower():
        if len(sourceText.split()) == 2:
            get_data = gf.loadjson(users_dir + str(id) + ".json")
            group = str(get_data['group'])
            chislo = sourceText.split()[1].lower()
            summa = 2000
            monetka_win = random.randint(1, 2)
            if chislo.isalpha() and chislo in ['���ק�', '���֧�', '��֧�ܧ�']:
                chislo = gf.check_word_monetka(chislo)
                if chislo != monetka_win:
                    if group == 'Premium':
                        pass_count = 2
                        while pass_count and monetka_win != chislo:
                            monetka_win = random.randint(1, 2)
                            pass_count -= 1
                    elif group == 'VIP':
                        pass_count = 1
                        while pass_count and monetka_win != chislo:
                            monetka_win = random.randint(1, 2)
                            pass_count -= 1
                    else:
                        pass_count = 0
                        while pass_count and monetka_win != chislo:
                            monetka_win = random.randint(1, 2)
                            pass_count -= 1

                if int(chislo) == int(monetka_win):
                    with open(users_dir + str(id) + ".json", "r", encoding='utf-8') as user_profile:
                        get_data = json.load(user_profile, encoding='utf-8')
                        user_balance = int(get_data['balance']) + int(summa)
                        get_data.update({"balance": '{}'.format(str(user_balance))})
                    with open(users_dir + str(id) + ".json", "w", encoding='utf-8') as write_file:
                        json.dump(get_data, write_file, ensure_ascii=False)
                    message_1 = ', �ӧ� ��ԧѧէѧݧ�! �9�9 ���ѧ� ���ڧ�: +2.000�� �0�1\n�9�0 �� �ܧ��֧ݧ�ܧ�: ' + str(user_balance) + '��'
                    gen_chislo = random.randint(1, 2)
                    if int(gen_chislo) == 1:
                        return message_1
                    else:
                        return message_1
                else:
                    message_2 = ', �ӧ� �ߧ� ��ԧѧէѧݧ�! �0�1 ' + str(gf.convert_win_monetka(monetka_win)) + '. �9�6'
                    gen_chislo = random.randint(1, 2)
                    if int(gen_chislo) == 1:
                        return message_2
                    else:
                        return message_2
            else:
                return ', �ڧ���ݧ�٧�ӧѧߧڧ�: �0�0����ߧ֧�ܧ� [���֧�/��֧�ܧ�]�0�3'
        elif len(sourceText.split()) >= 3:
            return casinoHelp
        else:
            return casinoHelp

    elif '���֧ۧ�' == sourceText.split()[0].lower():
        if len(sourceText.split()) == 3:
            get_data = gf.loadjson(users_dir + str(id) + ".json")
            group = str(get_data['group'])
            word = sourceText.split()[1].lower()
            traid_win = random.randint(1, 2)
            summa = sourceText.split()[2].lower()
            if word.isalpha() and word in ['�ӧӧ֧��', '�ӧߧڧ�']:
                user_balance = int(get_data['balance'])
                if user_balance >= 1:
                    if summa.isdigit():
                        chislo = gf.check_word_traid(word)
                        if chislo != traid_win:
                            if group == 'Premium':
                                pass_count = 2
                                while pass_count and traid_win != chislo:
                                    traid_win = random.randint(1, 2)
                                    pass_count -= 1
                            elif group == 'VIP':
                                pass_count = 1
                                while pass_count and traid_win != chislo:
                                    traid_win = random.randint(1, 2)
                                    pass_count -= 1
                            else:
                                pass_count = 0
                                while pass_count and traid_win != chislo:
                                    traid_win = random.randint(1, 2)
                                    pass_count -= 1

                        if int(chislo) == int(traid_win):
                            gen_traid = random.randint(5, 45)
                            trade_wins = random.randint(200, 500)
                            with open(users_dir + str(id) + ".json", "r", encoding='utf-8') as user_profile:
                                get_data = json.load(user_profile, encoding='utf-8')
                                user_balance = int(get_data['balance']) + int(trade_wins)
                                get_data.update({"balance": '{}'.format(str(user_balance))})
                            with open(users_dir + str(id) + ".json", "w", encoding='utf-8') as write_file:
                                json.dump(get_data, write_file, ensure_ascii=False)
                            message_1 = ', �ܧ��� ���էߧ�ݧ��7�2 �ߧ� ' + str(gen_traid) + '��\n�7�3 ���� �٧ѧ�ѧҧ��ѧݧ� +' + str(trade_wins) + '��\n�9�0 �� �ܧ��֧ݧ�ܧ�: ' + str(user_balance) + '��'
                            message_2 = ', �ܧ��� ���ѧ݁7�3 �ߧ� ' + str(gen_traid) + '��\n�7�3 ���� �٧ѧ�ѧҧ��ѧݧ� +' + str(trade_wins) + '��\n�9�0 �� �ܧ��֧ݧ�ܧ�: ' + str(user_balance) + '��'
                            gen_chislo = random.randint(1, 2)
                            if int(gen_chislo) == 1:
                                return message_1
                            else:
                                return message_2
                        else:
                            gen_traid = random.randint(5, 45)
                            with open(users_dir + str(id) + ".json", "r", encoding='utf-8') as user_profile:
                                get_data = json.load(user_profile, encoding='utf-8')
                                user_balance = int(get_data['balance']) - int(summa)
                                get_data.update({"balance": '{}'.format(str(user_balance))})
                            with open(users_dir + str(id) + ".json", "w", encoding='utf-8') as write_file:
                                json.dump(get_data, write_file, ensure_ascii=False)

                            gen_chislo = random.randint(1, 2)
                            message_1 = ', �ܧ��� ���էߧ�ݧ��7�2 �ߧ� ' + str(gen_traid) + '��\n�7�4 ���� ����֧��ݧ�: ' + str(summa) + '��\n�9�0 �� �ܧ��֧ݧ�ܧ�: ' + str(user_balance) + '��'
                            message_2 = ', �ܧ��� ���ѧ݁7�3 �ߧ� ' + str(gen_traid) + '��\n�7�4 ���� ����֧��ݧ�: ' + str(summa) + '��\n�9�0 �� �ܧ��֧ݧ�ܧ�: ' + str(user_balance) + '��'
                            if int(gen_chislo) == 1:
                                return message_1
                            else:
                                return message_2
                    else:
                        return ', �ڧ���ݧ�٧�ӧѧߧڧ�: �0�0����֧ۧ� [�ӧӧ֧��/�ӧߧڧ�] [���ާާ�]�0�3'
                else:
                    return ', �ӧѧ� �ҧѧݧѧߧ� ��ѧӧ֧� 0 ���ҧݧ֧�! �9�7'
            else:
                return ', �ڧ���ݧ�٧�ӧѧߧڧ�: �0�0����֧ۧ� [�ӧӧ֧��/�ӧߧڧ�] [���ާާ�]�0�3'
        elif len(sourceText.split()) >= 3:
            return casinoHelp
        else:
            return casinoHelp

    elif '���ѧܧѧߧ�ڧ�' == sourceText.split()[0].lower():
        if len(sourceText.split()) > 2:
            get_data = gf.loadjson(users_dir + str(id) + ".json")
            group = str(get_data['group'])
            user_balance = get_data['balance']
            chislo = sourceText.split()[1].lower()
            summa = sourceText.split()[2].lower()
            if chislo.isdigit() and summa.isdigit():
                if int(summa) <= int(user_balance):
                    if int(get_data['balance']) > 0:
                            glass_win = random.randint(1, 3)
                            if int(chislo) <= 3:
                                if int(chislo) == 0: return ', ��ڧ�ݧ� �է�ݧاߧ� �ҧ��� �ҧ�ݧ��� 0! ������ݧ�٧�ۧ�� (��ڧ�ݧ� ��� 1 �է� 3) �9�7'
                                if int(summa) == 0: return ', ���ާާ� �է�ݧاߧ� �ҧ��� �ҧ�ݧ��� 0! �9�7'
                                chislo = int(chislo)
                                if chislo != glass_win:
                                    if group == 'Premium':
                                        pass_count = 3
                                        while pass_count and glass_win != chislo:
                                            glass_win = random.randint(1, 3)
                                            pass_count -= 1
                                    elif group == 'VIP':
                                        pass_count = 1
                                        while pass_count and glass_win != chislo:
                                            glass_win = random.randint(1, 3)
                                            pass_count -= 1
                                    else:
                                        pass_count = 0
                                        while pass_count and glass_win != chislo:
                                            glass_win = random.randint(1, 3)
                                            pass_count -= 1

                                if int(chislo) == int(glass_win):
                                    with open(users_dir + str(id) + ".json", "r", encoding='utf-8') as user_profile:
                                        get_data = json.load(user_profile, encoding='utf-8')
                                        user_balance = int(get_data['balance']) + int(summa)
                                        get_data.update({"balance": '{}'.format(str(user_balance))})
                                    with open(users_dir + str(id) + ".json", "w", encoding='utf-8') as write_file:
                                        json.dump(get_data, write_file, ensure_ascii=False)
                                    return ', �ӧ� ��ԧѧէѧݧ�! �0�3 ����ڧ�: ' + str(summa) + '��\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(user_balance) + '��'
                                else:
                                    with open(users_dir + str(id) + ".json", "r", encoding='utf-8') as user_profile:
                                        get_data = json.load(user_profile, encoding='utf-8')
                                        user_balance = int(get_data['balance']) - int(summa)
                                        get_data.update({"balance": '{}'.format(str(user_balance))})
                                    with open(users_dir + str(id) + ".json", "w", encoding='utf-8') as write_file:
                                        json.dump(get_data, write_file, ensure_ascii=False)
                                    return ', �ӧ� �ߧ� ��ԧѧէѧݧ�, ���� �ҧ��: ' + str(glass_win) + '-��� ���ѧܧѧߧ�ڧ�! �9�6\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(user_balance) + '��'
                            else:
                                return ', ��ݧڧ�ܧ�� �ҧ�ݧ���� ��ڧ�ݧ�! �9�7'
                    else:
                        return ', �ӧѧ� �ҧѧݧѧߧ� ��ѧӧ֧� 0 ���ҧݧ֧�! �9�7'
                else:
                    file = open(users_dir + str(id) + ".json", "r", encoding='utf-8')
                    get_data = json.load(file, encoding='utf-8')
                    file.close()
                    user_balance = get_data['balance']
                    return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�, ���ѧӧܧ� �ӧ��� ��֧� �է֧ߧ֧� �� �ӧѧ� �ߧ� �ҧѧݧѧߧ��! �9�6\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(user_balance) + '��'
            else:
                return ', �ҧ�ܧӧ� �� ��ڧާӧ�ݧ� �٧ѧ��֧�֧ߧ�! �9�7'

        else:
            return casinoHelp
    else:
        return None