import os
import time
from plugins import gf

users_dir = os.path.join(r"users/")

def shop(sourceText, id):
    get_data = gf.loadjson(users_dir + str(id) + ".json")
    user_balance = int(get_data['balance'])

    shopHelp = ', ���ާ��� ��� �ާѧԧѧ٧ڧߧ�:\n\n�7�4�0�6 ����ܧ��ѧۧ�� ��ѧ٧ݧڧ�ߧ�� �ڧާ��֧��ӧ� �� ��էڧ� �ܧݧڧ�! �����ݧ� ���ܧ��ܧ� �է�ާ�, �ӧ� ��ާ�ا֧�� ���֧�ҧ�֧��� ���ѧߧ����� �� ��֧�ާ� �էݧ� �ާѧۧߧڧߧԧ� �ҧڧ�ܧ�ڧߧ��.\n\n�9�8 ����ߧ�ӧߧ��:\n�7�4�7�4�9�2 ����ާ�\n�7�4�7�4�0�7 ���ѧ�ڧߧ�\n�7�4�7�4�7�6 ���ѧާ�ݧק��\n�7�4�7�4�0�5 ���֧���ݧק��\n�7�4�7�4�0�5 ������\n\n�9�5 �����ѧݧ�ߧ��:\n�7�4�7�4�9�5 ����ާ����֧��\n�7�4�7�4�9�5 ���֧ݧ֧��ߧ�\n�7�4�7�4�9�1 ���֧�ާ�\n\n�7�1 ����ާ���:\n�7�4�7�4�9�4 ���ѧԧѧ٧ڧ� [�ܧѧ�֧ԧ��ڧ�] - ���ӧѧ��.\n�7�4�7�4�0�6 ���ѧԧѧ٧ڧ� [�ܧѧ�֧ԧ��ڧ�] [�ߧ�ާ֧�] - �ܧ��ڧ�� ���ӧѧ�.'

    if sourceText != '':
        if '�ާѧԧѧ٧ڧ�' == sourceText.split()[0].lower():
            if len(sourceText.split()) == 2:
                if sourceText.split()[1].lower() in ['�է��', '�է�ާ�']:
                    return ', ���ڧ��� �է�����ߧ�� �է�ާ��:\n\n�7�4�9�0 �����ݧ� ���ܧ��ܧ� �է�ާ�, �ӧ� ��ާ�ا֧�� �ܧ��ڧ�� ���ѧߧ����� �� ��֧�ާ�!\n\n�7�4�7�4�9�2 1. ������ҧܧ� �� 25.000��\n�7�4�7�4�9�2 2. ����էӧѧ� �� 65.000��\n�7�4�7�4�9�2 3. ���ѧ�ѧ� �� 225.000��\n�7�4�7�4�9�2 4. ���ѧ�ѧ� �� 595.000��\n�7�4�7�4�9�2 5. ���֧��ѧ� ��ڧاڧߧ� �� 655.000��\n�7�4�7�4�9�2 6. ���֧�֧ӧ�ߧߧ�� �է�ާڧ� �� 1.525.000��\n�7�4�7�4�9�2 7. ���ڧ��ڧ�ߧ�� �է�� �� 8.525.000��\n�7�4�7�4�9�2 8. ������֧է� �� 35.650.000��\n�7�4�7�4�9�2 9. ����� �ߧ� ����ާѧӧ�է� �� 68.250.000��\n�7�4�7�4�9�2 10. ���ڧݧݧ� �ߧ� ����ާѧӧ�է� �� 93.500.000��\n�7�4�7�4�9�2 11. ���ڧ�ߧ�� ������� �� 999.999.999��\n\n�7�1 ���ݧ� ���ܧ��ܧ� �է�ާ�, �ڧ���ݧ�٧�ۧ��:\n�7�4�7�4�0�6 ���ѧԧѧ٧ڧ� �է�� [�ߧ�ާ֧�]'
                elif sourceText.split()[1].lower() in ['�ާѧ�ڧߧ�', '�ާѧ�ڧߧ�']:
                    return ', ���ڧ��� �է�����ߧ�� �ާѧ�ڧ�:\n\n�7�4�9�0 ����ܧ��ѧۧ�� ���ѧߧ����� �� ��էڧ� �ܧݧڧ�!\n\n�7�4�7�4�0�7 1. ���֧ݧ��ڧ�֧� �� 125.000��\n�7�4�7�4�0�7 2. ���ڧ���ܧ��֧� �� 255.000��\n�7�4�7�4�9�3 3. Ducati Scrambler �� 525.000��\n�7�4�7�4�9�3 4. Honda CTX1300 �� 1.275.000��\n�7�4�7�4�0�7 5. Ferrari California front �� 1.650.000��\n�7�4�7�4�0�7 6. Porsche 911 �� 2.000.000��\n�7�4�7�4�0�7 7. Nissan GT-R �� 4.350.000��\n�7�4�7�4�0�7 8. BMW X6 �� 15.650.000��\n�7�4�7�4�0�7 9. Jaguar F-Type �� 25.735.000��\n�7�4�7�4�0�7 10. Lamborghini Hurac��n �� 30.800.000��\n�7�4�7�4�0�7 11. Lamborghini Gallardo �� 37.580.000��\n�7�4�7�4�0�7 12. Ferrari F80 Concept �� 57.999.999��\n�7�4�7�4�0�7 13. Lamborghini Sesto �� 108.555.000��\n�7�4�7�4�0�7 14. Various Ford-based trucks �� 999.999.999��\n�7�4�7�4�0�7 15. Tesla Cybertruck �� 1.500.000.000��\n\n�7�1 ���ݧ� ���ܧ��ܧ� ���ѧߧ������, �ڧ���ݧ�٧�ۧ��:\n�7�4�7�4�0�6 ���ѧԧѧ٧ڧ� �ާѧ�ڧߧ� [�ߧ�ާ֧�]'
                elif sourceText.split()[1].lower() in ['�����', '�����']:
                    return ', ���ڧ��� �է�����ߧ�� ����:\n\n�7�4�7�4�0�5 1. RHIB �� 575.000��\n�7�4�7�4�0�5 2. Kawasaki �� 1.225.000��\n�7�4�7�4�0�5 3. Riva Aquarama �� 2.500.000��\n�7�4�7�4�0�5 4. Various �� 3.650.000��\n�7�4�7�4�0�5 5. ��rin���ss 60 �� 8.355.000��\n�7�4�7�4�0�5 6. ��zimut 70 �� 12.850.000��\n�7�4�7�4�0�5 7. D��min��t��r 40M �� 23.125.000��\n�7�4�7�4�0�5 8. M���n��n 124 �� 34.666.000��\n�7�4�7�4�0�5 9. Wid��r 150 �� 66.225.000��\n�7�4�7�4�0�5 10. Palmer J��hns��n 42M Su���rS���rt �� 96.000.000��\n�7�4�7�4�0�5 11. Wid��r 165 �� 126.650.000��\n�7�4�7�4�0�5 12. ����li��s�� �� 527.777.777��\n�7�4�7�4�0�5 13. Dub��i �� 999.999.999��\n�7�4�7�4�0�5 14. Str�֧�ts ��f M��n�ѧ�� �� 1.255.000.000��\n\n�7�1 ���ݧ� ���ܧ��ܧ� ���ѧߧ������, �ڧ���ݧ�٧�ۧ��:\n�7�4�7�4�0�6 ���ѧԧѧ٧ڧ� ����� [�ߧ�ާ֧�]'
                elif sourceText.split()[1].lower() in ['��ѧާ�ݧק�', '��ѧާ�ݧ֧�', '��ѧާ�ݧק��', '��ѧާ�ݧ֧��']:
                    return ', ���ڧ��� �է�����ߧ�� ��ѧާ�ݧק���:\n\n�7�4�9�0 ����ܧ��ѧۧ�� ���ѧߧ����� �� ��էڧ� �ܧݧڧ�!\n\n�7�4�7�4�7�6 1. de Havilland Canada DHC-2 �� 500.000��\n�7�4�7�4�7�6 2. Piper PA-46 �� 3.995.000��\n�7�4�7�4�7�6 3. Cessna 310 �� 6.350.000��\n�7�4�7�4�7�6 4. Learjet 55 �� 15.500.000��\n�7�4�7�4�7�6 5. Bombardier Global Express �� 17.800.000��\n�7�4�7�4�7�6 6. Cessna Citation X �� 22.250.000��\n�7�4�7�4�7�6 7. C-130 �� 43.000.000��\n�7�4�7�4�7�6 8. VOLATOL �� 65.505.000��\n�7�4�7�4�7�6 9. RM-10 BOMBUSHKA �� 75.985.000��\n�7�4�7�4�7�6 10. AVENGER �� HYV �� 86.495.000��\n�7�4�7�4�7�6 11. F-16 Fighting Falcon �� 109.999.999��\n�7�4�7�4�7�6 12. RM-10 BOMBUSHKA �� 313.000.000��\n�7�4�7�4�7�6 13. TULA �� MAMMOTH �� 617.555.000��\n�7�4�7�4�7�6 14. V-65 MOLOTOK �� 850.000.000��\n�7�4�7�4�7�6 15. MOGUL �� MAMMOTH �� 2.000.000.000��\n\n�7�1 ���ݧ� ���ܧ��ܧ� ���ѧߧ������, �ڧ���ݧ�٧�ۧ��:\n�7�4�7�4�0�6 ���ѧԧѧ٧ڧ� ��ѧާ�ݧק� [�ߧ�ާ֧�]'
                elif sourceText.split()[1].lower() in ['�ӧ֧���ݧק�', '�ӧ֧���ݧ֧�', '�ӧ֧���ݧק��', '�ӧ֧���ݧ֧��']:
                    return ', ���ڧ��� �է�����ߧ�� �ӧ֧���ݧק���:\n\n�7�4�9�0 ����ܧ��ѧۧ�� ���ѧߧ����� �� ��էڧ� �ܧݧڧ�!\n\n�7�4�7�4�0�5 1. Eurocopter EC130/135/14 �� 1.300.000��\n�7�4�7�4�0�5 2. Boeing MH-6 �� 1.750.000��\n�7�4�7�4�0�5 3. Sikorsky UH-60 �� 2.225.000��\n�7�4�7�4�0�5 4. HAVOK �� NAGASAKI �� 3.500.000��\n�7�4�7�4�0�5 5. Eurocopter EC145 �� 8.850.000��\n�7�4�7�4�0�5 6. Airbus H160 �� 25.555.555��\n�7�4�7�4�0�5 7. Mil Mi-24 �� 58.000.000��\n�7�4�7�4�0�5 8. POLICE MAVERICK �� 215.000.000��\n�7�4�7�4�0�5 9. MAVERICK �� 525.000.000��\n\n�7�1 ���ݧ� ���ܧ��ܧ� ���ѧߧ������, �ڧ���ݧ�٧�ۧ��:\n�7�4�7�4�0�6 ���ѧԧѧ٧ڧ� �ӧ֧���ݧק� [�ߧ�ާ֧�]'
                elif sourceText.split()[1].lower() in ['��֧�ާ�', '��֧�ާ�']:
                    return ', ���ڧ��� �է�����ߧ�� ��֧��:\n\n�7�4�9�0 �����ݧ� ���ܧ��ܧ� ��֧�ާ�, �ӧ� ��ާ�ا֧�� �ާѧۧߧڧ�� �ҧڧ�ܧ�ڧߧ�!\n\n�7�4�7�4�9�1 1. Miner (5�2�1/�է֧ߧ�) �� 500.000��\n�7�4�7�4�9�1 2. Miner S (50�2�1/�է֧ߧ�) �� 5.000.000��\n�7�4�7�4�9�1 3. Miner X (1 000�2�1/�է֧ߧ�) �� 500.000.000��\n\n�7�1 ���ݧ� ���ܧ��ܧ� ��֧�ާ�, �ڧ���ݧ�٧�ۧ��:\n�7�4�7�4�0�6 ���ѧԧѧ٧ڧ� ��֧�ާ� [�ߧ�ާ֧�]'
                elif sourceText.split()[1].lower() in ['�ܧ�ާ�', '�ܧ�ާ����֧�', '�ߧ���', '�ߧ���ҧ��', '�ܧ�ާ��', '�ܧ�ާ����֧��', '�ߧ����', '�ߧ���ҧ�ܧ�']:
                    return ', ���ڧ��� �է�����ߧ�� �ܧ�ާ����֧���:\n\n�7�4�9�0 �����ݧ� ���ܧ��ܧ� �ܧ�ާ����֧��, �ӧ� ��ާ�ا֧�� ����ڧ٧ӧ�էڧ�� �ӧ٧ݧ�ާ�!\n\n�7�4�7�4�9�5 1. Book �� 35.000.000��\n�7�4�7�4�9�5 2. Book Air �� 45.000.000��\n�7�4�7�4�9�5 3. Book Pro �� 150.000.000��\n\n�7�1 ���ݧ� ���ܧ��ܧ� �ܧ�ާ����֧��, �ڧ���ݧ�٧�ۧ��:\n�7�4�7�4�0�6 ���ѧԧѧ٧ڧ� �ܧ�ާ����֧� [�ߧ�ާ֧�]'
                elif sourceText.split()[1].lower() in ['��֧ݧ֧���', '��ާѧ�����', '��֧ݧ֧��ߧ�', '��ާѧ����ߧ�']:
                    return ', ���ڧ��� �է�����ߧ�� ��֧ݧ֧��ߧ��:\n\n�7�4�9�0 ����ܧ��ѧۧ�� ��֧ݧ֧��ߧ� �� ��էڧ� �ܧݧڧ�!\n\n�7�4�7�4�9�5 1. iPhone �� 25.800.000��\n�7�4�7�4�9�5 2. iPhone Pro �� 30.000.000��\n�7�4�7�4�9�5 3. iPhone Pro Max �� 35.250.000��\n\n�7�1 ���ݧ� ���ܧ��ܧ� ��ާѧ����ߧ�, �ڧ���ݧ�٧�ۧ��:\n�7�4�7�4�0�6 ���ѧԧѧ٧ڧ� ��ާѧ����� [�ߧ�ާ֧�]'
            elif len(sourceText.split()) == 3:
                id_own = str(sourceText.split()[2].lower())
                if sourceText.split()[1].lower() in ['�է��', '�է�ާ�']:
                    own_housing = int(get_data['own_housing'])
                    price_own_housing1 = 25000
                    price_own_housing2 = 65000
                    price_own_housing3 = 225000
                    price_own_housing4 = 595000
                    price_own_housing5 = 655000
                    price_own_housing6 = 1525000
                    price_own_housing7 = 8525000
                    price_own_housing8 = 35650000
                    price_own_housing9 = 68250000
                    price_own_housing10 = 93500000
                    price_own_housing11 = 999999999
                    if id_own.isdigit():
                        if int(id_own) == 1:
                            if own_housing == 0:
                                if price_own_housing1 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing1
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�2 ������ҧܧ� �٧� ' + str(price_own_housing1) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                else:
                                    return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                            else:
                                return ', �� �ӧѧ� ��ا� �֧��� �է��! �9�5'
                        elif int(id_own) == 2:
                            if own_housing == 0:
                                if price_own_housing2 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing2
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�2 ����էӧѧ� �٧� ' + str(price_own_housing2) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                else:
                                    return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                            else:
                                return ', �� �ӧѧ� ��ا� �֧��� �է��! �9�5'
                        elif int(id_own) == 3:
                            if own_housing == 0:
                                if price_own_housing3 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing3
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�2 ���ѧ�ѧ� �٧� ' + str(price_own_housing3) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                else:
                                    return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                            else:
                                return ', �� �ӧѧ� ��ا� �֧��� �է��! �9�5'
                        elif int(id_own) == 4:
                            if own_housing == 0:
                                if price_own_housing4 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing4
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�2 ���ѧ�ѧ� �٧� ' + str(price_own_housing4) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                else:
                                    return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                            else:
                                return ', �� �ӧѧ� ��ا� �֧��� �է��! �9�5'
                        elif int(id_own) == 5:
                            if own_housing == 0:
                                if price_own_housing5 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing5
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�2 ���֧���� ��ڧاڧߧ� �٧� ' + str(price_own_housing5) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                else:
                                    return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                            else:
                                return ', �� �ӧѧ� ��ا� �֧��� �է��! �9�5'
                        elif int(id_own) == 6:
                            if own_housing == 0:
                                if price_own_housing6 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing6
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�2 ���֧�֧ӧ�ߧߧ�� �է�ާڧ� �٧� ' + str(price_own_housing6) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                else:
                                    return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                            else:
                                return ', �� �ӧѧ� ��ا� �֧��� �է��! �9�5'
                        elif int(id_own) == 7:
                            if own_housing == 0:
                                if price_own_housing7 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing7
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�2 ���ڧ��ڧ�ߧ�� �է�� �٧� ' + str(price_own_housing7) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                else:
                                    return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                            else:
                                return ', �� �ӧѧ� ��ا� �֧��� �է��! �9�5'
                        elif int(id_own) == 8:
                            if own_housing == 0:
                                if price_own_housing8 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing8
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�2 ������֧է� �٧� ' + str(price_own_housing8) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                else:
                                    return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                            else:
                                return ', �� �ӧѧ� ��ا� �֧��� �է��! �9�5'
                        elif int(id_own) == 9:
                            if own_housing == 0:
                                if price_own_housing9 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing9
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�2 ����� �ߧ� ����ާѧӧ�է� �٧� ' + str(price_own_housing9) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                else:
                                    return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                            else:
                                return ', �� �ӧѧ� ��ا� �֧��� �է��! �9�5'
                        elif int(id_own) == 10:
                            if own_housing == 0:
                                if price_own_housing10 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing10
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�2 ���ڧݧݧ� �ߧ� ����ާѧӧ�է� �٧� ' + str(price_own_housing10) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                else:
                                    return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                            else:
                                return ', �� �ӧѧ� ��ا� �֧��� �է��! �9�5'
                        elif int(id_own) == 11:
                            if own_housing == 0:
                                if price_own_housing11 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing11
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�2 ���ڧ�ߧ�� ������� �٧� ' + str(price_own_housing11) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                else:
                                    return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                            else:
                                return ', �� �ӧѧ� ��ا� �֧��� �է��! �9�5'
                        else:
                            return ', �է�ާ� �� ��ѧܧڧ� ID �ߧ� ����֧��ӧ�֧�! �9�6'
                    else:
                        return ', ��ڧާӧ�ݧ� �� �ҧ�ܧӧ� �٧ѧ��֧�֧ߧ�! �9�6'

                elif sourceText.split()[1].lower() in ['�ާѧ�ڧߧ�', '�ާѧ�ڧߧ�']:
                    own_car = int(get_data['own_car'])
                    own_housing = int(get_data['own_housing'])
                    if own_housing >= 1 or own_housing != 30:
                        price_own_car1 = 125000
                        price_own_car2 = 255000
                        price_own_car3 = 525000
                        price_own_car4 = 1275000
                        price_own_car5 = 1650000
                        price_own_car6 = 2000000
                        price_own_car7 = 4350000
                        price_own_car8 = 15650000
                        price_own_car9 = 25735000
                        price_own_car10 = 30800000
                        price_own_car11 = 37580000
                        price_own_car12 = 57999999
                        price_own_car13 = 108555000
                        price_own_car14 = 999999999
                        price_own_car15 = 1500000000

                        if id_own.isdigit():
                            if int(id_own) == 1:
                                if own_car == 0:
                                    if price_own_car1 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car1
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�7 ���֧ݧ��ڧ�֧� �٧� ' + str(price_own_car1) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ާѧ�ڧߧ�! �9�5'
                            elif int(id_own) == 2:
                                if own_car == 0:
                                    if price_own_car2 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car2
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�7 ���ڧ���ܧ��֧� �٧� ' + str(price_own_car2) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ާѧ�ڧߧ�! �9�5'

                            elif int(id_own) == 3:
                                if own_car == 0:
                                    if price_own_car3 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car3
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�3 Ducati Scrambler �٧� ' + str(price_own_car3) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ާѧ�ڧߧ�! �9�5'
                            elif int(id_own) == 4:
                                if own_car == 0:
                                    if price_own_car4 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car4
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�3 Honda CTX1300 �٧� ' + str(price_own_car4) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ާѧ�ڧߧ�! �9�5'

                            elif int(id_own) == 5:
                                if own_car == 0:
                                    if price_own_car5 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car5
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�7 Ferrari California front �٧� ' + str(price_own_car5) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ާѧ�ڧߧ�! �9�5'
                            elif int(id_own) == 6:
                                if own_car == 0:
                                    if price_own_car6 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car6
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�7 Porsche 911 �٧� ' + str(price_own_car6) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ާѧ�ڧߧ�! �9�5'
                            elif int(id_own) == 7:
                                if own_car == 0:
                                    if price_own_car7 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car7
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�7 Nissan GT-R �٧� ' + str(price_own_car7) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ާѧ�ڧߧ�! �9�5'
                            elif int(id_own) == 8:
                                if own_car == 0:
                                    if price_own_car8 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car8
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�7 BMW X6 �٧� ' + str(price_own_car8) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ާѧ�ڧߧ�! �9�5'
                            elif int(id_own) == 9:
                                if own_car == 0:
                                    if price_own_car9 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car9
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�7 Jaguar F-Type �٧� ' + str(price_own_car9) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ާѧ�ڧߧ�! �9�5'
                            elif int(id_own) == 10:
                                if own_car == 0:
                                    if price_own_car10 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car10
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�7 Lamborghini Hurac��n �٧� ' + str(price_own_car10) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ާѧ�ڧߧ�! �9�5'
                            elif int(id_own) == 11:
                                if own_car == 0:
                                    if price_own_car11 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car11
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�7 Lamborghini Gallardo �٧� ' + str(price_own_car11) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ާѧ�ڧߧ�! �9�5'
                            elif int(id_own) == 12:
                                if own_car == 0:
                                    if price_own_car12 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car12
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�7 Ferrari F80 Concept �٧� ' + str(price_own_car12) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ާѧ�ڧߧ�! �9�5'
                            elif int(id_own) == 13:
                                if own_car == 0:
                                    if price_own_car13 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car13
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�7 Lamborghini Sesto �٧� ' + str(price_own_car13) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ާѧ�ڧߧ�! �9�5'
                            elif int(id_own) == 14:
                                if own_car == 0:
                                    if price_own_car14 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car14
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�7 Various Ford-based trucks �٧� ' + str(price_own_car14) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ާѧ�ڧߧ�! �9�5'
                            elif int(id_own) == 15:
                                if own_car == 0:
                                    if price_own_car15 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car15
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�7 Tesla Cybertruck �٧� ' + str(price_own_car15) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ާѧ�ڧߧ�! �9�5'
                            else:
                                return ', �ާѧ�ڧߧ� �� ��ѧܧڧ� ID �ߧ� ����֧��ӧ�֧�! �9�6'
                        else:
                            return ', ��ڧާӧ�ݧ� �� �ҧ�ܧӧ� �٧ѧ��֧�֧ߧ�! �9�6'
                    else:
                        return ', �էݧ� ���ܧ��ܧ� ���ѧߧ������ �ߧ֧�ҧ��էڧާ� �է��! �9�5'
                elif sourceText.split()[1].lower() in ['�����', '�����']:
                    own_housing = int(get_data['own_housing'])
                    if own_housing >= 1 or own_housing != 30:
                        own_yacht = int(get_data['own_yacht'])
                        price_own_yacht1 = 575000
                        price_own_yacht2 = 1225000
                        price_own_yacht3 = 2500000
                        price_own_yacht4 = 3650000
                        price_own_yacht5 = 8355000
                        price_own_yacht6 = 12850000
                        price_own_yacht7 = 23125000
                        price_own_yacht8 = 34666000
                        price_own_yacht9 = 66225000
                        price_own_yacht10 = 96000000
                        price_own_yacht11 = 126650000
                        price_own_yacht12 = 527777777
                        price_own_yacht13 = 999999999
                        price_own_yacht14 = 1255000000

                        if id_own.isdigit():
                            if int(id_own) == 1:
                                if own_yacht == 0:
                                    if price_own_yacht1 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht1
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�5 RHIB �٧� ' + str(price_own_yacht1) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �����! �9�5'
                            elif int(id_own) == 2:
                                if own_yacht == 0:
                                    if price_own_yacht2 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht2
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�5 Kawasaki �٧� ' + str(price_own_yacht2) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �����! �9�5'

                            elif int(id_own) == 3:
                                if own_yacht == 0:
                                    if price_own_yacht3 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht3
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�5 Riva Aquarama �٧� ' + str(price_own_yacht3) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �����! �9�5'
                            elif int(id_own) == 4:
                                if own_yacht == 0:
                                    if price_own_yacht4 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht4
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�5 Various �٧� ' + str(price_own_yacht4) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �����! �9�5'

                            elif int(id_own) == 5:
                                if own_yacht == 0:
                                    if price_own_yacht5 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht5
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�5 ��rin���ss 60 �٧� ' + str(price_own_yacht5) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �����! �9�5'
                            elif int(id_own) == 6:
                                if own_yacht == 0:
                                    if price_own_yacht6 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht6
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�5 ��zimut 70 �٧� ' + str(price_own_yacht6) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �����! �9�5'
                            elif int(id_own) == 7:
                                if own_yacht == 0:
                                    if price_own_yacht7 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht7
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�5 D��min��t��r 40M �٧� ' + str(price_own_yacht7) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �����! �9�5'
                            elif int(id_own) == 8:
                                if own_yacht == 0:
                                    if price_own_yacht8 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht8
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�5 M���n��n 124 �٧� ' + str(price_own_yacht8) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �����! �9�5'
                            elif int(id_own) == 9:
                                if own_yacht == 0:
                                    if price_own_yacht9 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht9
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�5 Wid��r 150 �٧� ' + str(price_own_yacht9) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �����! �9�5'
                            elif int(id_own) == 10:
                                if own_yacht == 0:
                                    if price_own_yacht10 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht10
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�5 Palmer J��hns��n 42M Su���rS���rt �٧� ' + str(
                                            price_own_yacht10) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �����! �9�5'
                            elif int(id_own) == 11:
                                if own_yacht == 0:
                                    if price_own_yacht11 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht11
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�5 Wid��r 165 �٧� ' + str(price_own_yacht11) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �����! �9�5'
                            elif int(id_own) == 12:
                                if own_yacht == 0:
                                    if price_own_yacht12 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht12
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�5 ����li��s�� �٧� ' + str(price_own_yacht12) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �����! �9�5'
                            elif int(id_own) == 13:
                                if own_yacht == 0:
                                    if price_own_yacht13 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht13
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�5 Dub��i �٧� ' + str(price_own_yacht13) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �����! �9�5'
                            elif int(id_own) == 14:
                                if own_yacht == 0:
                                    if price_own_yacht14 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht14
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�5 Str�֧�ts ��f M��n�ѧ�� �٧� ' + str(price_own_yacht14) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �����! �9�5'
                            else:
                                return ', ����� �� ��ѧܧڧ� ID �ߧ� ����֧��ӧ�֧�! �9�6'
                        else:
                            return ', ��ڧާӧ�ݧ� �� �ҧ�ܧӧ� �٧ѧ��֧�֧ߧ�! �9�6'
                    else:
                        return ', �էݧ� ���ܧ��ܧ� ���ѧߧ������ �ߧ֧�ҧ��էڧ� �է��! �9�5'
                elif sourceText.split()[1].lower() in ['��ѧާ�ݧק�', '��ѧާ�ݧ֧�', '��ѧާ�ݧק��', '��ѧާ�ݧ֧��']:
                    own_housing = int(get_data['own_housing'])
                    if own_housing >= 1 or own_housing != 30:
                        own_air = int(get_data['own_air'])
                        price_own_air1 = 500000
                        price_own_air2 = 3995000
                        price_own_air3 = 6350000
                        price_own_air4 = 15500000
                        price_own_air5 = 17800000
                        price_own_air6 = 22250000
                        price_own_air7 = 43000000
                        price_own_air8 = 65505000
                        price_own_air9 = 75985000
                        price_own_air10 = 86495000
                        price_own_air11 = 109999999
                        price_own_air12 = 313000000
                        price_own_air13 = 617555000
                        price_own_air14 = 850000000
                        price_own_air15 = 2000000000

                        if id_own.isdigit():
                            if int(id_own) == 1:
                                if own_air == 0:
                                    if price_own_air1 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air1
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �7�6 de Havilland Canada DHC-2 �٧� ' + str(price_own_air1) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� ��ѧާ�ݧק�! �9�5'
                            elif int(id_own) == 2:
                                if own_air == 0:
                                    if price_own_air2 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air2
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �7�6 Piper PA-46 �٧� ' + str(price_own_air2) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� ��ѧާ�ݧק�! �9�5'

                            elif int(id_own) == 3:
                                if own_air == 0:
                                    if price_own_air3 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air3
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �7�6 Cessna 310 �٧� ' + str(price_own_air3) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� ��ѧާ�ݧק�! �9�5'
                            elif int(id_own) == 4:
                                if own_air == 0:
                                    if price_own_air4 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air4
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �7�6 Learjet 55 �٧� ' + str(price_own_air4) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� ��ѧާ�ݧק�! �9�5'

                            elif int(id_own) == 5:
                                if own_air == 0:
                                    if price_own_air5 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air5
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �7�6 Bombardier Global Express �٧� ' + str(price_own_air5) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� ��ѧާ�ݧק�! �9�5'
                            elif int(id_own) == 6:
                                if own_air == 0:
                                    if price_own_air6 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air6
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �7�6 Cessna Citation X �٧� ' + str(price_own_air6) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� ��ѧާ�ݧק�! �9�5'
                            elif int(id_own) == 7:
                                if own_air == 0:
                                    if price_own_air7 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air7
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �7�6 C-130 �٧� ' + str(price_own_air7) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� ��ѧާ�ݧק�! �9�5'
                            elif int(id_own) == 8:
                                if own_air == 0:
                                    if price_own_air8 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air8
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �7�6 VOLATOL �٧� ' + str(price_own_air8) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� ��ѧާ�ݧק�! �9�5'
                            elif int(id_own) == 9:
                                if own_air == 0:
                                    if price_own_air9 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air9
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �7�6 RM-10 BOMBUSHKA �٧� ' + str(
                                            price_own_air9) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� ��ѧާ�ݧק�! �9�5'
                            elif int(id_own) == 10:
                                if own_air == 0:
                                    if price_own_air10 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air10
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �7�6 AVENGER �� HYV �٧� ' + str(price_own_air10) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� ��ѧާ�ݧק�! �9�5'
                            elif int(id_own) == 11:
                                if own_air == 0:
                                    if price_own_air11 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air11
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �7�6 F-16 Fighting Falcon �٧� ' + str(price_own_air11) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� ��ѧާ�ݧק�! �9�5'
                            elif int(id_own) == 12:
                                if own_air == 0:
                                    if price_own_air12 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air12
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �7�6 RM-10 BOMBUSHKA �٧� ' + str(price_own_air12) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� ��ѧާ�ݧק�! �9�5'
                            elif int(id_own) == 13:
                                if own_air == 0:
                                    if price_own_air13 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air13
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �7�6 TULA �� MAMMOTH �٧� ' + str(price_own_air13) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� ��ѧާ�ݧק�! �9�5'
                            elif int(id_own) == 14:
                                if own_air == 0:
                                    if price_own_air14 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air14
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �7�6 V-65 MOLOTOK �٧� ' + str(price_own_air14) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� ��ѧާ�ݧק�! �9�5'
                            elif int(id_own) == 15:
                                if own_air == 0:
                                    if price_own_air15 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air15
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �7�6 MOGUL �� MAMMOTH �٧� ' + str(price_own_air15) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� ��ѧާ�ݧק�! �9�5'
                            else:
                                return ', ��ѧާ�ݧק�� �� ��ѧܧڧ� ID �ߧ� ����֧��ӧ�֧�! �9�6'
                        else:
                            return ', ��ڧާӧ�ݧ� �� �ҧ�ܧӧ� �٧ѧ��֧�֧ߧ�! �9�6'
                    else:
                        return ', �էݧ� ���ܧ��ܧ� ���ѧߧ������ �ߧ֧�ҧ��էڧ� �է��! �9�5'
                elif sourceText.split()[1].lower() in ['�ӧ֧���ݧק�', '�ӧ֧���ݧ֧�', '�ӧ֧���ݧק��', '�ӧ֧���ݧ֧��']:
                    own_housing = int(get_data['own_housing'])
                    if own_housing >= 1 or own_housing != 30:
                        own_helicopter = int(get_data['own_helicopter'])
                        price_own_helicopter1 = 1300000
                        price_own_helicopter2 = 1750000
                        price_own_helicopter3 = 2225000
                        price_own_helicopter4 = 3500000
                        price_own_helicopter5 = 8850000
                        price_own_helicopter6 = 25555555
                        price_own_helicopter7 = 58000000
                        price_own_helicopter8 = 215000000
                        price_own_helicopter9 = 525000000

                        if id_own.isdigit():
                            if int(id_own) == 1:
                                if own_helicopter == 0:
                                    if price_own_helicopter1 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter1
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�5 Eurocopter EC130/135/14 �٧� ' + str(price_own_helicopter1) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ӧ֧���ݧק�! �9�5'
                            elif int(id_own) == 2:
                                if own_helicopter == 0:
                                    if price_own_helicopter2 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter2
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�5 Boeing MH-6 �٧� ' + str(price_own_helicopter2) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ӧ֧���ݧק�! �9�5'

                            elif int(id_own) == 3:
                                if own_helicopter == 0:
                                    if price_own_helicopter3 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter3
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�5 Sikorsky UH-60 �٧� ' + str(price_own_helicopter3) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ӧ֧���ݧק�! �9�5'
                            elif int(id_own) == 4:
                                if own_helicopter == 0:
                                    if price_own_helicopter4 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter4
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�5 HAVOK �� NAGASAKI �٧� ' + str(price_own_helicopter4) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ӧ֧���ݧק�! �9�5'

                            elif int(id_own) == 5:
                                if own_helicopter == 0:
                                    if price_own_helicopter5 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter5
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�5 Eurocopter EC145 �٧� ' + str(price_own_helicopter5) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ӧ֧���ݧק�! �9�5'
                            elif int(id_own) == 6:
                                if own_helicopter == 0:
                                    if price_own_helicopter6 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter6
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�5 Airbus H160 �٧� ' + str(price_own_helicopter6) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ӧ֧���ݧק�! �9�5'
                            elif int(id_own) == 7:
                                if own_helicopter == 0:
                                    if price_own_helicopter7 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter7
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�5 Mil Mi-24 �٧� ' + str(price_own_helicopter7) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ӧ֧���ݧק�! �9�5'
                            elif int(id_own) == 8:
                                if own_helicopter == 0:
                                    if price_own_helicopter8 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter8
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�5 POLICE MAVERICK �٧� ' + str(price_own_helicopter8) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ӧ֧���ݧק�! �9�5'
                            elif int(id_own) == 9:
                                if own_helicopter == 0:
                                    if price_own_helicopter9 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter9
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�5 MAVERICK �٧� ' + str(price_own_helicopter9) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ӧ֧���ݧק�! �9�5'
                            else:
                                return ', �ӧ֧���ݧק�� �� ��ѧܧڧ� ID �ߧ� ����֧��ӧ�֧�! �9�6'
                        else:
                            return ', ��ڧާӧ�ݧ� �� �ҧ�ܧӧ� �٧ѧ��֧�֧ߧ�! �9�6'
                    else:
                        return ', �էݧ� ���ܧ��ܧ� ���ѧߧ������ �ߧ֧�ҧ��էڧ� �է��! �9�5'
                elif sourceText.split()[1].lower() in ['��֧�ާ�', '��֧�ާ�']:
                    own_farm = int(get_data['own_farm'])
                    own_housing = int(get_data['own_housing'])
                    price_own_farm1 = 500000
                    price_own_farm2 = 5000000
                    price_own_farm3 = 500000000
                    if own_housing >= 1 or own_housing == 30:
                        if id_own.isdigit():
                            if int(id_own) == 1:
                                if own_farm == 0:
                                    if price_own_farm1 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_farm1
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_farm": '{}'.format(id_own)})
                                        get_data.update({"farm_profit": '{}'.format(5)})
                                        get_data.update({"farm_time": '{}'.format(time.time())})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�1 Miner �٧� ' + str(price_own_farm1) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� ��֧�ާ�! �9�5'
                            elif int(id_own) == 2:
                                if own_farm == 0:
                                    if price_own_farm2 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_farm2
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_farm": '{}'.format(id_own)})
                                        get_data.update({"farm_profit": '{}'.format(50)})
                                        get_data.update({"farm_time": '{}'.format(time.time())})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�1 Miner S �٧� ' + str(price_own_farm2) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� ��֧�ާ�! �9�5'

                            elif int(id_own) == 3:
                                if own_farm == 0:
                                    if price_own_farm3 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_farm3
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_farm": '{}'.format(id_own)})
                                        get_data.update({"farm_profit": '{}'.format(1000)})
                                        get_data.update({"farm_time": '{}'.format(time.time())})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�1 Miner X �٧� ' + str(price_own_farm3) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� ��֧�ާ�! �9�5'
                            else:
                                return ', ��֧�ާ� �� ��ѧܧڧ� ID �ߧ� ����֧��ӧ�֧�! �9�6'
                        else:
                            return ', ��ڧާӧ�ݧ� �� �ҧ�ܧӧ� �٧ѧ��֧�֧ߧ�! �9�6'
                    else:
                        return ', �էݧ� ���ܧ��ܧ� ��֧�ާ� �ߧ֧�ҧ��էڧ� �է��! �9�5'
                elif sourceText.split()[1].lower() in ['�ܧ�ާ�', '�ܧ�ާ����֧�', '�ߧ���', '�ߧ���ҧ��', '�ܧ�ާ��','�ܧ�ާ����֧��', '�ߧ����', '�ߧ���ҧ�ܧ�']:
                    own_comp = int(get_data['own_comp'])
                    price_own_comp1 = 35000000
                    price_own_comp2 = 45000000
                    price_own_comp3 = 150000000

                    if id_own.isdigit():
                        if int(id_own) == 1:
                            if own_comp == 0:
                                if price_own_comp1 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_comp1
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_comp": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�5 Book �٧� ' + str(price_own_comp1) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                else:
                                    return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                            else:
                                return ', �� �ӧѧ� ��ا� �֧��� �ܧ�ާ����֧�! �9�5'
                        elif int(id_own) == 2:
                            if own_comp == 0:
                                if price_own_comp2 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_comp2
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_comp": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�5 Book Air �٧� ' + str(price_own_comp2) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                else:
                                    return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                            else:
                                return ', �� �ӧѧ� ��ا� �֧��� �ܧ�ާ����֧�! �9�5'

                        elif int(id_own) == 3:
                            if own_comp == 0:
                                if price_own_comp3 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_comp3
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_comp": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�5 Book Pro �٧� ' + str(price_own_comp3) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                else:
                                    return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                            else:
                                return ', �� �ӧѧ� ��ا� �֧��� �ܧ�ާ����֧�! �9�5'
                        else:
                            return ', �ܧ�ާ����֧�� �� ��ѧܧڧ� ID �ߧ� ����֧��ӧ�֧�! �9�6'
                    else:
                        return ', ��ڧާӧ�ݧ� �� �ҧ�ܧӧ� �٧ѧ��֧�֧ߧ�! �9�6'
                elif sourceText.split()[1].lower() in ['��֧ݧ֧���', '��ާѧ�����', '��֧ݧ֧��ߧ�', '��ާѧ����ߧ�']:
                    own_smart = int(get_data['own_smart'])
                    price_own_smart1 = 25800000
                    price_own_smart2 = 30000000
                    price_own_smart3 = 35250000

                    if id_own.isdigit():
                        if int(id_own) == 1:
                            if own_smart == 0:
                                if price_own_smart1 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_smart1
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_smart": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�5 iPhone �٧� ' + str(price_own_smart1) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                else:
                                    return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                            else:
                                return ', �� �ӧѧ� ��ا� �֧��� ��ާѧ�����! �9�5'
                        elif int(id_own) == 2:
                            if own_smart == 0:
                                if price_own_smart2 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_smart2
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_smart": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�5 iPhone Pro �٧� ' + str(price_own_smart2) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                else:
                                    return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                            else:
                                return ', �� �ӧѧ� ��ا� �֧��� ��ާѧ�����! �9�5'

                        elif int(id_own) == 3:
                            if own_smart == 0:
                                if price_own_smart3 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_smart3
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_smart": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�5 iPhone Pro Max �٧� ' + str(price_own_smart3) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                else:
                                    return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                            else:
                                return ', �� �ӧѧ� ��ا� �֧��� ��ާѧ�����! �9�5'
                        else:
                            return ', ��ާѧ����ߧ� �� ��ѧܧڧ� ID �ߧ� ����֧��ӧ�֧�! �9�6'
                    elif sourceText.split()[1].lower() in ['��֧ݧ֧���', '��ާѧ�����', '��֧ݧ֧��ߧ�', '��ާѧ����ߧ�']:
                        own_smart = int(get_data['own_smart'])
                        price_own_smart1 = 800000
                        price_own_smart2 = 1000000
                        price_own_smart3 = 1250000

                        if id_own.isdigit():
                            if int(id_own) == 1:
                                if own_smart == 0:
                                    if price_own_smart1 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_smart1
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_smart": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�5 iPhone �٧� ' + str(
                                            price_own_smart1) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� ��ާѧ�����! �9�5'
                            elif int(id_own) == 2:
                                if own_smart == 0:
                                    if price_own_smart2 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_smart2
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_smart": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�5 iPhone Pro �٧� ' + str(
                                            price_own_smart2) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� ��ާѧ�����! �9�5'

                            elif int(id_own) == 3:
                                if own_smart == 0:
                                    if price_own_smart3 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_smart3
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_smart": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�5 iPhone Pro Max �٧� ' + str(
                                            price_own_smart3) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� ��ާѧ�����! �9�5'
                            else:
                                return ', ��ާѧ����ߧ� �� ��ѧܧڧ� ID �ߧ� ����֧��ӧ�֧�! �9�6'
                    else:
                        return ', ��ڧާӧ�ݧ� �� �ҧ�ܧӧ� �٧ѧ��֧�֧ߧ�! �9�6'
                else:
                    return ', ��ѧܧ�� �ܧѧ�֧ԧ��ڧ� �ߧ� ����֧��ӧ�֧�! �9�6'
            else:
                return shopHelp
        else:
            return None
    passet_data, users_dir + str(id) + ".json")
                                    return ', вы успешно преобрели - 🏠 Деревянный домик за ' + str(price_own_housing6) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                else:
                                    return ', у вас недостаточно денег! 😔'
                            else:
                                return ', у вас уже есть дом! 😉'
                        elif int(id_own) == 7:
                            if own_housing == 0:
                                if price_own_housing7 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing7
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', вы успешно преобрели - 🏠 Кирпичный дом за ' + str(price_own_housing7) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                else:
                                    return ', у вас недостаточно денег! 😔'
                            else:
                                return ', у вас уже есть дом! 😉'
                        elif int(id_own) == 8:
                            if own_housing == 0:
                                if price_own_housing8 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing8
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', вы успешно преобрели - 🏠 Коттедж за ' + str(price_own_housing8) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                else:
                                    return ', у вас недостаточно денег! 😔'
                            else:
                                return ', у вас уже есть дом! 😉'
                        elif int(id_own) == 9:
                            if own_housing == 0:
                                if price_own_housing9 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing9
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', вы успешно преобрели - 🏠 Дом на Пумавуде за ' + str(price_own_housing9) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                else:
                                    return ', у вас недостаточно денег! 😔'
                            else:
                                return ', у вас уже есть дом! 😉'
                        elif int(id_own) == 10:
                            if own_housing == 0:
                                if price_own_housing10 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing10
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', вы успешно преобрели - 🏠 Виллу на Пумавуде за ' + str(price_own_housing10) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                else:
                                    return ', у вас недостаточно денег! 😔'
                            else:
                                return ', у вас уже есть дом! 😉'
                        elif int(id_own) == 11:
                            if own_housing == 0:
                                if price_own_housing11 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing11
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', вы успешно преобрели - 🏠 Личный остров за ' + str(price_own_housing11) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                else:
                                    return ', у вас недостаточно денег! 😔'
                            else:
                                return ', у вас уже есть дом! 😉'
                        else:
                            return ', дома с таким ID не существует! 😔'
                    else:
                        return ', символы и буквы запрещены! 😔'

                elif sourceText.split()[1].lower() in ['машина', 'машины']:
                    own_car = int(get_data['own_car'])
                    own_housing = int(get_data['own_housing'])
                    if own_housing >= 1 or own_housing != 30:
                        price_own_car1 = 125000
                        price_own_car2 = 255000
                        price_own_car3 = 525000
                        price_own_car4 = 1275000
                        price_own_car5 = 1650000
                        price_own_car6 = 2000000
                        price_own_car7 = 4350000
                        price_own_car8 = 15650000
                        price_own_car9 = 25735000
                        price_own_car10 = 30800000
                        price_own_car11 = 37580000
                        price_own_car12 = 57999999
                        price_own_car13 = 108555000
                        price_own_car14 = 999999999
                        price_own_car15 = 1500000000

                        if id_own.isdigit():
                            if int(id_own) == 1:
                                if own_car == 0:
                                    if price_own_car1 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car1
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🚗 Велосипед за ' + str(price_own_car1) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть машина! 😉'
                            elif int(id_own) == 2:
                                if own_car == 0:
                                    if price_own_car2 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car2
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🚗 Гироскутер за ' + str(price_own_car2) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть машина! 😉'

                            elif int(id_own) == 3:
                                if own_car == 0:
                                    if price_own_car3 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car3
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🏍 Ducati Scrambler за ' + str(price_own_car3) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть машина! 😉'
                            elif int(id_own) == 4:
                                if own_car == 0:
                                    if price_own_car4 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car4
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🏍 Honda CTX1300 за ' + str(price_own_car4) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть машина! 😉'

                            elif int(id_own) == 5:
                                if own_car == 0:
                                    if price_own_car5 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car5
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🚗 Ferrari California front за ' + str(price_own_car5) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть машина! 😉'
                            elif int(id_own) == 6:
                                if own_car == 0:
                                    if price_own_car6 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car6
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🚗 Porsche 911 за ' + str(price_own_car6) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть машина! 😉'
                            elif int(id_own) == 7:
                                if own_car == 0:
                                    if price_own_car7 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car7
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🚗 Nissan GT-R за ' + str(price_own_car7) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть машина! 😉'
                            elif int(id_own) == 8:
                                if own_car == 0:
                                    if price_own_car8 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car8
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🚗 BMW X6 за ' + str(price_own_car8) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть машина! 😉'
                            elif int(id_own) == 9:
                                if own_car == 0:
                                    if price_own_car9 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car9
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🚗 Jaguar F-Type за ' + str(price_own_car9) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть машина! 😉'
                            elif int(id_own) == 10:
                                if own_car == 0:
                                    if price_own_car10 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car10
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🚗 Lamborghini Huracán за ' + str(price_own_car10) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть машина! 😉'
                            elif int(id_own) == 11:
                                if own_car == 0:
                                    if price_own_car11 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car11
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🚗 Lamborghini Gallardo за ' + str(price_own_car11) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть машина! 😉'
                            elif int(id_own) == 12:
                                if own_car == 0:
                                    if price_own_car12 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car12
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🚗 Ferrari F80 Concept за ' + str(price_own_car12) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть машина! 😉'
                            elif int(id_own) == 13:
                                if own_car == 0:
                                    if price_own_car13 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car13
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🚗 Lamborghini Sesto за ' + str(price_own_car13) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть машина! 😉'
                            elif int(id_own) == 14:
                                if own_car == 0:
                                    if price_own_car14 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car14
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🚗 Various Ford-based trucks за ' + str(price_own_car14) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть машина! 😉'
                            elif int(id_own) == 15:
                                if own_car == 0:
                                    if price_own_car15 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car15
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🚗 Tesla Cybertruck за ' + str(price_own_car15) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть машина! 😉'
                            else:
                                return ', машины с таким ID не существует! 😔'
                        else:
                            return ', символы и буквы запрещены! 😔'
                    else:
                        return ', для покупки транспорта необходимо дом! 😉'
                elif sourceText.split()[1].lower() in ['яхта', 'яхты']:
                    own_housing = int(get_data['own_housing'])
                    if own_housing >= 1 or own_housing != 30:
                        own_yacht = int(get_data['own_yacht'])
                        price_own_yacht1 = 575000
                        price_own_yacht2 = 1225000
                        price_own_yacht3 = 2500000
                        price_own_yacht4 = 3650000
                        price_own_yacht5 = 8355000
                        price_own_yacht6 = 12850000
                        price_own_yacht7 = 23125000
                        price_own_yacht8 = 34666000
                        price_own_yacht9 = 66225000
                        price_own_yacht10 = 96000000
                        price_own_yacht11 = 126650000
                        price_own_yacht12 = 527777777
                        price_own_yacht13 = 999999999
                        price_own_yacht14 = 1255000000

                        if id_own.isdigit():
                            if int(id_own) == 1:
                                if own_yacht == 0:
                                    if price_own_yacht1 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht1
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🛥 RHIB за ' + str(price_own_yacht1) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть яхта! 😉'
                            elif int(id_own) == 2:
                                if own_yacht == 0:
                                    if price_own_yacht2 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht2
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🛥 Kawasaki за ' + str(price_own_yacht2) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть яхта! 😉'

                            elif int(id_own) == 3:
                                if own_yacht == 0:
                                    if price_own_yacht3 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht3
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🛥 Riva Aquarama за ' + str(price_own_yacht3) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть яхта! 😉'
                            elif int(id_own) == 4:
                                if own_yacht == 0:
                                    if price_own_yacht4 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht4
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🛥 Various за ' + str(price_own_yacht4) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть яхта! 😉'

                            elif int(id_own) == 5:
                                if own_yacht == 0:
                                    if price_own_yacht5 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht5
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🛥 Рrinсеss 60 за ' + str(price_own_yacht5) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть яхта! 😉'
                            elif int(id_own) == 6:
                                if own_yacht == 0:
                                    if price_own_yacht6 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht6
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🛥 Аzimut 70 за ' + str(price_own_yacht6) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть яхта! 😉'
                            elif int(id_own) == 7:
                                if own_yacht == 0:
                                    if price_own_yacht7 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht7
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🛥 Dоminаtоr 40M за ' + str(price_own_yacht7) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть яхта! 😉'
                            elif int(id_own) == 8:
                                if own_yacht == 0:
                                    if price_own_yacht8 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht8
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🛥 Mооnеn 124 за ' + str(price_own_yacht8) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть яхта! 😉'
                            elif int(id_own) == 9:
                                if own_yacht == 0:
                                    if price_own_yacht9 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht9
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🛥 Widеr 150 за ' + str(price_own_yacht9) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть яхта! 😉'
                            elif int(id_own) == 10:
                                if own_yacht == 0:
                                    if price_own_yacht10 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht10
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🛥 Palmer Jоhnsоn 42M SuреrSроrt за ' + str(
                                            price_own_yacht10) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть яхта! 😉'
                            elif int(id_own) == 11:
                                if own_yacht == 0:
                                    if price_own_yacht11 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht11
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🛥 Widеr 165 за ' + str(price_own_yacht11) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть яхта! 😉'
                            elif int(id_own) == 12:
                                if own_yacht == 0:
                                    if price_own_yacht12 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht12
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🛥 Есliрsе за ' + str(price_own_yacht12) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть яхта! 😉'
                            elif int(id_own) == 13:
                                if own_yacht == 0:
                                    if price_own_yacht13 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht13
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🛥 Dubаi за ' + str(price_own_yacht13) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть яхта! 😉'
                            elif int(id_own) == 14:
                                if own_yacht == 0:
                                    if price_own_yacht14 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht14
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🛥 Strееts оf Mоnасо за ' + str(price_own_yacht14) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть яхта! 😉'
                            else:
                                return ', яхты с таким ID не существует! 😔'
                        else:
                            return ', символы и буквы запрещены! 😔'
                    else:
                        return ', для покупки транспорта необходим дом! 😉'
                elif sourceText.split()[1].lower() in ['самолёт', 'самолет', 'самолёты', 'самолеты']:
                    own_housing = int(get_data['own_housing'])
                    if own_housing >= 1 or own_housing != 30:
                        own_air = int(get_data['own_air'])
                        price_own_air1 = 500000
                        price_own_air2 = 3995000
                        price_own_air3 = 6350000
                        price_own_air4 = 15500000
                        price_own_air5 = 17800000
                        price_own_air6 = 22250000
                        price_own_air7 = 43000000
                        price_own_air8 = 65505000
                        price_own_air9 = 75985000
                        price_own_air10 = 86495000
                        price_own_air11 = 109999999
                        price_own_air12 = 313000000
                        price_own_air13 = 617555000
                        price_own_air14 = 850000000
                        price_own_air15 = 2000000000

                        if id_own.isdigit():
                            if int(id_own) == 1:
                                if own_air == 0:
                                    if price_own_air1 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air1
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - ✈ de Havilland Canada DHC-2 за ' + str(price_own_air1) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть самолёт! 😉'
                            elif int(id_own) == 2:
                                if own_air == 0:
                                    if price_own_air2 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air2
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - ✈ Piper PA-46 за ' + str(price_own_air2) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть самолёт! 😉'

                            elif int(id_own) == 3:
                                if own_air == 0:
                                    if price_own_air3 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air3
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - ✈ Cessna 310 за ' + str(price_own_air3) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть самолёт! 😉'
                            elif int(id_own) == 4:
                                if own_air == 0:
                                    if price_own_air4 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air4
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - ✈ Learjet 55 за ' + str(price_own_air4) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть самолёт! 😉'

                            elif int(id_own) == 5:
                                if own_air == 0:
                                    if price_own_air5 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air5
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - ✈ Bombardier Global Express за ' + str(price_own_air5) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть самолёт! 😉'
                            elif int(id_own) == 6:
                                if own_air == 0:
                                    if price_own_air6 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air6
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - ✈ Cessna Citation X за ' + str(price_own_air6) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть самолёт! 😉'
                            elif int(id_own) == 7:
                                if own_air == 0:
                                    if price_own_air7 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air7
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - ✈ C-130 за ' + str(price_own_air7) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть самолёт! 😉'
                            elif int(id_own) == 8:
                                if own_air == 0:
                                    if price_own_air8 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air8
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - ✈ VOLATOL за ' + str(price_own_air8) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть самолёт! 😉'
                            elif int(id_own) == 9:
                                if own_air == 0:
                                    if price_own_air9 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air9
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - ✈ RM-10 BOMBUSHKA за ' + str(
                                            price_own_air9) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть самолёт! 😉'
                            elif int(id_own) == 10:
                                if own_air == 0:
                                    if price_own_air10 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air10
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - ✈ AVENGER — HYV за ' + str(price_own_air10) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть самолёт! 😉'
                            elif int(id_own) == 11:
                                if own_air == 0:
                                    if price_own_air11 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air11
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - ✈ F-16 Fighting Falcon за ' + str(price_own_air11) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть самолёт! 😉'
                            elif int(id_own) == 12:
                                if own_air == 0:
                                    if price_own_air12 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air12
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - ✈ RM-10 BOMBUSHKA за ' + str(price_own_air12) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть самолёт! 😉'
                            elif int(id_own) == 13:
                                if own_air == 0:
                                    if price_own_air13 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air13
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - ✈ TULA — MAMMOTH за ' + str(price_own_air13) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть самолёт! 😉'
                            elif int(id_own) == 14:
                                if own_air == 0:
                                    if price_own_air14 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air14
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - ✈ V-65 MOLOTOK за ' + str(price_own_air14) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть самолёт! 😉'
                            elif int(id_own) == 15:
                                if own_air == 0:
                                    if price_own_air15 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air15
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - ✈ MOGUL — MAMMOTH за ' + str(price_own_air15) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть самолёт! 😉'
                            else:
                                return ', самолёта с таким ID не существует! 😔'
                        else:
                            return ', символы и буквы запрещены! 😔'
                    else:
                        return ', для покупки транспорта необходим дом! 😉'
                elif sourceText.split()[1].lower() in ['вертолёт', 'вертолет', 'вертолёты', 'вертолеты']:
                    own_housing = int(get_data['own_housing'])
                    if own_housing >= 1 or own_housing != 30:
                        own_helicopter = int(get_data['own_helicopter'])
                        price_own_helicopter1 = 1300000
                        price_own_helicopter2 = 1750000
                        price_own_helicopter3 = 2225000
                        price_own_helicopter4 = 3500000
                        price_own_helicopter5 = 8850000
                        price_own_helicopter6 = 25555555
                        price_own_helicopter7 = 58000000
                        price_own_helicopter8 = 215000000
                        price_own_helicopter9 = 525000000

                        if id_own.isdigit():
                            if int(id_own) == 1:
                                if own_helicopter == 0:
                                    if price_own_helicopter1 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter1
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🚁 Eurocopter EC130/135/14 за ' + str(price_own_helicopter1) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть вертолёт! 😉'
                            elif int(id_own) == 2:
                                if own_helicopter == 0:
                                    if price_own_helicopter2 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter2
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🚁 Boeing MH-6 за ' + str(price_own_helicopter2) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть вертолёт! 😉'

                            elif int(id_own) == 3:
                                if own_helicopter == 0:
                                    if price_own_helicopter3 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter3
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🚁 Sikorsky UH-60 за ' + str(price_own_helicopter3) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть вертолёт! 😉'
                            elif int(id_own) == 4:
                                if own_helicopter == 0:
                                    if price_own_helicopter4 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter4
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🚁 HAVOK — NAGASAKI за ' + str(price_own_helicopter4) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть вертолёт! 😉'

                            elif int(id_own) == 5:
                                if own_helicopter == 0:
                                    if price_own_helicopter5 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter5
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🚁 Eurocopter EC145 за ' + str(price_own_helicopter5) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть вертолёт! 😉'
                            elif int(id_own) == 6:
                                if own_helicopter == 0:
                                    if price_own_helicopter6 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter6
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🚁 Airbus H160 за ' + str(price_own_helicopter6) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть вертолёт! 😉'
                            elif int(id_own) == 7:
                                if own_helicopter == 0:
                                    if price_own_helicopter7 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter7
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🚁 Mil Mi-24 за ' + str(price_own_helicopter7) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть вертолёт! 😉'
                            elif int(id_own) == 8:
                                if own_helicopter == 0:
                                    if price_own_helicopter8 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter8
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🚁 POLICE MAVERICK за ' + str(price_own_helicopter8) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть вертолёт! 😉'
                            elif int(id_own) == 9:
                                if own_helicopter == 0:
                                    if price_own_helicopter9 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter9
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🚁 MAVERICK за ' + str(price_own_helicopter9) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть вертолёт! 😉'
                            else:
                                return ', вертолёта с таким ID не существует! 😔'
                        else:
                            return ', символы и буквы запрещены! 😔'
                    else:
                        return ', для покупки транспорта необходим дом! 😉'
                elif sourceText.split()[1].lower() in ['ферма', 'фермы']:
                    own_farm = int(get_data['own_farm'])
                    own_housing = int(get_data['own_housing'])
                    price_own_farm1 = 500000
                    price_own_farm2 = 5000000
                    price_own_farm3 = 500000000
                    if own_housing >= 1 or own_housing == 30:
                        if id_own.isdigit():
                            if int(id_own) == 1:
                                if own_farm == 0:
                                    if price_own_farm1 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_farm1
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_farm": '{}'.format(id_own)})
                                        get_data.update({"farm_profit": '{}'.format(5)})
                                        get_data.update({"farm_time": '{}'.format(time.time())})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🔋 Miner за ' + str(price_own_farm1) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть ферма! 😉'
                            elif int(id_own) == 2:
                                if own_farm == 0:
                                    if price_own_farm2 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_farm2
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_farm": '{}'.format(id_own)})
                                        get_data.update({"farm_profit": '{}'.format(50)})
                                        get_data.update({"farm_time": '{}'.format(time.time())})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🔋 Miner S за ' + str(price_own_farm2) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть ферма! 😉'

                            elif int(id_own) == 3:
                                if own_farm == 0:
                                    if price_own_farm3 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_farm3
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_farm": '{}'.format(id_own)})
                                        get_data.update({"farm_profit": '{}'.format(1000)})
                                        get_data.update({"farm_time": '{}'.format(time.time())})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', вы успешно преобрели - 🔋 Miner X за ' + str(price_own_farm3) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                    else:
                                        return ', у вас недостаточно денег! 😔'
                                else:
                                    return ', у вас уже есть ферма! 😉'
                            else:
                                return ', фермы с таким ID не существует! 😔'
                        else:
                            return ', символы и буквы запрещены! 😔'
                    else:
                        return ', для покупки фермы необходим дом! 😉'
                elif sourceText.split()[1].lower() in ['комп', 'компьютер', 'ноут', 'ноутбук', 'компы','компьютеры', 'ноуты', 'ноутбуки']:
                    own_comp = int(get_data['own_comp'])
                    price_own_comp1 = 35000000
                    price_own_comp2 = 45000000
                    price_own_comp3 = 150000000

                    if id_own.isdigit():
                        if int(id_own) == 1:
                            if own_comp == 0:
                                if price_own_comp1 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_comp1
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_comp": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', вы успешно преобрели - 🖥 Book за ' + str(price_own_comp1) + '€!\n💰 Ваш баланс: ' + str(algo_buy_own) + '€'
                                else:
                                    return ', у вас недостаточно денег! 😔'
                            else:
                                return ', у вас уже есть компьютер! 😉'
                        elif int(id_own) == 2:
                            if own_comp == 0:
                                if price_own_comp2 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_comp2
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_comp": '{}'.format(id_oimport os
import time
from plugins import gf

