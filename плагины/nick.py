import os
from plugins import gf

users_dir = os.path.join(r"users/")

def nicks(sourceText, id):
    command = 'ник'
    on = 'вкл'
    off = 'выкл'

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
                            return ', обращение по нику включено!'
                        return ', обращение по нику уже было включено!'
                    elif get_data['user_nick'] == 'None':
                        return ', у вас не установлен ник!'
                    else:
                        return ', у вас уже установлен ник!'

                elif off == sourceText.split()[1].lower():
                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                    if get_data['user_nick'] != 'None':
                        if get_data['nick'] != '0':
                            get_data = gf.loadjson(users_dir + str(id) + ".json")
                            get_data.update({"nick": "0"})
                            gf.dumpjson(get_data, users_dir + str(id) + ".json")
                            return ', обращение по нику выключено!'
                        return ', обращение по нику уже было выключено!'
                    elif get_data['user_nick'] == 'None':
                        return ', у вас не установлен ник!'
                    else:
                        return ', у вас уже установлен ник!'

                elif sourceText.split()[1].lower() == 'None'.lower():
                    return ', такой ник установить нельзя! 🙁'

                if get_data['group'] == 'Player':
                    if len(sourceText.split()[1].lower()) <= 10:
                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                        get_data.update({"user_nick":'{}'.format(sourceText.split()[1])})
                        get_data.update({"nick": "1"})
                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                        return ', замечательный ник: ' + sourceText.split()[1] + '! 😉\nОбращение по нику включено! 👌'
                    else:
                        return ', ник слишком длинный, для вашей привилегии разрешено использовать максимум 10 симовлов! 🙁'

                elif get_data['group'] == 'VIP':
                    if len(sourceText.split()[1].lower()) <= 15:
                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                        get_data.update({"user_nick":'{}'.format(sourceText.split()[1])})
                        get_data.update({"nick": "1"})
                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                        return ', замечательный ник: ' + sourceText.split()[1] + '! 😉\nОбращение по нику включено! 👌'
                    else:
                        return ', ник слишком длинный, максимально кол-во 15 симовлов! 🙁'
                        
                elif get_data['group'] == 'Premium':
                    if len(sourceText.split()[1].lower()) <= 15:
                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                        get_data.update({"user_nick":'{}'.format(sourceText.split()[1])})
                        get_data.update({"nick": "1"})
                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                        return ', замечательный ник: ' + sourceText.split()[1] + '! 😉\nОбращение по нику включено! 👌'
                    else:
                        return ', ник слишком длинный, максимально кол-во 15 симовлов! 🙁'

                elif get_data['group'] == 'Admin':
                    if len(sourceText.split()[1].lower()) <= 15:
                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                        get_data.update({"user_nick":'{}'.format(sourceText.split()[1])})
                        get_data.update({"nick": "1"})
                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                        return ', замечательный ник: ' + sourceText.split()[1] + '! 😉\nОбращение по нику включено! 👌'
                    else:
                        return ', ник слишком длинный, максимально кол-во 15 симовлов! 🙁'

                elif get_data['group'] == 'Owner':
                    if len(sourceText.split()[1].lower()) <= 20:
                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                        get_data.update({"user_nick":'{}'.format(sourceText.split()[1])})
                        get_data.update({"nick": "1"})
                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                        return ', замечательный ник: ' + sourceText.split()[1] + '! 😉\nОбращение по нику включено! 👌'
                    else:
                        return ', ник слишком длинный, максимально кол-во 20 симовлов! 🙁'
                elif len(sourceText.split()[1].lower()) >= 21:
                    return ', ник слишком длинный (максимальная длина ника 20 символов). ☺'
            else:
                return ', команда ник позволяет установить своё собственное обращение бота к вам, например по псевдониму!\n🎮 Использование: «ник [вкл/выкл/ваш ник]»  '
        else:
            return None
    return None