                 if int(bank_balance) >= int(summa_up):

                                    get_data = loadjson(users_dir + str(id) + ".json")

                                    bank_balance = int(get_data['bank_balance'])

                                    user_balance = int(get_data['balance'])

                                    algo_popoln_bank_balance = int(bank_balance) - int(summa_up)

                                    algo_snyat_user_balance = int(user_balance) + int(summa_up)

                                    get_data.update({"bank_balance": '{}'.format(int(algo_popoln_bank_balance))})

                                    get_data.update({"balance": '{}'.format(int(algo_snyat_user_balance))})

                                    dumpjson(get_data, users_dir + str(id) + ".json")

                                    return ', вы сняли: ' + str(summa_up) + '€ с карты! 😀\n💳 В банке: ' + str(algo_popoln_bank_balance) + '€\n💰 В кошельке: ' + str(algo_snyat_user_balance) + '€'

                                else:

                                    get_data = loadjson(users_dir + str(id) + ".json")

                                    user_balance = get_data['balance']

                                    bank_balance = get_data['bank_balance']

                                    return ', у вас недостаточно средств на карте, для получение наличных! 😔\n💳 В банке: ' + str(bank_balance) + '€\n💰 В кошельке: ' + str(user_balance) + '€'

                            elif sourceText.split()[2].lower() == 'все':

                                if int(bank_balance) >= int(1):

                                    get_data = loadjson(users_dir + str(id) + ".json")

                                    bank_balance = int(get_data['bank_balance'])

                                    user_balance = int(get_data['balance'])

                                    algo_snyat_user_balance = int(user_balance) + int(bank_balance)

                                    algo_popoln_bank_balance = int(bank_balance) - int(bank_balance)

                                    get_data.update({"bank_balance": '{}'.format(int(algo_popoln_bank_balance))})

                                    get_data.update({"balance": '{}'.format(int(algo_snyat_user_balance))})

                                    dumpjson(get_data, users_dir + str(id) + ".json")

                                    return ', вы сняли ' + str(bank_balance) + '€ с карты! 😀\n💳 В банке: ' + str(algo_popoln_bank_balance) + '€\n💰 В кошельке: ' + str(algo_snyat_user_balance) + '€'

                                else:

                                    get_data = loadjson(users_dir + str(id) + ".json")

                                    user_balance = get_data['balance']

                                    bank_balance = get_data['bank_balance']

                                    return ', у вас недостаточно средств на карте, для получение наличных! 😔\n💳 В банке: ' + str(bank_balance) + '€\n💰 В кошельке: ' + str(user_balance) + '€'

                            elif sourceText.split()[2].lower() == 'всё':

                                if int(bank_balance) >= int(1):

                                    get_data = loadjson(users_dir + str(id) + ".json")

                                    bank_balance = int(get_data['bank_balance'])

                                    user_balance = int(get_data['balance'])

                                    algo_snyat_user_balance = int(user_balance) + int(bank_balance)

                                    algo_popoln_bank_balance = int(bank_balance) - int(bank_balance)

                                    get_data.update({"bank_balance": '{}'.format(int(algo_popoln_bank_balance))})

                                    get_data.update({"balance": '{}'.format(int(algo_snyat_user_balance))})

                                    dumpjson(get_data, users_dir + str(id) + ".json")

                                    return ', вы сняли ' + str(bank_balance) + '€ с карты! 😀\n💳 В банке: ' + str(algo_popoln_bank_balance) + '€\n💰 В кошельке: ' + str(algo_snyat_user_balance) + '€'

                                else:

                                    get_data = loadjson(users_dir + str(id) + ".json")

                                    user_balance = get_data['balance']

                                    bank_balance = get_data['bank_balance']

                                    return ', у вас недостаточно средств на карте, для получение наличных! 😔\n💳 В банке: ' + str(bank_balance) + '€\n💰 В кошельке: ' + str(user_balance) + '€'

                            else:

                                return ', для снятие денег с банковского счёта, используйте для суммы - цифры! 😉'

                        else:

                            return ', использование: 💸 Банк снять [сумма/все]'

                    else:

                        get_data = loadjson(users_dir + str(id) + ".json")

                        if int(get_data['bank_balance']) <= 20000000:

                            bank_proc_raznica_time = float(time.time()) - float(get_data['bank_vd_time'])

                            bank_hours = int(bank_proc_raznica_time) / 3600

                            bank_balance = int(get_data['bank_balance'])

                            если банк_часы >= 24:

                                bank_proc_profit = int(1.2 * bank_balance)

                                get_data = loadjson (users_dir + str (id) + ".json")

                                get_data.update({"bank_balance": '{}'.format(int(bank_proc_profit))})

                                get_data.update({"bank_vd_time": '{}'.format(time.time())})

                                dumpjson(get_data, users_dir + str(id) + ".json")

                                return ', помощь по банку:\n\n📋 Счёт в банке:\n⠀⠀💳 На карте: ' + str(bank_proc_profit) + '€\n⠀⠀🏮 Биткоинов: ' + str(get_data['bank_cr_balance'] ) + '฿' + bankHelp + procHelp

                            еще:

                                get_data = loadjson (users_dir + str (id) + ".json")

                                return ', помощь по банку:\n\n📋 Счёт в банке:\n⠀⠀💳 На карте: ' + str(get_data['bank_balance']) + '€\n⠀⠀🏮 Биткоинов: ' + str(get_data ['bank_cr_balance']) + '฿' + bankHelp + procHelp

                        еще:

                            get_data = loadjson (users_dir + str (id) + ".json")

                            return ', помощь по банку:\n\n📋 Счёт в банке:\n⠀⠀💳 На карте: ' + str(get_data['bank_balance']) + '€\n⠀⠀🏮 Биткоинов: ' + str(get_data ['bank_cr_balance']) + '฿' + bankHelp + NoprocHelp

                еще:

                    get_data = loadjson (users_dir + str (id) + ".json")

                    если int(get_data['bank_balance']) <= 20000000:

                        bank_proc_raznica_time = float(time.time()) - float(get_data['bank_vd_time'])

                        bank_hours = int(bank_proc_raznica_time) / 3600

                        bank_balance = int(get_data['bank_balance'])

                        если банк_часы >= 24:

                            bank_proc_profit = int(1.2 * bank_balance)

                            get_data = loadjson (users_dir + str (id) + ".json")

                            get_data.update({"bank_balance": '{}'.format(int(bank_proc_profit))})

                            get_data.update({"bank_vd_time": '{}'.format(time.time())})

                            dumpjson(get_data, users_dir + str(id) + ".json")

                            return ', помощь по банку:\n\n📋 Счёт в банке:\n⠀⠀💳 На карте: ' + str(bank_proc_profit) + '€\n⠀⠀🏮 Биткоинов: ' + str(get_data['bank_cr_balance'] ) + '฿' + bankHelp + procHelp

                        еще:

                            get_data = loadjson (users_dir + str (id) + ".json")

                            return ', помощь по банку:\n\n📋 Счёт в банке:\n⠀⠀💳 На карте: ' + str(

                                get_data['bank_balance']) + '€\n⠀⠀🏮 Биткоинов: ' + str(get_data['bank_cr_balance']) + '฿' + bankHelp + procHelp

                    еще:

                        get_data = loadjson (users_dir + str (id) + ".json")

                        return ', помощь по банку:\n\n📋 Счёт в банке:\n⠀⠀💳 На карте: ' + str(get_data['bank_balance']) + '€\n⠀⠀🏮 Биткоинов: ' + str(get_data ['bank_cr_balance']) + '฿' + bankHelp + NoprocHelp

            еще:

                return', для использования банка, преобретите телефон! 😐\n📱 Посмотреть телефоны: Магазин телефонов'

        еще:

            возврат Нет

    pass
