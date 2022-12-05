import os
from plugins import gf

users_dir = os.path.join(r"users/")

def nicks(sourceText, id):
    command = '�ߧڧ�'
    on = '�ӧܧ�'
    off = '�ӧ�ܧ�'

    get_data = gf.loadjson(users_dir + str(id) + ".json")

    if sourceText != '':
        if command == sourceText.split()[0].lower():
            if len(sourceText.split()) > 1:
                if on == sourceText.split()[1].lower():
                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                    if get_data['user_nick'] != 'None':
                        if get_data['nick'] != '1':
                            get_data = gf.loadjson(users_dir + str(id) + ".json")
                            get_data.update({"nick": "1"})
                            gf.dumpjson(get_data, users_dir + str(id) + ".json")
                            return ', ��ҧ�ѧ�֧ߧڧ� ��� �ߧڧܧ� �ӧܧݧ��֧ߧ�!'
                        return ', ��ҧ�ѧ�֧ߧڧ� ��� �ߧڧܧ� ��ا� �ҧ�ݧ� �ӧܧݧ��֧ߧ�!'
                    elif get_data['user_nick'] == 'None':
                        return ', �� �ӧѧ� �ߧ� ����ѧߧ�ӧݧ֧� �ߧڧ�!'
                    else:
                        return ', �� �ӧѧ� ��ا� ����ѧߧ�ӧݧ֧� �ߧڧ�!'

                elif off == sourceText.split()[1].lower():
                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                    if get_data['user_nick'] != 'None':
                        if get_data['nick'] != '0':
                            get_data = gf.loadjson(users_dir + str(id) + ".json")
                            get_data.update({"nick": "0"})
                            gf.dumpjson(get_data, users_dir + str(id) + ".json")
                            return ', ��ҧ�ѧ�֧ߧڧ� ��� �ߧڧܧ� �ӧ�ܧݧ��֧ߧ�!'
                        return ', ��ҧ�ѧ�֧ߧڧ� ��� �ߧڧܧ� ��ا� �ҧ�ݧ� �ӧ�ܧݧ��֧ߧ�!'
                    elif get_data['user_nick'] == 'None':
                        return ', �� �ӧѧ� �ߧ� ����ѧߧ�ӧݧ֧� �ߧڧ�!'
                    else:
                        return ', �� �ӧѧ� ��ا� ����ѧߧ�ӧݧ֧� �ߧڧ�!'

                elif sourceText.split()[1].lower() == 'None'.lower():
                    return ', ��ѧܧ�� �ߧڧ� ����ѧߧ�ӧڧ�� �ߧ֧ݧ�٧�! �0�1'

                if get_data['group'] == 'Player':
                    if len(sourceText.split()[1].lower()) <= 10:
                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                        get_data.update({"user_nick":'{}'.format(sourceText.split()[1])})
                        get_data.update({"nick": "1"})
                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                        return ', �٧ѧާ֧�ѧ�֧ݧ�ߧ�� �ߧڧ�: ' + sourceText.split()[1] + '! �9�5\n���ҧ�ѧ�֧ߧڧ� ��� �ߧڧܧ� �ӧܧݧ��֧ߧ�! �9�0'
                    else:
                        return ', �ߧڧ� ��ݧڧ�ܧ�� �էݧڧߧߧ��, �էݧ� �ӧѧ�֧� ���ڧӧڧݧ֧ԧڧ� ��ѧ٧�֧�֧ߧ� �ڧ���ݧ�٧�ӧѧ�� �ާѧܧ�ڧާ�� 10 ��ڧާ�ӧݧ��! �0�1'

                elif get_data['group'] == 'VIP':
                    if len(sourceText.split()[1].lower()) <= 15:
                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                        get_data.update({"user_nick":'{}'.format(sourceText.split()[1])})
                        get_data.update({"nick": "1"})
                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                        return ', �٧ѧާ֧�ѧ�֧ݧ�ߧ�� �ߧڧ�: ' + sourceText.split()[1] + '! �9�5\n���ҧ�ѧ�֧ߧڧ� ��� �ߧڧܧ� �ӧܧݧ��֧ߧ�! �9�0'
                    else:
                        return ', �ߧڧ� ��ݧڧ�ܧ�� �էݧڧߧߧ��, �ާѧܧ�ڧާѧݧ�ߧ� �ܧ��-�ӧ� 15 ��ڧާ�ӧݧ��! �0�1'
                        
                elif get_data['group'] == 'Premium':
                    if len(sourceText.split()[1].lower()) <= 15:
                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                        get_data.update({"user_nick":'{}'.format(sourceText.split()[1])})
                        get_data.update({"nick": "1"})
                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                        return ', �٧ѧާ֧�ѧ�֧ݧ�ߧ�� �ߧڧ�: ' + sourceText.split()[1] + '! �9�5\n���ҧ�ѧ�֧ߧڧ� ��� �ߧڧܧ� �ӧܧݧ��֧ߧ�! �9�0'
                    else:
                        return ', �ߧڧ� ��ݧڧ�ܧ�� �էݧڧߧߧ��, �ާѧܧ�ڧާѧݧ�ߧ� �ܧ��-�ӧ� 15 ��ڧާ�ӧݧ��! �0�1'

                elif get_data['group'] == 'Admin':
                    if len(sourceText.split()[1].lower()) <= 15:
                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                        get_data.update({"user_nick":'{}'.format(sourceText.split()[1])})
                        get_data.update({"nick": "1"})
                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                        return ', �٧ѧާ֧�ѧ�֧ݧ�ߧ�� �ߧڧ�: ' + sourceText.split()[1] + '! �9�5\n���ҧ�ѧ�֧ߧڧ� ��� �ߧڧܧ� �ӧܧݧ��֧ߧ�! �9�0'
                    else:
                        return ', �ߧڧ� ��ݧڧ�ܧ�� �էݧڧߧߧ��, �ާѧܧ�ڧާѧݧ�ߧ� �ܧ��-�ӧ� 15 ��ڧާ�ӧݧ��! �0�1'

                elif get_data['group'] == 'Owner':
                    if len(sourceText.split()[1].lower()) <= 20:
                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                        get_data.update({"user_nick":'{}'.format(sourceText.split()[1])})
                        get_data.update({"nick": "1"})
                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                        return ', �٧ѧާ֧�ѧ�֧ݧ�ߧ�� �ߧڧ�: ' + sourceText.split()[1] + '! �9�5\n���ҧ�ѧ�֧ߧڧ� ��� �ߧڧܧ� �ӧܧݧ��֧ߧ�! �9�0'
                    else:
                        return ', �ߧڧ� ��ݧڧ�ܧ�� �էݧڧߧߧ��, �ާѧܧ�ڧާѧݧ�ߧ� �ܧ��-�ӧ� 20 ��ڧާ�ӧݧ��! �0�1'
                elif len(sourceText.split()[1].lower()) >= 21:
                    return ', �ߧڧ� ��ݧڧ�ܧ�� �էݧڧߧߧ�� (�ާѧܧ�ڧާѧݧ�ߧѧ� �էݧڧߧ� �ߧڧܧ� 20 ��ڧާӧ�ݧ��). �7�2'
            else:
                return ', �ܧ�ާѧߧէ� �ߧڧ� ���٧ӧ�ݧ�֧� ����ѧߧ�ӧڧ�� ��ӧ�� ���ҧ��ӧ֧ߧߧ�� ��ҧ�ѧ�֧ߧڧ� �ҧ��� �� �ӧѧ�, �ߧѧ��ڧާ֧� ��� ���֧ӧէ�ߧڧާ�!\n�9�2 ������ݧ�٧�ӧѧߧڧ�: �0�0�ߧڧ� [�ӧܧ�/�ӧ�ܧ�/�ӧѧ� �ߧڧ�]�0�3  '
        else:
            return None
    return None