users_dir = os.path.join(r"users/")

def shop(sourceText, id):
    get_data = gf.loadjson(users_dir + str(id) + ".json")
    user_balance = int(get_data['balance'])

    shopHelp = ', ���ާ��� ��� �ާѧԧѧ٧ڧߧ�:\n\n�7�4�0�6 ����ܧ��ѧۧ�� ��ѧ٧ݧڧ�ߧ�� �ڧާ��֧��ӧ� �� ��էڧ� �ܧݧڧ�! �����ݧ� ���ܧ��ܧ� �է�ާ�, �ӧ� ��ާ�ا֧�� ���֧�ҧ�֧��� ���ѧߧ����� �� ��֧�ާ� �էݧ� �ާѧۧߧڧߧԧ� �ҧڧ�ܧ�ڧߧ��.\n\n�9�8 ����ߧ�ӧߧ��:\n�7�4�7�4�9�2 ����ާ�\n�7�4�7�4�0�7 ���ѧ�ڧߧ�\n�7�4�7�4�7�6 ���ѧާ�ݧק��\n�7�4�7�4�0�5 ���֧���ݧק��\n�7�4�7�4�0�5 ������\n\n�9�5 �����ѧݧ�ߧ��:\n�7�4�7�4�9�5 ����ާ����֧��\n�7�4�7�4�9�5 ���֧ݧ֧��ߧ�\n�7�4�7�4�9�1 ���֧�ާ�\n\n�7�1 ����ާ���:\n�7�4�7�4�9�4 ���ѧԧѧ٧ڧ� [�ܧѧ�֧ԧ��ڧ�] - ���ӧѧ��.\n�7�4�7�4�0�6 ���ѧԧѧ٧ڧ� [�ܧѧ�֧ԧ��ڧ�] [�ߧ�ާ֧�] - �ܧ��ڧ�� ���ӧѧ�.'

    if sourceText != '':
        if '�ާѧԧѧ٧ڧ�' == sourceText.split()[0].lower():
            if len(sourceText.split()) == 2:
                if sourceText.split()[1].lower() in ['�է��', '�է�ާ�']:
                    return ', ���ڧ��� �է�����ߧ�� �է�ާ��:\n\n�7�4�9�0 �����ݧ� ���ܧ��ܧ� �է�ާ�, �ӧ� ��ާ�ا֧�� �ܧ��ڧ�� ���ѧߧ����� �� ��֧�ާ�!\n\n�7�4�7�4�9�2 1. ������ҧܧ� �� 25.000��\n�7�4�7�4�9�2 2. ����էӧѧ� �� 65.000��\n�7�4�7�4�9�2 3. ���ѧ�ѧ� �� 225.000��\n�7�4�7�4�9�2 4. ���ѧ�ѧ� �� 595.000��\n�7�4�7�4�9�2 5. ���֧��ѧ� ��ڧاڧߧ� �� 655.000��\n�7�4�7�4�9�2 6. ���֧�֧ӧ�ߧߧ�� �է�ާڧ� �� 1.525.000��\n�7�4�7�4�9�2 7. ���ڧ��ڧ�ߧ�� �է�� �� 8.525.000��\n�7�4�7�4�9�2 8. ������֧է� �� 35.650.000��\n�7�4�7�4�9�2 9. ����� �ߧ� ����ާѧӧ�է� �� 68.250.000��\n�7�4�7�4�9�2 10. ���ڧݧݧ� �ߧ� ����ާѧӧ�է� �� 93.500.000��\n�7�4�7�4�9�2 11. ���ڧ�ߧ�� ������� �� 999.999.999��\n\n�7�1 ���ݧ� ���ܧ��ܧ� �է�ާ�, �ڧ���ݧ�٧�ۧ��:\n�7�4�7�4�0�6 ���ѧԧѧ٧ڧ� �է�� [�ߧ�ާ֧�]'
                elif sourceText.split()[1].lower() in ['�ާѧ�ڧߧ�', '�ާѧ�ڧߧ�']:
                    return ', ���ڧ��� �է�����ߧ�� �ާѧ�ڧ�:\n\n�7�4�9�0 ����ܧ��ѧۧ�� ���ѧߧ����� �� ��էڧ� �ܧݧڧ�!\n\n�7�4�7�4�0�7 1. ���֧ݧ��ڧ�֧� �� 125.000��\n�7�4�7�4�0�7 2. ���ڧ���ܧ��֧� �� 255.000��\n�7�4�7�4�9�3 3. Ducati Scrambler �� 525.000��\n�7�4�7�4�9�3 4. Honda CTX1300 �� 1.275.000��\n�7�4�7�4�0�7 5. Ferrari California front �� 1.650.000��\n�7�4�7�4�0�7 6. Porsche 911 �� 2.000.000��\n�7�4�7�4�0�7 7. Nissan GT-R �� 4.350.000��\n�7�4�7�4�0�7 8. BMW X6 �� 15.650.000��\n�7�4�7�4�0�7 9. Jaguar F-Type �� 25.735.000��\n�7�4�7�4�0�7 10. Lamborghini Hurac��n �� 30.800.000��\n�7�4�7�4�0�7 11. Lamborghini Gallardo �� 37.580.000��\n�7�4�7�4�0�7 12. Ferrari F80 Concept �� 57.999.999��\n�7�4�7�4�0�7 13. Lamborghini Sesto �� 108.555.000��\n�7�4�7�4�0�7 14. Various Ford-based trucks �� 999.999.999��\n�7�4�7�4�0�7 15. Tesla Cybertruck �� 1.500.000.000��\n\n�7�1 ���ݧ� ���ܧ��ܧ� ���ѧߧ������, �ڧ���ݧ�٧�ۧ��:\n�7�4�7�4�0�6 ���ѧԧѧ٧ڧ� �ާѧ�ڧߧ� [�ߧ�ާ֧�]'
                elif sourceText.split()[1].lower() in ['�����', '�����']:
                    return ', ���ڧ��� �է�����ߧ�� ����:\n\n�7�4�7�4�0�5 1. RHIB �� 575.000��\n�7�4�7�4�0�5 2. Kawasaki �� 1.225.000��\n�7�4�7�4�0�5 3. Riva Aquarama �� 2.500.000��\n�7�4�7�4�0�5 4. Various �� 3.650.000��\n�7�4�7�4�0�5 5. ��rin���ss 60 �� 8.355.000��\n�7�4�7�4�0�5 6. ��zimut 70 �� 12.850.000��\n�7�4�7�4�0�5 7. D��min��t��r 40M �� 23.125.000��\n�7�4�7�4�0�5 8. M���n��n 124 �� 34.666.000��\n�7�4�7�4�0�5 9. Wid��r 150 �� 66.225.000��\n�7�4�7�4�0�5 10. Palmer J��hns��n 42M Su���rS���rt �� 96.000.000��\n�7�4�7�4�0�5 11. Wid��r 165 �� 126.650.000��\n�7�4�7�4�0�5 12. ����li��s�� �� 527.777.777��\n�7�4�7�4�0�5 13. Dub��i �� 999.999.999��\n�7�4�7�4�0�5 14. Str�֧�ts ��f M��n�ѧ�� �� 1.255.000.000��\n\n�7�1 ���ݧ� ���ܧ��ܧ� ���ѧߧ������, �ڧ���ݧ�٧�ۧ��:\n�7�4�7�4�0�6 ���ѧԧѧ٧ڧ� ����� [�ߧ�ާ֧�]'
                elif sourceText.split()[1].lower() in ['��ѧާ�ݧק�', '��ѧާ�ݧ֧�', '��ѧާ�ݧק��', '��ѧާ�ݧ֧��']:
                    return ', ���ڧ��� �է�����ߧ�� ��ѧާ�ݧק���:\n\n�7�4�9�0 ����ܧ��ѧۧ�� ���ѧߧ����� �� ��էڧ� �ܧݧڧ�!\n\n�7�4�7�4�7�6 1. de Havilland Canada DHC-2 �� 500.000��\n�7�4�7�4�7�6 2. Piper PA-46 �� 3.995.000��\n�7�4�7�4�7�6 3. Cessna 310 �� 6.350.000��\n�7�4�7�4�7�6 4. Learjet 55 �� 15.500.000��\n�7�4�7�4�7�6 5. Bombardier Global Express �� 17.800.000��\n�7�4�7�4�7�6 6. Cessna Citation X �� 22.250.000��\n�7�4�7�4�7�6 7. C-130 �� 43.000.000��\n�7�4�7�4�7�6 8. VOLATOL �� 65.505.000��\n�7�4�7�4�7�6 9. RM-10 BOMBUSHKA �� 75.985.000��\n�7�4�7�4�7�6 10. AVENGER �� HYV �� 86.495.000��\n�7�4�7�4�7�6 11. F-16 Fighting Falcon �� 109.999.999��\n�7�4�7�4�7�6 12. RM-10 BOMBUSHKA �� 313.000.000��\n�7�4�7�4�7�6 13. TULA �� MAMMOTH �� 617.555.000��\n�7�4�7�4�7�6 14. V-65 MOLOTOK �� 850.000.000��\n�7�4�7�4�7�6 15. MOGUL �� MAMMOTH �� 2.000.000.000��\n\n�7�1 ���ݧ� ���ܧ��ܧ� ���ѧߧ������, �ڧ���ݧ�٧�ۧ��:\n�7�4�7�4�0�6 ���ѧԧѧ٧ڧ� ��ѧާ�ݧק� [�ߧ�ާ֧�]'
                elif sourceText.split()[1].lower() in ['�ӧ֧���ݧק�', '�ӧ֧���ݧ֧�', '�ӧ֧���ݧק��', '�ӧ֧���ݧ֧��']:
                    return ', ���ڧ��� �է�����ߧ�� �ӧ֧���ݧק���:\n\n�7�4�9�0 ����ܧ��ѧۧ�� ���ѧߧ����� �� ��էڧ� �ܧݧڧ�!\n\n�7�4�7�4�0�5 1. Eurocopter EC130/135/14 �� 1.300.000��\n�7�4�7�4�0�5 2. Boeing MH-6 �� 1.750.000��\n�7�4�7�4�0�5 3. Sikorsky UH-60 �� 2.225.000��\n�7�4�7�4�0�5 4. HAVOK �� NAGASAKI �� 3.500.000��\n�7�4�7�4�0�5 5. Eurocopter EC145 �� 8.850.000��\n�7�4�7�4�0�5 6. Airbus H160 �� 25.555.555��\n�7�4�7�4�0�5 7. Mil Mi-24 �� 58.000.000��\n�7�4�7�4�0�5 8. POLICE MAVERICK �� 215.000.000��\n�7�4�7�4�0�5 9. MAVERICK �� 525.000.000��\n\n�7�1 ���ݧ� ���ܧ��ܧ� ���ѧߧ������, �ڧ���ݧ�٧�ۧ��:\n�7�4�7�4�0�6 ���ѧԧѧ٧ڧ� �ӧ֧���ݧק� [�ߧ�ާ֧�]'
                elif sourceText.split()[1].lower() in ['��֧�ާ�', '��֧�ާ�']:
                    return ', ���ڧ��� �է�����ߧ�� ��֧��:\n\n�7�4�9�0 �����ݧ� ���ܧ��ܧ� ��֧�ާ�, �ӧ� ��ާ�ا֧�� �ާѧۧߧڧ�� �ҧڧ�ܧ�ڧߧ�!\n\n�7�4�7�4�9�1 1. Miner (5�2�1/�է֧ߧ�) �� 500.000��\n�7�4�7�4�9�1 2. Miner S (50�2�1/�է֧ߧ�) �� 5.000.000��\n�7�4�7�4�9�1 3. Miner X (1 000�2�1/�է֧ߧ�) �� 500.000.000��\n\n�7�1 ���ݧ� ���ܧ��ܧ� ��֧�ާ�, �ڧ���ݧ�٧�ۧ��:\n�7�4�7�4�0�6 ���ѧԧѧ٧ڧ� ��֧�ާ� [�ߧ�ާ֧�]'
                elif sourceText.split()[1].lower() in ['�ܧ�ާ�', '�ܧ�ާ����֧�', '�ߧ���', '�ߧ���ҧ��', '�ܧ�ާ��', '�ܧ�ާ����֧��', '�ߧ����', '�ߧ���ҧ�ܧ�']:
                    return ', ���ڧ��� �է�����ߧ�� �ܧ�ާ����֧���:\n\n�7�4�9�0 �����ݧ� ���ܧ��ܧ� �ܧ�ާ����֧��, �ӧ� ��ާ�ا֧�� ����ڧ٧ӧ�էڧ�� �ӧ٧ݧ�ާ�!\n\n�7�4�7�4�9�5 1. Book �� 35.000.000��\n�7�4�7�4�9�5 2. Book Air �� 45.000.000��\n�7�4�7�4�9�5 3. Book Pro �� 150.000.000��\n\n�7�1 ���ݧ� ���ܧ��ܧ� �ܧ�ާ����֧��, �ڧ���ݧ�٧�ۧ��:\n�7�4�7�4�0�6 ���ѧԧѧ٧ڧ� �ܧ�ާ����֧� [�ߧ�ާ֧�]'
                elif sourceText.split()[1].lower() in ['��֧ݧ֧���', '��ާѧ�����', '��֧ݧ֧��ߧ�', '��ާѧ����ߧ�']:
                    return ', ���ڧ��� �է�����ߧ�� ��֧ݧ֧��ߧ��:\n\n�7�4�9�0 ����ܧ��ѧۧ�� ��֧ݧ֧��ߧ� �� ��էڧ� �ܧݧڧ�!\n\n�7�4�7�4�9�5 1. iPhone �� 25.800.000��\n�7�4�7�4�9�5 2. iPhone Pro �� 30.000.000��\n�7�4�7�4�9�5 3. iPhone Pro Max �� 35.250.000��\n\n�7�1 ���ݧ� ���ܧ��ܧ� ��ާѧ����ߧ�, �ڧ���ݧ�٧�ۧ��:\n�7�4�7�4�0�6 ���ѧԧѧ٧ڧ� ��ާѧ����� [�ߧ�ާ֧�]'
            elif len(sourceText.split()) == 3:
                id_own = str(sourceText.split()[2].lower())
                if sourceText.split()[1].lower() in ['�է��', '�է�ާ�']:
                    own_housing = int(get_data['own_housing'])
                    price_own_housing1 = 25000
                    price_own_housing2 = 65000
                    price_own_housing3 = 225000
                    price_own_housing4 = 595000
                    price_own_housing5 = 655000
                    price_own_housing6 = 1525000
                    price_own_housing7 = 8525000
                    price_own_housing8 = 35650000
                    price_own_housing9 = 68250000
                    price_own_housing10 = 93500000
                    price_own_housing11 = 999999999
                    if id_own.isdigit():
                        if int(id_own) == 1:
                            if own_housing == 0:
                                if price_own_housing1 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing1
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�2 ������ҧܧ� �٧� ' + str(price_own_housing1) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                else:
                                    return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                            else:
                                return ', �� �ӧѧ� ��ا� �֧��� �է��! �9�5'
                        elif int(id_own) == 2:
                            if own_housing == 0:
                                if price_own_housing2 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing2
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�2 ����էӧѧ� �٧� ' + str(price_own_housing2) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                else:
                                    return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                            else:
                                return ', �� �ӧѧ� ��ا� �֧��� �է��! �9�5'
                        elif int(id_own) == 3:
                            if own_housing == 0:
                                if price_own_housing3 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing3
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�2 ���ѧ�ѧ� �٧� ' + str(price_own_housing3) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                else:
                                    return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                            else:
                                return ', �� �ӧѧ� ��ا� �֧��� �է��! �9�5'
                        elif int(id_own) == 4:
                            if own_housing == 0:
                                if price_own_housing4 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing4
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�2 ���ѧ�ѧ� �٧� ' + str(price_own_housing4) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                else:
                                    return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                            else:
                                return ', �� �ӧѧ� ��ا� �֧��� �է��! �9�5'
                        elif int(id_own) == 5:
                            if own_housing == 0:
                                if price_own_housing5 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing5
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�2 ���֧���� ��ڧاڧߧ� �٧� ' + str(price_own_housing5) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                else:
                                    return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                            else:
                                return ', �� �ӧѧ� ��ا� �֧��� �է��! �9�5'
                        elif int(id_own) == 6:
                            if own_housing == 0:
                                if price_own_housing6 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing6
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�2 ���֧�֧ӧ�ߧߧ�� �է�ާڧ� �٧� ' + str(price_own_housing6) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                else:
                                    return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                            else:
                                return ', �� �ӧѧ� ��ا� �֧��� �է��! �9�5'
                        elif int(id_own) == 7:
                            if own_housing == 0:
                                if price_own_housing7 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing7
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�2 ���ڧ��ڧ�ߧ�� �է�� �٧� ' + str(price_own_housing7) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                else:
                                    return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                            else:
                                return ', �� �ӧѧ� ��ا� �֧��� �է��! �9�5'
                        elif int(id_own) == 8:
                            if own_housing == 0:
                                if price_own_housing8 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing8
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�2 ������֧է� �٧� ' + str(price_own_housing8) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                else:
                                    return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                            else:
                                return ', �� �ӧѧ� ��ا� �֧��� �է��! �9�5'
                        elif int(id_own) == 9:
                            if own_housing == 0:
                                if price_own_housing9 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing9
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�2 ����� �ߧ� ����ާѧӧ�է� �٧� ' + str(price_own_housing9) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                else:
                                    return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                            else:
                                return ', �� �ӧѧ� ��ا� �֧��� �է��! �9�5'
                        elif int(id_own) == 10:
                            if own_housing == 0:
                                if price_own_housing10 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing10
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�2 ���ڧݧݧ� �ߧ� ����ާѧӧ�է� �٧� ' + str(price_own_housing10) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                else:
                                    return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                            else:
                                return ', �� �ӧѧ� ��ا� �֧��� �է��! �9�5'
                        elif int(id_own) == 11:
                            if own_housing == 0:
                                if price_own_housing11 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing11
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�2 ���ڧ�ߧ�� ������� �٧� ' + str(price_own_housing11) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                else:
                                    return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                            else:
                                return ', �� �ӧѧ� ��ا� �֧��� �է��! �9�5'
                        else:
                            return ', �է�ާ� �� ��ѧܧڧ� ID �ߧ� ����֧��ӧ�֧�! �9�6'
                    else:
                        return ', ��ڧާӧ�ݧ� �� �ҧ�ܧӧ� �٧ѧ��֧�֧ߧ�! �9�6'

                elif sourceText.split()[1].lower() in ['�ާѧ�ڧߧ�', '�ާѧ�ڧߧ�']:
                    own_car = int(get_data['own_car'])
                    own_housing = int(get_data['own_housing'])
                    if own_housing >= 1 or own_housing != 30:
                        price_own_car1 = 125000
                        price_own_car2 = 255000
                        price_own_car3 = 525000
                        price_own_car4 = 1275000
                        price_own_car5 = 1650000
                        price_own_car6 = 2000000
                        price_own_car7 = 4350000
                        price_own_car8 = 15650000
                        price_own_car9 = 25735000
                        price_own_car10 = 30800000
                        price_own_car11 = 37580000
                        price_own_car12 = 57999999
                        price_own_car13 = 108555000
                        price_own_car14 = 999999999
                        price_own_car15 = 1500000000

                        if id_own.isdigit():
                            if int(id_own) == 1:
                                if own_car == 0:
                                    if price_own_car1 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car1
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�7 ���֧ݧ��ڧ�֧� �٧� ' + str(price_own_car1) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ާѧ�ڧߧ�! �9�5'
                            elif int(id_own) == 2:
                                if own_car == 0:
                                    if price_own_car2 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car2
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�7 ���ڧ���ܧ��֧� �٧� ' + str(price_own_car2) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ާѧ�ڧߧ�! �9�5'

                            elif int(id_own) == 3:
                                if own_car == 0:
                                    if price_own_car3 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car3
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�3 Ducati Scrambler �٧� ' + str(price_own_car3) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ާѧ�ڧߧ�! �9�5'
                            elif int(id_own) == 4:
                                if own_car == 0:
                                    if price_own_car4 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car4
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�3 Honda CTX1300 �٧� ' + str(price_own_car4) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ާѧ�ڧߧ�! �9�5'

                            elif int(id_own) == 5:
                                if own_car == 0:
                                    if price_own_car5 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car5
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�7 Ferrari California front �٧� ' + str(price_own_car5) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ާѧ�ڧߧ�! �9�5'
                            elif int(id_own) == 6:
                                if own_car == 0:
                                    if price_own_car6 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car6
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�7 Porsche 911 �٧� ' + str(price_own_car6) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ާѧ�ڧߧ�! �9�5'
                            elif int(id_own) == 7:
                                if own_car == 0:
                                    if price_own_car7 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car7
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�7 Nissan GT-R �٧� ' + str(price_own_car7) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ާѧ�ڧߧ�! �9�5'
                            elif int(id_own) == 8:
                                if own_car == 0:
                                    if price_own_car8 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car8
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�7 BMW X6 �٧� ' + str(price_own_car8) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ާѧ�ڧߧ�! �9�5'
                            elif int(id_own) == 9:
                                if own_car == 0:
                                    if price_own_car9 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car9
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�7 Jaguar F-Type �٧� ' + str(price_own_car9) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ާѧ�ڧߧ�! �9�5'
                            elif int(id_own) == 10:
                                if own_car == 0:
                                    if price_own_car10 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car10
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�7 Lamborghini Hurac��n �٧� ' + str(price_own_car10) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ާѧ�ڧߧ�! �9�5'
                            elif int(id_own) == 11:
                                if own_car == 0:
                                    if price_own_car11 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car11
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�7 Lamborghini Gallardo �٧� ' + str(price_own_car11) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ާѧ�ڧߧ�! �9�5'
                            elif int(id_own) == 12:
                                if own_car == 0:
                                    if price_own_car12 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car12
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�7 Ferrari F80 Concept �٧� ' + str(price_own_car12) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ާѧ�ڧߧ�! �9�5'
                            elif int(id_own) == 13:
                                if own_car == 0:
                                    if price_own_car13 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car13
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�7 Lamborghini Sesto �٧� ' + str(price_own_car13) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ާѧ�ڧߧ�! �9�5'
                            elif int(id_own) == 14:
                                if own_car == 0:
                                    if price_own_car14 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car14
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�7 Various Ford-based trucks �٧� ' + str(price_own_car14) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ާѧ�ڧߧ�! �9�5'
                            elif int(id_own) == 15:
                                if own_car == 0:
                                    if price_own_car15 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car15
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�7 Tesla Cybertruck �٧� ' + str(price_own_car15) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ާѧ�ڧߧ�! �9�5'
                            else:
                                return ', �ާѧ�ڧߧ� �� ��ѧܧڧ� ID �ߧ� ����֧��ӧ�֧�! �9�6'
                        else:
                            return ', ��ڧާӧ�ݧ� �� �ҧ�ܧӧ� �٧ѧ��֧�֧ߧ�! �9�6'
                    else:
                        return ', �էݧ� ���ܧ��ܧ� ���ѧߧ������ �ߧ֧�ҧ��էڧާ� �է��! �9�5'
                elif sourceText.split()[1].lower() in ['�����', '�����']:
                    own_housing = int(get_data['own_housing'])
                    if own_housing >= 1 or own_housing != 30:
                        own_yacht = int(get_data['own_yacht'])
                        price_own_yacht1 = 575000
                        price_own_yacht2 = 1225000
                        price_own_yacht3 = 2500000
                        price_own_yacht4 = 3650000
                        price_own_yacht5 = 8355000
                        price_own_yacht6 = 12850000
                        price_own_yacht7 = 23125000
                        price_own_yacht8 = 34666000
                        price_own_yacht9 = 66225000
                        price_own_yacht10 = 96000000
                        price_own_yacht11 = 126650000
                        price_own_yacht12 = 527777777
                        price_own_yacht13 = 999999999
                        price_own_yacht14 = 1255000000

                        if id_own.isdigit():
                            if int(id_own) == 1:
                                if own_yacht == 0:
                                    if price_own_yacht1 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht1
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�5 RHIB �٧� ' + str(price_own_yacht1) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �����! �9�5'
                            elif int(id_own) == 2:
                                if own_yacht == 0:
                                    if price_own_yacht2 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht2
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�5 Kawasaki �٧� ' + str(price_own_yacht2) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �����! �9�5'

                            elif int(id_own) == 3:
                                if own_yacht == 0:
                                    if price_own_yacht3 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht3
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�5 Riva Aquarama �٧� ' + str(price_own_yacht3) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �����! �9�5'
                            elif int(id_own) == 4:
                                if own_yacht == 0:
                                    if price_own_yacht4 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht4
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�5 Various �٧� ' + str(price_own_yacht4) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �����! �9�5'

                            elif int(id_own) == 5:
                                if own_yacht == 0:
                                    if price_own_yacht5 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht5
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�5 ��rin���ss 60 �٧� ' + str(price_own_yacht5) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �����! �9�5'
                            elif int(id_own) == 6:
                                if own_yacht == 0:
                                    if price_own_yacht6 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht6
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�5 ��zimut 70 �٧� ' + str(price_own_yacht6) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �����! �9�5'
                            elif int(id_own) == 7:
                                if own_yacht == 0:
                                    if price_own_yacht7 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht7
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�5 D��min��t��r 40M �٧� ' + str(price_own_yacht7) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �����! �9�5'
                            elif int(id_own) == 8:
                                if own_yacht == 0:
                                    if price_own_yacht8 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht8
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�5 M���n��n 124 �٧� ' + str(price_own_yacht8) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �����! �9�5'
                            elif int(id_own) == 9:
                                if own_yacht == 0:
                                    if price_own_yacht9 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht9
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�5 Wid��r 150 �٧� ' + str(price_own_yacht9) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �����! �9�5'
                            elif int(id_own) == 10:
                                if own_yacht == 0:
                                    if price_own_yacht10 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht10
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�5 Palmer J��hns��n 42M Su���rS���rt �٧� ' + str(
                                            price_own_yacht10) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �����! �9�5'
                            elif int(id_own) == 11:
                                if own_yacht == 0:
                                    if price_own_yacht11 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht11
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�5 Wid��r 165 �٧� ' + str(price_own_yacht11) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �����! �9�5'
                            elif int(id_own) == 12:
                                if own_yacht == 0:
                                    if price_own_yacht12 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht12
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�5 ����li��s�� �٧� ' + str(price_own_yacht12) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �����! �9�5'
                            elif int(id_own) == 13:
                                if own_yacht == 0:
                                    if price_own_yacht13 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht13
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�5 Dub��i �٧� ' + str(price_own_yacht13) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �����! �9�5'
                            elif int(id_own) == 14:
                                if own_yacht == 0:
                                    if price_own_yacht14 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht14
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�5 Str�֧�ts ��f M��n�ѧ�� �٧� ' + str(price_own_yacht14) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �����! �9�5'
                            else:
                                return ', ����� �� ��ѧܧڧ� ID �ߧ� ����֧��ӧ�֧�! �9�6'
                        else:
                            return ', ��ڧާӧ�ݧ� �� �ҧ�ܧӧ� �٧ѧ��֧�֧ߧ�! �9�6'
                    else:
                        return ', �էݧ� ���ܧ��ܧ� ���ѧߧ������ �ߧ֧�ҧ��էڧ� �է��! �9�5'
                elif sourceText.split()[1].lower() in ['��ѧާ�ݧק�', '��ѧާ�ݧ֧�', '��ѧާ�ݧק��', '��ѧާ�ݧ֧��']:
                    own_housing = int(get_data['own_housing'])
                    if own_housing >= 1 or own_housing != 30:
                        own_air = int(get_data['own_air'])
                        price_own_air1 = 500000
                        price_own_air2 = 3995000
                        price_own_air3 = 6350000
                        price_own_air4 = 15500000
                        price_own_air5 = 17800000
                        price_own_air6 = 22250000
                        price_own_air7 = 43000000
                        price_own_air8 = 65505000
                        price_own_air9 = 75985000
                        price_own_air10 = 86495000
                        price_own_air11 = 109999999
                        price_own_air12 = 313000000
                        price_own_air13 = 617555000
                        price_own_air14 = 850000000
                        price_own_air15 = 2000000000

                        if id_own.isdigit():
                            if int(id_own) == 1:
                                if own_air == 0:
                                    if price_own_air1 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air1
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �7�6 de Havilland Canada DHC-2 �٧� ' + str(price_own_air1) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� ��ѧާ�ݧק�! �9�5'
                            elif int(id_own) == 2:
                                if own_air == 0:
                                    if price_own_air2 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air2
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �7�6 Piper PA-46 �٧� ' + str(price_own_air2) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� ��ѧާ�ݧק�! �9�5'

                            elif int(id_own) == 3:
                                if own_air == 0:
                                    if price_own_air3 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air3
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �7�6 Cessna 310 �٧� ' + str(price_own_air3) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� ��ѧާ�ݧק�! �9�5'
                            elif int(id_own) == 4:
                                if own_air == 0:
                                    if price_own_air4 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air4
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �7�6 Learjet 55 �٧� ' + str(price_own_air4) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� ��ѧާ�ݧק�! �9�5'

                            elif int(id_own) == 5:
                                if own_air == 0:
                                    if price_own_air5 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air5
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �7�6 Bombardier Global Express �٧� ' + str(price_own_air5) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� ��ѧާ�ݧק�! �9�5'
                            elif int(id_own) == 6:
                                if own_air == 0:
                                    if price_own_air6 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air6
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �7�6 Cessna Citation X �٧� ' + str(price_own_air6) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� ��ѧާ�ݧק�! �9�5'
                            elif int(id_own) == 7:
                                if own_air == 0:
                                    if price_own_air7 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air7
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �7�6 C-130 �٧� ' + str(price_own_air7) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� ��ѧާ�ݧק�! �9�5'
                            elif int(id_own) == 8:
                                if own_air == 0:
                                    if price_own_air8 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air8
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �7�6 VOLATOL �٧� ' + str(price_own_air8) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� ��ѧާ�ݧק�! �9�5'
                            elif int(id_own) == 9:
                                if own_air == 0:
                                    if price_own_air9 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air9
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �7�6 RM-10 BOMBUSHKA �٧� ' + str(
                                            price_own_air9) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� ��ѧާ�ݧק�! �9�5'
                            elif int(id_own) == 10:
                                if own_air == 0:
                                    if price_own_air10 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air10
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �7�6 AVENGER �� HYV �٧� ' + str(price_own_air10) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� ��ѧާ�ݧק�! �9�5'
                            elif int(id_own) == 11:
                                if own_air == 0:
                                    if price_own_air11 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air11
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �7�6 F-16 Fighting Falcon �٧� ' + str(price_own_air11) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� ��ѧާ�ݧק�! �9�5'
                            elif int(id_own) == 12:
                                if own_air == 0:
                                    if price_own_air12 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air12
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �7�6 RM-10 BOMBUSHKA �٧� ' + str(price_own_air12) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� ��ѧާ�ݧק�! �9�5'
                            elif int(id_own) == 13:
                                if own_air == 0:
                                    if price_own_air13 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air13
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �7�6 TULA �� MAMMOTH �٧� ' + str(price_own_air13) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� ��ѧާ�ݧק�! �9�5'
                            elif int(id_own) == 14:
                                if own_air == 0:
                                    if price_own_air14 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air14
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �7�6 V-65 MOLOTOK �٧� ' + str(price_own_air14) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� ��ѧާ�ݧק�! �9�5'
                            elif int(id_own) == 15:
                                if own_air == 0:
                                    if price_own_air15 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air15
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �7�6 MOGUL �� MAMMOTH �٧� ' + str(price_own_air15) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� ��ѧާ�ݧק�! �9�5'
                            else:
                                return ', ��ѧާ�ݧק�� �� ��ѧܧڧ� ID �ߧ� ����֧��ӧ�֧�! �9�6'
                        else:
                            return ', ��ڧާӧ�ݧ� �� �ҧ�ܧӧ� �٧ѧ��֧�֧ߧ�! �9�6'
                    else:
                        return ', �էݧ� ���ܧ��ܧ� ���ѧߧ������ �ߧ֧�ҧ��էڧ� �է��! �9�5'
                elif sourceText.split()[1].lower() in ['�ӧ֧���ݧק�', '�ӧ֧���ݧ֧�', '�ӧ֧���ݧק��', '�ӧ֧���ݧ֧��']:
                    own_housing = int(get_data['own_housing'])
                    if own_housing >= 1 or own_housing != 30:
                        own_helicopter = int(get_data['own_helicopter'])
                        price_own_helicopter1 = 1300000
                        price_own_helicopter2 = 1750000
                        price_own_helicopter3 = 2225000
                        price_own_helicopter4 = 3500000
                        price_own_helicopter5 = 8850000
                        price_own_helicopter6 = 25555555
                        price_own_helicopter7 = 58000000
                        price_own_helicopter8 = 215000000
                        price_own_helicopter9 = 525000000

                        if id_own.isdigit():
                            if int(id_own) == 1:
                                if own_helicopter == 0:
                                    if price_own_helicopter1 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter1
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�5 Eurocopter EC130/135/14 �٧� ' + str(price_own_helicopter1) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ӧ֧���ݧק�! �9�5'
                            elif int(id_own) == 2:
                                if own_helicopter == 0:
                                    if price_own_helicopter2 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter2
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�5 Boeing MH-6 �٧� ' + str(price_own_helicopter2) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ӧ֧���ݧק�! �9�5'

                            elif int(id_own) == 3:
                                if own_helicopter == 0:
                                    if price_own_helicopter3 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter3
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�5 Sikorsky UH-60 �٧� ' + str(price_own_helicopter3) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ӧ֧���ݧק�! �9�5'
                            elif int(id_own) == 4:
                                if own_helicopter == 0:
                                    if price_own_helicopter4 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter4
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�5 HAVOK �� NAGASAKI �٧� ' + str(price_own_helicopter4) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ӧ֧���ݧק�! �9�5'

                            elif int(id_own) == 5:
                                if own_helicopter == 0:
                                    if price_own_helicopter5 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter5
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�5 Eurocopter EC145 �٧� ' + str(price_own_helicopter5) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ӧ֧���ݧק�! �9�5'
                            elif int(id_own) == 6:
                                if own_helicopter == 0:
                                    if price_own_helicopter6 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter6
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�5 Airbus H160 �٧� ' + str(price_own_helicopter6) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ӧ֧���ݧק�! �9�5'
                            elif int(id_own) == 7:
                                if own_helicopter == 0:
                                    if price_own_helicopter7 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter7
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�5 Mil Mi-24 �٧� ' + str(price_own_helicopter7) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ӧ֧���ݧק�! �9�5'
                            elif int(id_own) == 8:
                                if own_helicopter == 0:
                                    if price_own_helicopter8 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter8
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�5 POLICE MAVERICK �٧� ' + str(price_own_helicopter8) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ӧ֧���ݧק�! �9�5'
                            elif int(id_own) == 9:
                                if own_helicopter == 0:
                                    if price_own_helicopter9 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter9
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �0�5 MAVERICK �٧� ' + str(price_own_helicopter9) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� �ӧ֧���ݧק�! �9�5'
                            else:
                                return ', �ӧ֧���ݧק�� �� ��ѧܧڧ� ID �ߧ� ����֧��ӧ�֧�! �9�6'
                        else:
                            return ', ��ڧާӧ�ݧ� �� �ҧ�ܧӧ� �٧ѧ��֧�֧ߧ�! �9�6'
                    else:
                        return ', �էݧ� ���ܧ��ܧ� ���ѧߧ������ �ߧ֧�ҧ��էڧ� �է��! �9�5'
                elif sourceText.split()[1].lower() in ['��֧�ާ�', '��֧�ާ�']:
                    own_farm = int(get_data['own_farm'])
                    own_housing = int(get_data['own_housing'])
                    price_own_farm1 = 500000
                    price_own_farm2 = 5000000
                    price_own_farm3 = 500000000
                    if own_housing >= 1 or own_housing == 30:
                        if id_own.isdigit():
                            if int(id_own) == 1:
                                if own_farm == 0:
                                    if price_own_farm1 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_farm1
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_farm": '{}'.format(id_own)})
                                        get_data.update({"farm_profit": '{}'.format(5)})
                                        get_data.update({"farm_time": '{}'.format(time.time())})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�1 Miner �٧� ' + str(price_own_farm1) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� ��֧�ާ�! �9�5'
                            elif int(id_own) == 2:
                                if own_farm == 0:
                                    if price_own_farm2 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_farm2
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_farm": '{}'.format(id_own)})
                                        get_data.update({"farm_profit": '{}'.format(50)})
                                        get_data.update({"farm_time": '{}'.format(time.time())})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�1 Miner S �٧� ' + str(price_own_farm2) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� ��֧�ާ�! �9�5'

                            elif int(id_own) == 3:
                                if own_farm == 0:
                                    if price_own_farm3 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_farm3
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_farm": '{}'.format(id_own)})
                                        get_data.update({"farm_profit": '{}'.format(1000)})
                                        get_data.update({"farm_time": '{}'.format(time.time())})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�1 Miner X �٧� ' + str(price_own_farm3) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� ��֧�ާ�! �9�5'
                            else:
                                return ', ��֧�ާ� �� ��ѧܧڧ� ID �ߧ� ����֧��ӧ�֧�! �9�6'
                        else:
                            return ', ��ڧާӧ�ݧ� �� �ҧ�ܧӧ� �٧ѧ��֧�֧ߧ�! �9�6'
                    else:
                        return ', �էݧ� ���ܧ��ܧ� ��֧�ާ� �ߧ֧�ҧ��էڧ� �է��! �9�5'
                elif sourceText.split()[1].lower() in ['�ܧ�ާ�', '�ܧ�ާ����֧�', '�ߧ���', '�ߧ���ҧ��', '�ܧ�ާ��','�ܧ�ާ����֧��', '�ߧ����', '�ߧ���ҧ�ܧ�']:
                    own_comp = int(get_data['own_comp'])
                    price_own_comp1 = 35000000
                    price_own_comp2 = 45000000
                    price_own_comp3 = 150000000

                    if id_own.isdigit():
                        if int(id_own) == 1:
                            if own_comp == 0:
                                if price_own_comp1 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_comp1
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_comp": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�5 Book �٧� ' + str(price_own_comp1) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                else:
                                    return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                            else:
                                return ', �� �ӧѧ� ��ا� �֧��� �ܧ�ާ����֧�! �9�5'
                        elif int(id_own) == 2:
                            if own_comp == 0:
                                if price_own_comp2 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_comp2
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_comp": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�5 Book Air �٧� ' + str(price_own_comp2) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                else:
                                    return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                            else:
                                return ', �� �ӧѧ� ��ا� �֧��� �ܧ�ާ����֧�! �9�5'

                        elif int(id_own) == 3:
                            if own_comp == 0:
                                if price_own_comp3 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_comp3
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_comp": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�5 Book Pro �٧� ' + str(price_own_comp3) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                else:
                                    return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                            else:
                                return ', �� �ӧѧ� ��ا� �֧��� �ܧ�ާ����֧�! �9�5'
                        else:
                            return ', �ܧ�ާ����֧�� �� ��ѧܧڧ� ID �ߧ� ����֧��ӧ�֧�! �9�6'
                    else:
                        return ', ��ڧާӧ�ݧ� �� �ҧ�ܧӧ� �٧ѧ��֧�֧ߧ�! �9�6'
                elif sourceText.split()[1].lower() in ['��֧ݧ֧���', '��ާѧ�����', '��֧ݧ֧��ߧ�', '��ާѧ����ߧ�']:
                    own_smart = int(get_data['own_smart'])
                    price_own_smart1 = 25800000
                    price_own_smart2 = 30000000
                    price_own_smart3 = 35250000

                    if id_own.isdigit():
                        if int(id_own) == 1:
                            if own_smart == 0:
                                if price_own_smart1 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_smart1
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_smart": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�5 iPhone �٧� ' + str(price_own_smart1) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                else:
                                    return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                            else:
                                return ', �� �ӧѧ� ��ا� �֧��� ��ާѧ�����! �9�5'
                        elif int(id_own) == 2:
                            if own_smart == 0:
                                if price_own_smart2 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_smart2
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_smart": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�5 iPhone Pro �٧� ' + str(price_own_smart2) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                else:
                                    return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                            else:
                                return ', �� �ӧѧ� ��ا� �֧��� ��ާѧ�����! �9�5'

                        elif int(id_own) == 3:
                            if own_smart == 0:
                                if price_own_smart3 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_smart3
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_smart": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�5 iPhone Pro Max �٧� ' + str(price_own_smart3) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                else:
                                    return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                            else:
                                return ', �� �ӧѧ� ��ا� �֧��� ��ާѧ�����! �9�5'
                        else:
                            return ', ��ާѧ����ߧ� �� ��ѧܧڧ� ID �ߧ� ����֧��ӧ�֧�! �9�6'
                    elif sourceText.split()[1].lower() in ['��֧ݧ֧���', '��ާѧ�����', '��֧ݧ֧��ߧ�', '��ާѧ����ߧ�']:
                        own_smart = int(get_data['own_smart'])
                        price_own_smart1 = 800000
                        price_own_smart2 = 1000000
                        price_own_smart3 = 1250000

                        if id_own.isdigit():
                            if int(id_own) == 1:
                                if own_smart == 0:
                                    if price_own_smart1 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_smart1
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_smart": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�5 iPhone �٧� ' + str(
                                            price_own_smart1) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� ��ާѧ�����! �9�5'
                            elif int(id_own) == 2:
                                if own_smart == 0:
                                    if price_own_smart2 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_smart2
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_smart": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�5 iPhone Pro �٧� ' + str(
                                            price_own_smart2) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� ��ާѧ�����! �9�5'

                            elif int(id_own) == 3:
                                if own_smart == 0:
                                    if price_own_smart3 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_smart3
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_smart": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', �ӧ� ����֧�ߧ� ���֧�ҧ�֧ݧ� - �9�5 iPhone Pro Max �٧� ' + str(
                                            price_own_smart3) + '��!\n�9�0 ���ѧ� �ҧѧݧѧߧ�: ' + str(algo_buy_own) + '��'
                                    else:
                                        return ', �� �ӧѧ� �ߧ֧է���ѧ���ߧ� �է֧ߧ֧�! �9�6'
                                else:
                                    return ', �� �ӧѧ� ��ا� �֧��� ��ާѧ�����! �9�5'
                            else:
                                return ', ��ާѧ����ߧ� �� ��ѧܧڧ� ID �ߧ� ����֧��ӧ�֧�! �9�6'
                    else:
                        return ', ��ڧާӧ�ݧ� �� �ҧ�ܧӧ� �٧ѧ��֧�֧ߧ�! �9�6'
                else:
                    return ', ��ѧܧ�� �ܧѧ�֧ԧ��ڧ� �ߧ� ����֧��ӧ�֧�! �9�6'
            else:
                return shopHelp
        else:
            return None
    pass