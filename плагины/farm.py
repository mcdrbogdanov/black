import os
import time
from plugins import gf

users_dir = os.path.join(r"users/")

def check_own_farm(own_farm):
    if own_farm == 1:
        return '⠀⠀🔋 Ферма: Miner\n'
    elif own_farm == 2:
        return '⠀⠀🔋 Ферма: Miner S\n'
    elif own_farm == 3:
        return '⠀⠀🔋 Ферма: Miner X\n'
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

    statis_bs = ', статистика фермы:\n\n📋 Статистика:\n' + str(check_own_farm(own_farm)) + '⠀⠀💸 Прибыль: ' + str(farm_profit) + '฿/день.\n⠀⠀💰 Заработано: '+ str(hour_fm_profit) + '฿'
    dop_infa = '\n\n⠀🔔 Ваша ферма приносит максимально-возможнный доход для своей мощности! Рекомендуем вам установить ферму на модель выше, для получение максимального профита.\n\n'

    if sourceText != '':
        if sourceText.split()[0].lower() in ['ферма', 'фермы', 'майнинг', '🔋']:
            if len(sourceText.split()) == 1:
                if own_farm >= 1:
                    if farm_withdraw_hours >= 24:
                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                        get_data.update({"bank_cr_balance": '{}'.format(str(int(bank_cr_balance) + int(hour_fm_profit)))})
                        get_data.update({"farm_time": '{}'.format(time.time())})
                        gf.dumpjson(get_data, users_dir + str(id) + ".json")

                        if own_farm == 1:
                            return statis_bs + dop_infa + '\n\n❓ Помощь:\n⠀⠀✅ Ферма улучшить\n⠀⠀📛 Ферма продать\n\n✅ Намайненные деньги зачисляются автоматически, если проверять ферму командой «ферма».\n🔔 Обменять заработанные биткоины: Банк обмен'
                        elif own_farm == 2:
                            return statis_bs + dop_infa + '\n\n❓ Помощь:\n⠀⠀✅ Ферма улучшить\n⠀⠀📛 Ферма продать\n\n✅ Намайненные деньги зачисляются автоматически, если проверять ферму командой «ферма».\n🔔 Обменять заработанные биткоины: Банк обмен'
                        else:
                            return statis_bs + '\n\n❓ Помощь:\n⠀⠀📛 Ферма продать\n\n✅ Намайненные деньги зачисляются автоматически, если проверять ферму командой «ферма».\n🔔 Обменять заработанные биткоины: Банк обмен'
                    else:
                        if own_farm == 1:
                            return statis_bs + dop_infa + '\n\n❓ Помощь:\n⠀⠀✅ Ферма улучшить\n⠀⠀📛 Ферма продать\n\n✅ Намайненные деньги зачисляются автоматически, если проверять ферму командой «ферма».'
                        elif own_farm == 2:
                            return statis_bs + dop_infa + '\n\n❓ Помощь:\n⠀⠀✅ Ферма улучшить\n⠀⠀📛 Ферма продать\n\n✅ Намайненные деньги зачисляются автоматически, если проверять ферму командой «ферма».'
                        else:
                            return statis_bs + '\n\n❓ Помощь:\n⠀⠀📛 Ферма продать\n\n✅ Намайненные деньги зачисляются автоматически, если проверять ферму командой «ферма».'
                else:
                    return ', у вас еще нет фермы! 😔\n\n 🔔 После покупки фермы, она начинает автоматически сразу приносить доход!\n\n❓ Для просмотра ферм, используйте:\n⠀⠀🛒 Магазин фермы'
            elif len(sourceText.split()) == 2:
                if 'продать' == sourceText.split()[1].lower():
                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                    own_farm = int(get_data['own_farm'])
                    if own_farm >= 1:
                        get_data.update({"farm_time": '{}'.format(0.0)})
                        get_data.update({"own_farm": '{}'.format(0)})
                        get_data.update({"farm_profit": '{}'.format(0)})
                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                        return ', вы успешно продали ферму! 🙂'
                    else:
                        return ', у вас еще нет фермы! 😔\n\n 🔔 После покупки фермы, она начинает автоматически сразу приносить доход!\n\n❓ Для просмотра ферм, используйте:\n⠀⠀🛒 Магазин фермы'
                elif 'улучшить' == sourceText.split()[1].lower():
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
                            return ', вы успешно улучшили ферму, до - 🔋 Miner S! 🙂'
                        else:
                            return ', у вас еще нет фермы! 😔\n\n 🔔 После покупки фермы, она начинает автоматически сразу приносить доход!\n\n❓ Для просмотра ферм, используйте:\n⠀⠀🛒 Магазин фермы'
                    elif own_farm == 2:
                        if price_own_farm3 <= user_balance:
                            algo_balance = user_balance - price_own_farm3
                            get_data.update({"balance": '{}'.format(algo_balance)})
                            get_data.update({"farm_time": '{}'.format(time.time())})
                            get_data.update({"own_farm": '{}'.format(3)})
                            get_data.update({"farm_profit": '{}'.format(1000)})
                            gf.dumpjson(get_data, users_dir + str(id) + ".json")
                            return ', вы успешно улучшили ферму, до - 🔋 Miner X! 🙂'
                        else:
                            return ', у вас недостаточно денег! 😔\n✅ Улучшение стоит: ' + str(price_own_farm3) + '€'
                    elif own_farm == 3:
                        return ', ваша ферма имеет максимальные улучшений! 😎'
                    else:
                        return ', у вас еще нет фермы! 😔\n\n 🔔 После покупки фермы, она начинает автоматически сразу приносить доход!\n\n❓ Для просмотра ферм, используйте:\n⠀⠀🛒 Магазин фермы'
                else:
                    if own_farm >= 1:
                        if farm_withdraw_hours >= 24:
                            get_data = gf.loadjson(users_dir + str(id) + ".json")
                            get_data.update({"bank_cr_balance": '{}'.format(str(int(bank_cr_balance) + int(hour_fm_profit)))})
                            get_data.update({"farm_time": '{}'.format(time.time())})
                            gf.dumpjson(get_data, users_dir + str(id) + ".json")

                            if own_farm == 1:
                                return statis_bs + dop_infa + '\n\n❓ Помощь:\n⠀⠀✅ Ферма улучшить\n⠀⠀📛 Ферма продать\n\n✅ Намайненные деньги зачисляются автоматически, если проверять ферму командой «ферма».\n🔔 Обменять заработанные биткоины: Банк обмен'
                            elif own_farm == 2:
                                return statis_bs + dop_infa + '\n\n❓ Помощь:\n⠀⠀✅ Ферма улучшить\n⠀⠀📛 Ферма продать\n\n✅ Намайненные деньги зачисляются автоматически, если проверять ферму командой «ферма».\n🔔 Обменять заработанные биткоины: Банк обмен'
                            else:
                                return statis_bs + '\n\n❓ Помощь:\n⠀⠀📛 Ферма продать\n\n✅ Намайненные деньги зачисляются автоматически, если проверять ферму командой «ферма».\n🔔 Обменять заработанные биткоины: Банк обмен'
                        else:
                            if own_farm == 1:
                                return statis_bs + dop_infa + '\n\n❓ Помощь:\n⠀⠀✅ Ферма улучшить\n⠀⠀📛 Ферма продать\n\n✅ Намайненные деньги зачисляются автоматически, если проверять ферму командой «ферма».'
                            elif own_farm == 2:
                                return statis_bs + dop_infa + '\n\n❓ Помощь:\n⠀⠀✅ Ферма улучшить\n⠀⠀📛 Ферма продать\n\n✅ Намайненные деньги зачисляются автоматически, если проверять ферму командой «ферма».'
                            else:
                                return statis_bs + '\n\n❓ Помощь:\n⠀⠀📛 Ферма продать\n\n✅ Намайненные деньги зачисляются автоматически, если проверять ферму командой «ферма».'
                    else:
                        return ', у вас еще нет фермы! 😔\n\n 🔔 После покупки фермы, она начинает автоматически сразу приносить доход!\n\n❓ Для просмотра ферм, используйте:\n⠀⠀🛒 Магазин фермы'
            else:
                if own_farm >= 1:
                    if farm_withdraw_hours >= 24:
                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                        get_data.update({"bank_cr_balance": '{}'.format(str(int(bank_cr_balance) + int(hour_fm_profit)))})
                        get_data.update({"farm_time": '{}'.format(time.time())})
                        gf.dumpjson(get_data, users_dir + str(id) + ".json")

                        if own_farm == 1:
                            return statis_bs + dop_infa + '\n\n❓ Помощь:\n⠀⠀✅ Ферма улучшить\n⠀⠀📛 Ферма продать\n\n✅ Намайненные деньги зачисляются автоматически, если проверять ферму командой «ферма».\n🔔 Обменять заработанные биткоины: Банк обмен'
                        elif own_farm == 2:
                            return statis_bs + dop_infa + '\n\n❓ Помощь:\n⠀⠀✅ Ферма улучшить\n⠀⠀📛 Ферма продать\n\n✅ Намайненные деньги зачисляются автоматически, если проверять ферму командой «ферма».\n🔔 Обменять заработанные биткоины: Банк обмен'
                        else:
                            return statis_bs + '\n\n❓ Помощь:\n⠀⠀📛 Ферма продать\n\n✅ Намайненные деньги зачисляются автоматически, если проверять ферму командой «ферма».\n🔔 Обменять заработанные биткоины: Банк обмен'
                    else:
                        if own_farm == 1:
                            return statis_bs + dop_infa + '\n\n❓ Помощь:\n⠀⠀✅ Ферма улучшить\n⠀⠀📛 Ферма продать\n\n✅ Намайненные деньги зачисляются автоматически, если проверять ферму командой «ферма».'
                        elif own_farm == 2:
                            return statis_bs + dop_infa + '\n\n❓ Помощь:\n⠀⠀✅ Ферма улучшить\n⠀⠀📛 Ферма продать\n\n✅ Намайненные деньги зачисляются автоматически, если проверять ферму командой «ферма».'
                        else:
                            return statis_bs + '\n\n❓ Помощь:\n⠀⠀📛 Ферма продать\n\n✅ Намайненные деньги зачисляются автоматически, если проверять ферму командой «ферма».'
                else:
                    return ', у вас еще нет фермы! 😔\n\n 🔔 После покупки фермы, она начинает автоматически сразу приносить доход!\n\n❓ Для просмотра ферм, используйте:\n⠀⠀🛒 Магазин фермы'
        else:
            return None
    pass