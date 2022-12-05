import vk_api
import random
import json
import os
import re
import math

users_dir = os.path.join(r"users/")

def loadjson(filepath):
    with open(filepath, 'r', encoding='utf-8') as jsonfile:
        return json.load(jsonfile, encoding='utf-8')

def dumpjson(data, filepath):
    with open(filepath, 'w', encoding='utf-8') as jsonfile:
        return json.dump(data, jsonfile, ensure_ascii=False)

#����ߧ�ӧߧѧ� �ԧ�����
get_data = loadjson("conf.json")
token = str(get_data['token'])

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()

def check_casino_win(user_id):
    read_file = open(users_dir + str(user_id) + ".json", "r", encoding='utf-8')
    get_data = json.load(read_file, encoding='utf-8')
    read_file.close()
    donate_group = get_data['group']
    chance = math.ceil(random.randint(1, 100) / 33.0000)
    if donate_group == 'VIP':
        pass_count = 1
        while chance != 1 and pass_count:
            chance = math.ceil(random.randint(1, 100) / 33.0000)
            pass_count -= 1
    elif donate_group == 'Premium':
        pass_count = 2
        while chance != 1 and pass_count:
            chance = math.ceil(random.randint(1, 100) / 33.0000)
            pass_count -= 1
    else:
        pass_count = 0
        while chance != 1 and pass_count:
            chance = math.ceil(random.randint(1, 100) / 33.0000)
            pass_count -= 1
    return chance

def check_word_monetka(word):
    if str(word) == '���ק�':
        return 1
    elif str(word) == '���֧�':
        return 1
    elif str(word) == '��֧�ܧ�':
        return 2

def check_word_traid(word):
    if str(word) == '�ӧӧ֧��':
        return 1
    elif str(word) == '�ӧߧڧ�':
        return 2

def convert_win_monetka(chislo_rand):
    if int(chislo_rand) == 1:
        return '�����ѧ�: ����֧�'
    elif int(chislo_rand) == 2:
        return '�����ѧݧ�: ���֧�ܧ�'

def ruda_price_salem(col_ruda, price_ruda):
    if col_ruda > 1:
        algo = col_ruda * price_ruda
        return algo
    else:
        return 0

def check_group(id):
    get_data = loadjson(users_dir + str(id) + ".json")
    donate_group = get_data['group']
    if get_data['group'] == 'Player':
        donate_group = '�9�8 ����ڧӧڧݧ֧ԧڧ�: ���ԧ���'
    elif get_data['group'] == 'VIP':
        donate_group = '�7�8 ����ڧӧڧݧ֧ԧڧ�: ������'
    elif get_data['group'] == 'Premium':
        donate_group = '�9�9 ����ڧӧڧݧ֧ԧڧ�: ����֧ާڧ��'
    return donate_group

def check_nick(id):
    get_data = loadjson(users_dir + str(id) + ".json")
    user_nick = get_data['user_nick']
    if get_data['user_nick'] == 'None':
        user_nick = '���� ����ѧߧ�ӧݧ֧�'
        return user_nick
    else:
        return user_nick

def check_own_housing(own_housing):
    if own_housing == 0:
        return ''
    elif own_housing == 1:
        return '�7�4�7�4�9�2 ������ҧܧ�\n'
    elif own_housing == 2:
        return '�7�4�7�4�9�2 ����էӧѧ�\n'
    elif own_housing == 3:
        return '�7�4�7�4�9�2 ���ѧ�ѧ�\n'
    elif own_housing == 4:
        return '�7�4�7�4�9�2 ���ѧ�ѧ�\n'
    elif own_housing == 5:
        return '�7�4�7�4�9�2 ���֧��ѧ� ��ڧاڧߧ�\n'
    elif own_housing == 6:
        return '�7�4�7�4�9�2 ���֧�֧ӧ�ߧߧ�� �է�ާ�\n'
    elif own_housing == 7:
        return '�7�4�7�4�9�2 ���ڧ��ڧ�ߧ�� �է��\n'
    elif own_housing == 8:
        return '�7�4�7�4�9�2 ������֧է�\n'
    elif own_housing == 9:
        return '�7�4�7�4�9�2 ����� �ߧ� ����ާѧӧ�է�\n'
    elif own_housing == 10:
        return '�7�4�7�4�9�2 ���ڧݧݧ� �ߧ� ����ާѧӧ�է�\n'
    elif own_housing == 11:
        return '�7�4�7�4�9�2 ���ڧ�ߧ�� �������\n'
    elif own_housing == 30:
        return '�7�4�7�4�9�2 ���֧ܧ�֧�ߧ�� �اڧݧ��\n'

