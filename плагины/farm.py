import os
import time
from plugins import gf

users_dir = os.path.join(r"users/")

def check_own_farm(own_farm):
    if own_farm == 1:
        return '�7�4�7�4�9�1 ���֧�ާ�: Miner\n'
    elif own_farm == 2:
        return '�7�4�7�4�9�1 ���֧�ާ�: Miner S\n'
    elif own_farm == 3:
        return '�7�4�7�4�9�1 ���֧�ާ�: Miner X\n'
    else:
        pass

def farm(sourceText, id):
    get_data = gf.loadjson(users_dir + str(id) + ".json")
    own_farm = int(get_data['own_farm'])
    farm_profit = int(get_data['farm_profit'])
    farm_time = float(get_data['farm_time'])
    bank_cr_balance = get_data['bank_cr_balance']

    farm_withdraw_raznica_time = float(time.time()) - float(farm_time)
    farm_withdraw_hours = int(farm_withdraw_raznica_time) / 3599
    za_hour = int(farm_profit / 24)
    hour_fm_profit = int(za_hour) * int(farm_withdraw_hours)

    statis_bs = ', ���ѧ�ڧ��ڧܧ� ��֧�ާ�:\n\n�9�7 ����ѧ�ڧ��ڧܧ�:\n' + str(check_own_farm(own_farm)) + '�7�4�7�4�9�8 ����ڧҧ�ݧ�: ' + str(farm_profit) + '�2�1/�է֧ߧ�.\n�7�4�7�4�9�0 ���ѧ�ѧҧ��ѧߧ�: '+ str(hour_fm_profit) + '�2�1'
    dop_infa = '\n\n�7�4�9�0 ���ѧ�� ��֧�ާ� ���ڧߧ��ڧ� �ާѧܧ�ڧާѧݧ�ߧ�-�ӧ�٧ާ�اߧߧ�� �է���� �էݧ� ��ӧ�֧� �ާ��ߧ����! ���֧ܧ�ާ֧ߧէ�֧� �ӧѧ� ����ѧߧ�ӧڧ�� ��֧�ާ� �ߧ� �ާ�է֧ݧ� �ӧ���, �էݧ� ���ݧ��֧ߧڧ� �ާѧܧ�ڧާѧݧ�ߧ�ԧ� �����ڧ��.\n\n'

    if sourceText != '':
        if sourceText.split()[0].lower() in ['��֧�ާ�', '��֧�ާ�', '�ާѧۧߧڧߧ�', '�9�1']:
            if len(sourceText.split()) == 1:
                if own_farm >= 1:
                    if farm_withdraw_hours >= 24:
                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                        get_data.update({"bank_cr_balance": '{}'.format(str(int(bank_cr_balance) + int(hour_fm_profit)))})
                        get_data.update({"farm_time": '{}'.format(time.time())})
                        gf.dumpjson(get_data, users_dir + str(id) + ".json")

                        if own_farm == 1:
                            return statis_bs + dop_infa + '\n\n�7�1 ����ާ���:\n�7�4�7�4�7�3 ���֧�ާ� ��ݧ���ڧ��\n�7�4�7�4�9�3 ���֧�ާ� ����էѧ��\n\n�7�3 ���ѧާѧۧߧ֧ߧߧ�� �է֧ߧ�ԧ� �٧ѧ�ڧ�ݧ����� �ѧӧ��ާѧ�ڧ�֧�ܧ�, �֧�ݧ� ����ӧ֧���� ��֧�ާ� �ܧ�ާѧߧէ�� �0�0��֧�ާс0�3.\n�9�0 ���ҧާ֧ߧ��� �٧ѧ�ѧҧ��ѧߧߧ�� �ҧڧ�ܧ�ڧߧ�: ���ѧߧ� ��ҧާ֧�'
                        elif own_farm == 2:
                            return statis_bs + dop_infa + '\n\n�7�1 ����ާ���:\n�7�4�7�4�7�3 ���֧�ާ� ��ݧ���ڧ��\n�7�4�7�4�9�3 ���֧�ާ� ����էѧ��\n\n�7�3 ���ѧާѧۧߧ֧ߧߧ�� �է֧ߧ�ԧ� �٧ѧ�ڧ�ݧ����� �ѧӧ��ާѧ�ڧ�֧�ܧ�, �֧�ݧ� ����ӧ֧���� ��֧�ާ� �ܧ�ާѧߧէ�� �0�0��֧�ާс0�3.\n�9�0 ���ҧާ֧ߧ��� �٧ѧ�ѧҧ��ѧߧߧ�� �ҧڧ�ܧ�ڧߧ�: ���ѧߧ� ��ҧާ֧�'
                        else:
                            return statis_bs + '\n\n�7�1 ����ާ���:\n�7�4�7�4�9�3 ���֧�ާ� ����էѧ��\n\n�7�3 ���ѧާѧۧߧ֧ߧߧ�� �է֧ߧ�ԧ� �٧ѧ�ڧ�ݧ����� �ѧӧ��ާѧ�ڧ�֧�ܧ�, �֧�ݧ� ����ӧ֧���� ��֧�ާ� �ܧ�ާѧߧէ�� �0�0��֧�ާс0�3.\n�9�0 ���ҧާ֧ߧ��� �٧ѧ�ѧҧ��ѧߧߧ�� �ҧڧ�ܧ�ڧߧ�: ���ѧߧ� ��ҧާ֧�'
                    else:
                        if own_farm == 1:
                            return statis_bs + dop_infa + '\n\n�7�1 ����ާ���:\n�7�4�7�4�7�3 ���֧�ާ� ��ݧ���ڧ��\n�7�4�7�4�9�3 ���֧�ާ� ����էѧ��\n\n�7�3 ���ѧާѧۧߧ֧ߧߧ�� �է֧ߧ�ԧ� �٧ѧ�ڧ�ݧ����� �ѧӧ��ާѧ�ڧ�֧�ܧ�, �֧�ݧ� ����ӧ֧���� ��֧�ާ� �ܧ�ާѧߧէ�� �0�0��֧�ާс0�3.'
                        elif own_farm == 2:
                            return statis_bs + dop_infa + '\n\n�7�1 ����ާ���:\n�7�4�7�4�7�3 ���֧�ާ� ��ݧ���ڧ��\n�7�4�7�4�9�3 ���֧�ާ� ����էѧ��\n\n�7�3 ���ѧާѧۧߧ֧ߧߧ�� �է֧ߧ�ԧ� �٧ѧ�ڧ�ݧ����� �ѧӧ��ާѧ�ڧ�֧�ܧ�, �֧�ݧ� ����ӧ֧���� ��֧�ާ� �ܧ�ާѧߧէ�� �0�0��֧�ާс0�3.'
                        else:
                            return statis_bs + '\n\n�7�1 ����ާ���:\n�7�4�7�4�9�3 ���֧�ާ� ����էѧ��\n\n�7�3 ���ѧާѧۧߧ֧ߧߧ�� �է֧ߧ�ԧ� �٧ѧ�ڧ�ݧ����� �ѧӧ��ާѧ�ڧ�֧�ܧ�, �֧�ݧ� ����ӧ֧���� ��֧�ާ� �ܧ�ާѧߧէ�� �0�0��֧�ާс0�3.'
                else:
                    return ', �� �ӧѧ� �֧�� �ߧ֧� ��֧�ާ�! �9�6\n\n �9�0 �����ݧ� ���ܧ��ܧ� ��֧�ާ�, ��ߧ� �ߧѧ�ڧߧѧ֧� �ѧӧ��ާѧ�ڧ�֧�ܧ� ���ѧ٧� ���ڧߧ��ڧ�� �է����!\n\n�7�1 ���ݧ� �����ާ���� ��֧��, �ڧ���ݧ�٧�ۧ��:\n�7�4�7�4�0�6 ���ѧԧѧ٧ڧ� ��֧�ާ�'
            elif len(sourceText.split()) == 2:
                if '����էѧ��' == sourceText.split()[1].lower():
                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                    own_farm = int(get_data['own_farm'])
                    if own_farm >= 1:
                        get_data.update({"farm_time": '{}'.format(0.0)})
                        get_data.update({"own_farm": '{}'.format(0)})
                        get_data.update({"farm_profit": '{}'.format(0)})
                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                        return ', �ӧ� ����֧�ߧ� ����էѧݧ� ��֧�ާ�! �0�2'
                    else:
                        return ', �� �ӧѧ� �֧�� �ߧ֧� ��֧�ާ�! �9�6\n\n �9�0 �����ݧ� ���ܧ��ܧ� ��֧�ާ�, ��ߧ� �ߧѧ�ڧߧѧ֧� �ѧӧ��ާѧ�ڧ�֧�ܧ� ���ѧ٧� ���ڧߧ��ڧ�� �է����!\n\n�7�1 ���ݧ� �����ާ���� ��֧��, �ڧ���ݧ�٧�ۧ��:\n�7�4�7�4�0�6 ���ѧԧѧ٧ڧ� ��֧�ާ�'
                elif '��ݧ���ڧ��' == sourceText.split()[1].lower():
                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                    own_farm = int(get_data['own_farm'])
                    user_balance = int(get_data['balance'])
                    price_own_farm2 = 60000000 - 5000000
                    price_own_farm3 = 500000000 - 60000000
                    if own_farm == 1:
                        if price_own_farm2 <= user_balance:
                            algo_balance = user_balance - price_own_farm2
                            get_data.update({"balance": '{}'.format(algo_balance)})
                            get_data.update({"farm_time": '{}'.format(time.time())})
                            get_data.update({"own_farm": '{}'.format(2)})
                            get_data.update({"farm_profit": '{}'.format(50)})
                            gf.dumpjson(get_data, users_dir + str(id) + ".json")
                            return ', �ӧ� ����֧�ߧ� ��ݧ���ڧݧ� ��֧�ާ�, �է� - �9�1 Miner S! �0�2'
                        else:
                            return ', �� �ӧѧ� �֧�� �ߧ֧� ��֧�ާ�! �9�6\n\n �9�0 �����ݧ� ���ܧ��ܧ� ��֧�ާ�, ��ߧ� �ߧѧ�ڧߧѧ֧� �ѧӧ��ާѧ�ڧ�֧�ܧ� ���ѧ٧� ���ڧߧ��ڧ�� �է����!\n\n�7�1 ���ݧ� �����ާ���� ��֧��, �ڧ���ݧ�٧�ۧ��:\n�7�4�7�4�0�6 ���ѧԧѧ٧ڧ� ��֧�ާ�'
                    elif own_farm == 2:
                        if price_own_farm3 <= user_balance:
                            algo_balance = user_balance - price_own_farm3
                            get_data.update({"balance": '{}'.format(algo_balance)})
                            get_data.update({"farm_time": '{}'.format(time.time())})
                            get_data.update({"own_farm": '{}'.format(3)})
                            get_data.update({"farm_profit": '{}'.format(1000)})
                            gf.dumpjson(get_data, users_dir + str(id) + ".json")
                            return ', �ӧ� ����֧�ߧ� ��ݧ���ڧݧ� ��֧�ާ�, �է� - �9�1 Miner X! �0�2'
                        else:
                            return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6\n�7�3 ���ݧ���֧ߧڧ� ����ڧ�: ' + str(price_own_farm3) + '��'
                    elif own_farm == 3:
                        return ', �ӧѧ�� ��֧�ާ� �ڧާ֧֧� �ާѧܧ�ڧާѧݧ�ߧ�� ��ݧ���֧ߧڧ�! �9�0'
                    else:
                        return ', �� �ӧѧ� �֧�� �ߧ֧� ��֧�ާ�! �9�6\n\n �9�0 �����ݧ� ���ܧ��ܧ� ��֧�ާ�, ��ߧ� �ߧѧ�ڧߧѧ֧� �ѧӧ��ާѧ�ڧ�֧�ܧ� ���ѧ٧� ���ڧߧ��ڧ�� �է����!\n\n�7�1 ���ݧ� �����ާ���� ��֧��, �ڧ���ݧ�٧�ۧ��:\n�7�4�7�4�0�6 ���ѧԧѧ٧ڧ� ��֧�ާ�'
                else:
                    if own_farm >= 1:
                        if farm_withdraw_hours >= 24:
                            get_data = gf.loadjson(users_dir + str(id) + ".json")
                            get_data.update({"bank_cr_balance": '{}'.format(str(int(bank_cr_balance) + int(hour_fm_profit)))})
                            get_data.update({"farm_time": '{}'.format(time.time())})
                            gf.dumpjson(get_data, users_dir + str(id) + ".json")

                            if own_farm == 1:
                                return statis_bs + dop_infa + '\n\n�7�1 ����ާ���:\n�7�4�7�4�7�3 ���֧�ާ� ��ݧ���ڧ��\n�7�4�7�4�9�3 ���֧�ާ� ����էѧ��\n\n�7�3 ���ѧާѧۧߧ֧ߧߧ�� �է֧ߧ�ԧ� �٧ѧ�ڧ�ݧ����� �ѧӧ��ާѧ�ڧ�֧�ܧ�, �֧�ݧ� ����ӧ֧���� ��֧�ާ� �ܧ�ާѧߧէ�� �0�0��֧�ާс0�3.\n�9�0 ���ҧާ֧ߧ��� �٧ѧ�ѧҧ��ѧߧߧ�� �ҧڧ�ܧ�ڧߧ�: ���ѧߧ� ��ҧާ֧�'
                            elif own_farm == 2:
                                return statis_bs + dop_infa + '\n\n�7�1 ����ާ���:\n�7�4�7�4�7�3 ���֧�ާ� ��ݧ���ڧ��\n�7�4�7�4�9�3 ���֧�ާ� ����էѧ��\n\n�7�3 ���ѧާѧۧߧ֧ߧߧ�� �է֧ߧ�ԧ� �٧ѧ�ڧ�ݧ����� �ѧӧ��ާѧ�ڧ�֧�ܧ�, �֧�ݧ� ����ӧ֧���� ��֧�ާ� �ܧ�ާѧߧէ�� �0�0��֧�ާс0�3.\n�9�0 ���ҧާ֧ߧ��� �٧ѧ�ѧҧ��ѧߧߧ�� �ҧڧ�ܧ�ڧߧ�: ���ѧߧ� ��ҧާ֧�'
                            else:
                                return statis_bs + '\n\n�7�1 ����ާ���:\n�7�4�7�4�9�3 ���֧�ާ� ����էѧ��\n\n�7�3 ���ѧާѧۧߧ֧ߧߧ�� �է֧ߧ�ԧ� �٧ѧ�ڧ�ݧ����� �ѧӧ��ާѧ�ڧ�֧�ܧ�, �֧�ݧ� ����ӧ֧���� ��֧�ާ� �ܧ�ާѧߧէ�� �0�0��֧�ާс0�3.\n�9�0 ���ҧާ֧ߧ��� �٧ѧ�ѧҧ��ѧߧߧ�� �ҧڧ�ܧ�ڧߧ�: ���ѧߧ� ��ҧާ֧�'
                        else:
                            if own_farm == 1:
                                return statis_bs + dop_infa + '\n\n�7�1 ����ާ���:\n�7�4�7�4�7�3 ���֧�ާ� ��ݧ���ڧ��\n�7�4�7�4�9�3 ���֧�ާ� ����էѧ��\n\n�7�3 ���ѧާѧۧߧ֧ߧߧ�� �է֧ߧ�ԧ� �٧ѧ�ڧ�ݧ����� �ѧӧ��ާѧ�ڧ�֧�ܧ�, �֧�ݧ� ����ӧ֧���� ��֧�ާ� �ܧ�ާѧߧէ�� �0�0��֧�ާс0�3.'
                            elif own_farm == 2:
                                return statis_bs + dop_infa + '\n\n�7�1 ����ާ���:\n�7�4�7�4�7�3 ���֧�ާ� ��ݧ���ڧ��\n�7�4�7�4�9�3 ���֧�ާ� ����էѧ��\n\n�7�3 ���ѧާѧۧߧ֧ߧߧ�� �է֧ߧ�ԧ� �٧ѧ�ڧ�ݧ����� �ѧӧ��ާѧ�ڧ�֧�ܧ�, �֧�ݧ� ����ӧ֧���� ��֧�ާ� �ܧ�ާѧߧէ�� �0�0��֧�ާс0�3.'
                            else:
                                return statis_bs + '\n\n�7�1 ����ާ���:\n�7�4�7�4�9�3 ���֧�ާ� ����էѧ��\n\n�7�3 ���ѧާѧۧߧ֧ߧߧ�� �է֧ߧ�ԧ� �٧ѧ�ڧ�ݧ����� �ѧӧ��ާѧ�ڧ�֧�ܧ�, �֧�ݧ� ����ӧ֧���� ��֧�ާ� �ܧ�ާѧߧէ�� �0�0��֧�ާс0�3.'
                    else:
                        return ', �� �ӧѧ� �֧�� �ߧ֧� ��֧�ާ�! �9�6\n\n �9�0 �����ݧ� ���ܧ��ܧ� ��֧�ާ�, ��ߧ� �ߧѧ�ڧߧѧ֧� �ѧӧ��ާѧ�ڧ�֧�ܧ� ���ѧ٧� ���ڧߧ��ڧ�� �է����!\n\n�7�1 ���ݧ� �����ާ���� ��֧��, �ڧ���ݧ�٧�ۧ��:\n�7�4�7�4�0�6 ���ѧԧѧ٧ڧ� ��֧�ާ�'
            else:
                if own_farm >= 1:
                    if farm_withdraw_hours >= 24:
                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                        get_data.update({"bank_cr_balance": '{}'.format(str(int(bank_cr_balance) + int(hour_fm_profit)))})
                        get_data.update({"farm_time": '{}'.format(time.time())})
                        gf.dumpjson(get_data, users_dir + str(id) + ".json")

                        if own_farm == 1:
                            return statis_bs + dop_infa + '\n\n�7�1 ����ާ���:\n�7�4�7�4�7�3 ���֧�ާ� ��ݧ���ڧ��\n�7�4�7�4�9�3 ���֧�ާ� ����էѧ��\n\n�7�3 ���ѧާѧۧߧ֧ߧߧ�� �է֧ߧ�ԧ� �٧ѧ�ڧ�ݧ����� �ѧӧ��ާѧ�ڧ�֧�ܧ�, �֧�ݧ� ����ӧ֧���� ��֧�ާ� �ܧ�ާѧߧէ�� �0�0��֧�ާс0�3.\n�9�0 ���ҧާ֧ߧ��� �٧ѧ�ѧҧ��ѧߧߧ�� �ҧڧ�ܧ�ڧߧ�: ���ѧߧ� ��ҧާ֧�'
                        elif own_farm == 2:
                            return statis_bs + dop_infa + '\n\n�7�1 ����ާ���:\n�7�4�7�4�7�3 ���֧�ާ� ��ݧ���ڧ��\n�7�4�7�4�9�3 ���֧�ާ� ����էѧ��\n\n�7�3 ���ѧާѧۧߧ֧ߧߧ�� �է֧ߧ�ԧ� �٧ѧ�ڧ�ݧ����� �ѧӧ��ާѧ�ڧ�֧�ܧ�, �֧�ݧ� ����ӧ֧���� ��֧�ާ� �ܧ�ާѧߧէ�� �0�0��֧�ާс0�3.\n�9�0 ���ҧާ֧ߧ��� �٧ѧ�ѧҧ��ѧߧߧ�� �ҧڧ�ܧ�ڧߧ�: ���ѧߧ� ��ҧާ֧�'
                        else:
                            return statis_bs + '\n\n�7�1 ����ާ���:\n�7�4�7�4�9�3 ���֧�ާ� ����էѧ��\n\n�7�3 ���ѧާѧۧߧ֧ߧߧ�� �է֧ߧ�ԧ� �٧ѧ�ڧ�ݧ����� �ѧӧ��ާѧ�ڧ�֧�ܧ�, �֧�ݧ� ����ӧ֧���� ��֧�ާ� �ܧ�ާѧߧէ�� �0�0��֧�ާс0�3.\n�9�0 ���ҧާ֧ߧ��� �٧ѧ�ѧҧ��ѧߧߧ�� �ҧڧ�ܧ�ڧߧ�: ���ѧߧ� ��ҧާ֧�'
                    else:
                        if own_farm == 1:
                            return statis_bs + dop_infa + '\n\n�7�1 ����ާ���:\n�7�4�7�4�7�3 ���֧�ާ� ��ݧ���ڧ��\n�7�4�7�4�9�3 ���֧�ާ� ����էѧ��\n\n�7�3 ���ѧާѧۧߧ֧ߧߧ�� �է֧ߧ�ԧ� �٧ѧ�ڧ�ݧ����� �ѧӧ��ާѧ�ڧ�֧�ܧ�, �֧�ݧ� ����ӧ֧���� ��֧�ާ� �ܧ�ާѧߧէ�� �0�0��֧�ާс0�3.'
                        elif own_farm == 2:
                            return statis_bs + dop_infa + '\n\n�7�1 ����ާ���:\n�7�4�7�4�7�3 ���֧�ާ� ��ݧ���ڧ��\n�7�4�7�4�9�3 ���֧�ާ� ����էѧ��\n\n�7�3 ���ѧާѧۧߧ֧ߧߧ�� �է֧ߧ�ԧ� �٧ѧ�ڧ�ݧ����� �ѧӧ��ާѧ�ڧ�֧�ܧ�, �֧�ݧ� ����ӧ֧���� ��֧�ާ� �ܧ�ާѧߧէ�� �0�0��֧�ާс0�3.'
                        else:
                            return statis_bs + '\n\n�7�1 ����ާ���:\n�7�4�7�4�9�3 ���֧�ާ� ����էѧ��\n\n�7�3 ���ѧާѧۧߧ֧ߧߧ�� �է֧ߧ�ԧ� �٧ѧ�ڧ�ݧ����� �ѧӧ��ާѧ�ڧ�֧�ܧ�, �֧�ݧ� ����ӧ֧���� ��֧�ާ� �ܧ�ާѧߧէ�� �0�0��֧�ާс0�3.'
                else:
                    return ', �� �ӧѧ� �֧�� �ߧ֧� ��֧�ާ�! �9�6\n\n �9�0 �����ݧ� ���ܧ��ܧ� ��֧�ާ�, ��ߧ� �ߧѧ�ڧߧѧ֧� �ѧӧ��ާѧ�ڧ�֧�ܧ� ���ѧ٧� ���ڧߧ��ڧ�� �է����!\n\n�7�1 ���ݧ� �����ާ���� ��֧��, �ڧ���ݧ�٧�ۧ��:\n�7�4�7�4�0�6 ���ѧԧѧ٧ڧ� ��֧�ާ�'
        else:
            return None
    pass