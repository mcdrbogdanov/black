# -*- coding: utf8 -*-
import os, json, requests, random, re
from plugins import gf
from modules import pluginMg
from vkbottle import Bot, Message, keyboard_gen, types
from vkbottle.keyboard import Keyboard, Text

#����ߧ�ӧߧѧ� �ԧ�����
get_data = gf.loadjson("conf.json")
token = str(get_data['token'])

bot = Bot(token=token)
users_dir = os.path.join(r"users/")

# ���֧ߧ֧�ѧ�ڧ�/���ҧߧ�ӧݧ֧ߧڧ� �ܧ�����
file = open("curs.json", "w", encoding='utf-8')
cursList = {"coin": '{}'.format(random.randint(5500, 9500))}
json.dump(cursList, file, ensure_ascii=False)
file.close()

@bot.on.message()
async def wrapper(ans: Message):
    check_profile = os.path.exists(users_dir + str(ans.from_id) + ".json")
    if check_profile == True:
        pass
    else:
        data = await bot.api.users.get(user_ids=ans.from_id)
        first_name = data[0]['first_name']
        last_name = data[0]['last_name']
        from_id = ans.from_id
        pluginMg.reg(first_name=first_name, last_name=last_name, from_id=from_id)

    text = ans.text
    text = re.sub(r'\[club\w+\|@?.+\]\s', '', text)
    text = re.sub(r'\[club\w+\|@?.+\],\s', '', text)
    text = re.sub('!', '', text)
    text = re.sub('/', '', text)

    MpluginMg = pluginMg.pluginMg(text=text, from_id=ans.from_id)
    if MpluginMg:
        keyboard = Keyboard(one_time=False)
        keyboard.add_row()
        keyboard.add_button(Text(label="�9�4 ������ڧݧ�"), color="negative")
        keyboard.add_button(Text(label="�9�6 ����ߧ��"), color="primary")
        keyboard.add_button(Text(label="�9�1 ���֧�ާ�"), color="primary")
        keyboard.add_row()
        keyboard.add_button(Text(label="�9�2 ����ާ���"), color="positive")
        await ans(MpluginMg, keyboard=keyboard.generate())
    else:
        await ans('����ާѧߧէ� �ߧ� �ߧѧۧէ֧ߧ�, �����ѧӧ� �0�0���ާ���0�3 ����ҧ� ��٧ߧѧ�� �ާ�� �ܧ�ާѧߧէ�.')

@bot.on.chat_invite()
async def wrapper(ans: Message):
    await ans("�6�9����ݧ���� ���ѧ�ڧҧ� �٧� ���ڧԧݧѧ�֧ߧڧ�! �����ѧاѧ֧� �ӧѧ� ��ԧ��ާߧ�� �ҧݧѧԧ�էѧ�ߧ���� �٧� �է�ҧѧӧݧ֧ߧڧ� �ҧ��� �� �ҧ֧�֧է�.\n\n ����էѧۧ�� �ҧ��� �է����� �ܧ� �ӧ�֧� ��֧�֧�ڧ�ܧ� �ڧݧ� ���ѧӧ� �ѧէާڧߧڧ���ѧ����, �� ��ݧ��ѧ� �֧�ݧ� �ӧ� �ߧ� ���٧էѧ�֧ݧ� �ҧ֧�֧է�, ���ݧ�٧�ӧѧ���� �ҧ���� �ާ�اߧ� ��֧�֧� ����ާڧߧѧߧڧ�.")

@bot.on.chat_message()
async def wrapper(ans: Message):
    check_profile = os.path.exists(users_dir + str(ans.from_id) + ".json")
    if check_profile == True:
        pass
    else:
        data = await bot.api.users.get(user_ids=ans.from_id)
        pluginMg.reg(first_name=data[0]['first_name'], last_name=data[0]['last_name'], from_id=ans.from_id)

    text = ans.text
    text = re.sub(r'\[club\w+\|@?.+\]\s', '', text)
    text = re.sub(r'\[club\w+\|@?.+\],\s', '', text)
    text = re.sub('!', '', text)
    text = re.sub('/', '', text)

    MpluginMg = pluginMg.pluginMg(text=text, from_id=ans.from_id)
    if MpluginMg:
        keyboard = Keyboard(one_time=False)
        keyboard.add_row()
        keyboard.add_button(Text(label="�9�4 ������ڧݧ�"), color="negative")
        keyboard.add_button(Text(label="�9�6 ����ߧ��"), color="primary")
        keyboard.add_button(Text(label="�9�1 ���֧�ާ�"), color="primary")
        keyboard.add_row()
        keyboard.add_button(Text(label="�9�2 ����ާ���"), color="positive")
        await ans(MpluginMg, keyboard=keyboard.generate())
    else:
        pass

@bot.error_handler(901, 902)
async def error(error):
    print("Cant send message to the user :(, error code:", error[0])

if __name__ == "__main__":
    bot.run_polling()