def check_own_car(own_car):
    if own_car == 0:
        return ''
    elif own_car == 1:
        return '�7�4�7�4�0�7 ���֧ݧ��ڧ�֧�\n'
    elif own_car == 2:
        return '�7�4�7�4�0�7 ���ڧ���ܧ��֧�\n'
    elif own_car == 3:
        return '�7�4�7�4�9�3 Ducati Scrambler\n'
    elif own_car == 4:
        return '�7�4�7�4�9�3 Honda CTX1300\n'
    elif own_car == 5:
        return '�7�4�7�4�0�7 Ferrari California front\n'
    elif own_car == 6:
        return '�7�4�7�4�0�7 Porsche 911\n'
    elif own_car == 7:
        return '�7�4�7�4�0�7 Nissan GT-R\n'
    elif own_car == 8:
        return '�7�4�7�4�0�7 BMW X6\n'
    elif own_car == 9:
        return '�7�4�7�4�0�7 Jaguar F-Type\n'
    elif own_car == 10:
        return '�7�4�7�4�0�7 Lamborghini Hurac��n\n'
    elif own_car == 11:
        return '�7�4�7�4�0�7 Lamborghini Gallardo\n'
    elif own_car == 12:
        return '�7�4�7�4�0�7 Ferrari F80 Concept\n'
    elif own_car == 13:
        return '�7�4�7�4�0�7 Lamborghini Sesto\n'
    elif own_car == 14:
        return '�7�4�7�4�0�7 Various Ford-based trucks\n'
    elif own_car == 15:
        return '�7�4�7�4�0�7 Tesla Cybertruck\n'
    elif own_car == 30:
        return '�7�4�7�4�0�7 ���֧ܧ�֧�ߧѧ� �ާѧ�ڧߧ�\n'

def check_own_yacht(own_yacht):
    if own_yacht == 0:
        return ''
    elif own_yacht == 1:
        return '�7�4�7�4�0�5 RHIB\n'
    elif own_yacht == 2:
        return '�7�4�7�4�0�5 Kawasaki\n'
    elif own_yacht == 3:
        return '�7�4�7�4�0�5 Riva Aquarama\n'
    elif own_yacht == 4:
        return '�7�4�7�4�0�5 Various\n'
    elif own_yacht == 5:
        return '�7�4�7�4�0�5 ��rin���ss 60\n'
    elif own_yacht == 6:
        return '�7�4�7�4�0�5 ��zimut 70\n'
    elif own_yacht == 7:
        return '�7�4�7�4�0�5 D��min��t��r 40M\n'
    elif own_yacht == 8:
        return '�7�4�7�4�0�5 M���n��n 124\n'
    elif own_yacht == 9:
        return '�7�4�7�4�0�5 Wid��r 150\n'
    elif own_yacht == 10:
        return '�7�4�7�4�0�5 Palmer J��hns��n 42M Su���rS���rt\n'
    elif own_yacht == 11:
        return '�7�4�7�4�0�5 Wid��r 165\n'
    elif own_yacht == 12:
        return '�7�4�7�4�0�5 ����li��s��\n'
    elif own_yacht == 13:
        return '�7�4�7�4�0�5 Dub��i\n'
    elif own_yacht == 14:
        return '�7�4�7�4�0�5 Str�֧�ts ��f M��n�ѧ��\n'
    elif own_yacht == 30:
        return '�7�4�7�4�0�5 ���֧ܧ�֧�ߧѧ� �����\n'

def check_own_air(own_air):
    if own_air == 0:
        return ''
    elif own_air == 1:
        return '�7�4�7�4�7�6 de Havilland Canada DHC-2\n'
    elif own_air == 2:
        return '�7�4�7�4�7�6 Piper PA-46\n'
    elif own_air == 3:
        return '�7�4�7�4�7�6 Cessna 310\n'
    elif own_air == 4:
        return '�7�4�7�4�7�6 Learjet 55\n'
    elif own_air == 5:
        return '�7�4�7�4�7�6 Bombardier Global Express\n'
    elif own_air == 6:
        return '�7�4�7�4�7�6 Cessna Citation X\n'
    elif own_air == 7:
        return '�7�4�7�4�7�6 C-130\n'
    elif own_air == 8:
        return '�7�4�7�4�7�6 VOLATOL\n'
    elif own_air == 9:
        return '�7�4�7�4�7�6 RM-10 BOMBUSHKA\n'
    elif own_air == 10:
        return '�7�4�7�4�7�6 AVENGER �� HYV\n'
    elif own_air == 11:
        return '�7�4�7�4�7�6 F-16 Fighting Falcon\n'
    elif own_air == 12:
        return '�7�4�7�4�7�6 RM-10 BOMBUSHKA\n'
    elif own_air == 13:
        return '�7�4�7�4�7�6 TULA �� MAMMOTH\n'
    elif own_air == 14:
        return '�7�4�7�4�7�6 V-65 MOLOTOK\n'
    elif own_air == 15:
        return '�7�4�7�4�7�6 MOGUL �� MAMMOTH\n'
    elif own_air == 30:
        return '�7�4�7�4�7�6 ���֧ܧ�֧�ߧ�� ��ѧާ�ݧק�\n'

def check_own_helicopter(own_helicopter):
    if own_helicopter == 0:
        return ''
    elif own_helicopter == 1:
        return '�7�4�7�4�0�5 Eurocopter EC130/135/14\n'
    elif own_helicopter == 2:
        return '�7�4�7�4�0�5 Boeing MH-6\n'
    elif own_helicopter == 3:
        return '�7�4�7�4�0�5 Sikorsky UH-60\n'
    elif own_helicopter == 4:
        return '�7�4�7�4�0�5 HAVOK �� NAGASAKI\n'
    elif own_helicopter == 5:
        return '�7�4�7�4�0�5 Eurocopter EC145\n'
    elif own_helicopter == 6:
        return '�7�4�7�4�0�5 Airbus H160\n'
    elif own_helicopter == 7:
        return '�7�4�7�4�0�5 Mil Mi-24\n'
    elif own_helicopter == 8:
        return '�7�4�7�4�0�5 POLICE MAVERICK\n'
    elif own_helicopter == 9:
        return '�7�4�7�4�0�5 MAVERICK\n'
    elif own_helicopter == 30:
        return '�7�4�7�4�0�5 ���֧ܧ�֧�ߧ�� �ӧ֧���ݧק�\n'

def check_own_comp(own_comp):
    if own_comp == 0:
        return ''
    elif own_comp == 1:
        return '�7�4�7�4�9�5 Book\n'
    elif own_comp == 2:
        return '�7�4�7�4�9�5 Book Air\n'
    elif own_comp == 3:
        return '�7�4�7�4�9�5 Book Pro\n'

def check_own_smart(own_smart):
    if own_smart == 0:
        return ''
    elif own_smart == 1:
        return '�7�4�7�4�9�5 iPhone\n'
    elif own_smart == 2:
        return '�7�4�7�4�9�5 iPhone Pro\n'
    elif own_smart == 3:
        return '�7�4�7�4�9�5 iPhone Pro Max\n'

def check_own_farm(own_farm):
    if own_farm == 0:
        return ''
    elif own_farm == 1:
        return '�7�4�7�4�9�1 Miner\n'
    elif own_farm == 2:
        return '�7�4�7�4�9�1 Miner S\n'
    elif own_farm == 3:
        return '�7�4�7�4�9�1 Miner X\n'

def check_own_profile(id):
    get_data = loadjson(users_dir + str(id) + ".json")
    own_housing = int(get_data['own_housing'])
    own_car = int(get_data['own_car'])
    own_yacht = int(get_data['own_yacht'])
    own_air = int(get_data['own_air'])
    own_helicopter = int(get_data['own_helicopter'])
    own_comp = int(get_data['own_comp'])
    own_smart = int(get_data['own_smart'])
    own_farm = int(get_data['own_farm'])
    if own_housing >= 1:
        return '\n\n�9�7 ���ާ��֧��ӧ�:\n'
    elif own_car >= 1:
        return '\n\n�9�7 ���ާ��֧��ӧ�:\n'
    elif own_yacht >= 1:
        return '\n\n�9�7 ���ާ��֧��ӧ�:\n'
    elif own_air >= 1:
        return '\n\n�9�7 ���ާ��֧��ӧ�:\n'
    elif own_helicopter >= 1:
        return '\n\n�9�7 ���ާ��֧��ӧ�:\n'
    elif own_comp >= 1:
        return '\n\n�9�7 ���ާ��֧��ӧ�:\n'
    elif own_smart >= 1:
        return '\n\n�9�7 ���ާ��֧��ӧ�:\n'
    elif own_farm >= 1:
        return '\n\n�9�7 ���ާ��֧��ӧ�:\n'
    else:
        return ''

def removeLink(text):
    try:
        text = re.sub('@', '', text)
        text = re.sub('https://vk.com/', '', text)
        text = re.sub('https://vk.com/id', '', text)
        try:
            text = re.search("id(\\d+)", text).group(1)
        except AttributeError:
            pass

        if text.isdigit():
            return text
        else:
            username = vk.utils.resolveScreenName(screen_name=text)
            if not username:
                pass
            else:
                check_type = username['type']
                if str(check_type) == 'user':
                    user_id = str(username['object_id'])
                    if user_id.isdigit():
                        return int(username['object_id'])
                    else:
                        pass
                else:
                    pass
    except vk_api.exceptions.ApiError:
        pass
    except AttributeError:
        pass

def sendMessageTOid(text, toID):
    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()
    users_dir = os.path.join(r"users/")

    read_file = open(users_dir + str(toID) + ".json", "r", encoding='utf-8')
    get_data = json.load(read_file, encoding='utf-8')
    read_file.close()
    if get_data['nick'] == '0':
        mention = '@id{}'.format(toID) + '(' + get_data['first_name'] + ')'
    elif get_data['nick'] == '1':
        mention = '@id{}'.format(toID) + '(' + get_data['user_nick'] + ')'
    else:
        mention = '@id{}'.format(toID) + '(' + get_data['first_name'] + ')'
    try:
        vk.messages.send(random_id=random.randint(-2147483648, +2147483648), peer_id=toID, message=mention + text)
    except vk_api.exceptions.ApiError:
        pass

def sendMessageTOid_attachment(text, toID, attachment):
    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()
    users_dir = os.path.join(r"users/")

    read_file = open(users_dir + str(toID) + ".json", "r", encoding='utf-8')
    get_data = json.load(read_file, encoding='utf-8')
    read_file.close()
    if get_data['nick'] == '0':
        mention = '@id{}'.format(toID) + '(' + get_data['first_name'] + ')'
    elif get_data['nick'] == '1':
        mention = '@id{}'.format(toID) + '(' + get_data['user_nick'] + ')'
    else:
        mention = '@id{}'.format(toID) + '(' + get_data['first_name'] + ')'
    try:
        vk.messages.send(random_id=random.randint(-2147483648, +2147483648), peer_id=toID, attachment=attachment, message=mention + text)
    except vk_api.exceptions.ApiError:
        pass