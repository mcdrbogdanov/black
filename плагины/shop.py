import os
import time
from plugins import gf

users_dir = os.path.join(r"users/")

def shop(sourceText, id):
    get_data = gf.loadjson(users_dir + str(id) + ".json")
    user_balance = int(get_data['balance'])

    shopHelp = ', §á§à§Þ§à§ë§î §á§à §Þ§Ñ§Ô§Ñ§Ù§Ú§ß§å:\n\n7Õ4•0“6 §±§à§Ü§å§á§Ñ§Û§ä§Ö §â§Ñ§Ù§Ý§Ú§é§ß§à§Ö §Ú§Þ§å§ë§Ö§ã§ä§Ó§à §Ó §à§Õ§Ú§ß §Ü§Ý§Ú§Ü! §±§à§ã§Ý§Ö §á§à§Ü§å§á§Ü§Ú §Õ§à§Þ§Ñ, §Ó§í §ã§Þ§à§Ø§Ö§ä§Ö §á§â§Ö§à§Ò§â§Ö§ã§ä§Ú §ä§â§Ñ§ß§ã§á§à§â§ä §Ú §æ§Ö§â§Þ§å §Õ§Ý§ñ §Þ§Ñ§Û§ß§Ú§ß§Ô§Ñ §Ò§Ú§ä§Ü§à§Ú§ß§à§Ó.\n\n”9Ý8 §°§ã§ß§à§Ó§ß§à§Ö:\n7Õ47Õ4”9Æ2 §¥§à§Þ§Ñ\n7Õ47Õ4•07 §®§Ñ§ê§Ú§ß§í\n7Õ47Õ47¼6 §³§Ñ§Þ§à§Ý§×§ä§í\n7Õ47Õ4•0‹5 §£§Ö§â§ä§à§Ý§×§ä§í\n7Õ47Õ4•0•5 §Á§ç§ä§í\n\n”9Ù5 §°§ã§ä§Ñ§Ý§î§ß§à§Ö:\n7Õ47Õ4”9ó5 §¬§à§Þ§á§î§ð§ä§Ö§â§í\n7Õ47Õ4”9á5 §´§Ö§Ý§Ö§æ§à§ß§í\n7Õ47Õ4”9ä1 §¶§Ö§â§Þ§í\n\n7Ä1 §±§à§Þ§à§ë§î:\n7Õ47Õ4”9ä4 §®§Ñ§Ô§Ñ§Ù§Ú§ß [§Ü§Ñ§ä§Ö§Ô§à§â§Ú§ñ] - §ä§à§Ó§Ñ§â§í.\n7Õ47Õ4•0“6 §®§Ñ§Ô§Ñ§Ù§Ú§ß [§Ü§Ñ§ä§Ö§Ô§à§â§Ú§ñ] [§ß§à§Þ§Ö§â] - §Ü§å§á§Ú§ä§î §ä§à§Ó§Ñ§â.'

    if sourceText != '':
        if '§Þ§Ñ§Ô§Ñ§Ù§Ú§ß' == sourceText.split()[0].lower():
            if len(sourceText.split()) == 2:
                if sourceText.split()[1].lower() in ['§Õ§à§Þ', '§Õ§à§Þ§Ñ']:
                    return ', §ã§á§Ú§ã§à§Ü §Õ§à§ã§ä§å§á§ß§í§ç §Õ§à§Þ§à§Ó:\n\n7Õ4”9å0 §±§à§ã§Ý§Ö §á§à§Ü§å§á§Ü§Ú §Õ§à§Þ§Ñ, §Ó§í §ã§Þ§à§Ø§Ö§ä§Ö §Ü§å§á§Ú§ä§î §ä§â§Ñ§ß§ã§á§à§â§ä §Ú §æ§Ö§â§Þ§å!\n\n7Õ47Õ4”9Æ2 1. §¬§à§â§à§Ò§Ü§Ñ ¡ª 25.000¢ã\n7Õ47Õ4”9Æ2 2. §±§à§Õ§Ó§Ñ§Ý ¡ª 65.000¢ã\n7Õ47Õ4”9Æ2 3. §³§Ñ§â§Ñ§Û ¡ª 225.000¢ã\n7Õ47Õ4”9Æ2 4. §¤§Ñ§â§Ñ§Ø ¡ª 595.000¢ã\n7Õ47Õ4”9Æ2 5. §£§Ö§ä§ç§Ñ§ñ §ç§Ú§Ø§Ú§ß§Ñ ¡ª 655.000¢ã\n7Õ47Õ4”9Æ2 6. §¥§Ö§â§Ö§Ó§ñ§ß§ß§í§Û §Õ§à§Þ§Ú§Ü ¡ª 1.525.000¢ã\n7Õ47Õ4”9Æ2 7. §¬§Ú§â§á§Ú§é§ß§í§Û §Õ§à§Þ ¡ª 8.525.000¢ã\n7Õ47Õ4”9Æ2 8. §¬§à§ä§ä§Ö§Õ§Ø ¡ª 35.650.000¢ã\n7Õ47Õ4”9Æ2 9. §¥§à§Þ §ß§Ñ §±§å§Þ§Ñ§Ó§å§Õ§Ö ¡ª 68.250.000¢ã\n7Õ47Õ4”9Æ2 10. §£§Ú§Ý§Ý§Ñ §ß§Ñ §±§å§Þ§Ñ§Ó§å§Õ§Ö ¡ª 93.500.000¢ã\n7Õ47Õ4”9Æ2 11. §­§Ú§é§ß§í§Û §à§ã§ä§â§à§Ó ¡ª 999.999.999¢ã\n\n7Ä1 §¥§Ý§ñ §á§à§Ü§å§á§Ü§Ú §Õ§à§Þ§Ñ, §Ú§ã§á§à§Ý§î§Ù§å§Û§ä§Ö:\n7Õ47Õ4•0“6 §®§Ñ§Ô§Ñ§Ù§Ú§ß §Õ§à§Þ [§ß§à§Þ§Ö§â]'
                elif sourceText.split()[1].lower() in ['§Þ§Ñ§ê§Ú§ß§Ñ', '§Þ§Ñ§ê§Ú§ß§í']:
                    return ', §ã§á§Ú§ã§à§Ü §Õ§à§ã§ä§å§á§ß§í§ç §Þ§Ñ§ê§Ú§ß:\n\n7Õ4”9å0 §±§à§Ü§å§á§Ñ§Û§ä§Ö §ä§â§Ñ§ß§ã§á§à§â§ä §Ó §à§Õ§Ú§ß §Ü§Ý§Ú§Ü!\n\n7Õ47Õ4•07 1. §£§Ö§Ý§à§ã§Ú§á§Ö§Õ ¡ª 125.000¢ã\n7Õ47Õ4•07 2. §¤§Ú§â§à§ã§Ü§å§ä§Ö§â ¡ª 255.000¢ã\n7Õ47Õ4”9Ä3 3. Ducati Scrambler ¡ª 525.000¢ã\n7Õ47Õ4”9Ä3 4. Honda CTX1300 ¡ª 1.275.000¢ã\n7Õ47Õ4•07 5. Ferrari California front ¡ª 1.650.000¢ã\n7Õ47Õ4•07 6. Porsche 911 ¡ª 2.000.000¢ã\n7Õ47Õ4•07 7. Nissan GT-R ¡ª 4.350.000¢ã\n7Õ47Õ4•07 8. BMW X6 ¡ª 15.650.000¢ã\n7Õ47Õ4•07 9. Jaguar F-Type ¡ª 25.735.000¢ã\n7Õ47Õ4•07 10. Lamborghini Hurac¨¢n ¡ª 30.800.000¢ã\n7Õ47Õ4•07 11. Lamborghini Gallardo ¡ª 37.580.000¢ã\n7Õ47Õ4•07 12. Ferrari F80 Concept ¡ª 57.999.999¢ã\n7Õ47Õ4•07 13. Lamborghini Sesto ¡ª 108.555.000¢ã\n7Õ47Õ4•07 14. Various Ford-based trucks ¡ª 999.999.999¢ã\n7Õ47Õ4•07 15. Tesla Cybertruck ¡ª 1.500.000.000¢ã\n\n7Ä1 §¥§Ý§ñ §á§à§Ü§å§á§Ü§Ú §ä§â§Ñ§ß§ã§á§à§â§ä§Ñ, §Ú§ã§á§à§Ý§î§Ù§å§Û§ä§Ö:\n7Õ47Õ4•0“6 §®§Ñ§Ô§Ñ§Ù§Ú§ß §Þ§Ñ§ê§Ú§ß§Ñ [§ß§à§Þ§Ö§â]'
                elif sourceText.split()[1].lower() in ['§ñ§ç§ä§Ñ', '§ñ§ç§ä§í']:
                    return ', §ã§á§Ú§ã§à§Ü §Õ§à§ã§ä§å§á§ß§í§ç §ñ§ç§ä:\n\n7Õ47Õ4•0•5 1. RHIB ¡ª 575.000¢ã\n7Õ47Õ4•0•5 2. Kawasaki ¡ª 1.225.000¢ã\n7Õ47Õ4•0•5 3. Riva Aquarama ¡ª 2.500.000¢ã\n7Õ47Õ4•0•5 4. Various ¡ª 3.650.000¢ã\n7Õ47Õ4•0•5 5. §²rin§ã§Öss 60 ¡ª 8.355.000¢ã\n7Õ47Õ4•0•5 6. §¡zimut 70 ¡ª 12.850.000¢ã\n7Õ47Õ4•0•5 7. D§àmin§Ñt§àr 40M ¡ª 23.125.000¢ã\n7Õ47Õ4•0•5 8. M§à§àn§Ön 124 ¡ª 34.666.000¢ã\n7Õ47Õ4•0•5 9. Wid§Ör 150 ¡ª 66.225.000¢ã\n7Õ47Õ4•0•5 10. Palmer J§àhns§àn 42M Su§â§ÖrS§â§àrt ¡ª 96.000.000¢ã\n7Õ47Õ4•0•5 11. Wid§Ör 165 ¡ª 126.650.000¢ã\n7Õ47Õ4•0•5 12. §¦§ãli§âs§Ö ¡ª 527.777.777¢ã\n7Õ47Õ4•0•5 13. Dub§Ñi ¡ª 999.999.999¢ã\n7Õ47Õ4•0•5 14. Str§Ö§Öts §àf M§àn§Ñ§ã§à ¡ª 1.255.000.000¢ã\n\n7Ä1 §¥§Ý§ñ §á§à§Ü§å§á§Ü§Ú §ä§â§Ñ§ß§ã§á§à§â§ä§Ñ, §Ú§ã§á§à§Ý§î§Ù§å§Û§ä§Ö:\n7Õ47Õ4•0“6 §®§Ñ§Ô§Ñ§Ù§Ú§ß §ñ§ç§ä§Ñ [§ß§à§Þ§Ö§â]'
                elif sourceText.split()[1].lower() in ['§ã§Ñ§Þ§à§Ý§×§ä', '§ã§Ñ§Þ§à§Ý§Ö§ä', '§ã§Ñ§Þ§à§Ý§×§ä§í', '§ã§Ñ§Þ§à§Ý§Ö§ä§í']:
                    return ', §ã§á§Ú§ã§à§Ü §Õ§à§ã§ä§å§á§ß§í§ç §ã§Ñ§Þ§à§Ý§×§ä§à§Ó:\n\n7Õ4”9å0 §±§à§Ü§å§á§Ñ§Û§ä§Ö §ä§â§Ñ§ß§ã§á§à§â§ä §Ó §à§Õ§Ú§ß §Ü§Ý§Ú§Ü!\n\n7Õ47Õ47¼6 1. de Havilland Canada DHC-2 ¡ª 500.000¢ã\n7Õ47Õ47¼6 2. Piper PA-46 ¡ª 3.995.000¢ã\n7Õ47Õ47¼6 3. Cessna 310 ¡ª 6.350.000¢ã\n7Õ47Õ47¼6 4. Learjet 55 ¡ª 15.500.000¢ã\n7Õ47Õ47¼6 5. Bombardier Global Express ¡ª 17.800.000¢ã\n7Õ47Õ47¼6 6. Cessna Citation X ¡ª 22.250.000¢ã\n7Õ47Õ47¼6 7. C-130 ¡ª 43.000.000¢ã\n7Õ47Õ47¼6 8. VOLATOL ¡ª 65.505.000¢ã\n7Õ47Õ47¼6 9. RM-10 BOMBUSHKA ¡ª 75.985.000¢ã\n7Õ47Õ47¼6 10. AVENGER ¡ª HYV ¡ª 86.495.000¢ã\n7Õ47Õ47¼6 11. F-16 Fighting Falcon ¡ª 109.999.999¢ã\n7Õ47Õ47¼6 12. RM-10 BOMBUSHKA ¡ª 313.000.000¢ã\n7Õ47Õ47¼6 13. TULA ¡ª MAMMOTH ¡ª 617.555.000¢ã\n7Õ47Õ47¼6 14. V-65 MOLOTOK ¡ª 850.000.000¢ã\n7Õ47Õ47¼6 15. MOGUL ¡ª MAMMOTH ¡ª 2.000.000.000¢ã\n\n7Ä1 §¥§Ý§ñ §á§à§Ü§å§á§Ü§Ú §ä§â§Ñ§ß§ã§á§à§â§ä§Ñ, §Ú§ã§á§à§Ý§î§Ù§å§Û§ä§Ö:\n7Õ47Õ4•0“6 §®§Ñ§Ô§Ñ§Ù§Ú§ß §ã§Ñ§Þ§à§Ý§×§ä [§ß§à§Þ§Ö§â]'
                elif sourceText.split()[1].lower() in ['§Ó§Ö§â§ä§à§Ý§×§ä', '§Ó§Ö§â§ä§à§Ý§Ö§ä', '§Ó§Ö§â§ä§à§Ý§×§ä§í', '§Ó§Ö§â§ä§à§Ý§Ö§ä§í']:
                    return ', §ã§á§Ú§ã§à§Ü §Õ§à§ã§ä§å§á§ß§í§ç §Ó§Ö§â§ä§à§Ý§×§ä§à§Ó:\n\n7Õ4”9å0 §±§à§Ü§å§á§Ñ§Û§ä§Ö §ä§â§Ñ§ß§ã§á§à§â§ä §Ó §à§Õ§Ú§ß §Ü§Ý§Ú§Ü!\n\n7Õ47Õ4•0‹5 1. Eurocopter EC130/135/14 ¡ª 1.300.000¢ã\n7Õ47Õ4•0‹5 2. Boeing MH-6 ¡ª 1.750.000¢ã\n7Õ47Õ4•0‹5 3. Sikorsky UH-60 ¡ª 2.225.000¢ã\n7Õ47Õ4•0‹5 4. HAVOK ¡ª NAGASAKI ¡ª 3.500.000¢ã\n7Õ47Õ4•0‹5 5. Eurocopter EC145 ¡ª 8.850.000¢ã\n7Õ47Õ4•0‹5 6. Airbus H160 ¡ª 25.555.555¢ã\n7Õ47Õ4•0‹5 7. Mil Mi-24 ¡ª 58.000.000¢ã\n7Õ47Õ4•0‹5 8. POLICE MAVERICK ¡ª 215.000.000¢ã\n7Õ47Õ4•0‹5 9. MAVERICK ¡ª 525.000.000¢ã\n\n7Ä1 §¥§Ý§ñ §á§à§Ü§å§á§Ü§Ú §ä§â§Ñ§ß§ã§á§à§â§ä§Ñ, §Ú§ã§á§à§Ý§î§Ù§å§Û§ä§Ö:\n7Õ47Õ4•0“6 §®§Ñ§Ô§Ñ§Ù§Ú§ß §Ó§Ö§â§ä§à§Ý§×§ä [§ß§à§Þ§Ö§â]'
                elif sourceText.split()[1].lower() in ['§æ§Ö§â§Þ§Ñ', '§æ§Ö§â§Þ§í']:
                    return ', §ã§á§Ú§ã§à§Ü §Õ§à§ã§ä§å§á§ß§í§ç §æ§Ö§â§Þ:\n\n7Õ4”9å0 §±§à§ã§Ý§Ö §á§à§Ü§å§á§Ü§Ú §æ§Ö§â§Þ§í, §Ó§í §ã§Þ§à§Ø§Ö§ä§Ö §Þ§Ñ§Û§ß§Ú§ä§î §Ò§Ú§ä§Ü§à§Ú§ß§í!\n\n7Õ47Õ4”9ä1 1. Miner (52Õ1/§Õ§Ö§ß§î) ¡ª 500.000¢ã\n7Õ47Õ4”9ä1 2. Miner S (502Õ1/§Õ§Ö§ß§î) ¡ª 5.000.000¢ã\n7Õ47Õ4”9ä1 3. Miner X (1 0002Õ1/§Õ§Ö§ß§î) ¡ª 500.000.000¢ã\n\n7Ä1 §¥§Ý§ñ §á§à§Ü§å§á§Ü§Ú §æ§Ö§â§Þ§í, §Ú§ã§á§à§Ý§î§Ù§å§Û§ä§Ö:\n7Õ47Õ4•0“6 §®§Ñ§Ô§Ñ§Ù§Ú§ß §æ§Ö§â§Þ§Ñ [§ß§à§Þ§Ö§â]'
                elif sourceText.split()[1].lower() in ['§Ü§à§Þ§á', '§Ü§à§Þ§á§î§ð§ä§Ö§â', '§ß§à§å§ä', '§ß§à§å§ä§Ò§å§Ü', '§Ü§à§Þ§á§í', '§Ü§à§Þ§á§î§ð§ä§Ö§â§í', '§ß§à§å§ä§í', '§ß§à§å§ä§Ò§å§Ü§Ú']:
                    return ', §ã§á§Ú§ã§à§Ü §Õ§à§ã§ä§å§á§ß§í§ç §Ü§à§Þ§á§î§ð§ä§Ö§â§à§Ó:\n\n7Õ4”9å0 §±§à§ã§Ý§Ö §á§à§Ü§å§á§Ü§Ú §Ü§à§Þ§á§î§ð§ä§Ö§â§Ñ, §Ó§í §ã§Þ§à§Ø§Ö§ä§Ö §á§â§à§Ú§Ù§Ó§à§Õ§Ú§ä§î §Ó§Ù§Ý§à§Þ§í!\n\n7Õ47Õ4”9ó5 1. Book ¡ª 35.000.000¢ã\n7Õ47Õ4”9ó5 2. Book Air ¡ª 45.000.000¢ã\n7Õ47Õ4”9ó5 3. Book Pro ¡ª 150.000.000¢ã\n\n7Ä1 §¥§Ý§ñ §á§à§Ü§å§á§Ü§Ú §Ü§à§Þ§á§î§ð§ä§Ö§â§Ñ, §Ú§ã§á§à§Ý§î§Ù§å§Û§ä§Ö:\n7Õ47Õ4•0“6 §®§Ñ§Ô§Ñ§Ù§Ú§ß §Ü§à§Þ§á§î§ð§ä§Ö§â [§ß§à§Þ§Ö§â]'
                elif sourceText.split()[1].lower() in ['§ä§Ö§Ý§Ö§æ§à§ß', '§ã§Þ§Ñ§â§ä§æ§à§ß', '§ä§Ö§Ý§Ö§æ§à§ß§í', '§ã§Þ§Ñ§â§ä§æ§à§ß§í']:
                    return ', §ã§á§Ú§ã§à§Ü §Õ§à§ã§ä§å§á§ß§í§ç §ä§Ö§Ý§Ö§æ§à§ß§à§Ó:\n\n7Õ4”9å0 §±§à§Ü§å§á§Ñ§Û§ä§Ö §ä§Ö§Ý§Ö§æ§à§ß§í §Ó §à§Õ§Ú§ß §Ü§Ý§Ú§Ü!\n\n7Õ47Õ4”9á5 1. iPhone ¡ª 25.800.000¢ã\n7Õ47Õ4”9á5 2. iPhone Pro ¡ª 30.000.000¢ã\n7Õ47Õ4”9á5 3. iPhone Pro Max ¡ª 35.250.000¢ã\n\n7Ä1 §¥§Ý§ñ §á§à§Ü§å§á§Ü§Ú §ã§Þ§Ñ§â§ä§æ§à§ß§Ñ, §Ú§ã§á§à§Ý§î§Ù§å§Û§ä§Ö:\n7Õ47Õ4•0“6 §®§Ñ§Ô§Ñ§Ù§Ú§ß §ã§Þ§Ñ§â§ä§æ§à§ß [§ß§à§Þ§Ö§â]'
            elif len(sourceText.split()) == 3:
                id_own = str(sourceText.split()[2].lower())
                if sourceText.split()[1].lower() in ['§Õ§à§Þ', '§Õ§à§Þ§Ñ']:
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
                                    return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9Æ2 §¬§à§â§à§Ò§Ü§å §Ù§Ñ ' + str(price_own_housing1) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                else:
                                    return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                            else:
                                return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Õ§à§Þ! ”9ý5'
                        elif int(id_own) == 2:
                            if own_housing == 0:
                                if price_own_housing2 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing2
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9Æ2 §±§à§Õ§Ó§Ñ§Ý §Ù§Ñ ' + str(price_own_housing2) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                else:
                                    return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                            else:
                                return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Õ§à§Þ! ”9ý5'
                        elif int(id_own) == 3:
                            if own_housing == 0:
                                if price_own_housing3 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing3
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9Æ2 §³§Ñ§â§Ñ§Û §Ù§Ñ ' + str(price_own_housing3) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                else:
                                    return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                            else:
                                return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Õ§à§Þ! ”9ý5'
                        elif int(id_own) == 4:
                            if own_housing == 0:
                                if price_own_housing4 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing4
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9Æ2 §¤§Ñ§â§Ñ§Ø §Ù§Ñ ' + str(price_own_housing4) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                else:
                                    return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                            else:
                                return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Õ§à§Þ! ”9ý5'
                        elif int(id_own) == 5:
                            if own_housing == 0:
                                if price_own_housing5 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing5
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9Æ2 §£§Ö§ä§ç§å§ð §ç§Ú§Ø§Ú§ß§å §Ù§Ñ ' + str(price_own_housing5) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                else:
                                    return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                            else:
                                return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Õ§à§Þ! ”9ý5'
                        elif int(id_own) == 6:
                            if own_housing == 0:
                                if price_own_housing6 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing6
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9Æ2 §¥§Ö§â§Ö§Ó§ñ§ß§ß§í§Û §Õ§à§Þ§Ú§Ü §Ù§Ñ ' + str(price_own_housing6) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                else:
                                    return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                            else:
                                return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Õ§à§Þ! ”9ý5'
                        elif int(id_own) == 7:
                            if own_housing == 0:
                                if price_own_housing7 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing7
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9Æ2 §¬§Ú§â§á§Ú§é§ß§í§Û §Õ§à§Þ §Ù§Ñ ' + str(price_own_housing7) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                else:
                                    return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                            else:
                                return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Õ§à§Þ! ”9ý5'
                        elif int(id_own) == 8:
                            if own_housing == 0:
                                if price_own_housing8 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing8
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9Æ2 §¬§à§ä§ä§Ö§Õ§Ø §Ù§Ñ ' + str(price_own_housing8) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                else:
                                    return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                            else:
                                return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Õ§à§Þ! ”9ý5'
                        elif int(id_own) == 9:
                            if own_housing == 0:
                                if price_own_housing9 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing9
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9Æ2 §¥§à§Þ §ß§Ñ §±§å§Þ§Ñ§Ó§å§Õ§Ö §Ù§Ñ ' + str(price_own_housing9) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                else:
                                    return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                            else:
                                return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Õ§à§Þ! ”9ý5'
                        elif int(id_own) == 10:
                            if own_housing == 0:
                                if price_own_housing10 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing10
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9Æ2 §£§Ú§Ý§Ý§å §ß§Ñ §±§å§Þ§Ñ§Ó§å§Õ§Ö §Ù§Ñ ' + str(price_own_housing10) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                else:
                                    return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                            else:
                                return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Õ§à§Þ! ”9ý5'
                        elif int(id_own) == 11:
                            if own_housing == 0:
                                if price_own_housing11 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing11
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9Æ2 §­§Ú§é§ß§í§Û §à§ã§ä§â§à§Ó §Ù§Ñ ' + str(price_own_housing11) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                else:
                                    return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                            else:
                                return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Õ§à§Þ! ”9ý5'
                        else:
                            return ', §Õ§à§Þ§Ñ §ã §ä§Ñ§Ü§Ú§Þ ID §ß§Ö §ã§å§ë§Ö§ã§ä§Ó§å§Ö§ä! ”9þ6'
                    else:
                        return ', §ã§Ú§Þ§Ó§à§Ý§í §Ú §Ò§å§Ü§Ó§í §Ù§Ñ§á§â§Ö§ë§Ö§ß§í! ”9þ6'

                elif sourceText.split()[1].lower() in ['§Þ§Ñ§ê§Ú§ß§Ñ', '§Þ§Ñ§ê§Ú§ß§í']:
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
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •07 §£§Ö§Ý§à§ã§Ú§á§Ö§Õ §Ù§Ñ ' + str(price_own_car1) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Þ§Ñ§ê§Ú§ß§Ñ! ”9ý5'
                            elif int(id_own) == 2:
                                if own_car == 0:
                                    if price_own_car2 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car2
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •07 §¤§Ú§â§à§ã§Ü§å§ä§Ö§â §Ù§Ñ ' + str(price_own_car2) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Þ§Ñ§ê§Ú§ß§Ñ! ”9ý5'

                            elif int(id_own) == 3:
                                if own_car == 0:
                                    if price_own_car3 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car3
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9Ä3 Ducati Scrambler §Ù§Ñ ' + str(price_own_car3) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Þ§Ñ§ê§Ú§ß§Ñ! ”9ý5'
                            elif int(id_own) == 4:
                                if own_car == 0:
                                    if price_own_car4 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car4
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9Ä3 Honda CTX1300 §Ù§Ñ ' + str(price_own_car4) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Þ§Ñ§ê§Ú§ß§Ñ! ”9ý5'

                            elif int(id_own) == 5:
                                if own_car == 0:
                                    if price_own_car5 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car5
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •07 Ferrari California front §Ù§Ñ ' + str(price_own_car5) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Þ§Ñ§ê§Ú§ß§Ñ! ”9ý5'
                            elif int(id_own) == 6:
                                if own_car == 0:
                                    if price_own_car6 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car6
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •07 Porsche 911 §Ù§Ñ ' + str(price_own_car6) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Þ§Ñ§ê§Ú§ß§Ñ! ”9ý5'
                            elif int(id_own) == 7:
                                if own_car == 0:
                                    if price_own_car7 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car7
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •07 Nissan GT-R §Ù§Ñ ' + str(price_own_car7) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Þ§Ñ§ê§Ú§ß§Ñ! ”9ý5'
                            elif int(id_own) == 8:
                                if own_car == 0:
                                    if price_own_car8 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car8
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •07 BMW X6 §Ù§Ñ ' + str(price_own_car8) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Þ§Ñ§ê§Ú§ß§Ñ! ”9ý5'
                            elif int(id_own) == 9:
                                if own_car == 0:
                                    if price_own_car9 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car9
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •07 Jaguar F-Type §Ù§Ñ ' + str(price_own_car9) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Þ§Ñ§ê§Ú§ß§Ñ! ”9ý5'
                            elif int(id_own) == 10:
                                if own_car == 0:
                                    if price_own_car10 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car10
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •07 Lamborghini Hurac¨¢n §Ù§Ñ ' + str(price_own_car10) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Þ§Ñ§ê§Ú§ß§Ñ! ”9ý5'
                            elif int(id_own) == 11:
                                if own_car == 0:
                                    if price_own_car11 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car11
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •07 Lamborghini Gallardo §Ù§Ñ ' + str(price_own_car11) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Þ§Ñ§ê§Ú§ß§Ñ! ”9ý5'
                            elif int(id_own) == 12:
                                if own_car == 0:
                                    if price_own_car12 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car12
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •07 Ferrari F80 Concept §Ù§Ñ ' + str(price_own_car12) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Þ§Ñ§ê§Ú§ß§Ñ! ”9ý5'
                            elif int(id_own) == 13:
                                if own_car == 0:
                                    if price_own_car13 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car13
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •07 Lamborghini Sesto §Ù§Ñ ' + str(price_own_car13) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Þ§Ñ§ê§Ú§ß§Ñ! ”9ý5'
                            elif int(id_own) == 14:
                                if own_car == 0:
                                    if price_own_car14 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car14
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •07 Various Ford-based trucks §Ù§Ñ ' + str(price_own_car14) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Þ§Ñ§ê§Ú§ß§Ñ! ”9ý5'
                            elif int(id_own) == 15:
                                if own_car == 0:
                                    if price_own_car15 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car15
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •07 Tesla Cybertruck §Ù§Ñ ' + str(price_own_car15) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Þ§Ñ§ê§Ú§ß§Ñ! ”9ý5'
                            else:
                                return ', §Þ§Ñ§ê§Ú§ß§í §ã §ä§Ñ§Ü§Ú§Þ ID §ß§Ö §ã§å§ë§Ö§ã§ä§Ó§å§Ö§ä! ”9þ6'
                        else:
                            return ', §ã§Ú§Þ§Ó§à§Ý§í §Ú §Ò§å§Ü§Ó§í §Ù§Ñ§á§â§Ö§ë§Ö§ß§í! ”9þ6'
                    else:
                        return ', §Õ§Ý§ñ §á§à§Ü§å§á§Ü§Ú §ä§â§Ñ§ß§ã§á§à§â§ä§Ñ §ß§Ö§à§Ò§ç§à§Õ§Ú§Þ§à §Õ§à§Þ! ”9ý5'
                elif sourceText.split()[1].lower() in ['§ñ§ç§ä§Ñ', '§ñ§ç§ä§í']:
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
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •0•5 RHIB §Ù§Ñ ' + str(price_own_yacht1) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ñ§ç§ä§Ñ! ”9ý5'
                            elif int(id_own) == 2:
                                if own_yacht == 0:
                                    if price_own_yacht2 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht2
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •0•5 Kawasaki §Ù§Ñ ' + str(price_own_yacht2) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ñ§ç§ä§Ñ! ”9ý5'

                            elif int(id_own) == 3:
                                if own_yacht == 0:
                                    if price_own_yacht3 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht3
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •0•5 Riva Aquarama §Ù§Ñ ' + str(price_own_yacht3) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ñ§ç§ä§Ñ! ”9ý5'
                            elif int(id_own) == 4:
                                if own_yacht == 0:
                                    if price_own_yacht4 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht4
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •0•5 Various §Ù§Ñ ' + str(price_own_yacht4) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ñ§ç§ä§Ñ! ”9ý5'

                            elif int(id_own) == 5:
                                if own_yacht == 0:
                                    if price_own_yacht5 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht5
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •0•5 §²rin§ã§Öss 60 §Ù§Ñ ' + str(price_own_yacht5) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ñ§ç§ä§Ñ! ”9ý5'
                            elif int(id_own) == 6:
                                if own_yacht == 0:
                                    if price_own_yacht6 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht6
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •0•5 §¡zimut 70 §Ù§Ñ ' + str(price_own_yacht6) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ñ§ç§ä§Ñ! ”9ý5'
                            elif int(id_own) == 7:
                                if own_yacht == 0:
                                    if price_own_yacht7 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht7
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •0•5 D§àmin§Ñt§àr 40M §Ù§Ñ ' + str(price_own_yacht7) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ñ§ç§ä§Ñ! ”9ý5'
                            elif int(id_own) == 8:
                                if own_yacht == 0:
                                    if price_own_yacht8 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht8
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •0•5 M§à§àn§Ön 124 §Ù§Ñ ' + str(price_own_yacht8) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ñ§ç§ä§Ñ! ”9ý5'
                            elif int(id_own) == 9:
                                if own_yacht == 0:
                                    if price_own_yacht9 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht9
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •0•5 Wid§Ör 150 §Ù§Ñ ' + str(price_own_yacht9) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ñ§ç§ä§Ñ! ”9ý5'
                            elif int(id_own) == 10:
                                if own_yacht == 0:
                                    if price_own_yacht10 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht10
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •0•5 Palmer J§àhns§àn 42M Su§â§ÖrS§â§àrt §Ù§Ñ ' + str(
                                            price_own_yacht10) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ñ§ç§ä§Ñ! ”9ý5'
                            elif int(id_own) == 11:
                                if own_yacht == 0:
                                    if price_own_yacht11 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht11
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •0•5 Wid§Ör 165 §Ù§Ñ ' + str(price_own_yacht11) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ñ§ç§ä§Ñ! ”9ý5'
                            elif int(id_own) == 12:
                                if own_yacht == 0:
                                    if price_own_yacht12 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht12
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •0•5 §¦§ãli§âs§Ö §Ù§Ñ ' + str(price_own_yacht12) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ñ§ç§ä§Ñ! ”9ý5'
                            elif int(id_own) == 13:
                                if own_yacht == 0:
                                    if price_own_yacht13 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht13
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •0•5 Dub§Ñi §Ù§Ñ ' + str(price_own_yacht13) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ñ§ç§ä§Ñ! ”9ý5'
                            elif int(id_own) == 14:
                                if own_yacht == 0:
                                    if price_own_yacht14 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht14
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •0•5 Str§Ö§Öts §àf M§àn§Ñ§ã§à §Ù§Ñ ' + str(price_own_yacht14) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ñ§ç§ä§Ñ! ”9ý5'
                            else:
                                return ', §ñ§ç§ä§í §ã §ä§Ñ§Ü§Ú§Þ ID §ß§Ö §ã§å§ë§Ö§ã§ä§Ó§å§Ö§ä! ”9þ6'
                        else:
                            return ', §ã§Ú§Þ§Ó§à§Ý§í §Ú §Ò§å§Ü§Ó§í §Ù§Ñ§á§â§Ö§ë§Ö§ß§í! ”9þ6'
                    else:
                        return ', §Õ§Ý§ñ §á§à§Ü§å§á§Ü§Ú §ä§â§Ñ§ß§ã§á§à§â§ä§Ñ §ß§Ö§à§Ò§ç§à§Õ§Ú§Þ §Õ§à§Þ! ”9ý5'
                elif sourceText.split()[1].lower() in ['§ã§Ñ§Þ§à§Ý§×§ä', '§ã§Ñ§Þ§à§Ý§Ö§ä', '§ã§Ñ§Þ§à§Ý§×§ä§í', '§ã§Ñ§Þ§à§Ý§Ö§ä§í']:
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
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - 7¼6 de Havilland Canada DHC-2 §Ù§Ñ ' + str(price_own_air1) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ã§Ñ§Þ§à§Ý§×§ä! ”9ý5'
                            elif int(id_own) == 2:
                                if own_air == 0:
                                    if price_own_air2 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air2
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - 7¼6 Piper PA-46 §Ù§Ñ ' + str(price_own_air2) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ã§Ñ§Þ§à§Ý§×§ä! ”9ý5'

                            elif int(id_own) == 3:
                                if own_air == 0:
                                    if price_own_air3 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air3
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - 7¼6 Cessna 310 §Ù§Ñ ' + str(price_own_air3) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ã§Ñ§Þ§à§Ý§×§ä! ”9ý5'
                            elif int(id_own) == 4:
                                if own_air == 0:
                                    if price_own_air4 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air4
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - 7¼6 Learjet 55 §Ù§Ñ ' + str(price_own_air4) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ã§Ñ§Þ§à§Ý§×§ä! ”9ý5'

                            elif int(id_own) == 5:
                                if own_air == 0:
                                    if price_own_air5 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air5
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - 7¼6 Bombardier Global Express §Ù§Ñ ' + str(price_own_air5) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ã§Ñ§Þ§à§Ý§×§ä! ”9ý5'
                            elif int(id_own) == 6:
                                if own_air == 0:
                                    if price_own_air6 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air6
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - 7¼6 Cessna Citation X §Ù§Ñ ' + str(price_own_air6) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ã§Ñ§Þ§à§Ý§×§ä! ”9ý5'
                            elif int(id_own) == 7:
                                if own_air == 0:
                                    if price_own_air7 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air7
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - 7¼6 C-130 §Ù§Ñ ' + str(price_own_air7) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ã§Ñ§Þ§à§Ý§×§ä! ”9ý5'
                            elif int(id_own) == 8:
                                if own_air == 0:
                                    if price_own_air8 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air8
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - 7¼6 VOLATOL §Ù§Ñ ' + str(price_own_air8) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ã§Ñ§Þ§à§Ý§×§ä! ”9ý5'
                            elif int(id_own) == 9:
                                if own_air == 0:
                                    if price_own_air9 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air9
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - 7¼6 RM-10 BOMBUSHKA §Ù§Ñ ' + str(
                                            price_own_air9) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ã§Ñ§Þ§à§Ý§×§ä! ”9ý5'
                            elif int(id_own) == 10:
                                if own_air == 0:
                                    if price_own_air10 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air10
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - 7¼6 AVENGER ¡ª HYV §Ù§Ñ ' + str(price_own_air10) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ã§Ñ§Þ§à§Ý§×§ä! ”9ý5'
                            elif int(id_own) == 11:
                                if own_air == 0:
                                    if price_own_air11 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air11
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - 7¼6 F-16 Fighting Falcon §Ù§Ñ ' + str(price_own_air11) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ã§Ñ§Þ§à§Ý§×§ä! ”9ý5'
                            elif int(id_own) == 12:
                                if own_air == 0:
                                    if price_own_air12 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air12
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - 7¼6 RM-10 BOMBUSHKA §Ù§Ñ ' + str(price_own_air12) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ã§Ñ§Þ§à§Ý§×§ä! ”9ý5'
                            elif int(id_own) == 13:
                                if own_air == 0:
                                    if price_own_air13 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air13
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - 7¼6 TULA ¡ª MAMMOTH §Ù§Ñ ' + str(price_own_air13) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ã§Ñ§Þ§à§Ý§×§ä! ”9ý5'
                            elif int(id_own) == 14:
                                if own_air == 0:
                                    if price_own_air14 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air14
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - 7¼6 V-65 MOLOTOK §Ù§Ñ ' + str(price_own_air14) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ã§Ñ§Þ§à§Ý§×§ä! ”9ý5'
                            elif int(id_own) == 15:
                                if own_air == 0:
                                    if price_own_air15 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air15
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - 7¼6 MOGUL ¡ª MAMMOTH §Ù§Ñ ' + str(price_own_air15) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ã§Ñ§Þ§à§Ý§×§ä! ”9ý5'
                            else:
                                return ', §ã§Ñ§Þ§à§Ý§×§ä§Ñ §ã §ä§Ñ§Ü§Ú§Þ ID §ß§Ö §ã§å§ë§Ö§ã§ä§Ó§å§Ö§ä! ”9þ6'
                        else:
                            return ', §ã§Ú§Þ§Ó§à§Ý§í §Ú §Ò§å§Ü§Ó§í §Ù§Ñ§á§â§Ö§ë§Ö§ß§í! ”9þ6'
                    else:
                        return ', §Õ§Ý§ñ §á§à§Ü§å§á§Ü§Ú §ä§â§Ñ§ß§ã§á§à§â§ä§Ñ §ß§Ö§à§Ò§ç§à§Õ§Ú§Þ §Õ§à§Þ! ”9ý5'
                elif sourceText.split()[1].lower() in ['§Ó§Ö§â§ä§à§Ý§×§ä', '§Ó§Ö§â§ä§à§Ý§Ö§ä', '§Ó§Ö§â§ä§à§Ý§×§ä§í', '§Ó§Ö§â§ä§à§Ý§Ö§ä§í']:
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
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •0‹5 Eurocopter EC130/135/14 §Ù§Ñ ' + str(price_own_helicopter1) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Ó§Ö§â§ä§à§Ý§×§ä! ”9ý5'
                            elif int(id_own) == 2:
                                if own_helicopter == 0:
                                    if price_own_helicopter2 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter2
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •0‹5 Boeing MH-6 §Ù§Ñ ' + str(price_own_helicopter2) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Ó§Ö§â§ä§à§Ý§×§ä! ”9ý5'

                            elif int(id_own) == 3:
                                if own_helicopter == 0:
                                    if price_own_helicopter3 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter3
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •0‹5 Sikorsky UH-60 §Ù§Ñ ' + str(price_own_helicopter3) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Ó§Ö§â§ä§à§Ý§×§ä! ”9ý5'
                            elif int(id_own) == 4:
                                if own_helicopter == 0:
                                    if price_own_helicopter4 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter4
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •0‹5 HAVOK ¡ª NAGASAKI §Ù§Ñ ' + str(price_own_helicopter4) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Ó§Ö§â§ä§à§Ý§×§ä! ”9ý5'

                            elif int(id_own) == 5:
                                if own_helicopter == 0:
                                    if price_own_helicopter5 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter5
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •0‹5 Eurocopter EC145 §Ù§Ñ ' + str(price_own_helicopter5) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Ó§Ö§â§ä§à§Ý§×§ä! ”9ý5'
                            elif int(id_own) == 6:
                                if own_helicopter == 0:
                                    if price_own_helicopter6 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter6
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •0‹5 Airbus H160 §Ù§Ñ ' + str(price_own_helicopter6) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Ó§Ö§â§ä§à§Ý§×§ä! ”9ý5'
                            elif int(id_own) == 7:
                                if own_helicopter == 0:
                                    if price_own_helicopter7 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter7
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •0‹5 Mil Mi-24 §Ù§Ñ ' + str(price_own_helicopter7) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Ó§Ö§â§ä§à§Ý§×§ä! ”9ý5'
                            elif int(id_own) == 8:
                                if own_helicopter == 0:
                                    if price_own_helicopter8 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter8
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •0‹5 POLICE MAVERICK §Ù§Ñ ' + str(price_own_helicopter8) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Ó§Ö§â§ä§à§Ý§×§ä! ”9ý5'
                            elif int(id_own) == 9:
                                if own_helicopter == 0:
                                    if price_own_helicopter9 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter9
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •0‹5 MAVERICK §Ù§Ñ ' + str(price_own_helicopter9) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Ó§Ö§â§ä§à§Ý§×§ä! ”9ý5'
                            else:
                                return ', §Ó§Ö§â§ä§à§Ý§×§ä§Ñ §ã §ä§Ñ§Ü§Ú§Þ ID §ß§Ö §ã§å§ë§Ö§ã§ä§Ó§å§Ö§ä! ”9þ6'
                        else:
                            return ', §ã§Ú§Þ§Ó§à§Ý§í §Ú §Ò§å§Ü§Ó§í §Ù§Ñ§á§â§Ö§ë§Ö§ß§í! ”9þ6'
                    else:
                        return ', §Õ§Ý§ñ §á§à§Ü§å§á§Ü§Ú §ä§â§Ñ§ß§ã§á§à§â§ä§Ñ §ß§Ö§à§Ò§ç§à§Õ§Ú§Þ §Õ§à§Þ! ”9ý5'
                elif sourceText.split()[1].lower() in ['§æ§Ö§â§Þ§Ñ', '§æ§Ö§â§Þ§í']:
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
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9ä1 Miner §Ù§Ñ ' + str(price_own_farm1) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §æ§Ö§â§Þ§Ñ! ”9ý5'
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
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9ä1 Miner S §Ù§Ñ ' + str(price_own_farm2) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §æ§Ö§â§Þ§Ñ! ”9ý5'

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
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9ä1 Miner X §Ù§Ñ ' + str(price_own_farm3) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §æ§Ö§â§Þ§Ñ! ”9ý5'
                            else:
                                return ', §æ§Ö§â§Þ§í §ã §ä§Ñ§Ü§Ú§Þ ID §ß§Ö §ã§å§ë§Ö§ã§ä§Ó§å§Ö§ä! ”9þ6'
                        else:
                            return ', §ã§Ú§Þ§Ó§à§Ý§í §Ú §Ò§å§Ü§Ó§í §Ù§Ñ§á§â§Ö§ë§Ö§ß§í! ”9þ6'
                    else:
                        return ', §Õ§Ý§ñ §á§à§Ü§å§á§Ü§Ú §æ§Ö§â§Þ§í §ß§Ö§à§Ò§ç§à§Õ§Ú§Þ §Õ§à§Þ! ”9ý5'
                elif sourceText.split()[1].lower() in ['§Ü§à§Þ§á', '§Ü§à§Þ§á§î§ð§ä§Ö§â', '§ß§à§å§ä', '§ß§à§å§ä§Ò§å§Ü', '§Ü§à§Þ§á§í','§Ü§à§Þ§á§î§ð§ä§Ö§â§í', '§ß§à§å§ä§í', '§ß§à§å§ä§Ò§å§Ü§Ú']:
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
                                    return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9ó5 Book §Ù§Ñ ' + str(price_own_comp1) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                else:
                                    return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                            else:
                                return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Ü§à§Þ§á§î§ð§ä§Ö§â! ”9ý5'
                        elif int(id_own) == 2:
                            if own_comp == 0:
                                if price_own_comp2 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_comp2
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_comp": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9ó5 Book Air §Ù§Ñ ' + str(price_own_comp2) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                else:
                                    return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                            else:
                                return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Ü§à§Þ§á§î§ð§ä§Ö§â! ”9ý5'

                        elif int(id_own) == 3:
                            if own_comp == 0:
                                if price_own_comp3 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_comp3
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_comp": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9ó5 Book Pro §Ù§Ñ ' + str(price_own_comp3) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                else:
                                    return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                            else:
                                return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Ü§à§Þ§á§î§ð§ä§Ö§â! ”9ý5'
                        else:
                            return ', §Ü§à§Þ§á§î§ð§ä§Ö§â§Ñ §ã §ä§Ñ§Ü§Ú§Þ ID §ß§Ö §ã§å§ë§Ö§ã§ä§Ó§å§Ö§ä! ”9þ6'
                    else:
                        return ', §ã§Ú§Þ§Ó§à§Ý§í §Ú §Ò§å§Ü§Ó§í §Ù§Ñ§á§â§Ö§ë§Ö§ß§í! ”9þ6'
                elif sourceText.split()[1].lower() in ['§ä§Ö§Ý§Ö§æ§à§ß', '§ã§Þ§Ñ§â§ä§æ§à§ß', '§ä§Ö§Ý§Ö§æ§à§ß§í', '§ã§Þ§Ñ§â§ä§æ§à§ß§í']:
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
                                    return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9á5 iPhone §Ù§Ñ ' + str(price_own_smart1) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                else:
                                    return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                            else:
                                return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ã§Þ§Ñ§â§ä§æ§à§ß! ”9ý5'
                        elif int(id_own) == 2:
                            if own_smart == 0:
                                if price_own_smart2 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_smart2
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_smart": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9á5 iPhone Pro §Ù§Ñ ' + str(price_own_smart2) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                else:
                                    return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                            else:
                                return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ã§Þ§Ñ§â§ä§æ§à§ß! ”9ý5'

                        elif int(id_own) == 3:
                            if own_smart == 0:
                                if price_own_smart3 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_smart3
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_smart": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9á5 iPhone Pro Max §Ù§Ñ ' + str(price_own_smart3) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                else:
                                    return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                            else:
                                return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ã§Þ§Ñ§â§ä§æ§à§ß! ”9ý5'
                        else:
                            return ', §ã§Þ§Ñ§â§ä§æ§à§ß§Ñ §ã §ä§Ñ§Ü§Ú§Þ ID §ß§Ö §ã§å§ë§Ö§ã§ä§Ó§å§Ö§ä! ”9þ6'
                    elif sourceText.split()[1].lower() in ['§ä§Ö§Ý§Ö§æ§à§ß', '§ã§Þ§Ñ§â§ä§æ§à§ß', '§ä§Ö§Ý§Ö§æ§à§ß§í', '§ã§Þ§Ñ§â§ä§æ§à§ß§í']:
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
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9á5 iPhone §Ù§Ñ ' + str(
                                            price_own_smart1) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ã§Þ§Ñ§â§ä§æ§à§ß! ”9ý5'
                            elif int(id_own) == 2:
                                if own_smart == 0:
                                    if price_own_smart2 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_smart2
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_smart": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9á5 iPhone Pro §Ù§Ñ ' + str(
                                            price_own_smart2) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ã§Þ§Ñ§â§ä§æ§à§ß! ”9ý5'

                            elif int(id_own) == 3:
                                if own_smart == 0:
                                    if price_own_smart3 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_smart3
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_smart": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9á5 iPhone Pro Max §Ù§Ñ ' + str(
                                            price_own_smart3) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ã§Þ§Ñ§â§ä§æ§à§ß! ”9ý5'
                            else:
                                return ', §ã§Þ§Ñ§â§ä§æ§à§ß§Ñ §ã §ä§Ñ§Ü§Ú§Þ ID §ß§Ö §ã§å§ë§Ö§ã§ä§Ó§å§Ö§ä! ”9þ6'
                    else:
                        return ', §ã§Ú§Þ§Ó§à§Ý§í §Ú §Ò§å§Ü§Ó§í §Ù§Ñ§á§â§Ö§ë§Ö§ß§í! ”9þ6'
                else:
                    return ', §ä§Ñ§Ü§à§Û §Ü§Ñ§ä§Ö§Ô§à§â§Ú§Ú §ß§Ö §ã§å§ë§Ö§ã§ä§Ó§å§Ö§ä! ”9þ6'
            else:
                return shopHelp
        else:
            return None
    passet_data, users_dir + str(id) + ".json")
                                    return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸ  Ð”ÐµÑ€ÐµÐ²ÑÐ½Ð½Ñ‹Ð¹ Ð´Ð¾Ð¼Ð¸Ðº Ð·Ð° ' + str(price_own_housing6) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                            else:
                                return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ Ð´Ð¾Ð¼! ðŸ˜‰'
                        elif int(id_own) == 7:
                            if own_housing == 0:
                                if price_own_housing7 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing7
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸ  ÐšÐ¸Ñ€Ð¿Ð¸Ñ‡Ð½Ñ‹Ð¹ Ð´Ð¾Ð¼ Ð·Ð° ' + str(price_own_housing7) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                            else:
                                return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ Ð´Ð¾Ð¼! ðŸ˜‰'
                        elif int(id_own) == 8:
                            if own_housing == 0:
                                if price_own_housing8 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing8
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸ  ÐšÐ¾Ñ‚Ñ‚ÐµÐ´Ð¶ Ð·Ð° ' + str(price_own_housing8) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                            else:
                                return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ Ð´Ð¾Ð¼! ðŸ˜‰'
                        elif int(id_own) == 9:
                            if own_housing == 0:
                                if price_own_housing9 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing9
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸ  Ð”Ð¾Ð¼ Ð½Ð° ÐŸÑƒÐ¼Ð°Ð²ÑƒÐ´Ðµ Ð·Ð° ' + str(price_own_housing9) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                            else:
                                return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ Ð´Ð¾Ð¼! ðŸ˜‰'
                        elif int(id_own) == 10:
                            if own_housing == 0:
                                if price_own_housing10 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing10
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸ  Ð’Ð¸Ð»Ð»Ñƒ Ð½Ð° ÐŸÑƒÐ¼Ð°Ð²ÑƒÐ´Ðµ Ð·Ð° ' + str(price_own_housing10) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                            else:
                                return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ Ð´Ð¾Ð¼! ðŸ˜‰'
                        elif int(id_own) == 11:
                            if own_housing == 0:
                                if price_own_housing11 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing11
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸ  Ð›Ð¸Ñ‡Ð½Ñ‹Ð¹ Ð¾ÑÑ‚Ñ€Ð¾Ð² Ð·Ð° ' + str(price_own_housing11) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                            else:
                                return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ Ð´Ð¾Ð¼! ðŸ˜‰'
                        else:
                            return ', Ð´Ð¾Ð¼Ð° Ñ Ñ‚Ð°ÐºÐ¸Ð¼ ID Ð½Ðµ ÑÑƒÑ‰ÐµÑÑ‚Ð²ÑƒÐµÑ‚! ðŸ˜”'
                    else:
                        return ', ÑÐ¸Ð¼Ð²Ð¾Ð»Ñ‹ Ð¸ Ð±ÑƒÐºÐ²Ñ‹ Ð·Ð°Ð¿Ñ€ÐµÑ‰ÐµÐ½Ñ‹! ðŸ˜”'

                elif sourceText.split()[1].lower() in ['Ð¼Ð°ÑˆÐ¸Ð½Ð°', 'Ð¼Ð°ÑˆÐ¸Ð½Ñ‹']:
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
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸš— Ð’ÐµÐ»Ð¾ÑÐ¸Ð¿ÐµÐ´ Ð·Ð° ' + str(price_own_car1) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ Ð¼Ð°ÑˆÐ¸Ð½Ð°! ðŸ˜‰'
                            elif int(id_own) == 2:
                                if own_car == 0:
                                    if price_own_car2 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car2
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸš— Ð“Ð¸Ñ€Ð¾ÑÐºÑƒÑ‚ÐµÑ€ Ð·Ð° ' + str(price_own_car2) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ Ð¼Ð°ÑˆÐ¸Ð½Ð°! ðŸ˜‰'

                            elif int(id_own) == 3:
                                if own_car == 0:
                                    if price_own_car3 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car3
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸ Ducati Scrambler Ð·Ð° ' + str(price_own_car3) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ Ð¼Ð°ÑˆÐ¸Ð½Ð°! ðŸ˜‰'
                            elif int(id_own) == 4:
                                if own_car == 0:
                                    if price_own_car4 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car4
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸ Honda CTX1300 Ð·Ð° ' + str(price_own_car4) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ Ð¼Ð°ÑˆÐ¸Ð½Ð°! ðŸ˜‰'

                            elif int(id_own) == 5:
                                if own_car == 0:
                                    if price_own_car5 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car5
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸš— Ferrari California front Ð·Ð° ' + str(price_own_car5) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ Ð¼Ð°ÑˆÐ¸Ð½Ð°! ðŸ˜‰'
                            elif int(id_own) == 6:
                                if own_car == 0:
                                    if price_own_car6 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car6
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸš— Porsche 911 Ð·Ð° ' + str(price_own_car6) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ Ð¼Ð°ÑˆÐ¸Ð½Ð°! ðŸ˜‰'
                            elif int(id_own) == 7:
                                if own_car == 0:
                                    if price_own_car7 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car7
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸš— Nissan GT-R Ð·Ð° ' + str(price_own_car7) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ Ð¼Ð°ÑˆÐ¸Ð½Ð°! ðŸ˜‰'
                            elif int(id_own) == 8:
                                if own_car == 0:
                                    if price_own_car8 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car8
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸš— BMW X6 Ð·Ð° ' + str(price_own_car8) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ Ð¼Ð°ÑˆÐ¸Ð½Ð°! ðŸ˜‰'
                            elif int(id_own) == 9:
                                if own_car == 0:
                                    if price_own_car9 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car9
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸš— Jaguar F-Type Ð·Ð° ' + str(price_own_car9) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ Ð¼Ð°ÑˆÐ¸Ð½Ð°! ðŸ˜‰'
                            elif int(id_own) == 10:
                                if own_car == 0:
                                    if price_own_car10 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car10
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸš— Lamborghini HuracÃ¡n Ð·Ð° ' + str(price_own_car10) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ Ð¼Ð°ÑˆÐ¸Ð½Ð°! ðŸ˜‰'
                            elif int(id_own) == 11:
                                if own_car == 0:
                                    if price_own_car11 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car11
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸš— Lamborghini Gallardo Ð·Ð° ' + str(price_own_car11) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ Ð¼Ð°ÑˆÐ¸Ð½Ð°! ðŸ˜‰'
                            elif int(id_own) == 12:
                                if own_car == 0:
                                    if price_own_car12 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car12
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸš— Ferrari F80 Concept Ð·Ð° ' + str(price_own_car12) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ Ð¼Ð°ÑˆÐ¸Ð½Ð°! ðŸ˜‰'
                            elif int(id_own) == 13:
                                if own_car == 0:
                                    if price_own_car13 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car13
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸš— Lamborghini Sesto Ð·Ð° ' + str(price_own_car13) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ Ð¼Ð°ÑˆÐ¸Ð½Ð°! ðŸ˜‰'
                            elif int(id_own) == 14:
                                if own_car == 0:
                                    if price_own_car14 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car14
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸš— Various Ford-based trucks Ð·Ð° ' + str(price_own_car14) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ Ð¼Ð°ÑˆÐ¸Ð½Ð°! ðŸ˜‰'
                            elif int(id_own) == 15:
                                if own_car == 0:
                                    if price_own_car15 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car15
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸš— Tesla Cybertruck Ð·Ð° ' + str(price_own_car15) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ Ð¼Ð°ÑˆÐ¸Ð½Ð°! ðŸ˜‰'
                            else:
                                return ', Ð¼Ð°ÑˆÐ¸Ð½Ñ‹ Ñ Ñ‚Ð°ÐºÐ¸Ð¼ ID Ð½Ðµ ÑÑƒÑ‰ÐµÑÑ‚Ð²ÑƒÐµÑ‚! ðŸ˜”'
                        else:
                            return ', ÑÐ¸Ð¼Ð²Ð¾Ð»Ñ‹ Ð¸ Ð±ÑƒÐºÐ²Ñ‹ Ð·Ð°Ð¿Ñ€ÐµÑ‰ÐµÐ½Ñ‹! ðŸ˜”'
                    else:
                        return ', Ð´Ð»Ñ Ð¿Ð¾ÐºÑƒÐ¿ÐºÐ¸ Ñ‚Ñ€Ð°Ð½ÑÐ¿Ð¾Ñ€Ñ‚Ð° Ð½ÐµÐ¾Ð±Ñ…Ð¾Ð´Ð¸Ð¼Ð¾ Ð´Ð¾Ð¼! ðŸ˜‰'
                elif sourceText.split()[1].lower() in ['ÑÑ…Ñ‚Ð°', 'ÑÑ…Ñ‚Ñ‹']:
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
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸ›¥ RHIB Ð·Ð° ' + str(price_own_yacht1) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ ÑÑ…Ñ‚Ð°! ðŸ˜‰'
                            elif int(id_own) == 2:
                                if own_yacht == 0:
                                    if price_own_yacht2 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht2
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸ›¥ Kawasaki Ð·Ð° ' + str(price_own_yacht2) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ ÑÑ…Ñ‚Ð°! ðŸ˜‰'

                            elif int(id_own) == 3:
                                if own_yacht == 0:
                                    if price_own_yacht3 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht3
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸ›¥ Riva Aquarama Ð·Ð° ' + str(price_own_yacht3) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ ÑÑ…Ñ‚Ð°! ðŸ˜‰'
                            elif int(id_own) == 4:
                                if own_yacht == 0:
                                    if price_own_yacht4 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht4
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸ›¥ Various Ð·Ð° ' + str(price_own_yacht4) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ ÑÑ…Ñ‚Ð°! ðŸ˜‰'

                            elif int(id_own) == 5:
                                if own_yacht == 0:
                                    if price_own_yacht5 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht5
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸ›¥ Ð rinÑÐµss 60 Ð·Ð° ' + str(price_own_yacht5) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ ÑÑ…Ñ‚Ð°! ðŸ˜‰'
                            elif int(id_own) == 6:
                                if own_yacht == 0:
                                    if price_own_yacht6 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht6
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸ›¥ Ðzimut 70 Ð·Ð° ' + str(price_own_yacht6) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ ÑÑ…Ñ‚Ð°! ðŸ˜‰'
                            elif int(id_own) == 7:
                                if own_yacht == 0:
                                    if price_own_yacht7 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht7
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸ›¥ DÐ¾minÐ°tÐ¾r 40M Ð·Ð° ' + str(price_own_yacht7) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ ÑÑ…Ñ‚Ð°! ðŸ˜‰'
                            elif int(id_own) == 8:
                                if own_yacht == 0:
                                    if price_own_yacht8 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht8
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸ›¥ MÐ¾Ð¾nÐµn 124 Ð·Ð° ' + str(price_own_yacht8) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ ÑÑ…Ñ‚Ð°! ðŸ˜‰'
                            elif int(id_own) == 9:
                                if own_yacht == 0:
                                    if price_own_yacht9 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht9
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸ›¥ WidÐµr 150 Ð·Ð° ' + str(price_own_yacht9) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ ÑÑ…Ñ‚Ð°! ðŸ˜‰'
                            elif int(id_own) == 10:
                                if own_yacht == 0:
                                    if price_own_yacht10 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht10
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸ›¥ Palmer JÐ¾hnsÐ¾n 42M SuÑ€ÐµrSÑ€Ð¾rt Ð·Ð° ' + str(
                                            price_own_yacht10) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ ÑÑ…Ñ‚Ð°! ðŸ˜‰'
                            elif int(id_own) == 11:
                                if own_yacht == 0:
                                    if price_own_yacht11 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht11
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸ›¥ WidÐµr 165 Ð·Ð° ' + str(price_own_yacht11) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ ÑÑ…Ñ‚Ð°! ðŸ˜‰'
                            elif int(id_own) == 12:
                                if own_yacht == 0:
                                    if price_own_yacht12 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht12
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸ›¥ Ð•ÑliÑ€sÐµ Ð·Ð° ' + str(price_own_yacht12) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ ÑÑ…Ñ‚Ð°! ðŸ˜‰'
                            elif int(id_own) == 13:
                                if own_yacht == 0:
                                    if price_own_yacht13 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht13
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸ›¥ DubÐ°i Ð·Ð° ' + str(price_own_yacht13) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ ÑÑ…Ñ‚Ð°! ðŸ˜‰'
                            elif int(id_own) == 14:
                                if own_yacht == 0:
                                    if price_own_yacht14 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht14
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸ›¥ StrÐµÐµts Ð¾f MÐ¾nÐ°ÑÐ¾ Ð·Ð° ' + str(price_own_yacht14) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ ÑÑ…Ñ‚Ð°! ðŸ˜‰'
                            else:
                                return ', ÑÑ…Ñ‚Ñ‹ Ñ Ñ‚Ð°ÐºÐ¸Ð¼ ID Ð½Ðµ ÑÑƒÑ‰ÐµÑÑ‚Ð²ÑƒÐµÑ‚! ðŸ˜”'
                        else:
                            return ', ÑÐ¸Ð¼Ð²Ð¾Ð»Ñ‹ Ð¸ Ð±ÑƒÐºÐ²Ñ‹ Ð·Ð°Ð¿Ñ€ÐµÑ‰ÐµÐ½Ñ‹! ðŸ˜”'
                    else:
                        return ', Ð´Ð»Ñ Ð¿Ð¾ÐºÑƒÐ¿ÐºÐ¸ Ñ‚Ñ€Ð°Ð½ÑÐ¿Ð¾Ñ€Ñ‚Ð° Ð½ÐµÐ¾Ð±Ñ…Ð¾Ð´Ð¸Ð¼ Ð´Ð¾Ð¼! ðŸ˜‰'
                elif sourceText.split()[1].lower() in ['ÑÐ°Ð¼Ð¾Ð»Ñ‘Ñ‚', 'ÑÐ°Ð¼Ð¾Ð»ÐµÑ‚', 'ÑÐ°Ð¼Ð¾Ð»Ñ‘Ñ‚Ñ‹', 'ÑÐ°Ð¼Ð¾Ð»ÐµÑ‚Ñ‹']:
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
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - âœˆ de Havilland Canada DHC-2 Ð·Ð° ' + str(price_own_air1) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ ÑÐ°Ð¼Ð¾Ð»Ñ‘Ñ‚! ðŸ˜‰'
                            elif int(id_own) == 2:
                                if own_air == 0:
                                    if price_own_air2 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air2
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - âœˆ Piper PA-46 Ð·Ð° ' + str(price_own_air2) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ ÑÐ°Ð¼Ð¾Ð»Ñ‘Ñ‚! ðŸ˜‰'

                            elif int(id_own) == 3:
                                if own_air == 0:
                                    if price_own_air3 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air3
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - âœˆ Cessna 310 Ð·Ð° ' + str(price_own_air3) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ ÑÐ°Ð¼Ð¾Ð»Ñ‘Ñ‚! ðŸ˜‰'
                            elif int(id_own) == 4:
                                if own_air == 0:
                                    if price_own_air4 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air4
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - âœˆ Learjet 55 Ð·Ð° ' + str(price_own_air4) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ ÑÐ°Ð¼Ð¾Ð»Ñ‘Ñ‚! ðŸ˜‰'

                            elif int(id_own) == 5:
                                if own_air == 0:
                                    if price_own_air5 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air5
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - âœˆ Bombardier Global Express Ð·Ð° ' + str(price_own_air5) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ ÑÐ°Ð¼Ð¾Ð»Ñ‘Ñ‚! ðŸ˜‰'
                            elif int(id_own) == 6:
                                if own_air == 0:
                                    if price_own_air6 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air6
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - âœˆ Cessna Citation X Ð·Ð° ' + str(price_own_air6) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ ÑÐ°Ð¼Ð¾Ð»Ñ‘Ñ‚! ðŸ˜‰'
                            elif int(id_own) == 7:
                                if own_air == 0:
                                    if price_own_air7 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air7
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - âœˆ C-130 Ð·Ð° ' + str(price_own_air7) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ ÑÐ°Ð¼Ð¾Ð»Ñ‘Ñ‚! ðŸ˜‰'
                            elif int(id_own) == 8:
                                if own_air == 0:
                                    if price_own_air8 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air8
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - âœˆ VOLATOL Ð·Ð° ' + str(price_own_air8) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ ÑÐ°Ð¼Ð¾Ð»Ñ‘Ñ‚! ðŸ˜‰'
                            elif int(id_own) == 9:
                                if own_air == 0:
                                    if price_own_air9 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air9
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - âœˆ RM-10 BOMBUSHKA Ð·Ð° ' + str(
                                            price_own_air9) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ ÑÐ°Ð¼Ð¾Ð»Ñ‘Ñ‚! ðŸ˜‰'
                            elif int(id_own) == 10:
                                if own_air == 0:
                                    if price_own_air10 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air10
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - âœˆ AVENGER â€” HYV Ð·Ð° ' + str(price_own_air10) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ ÑÐ°Ð¼Ð¾Ð»Ñ‘Ñ‚! ðŸ˜‰'
                            elif int(id_own) == 11:
                                if own_air == 0:
                                    if price_own_air11 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air11
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - âœˆ F-16 Fighting Falcon Ð·Ð° ' + str(price_own_air11) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ ÑÐ°Ð¼Ð¾Ð»Ñ‘Ñ‚! ðŸ˜‰'
                            elif int(id_own) == 12:
                                if own_air == 0:
                                    if price_own_air12 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air12
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - âœˆ RM-10 BOMBUSHKA Ð·Ð° ' + str(price_own_air12) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ ÑÐ°Ð¼Ð¾Ð»Ñ‘Ñ‚! ðŸ˜‰'
                            elif int(id_own) == 13:
                                if own_air == 0:
                                    if price_own_air13 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air13
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - âœˆ TULA â€” MAMMOTH Ð·Ð° ' + str(price_own_air13) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ ÑÐ°Ð¼Ð¾Ð»Ñ‘Ñ‚! ðŸ˜‰'
                            elif int(id_own) == 14:
                                if own_air == 0:
                                    if price_own_air14 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air14
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - âœˆ V-65 MOLOTOK Ð·Ð° ' + str(price_own_air14) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ ÑÐ°Ð¼Ð¾Ð»Ñ‘Ñ‚! ðŸ˜‰'
                            elif int(id_own) == 15:
                                if own_air == 0:
                                    if price_own_air15 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air15
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - âœˆ MOGUL â€” MAMMOTH Ð·Ð° ' + str(price_own_air15) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ ÑÐ°Ð¼Ð¾Ð»Ñ‘Ñ‚! ðŸ˜‰'
                            else:
                                return ', ÑÐ°Ð¼Ð¾Ð»Ñ‘Ñ‚Ð° Ñ Ñ‚Ð°ÐºÐ¸Ð¼ ID Ð½Ðµ ÑÑƒÑ‰ÐµÑÑ‚Ð²ÑƒÐµÑ‚! ðŸ˜”'
                        else:
                            return ', ÑÐ¸Ð¼Ð²Ð¾Ð»Ñ‹ Ð¸ Ð±ÑƒÐºÐ²Ñ‹ Ð·Ð°Ð¿Ñ€ÐµÑ‰ÐµÐ½Ñ‹! ðŸ˜”'
                    else:
                        return ', Ð´Ð»Ñ Ð¿Ð¾ÐºÑƒÐ¿ÐºÐ¸ Ñ‚Ñ€Ð°Ð½ÑÐ¿Ð¾Ñ€Ñ‚Ð° Ð½ÐµÐ¾Ð±Ñ…Ð¾Ð´Ð¸Ð¼ Ð´Ð¾Ð¼! ðŸ˜‰'
                elif sourceText.split()[1].lower() in ['Ð²ÐµÑ€Ñ‚Ð¾Ð»Ñ‘Ñ‚', 'Ð²ÐµÑ€Ñ‚Ð¾Ð»ÐµÑ‚', 'Ð²ÐµÑ€Ñ‚Ð¾Ð»Ñ‘Ñ‚Ñ‹', 'Ð²ÐµÑ€Ñ‚Ð¾Ð»ÐµÑ‚Ñ‹']:
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
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸš Eurocopter EC130/135/14 Ð·Ð° ' + str(price_own_helicopter1) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ Ð²ÐµÑ€Ñ‚Ð¾Ð»Ñ‘Ñ‚! ðŸ˜‰'
                            elif int(id_own) == 2:
                                if own_helicopter == 0:
                                    if price_own_helicopter2 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter2
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸš Boeing MH-6 Ð·Ð° ' + str(price_own_helicopter2) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ Ð²ÐµÑ€Ñ‚Ð¾Ð»Ñ‘Ñ‚! ðŸ˜‰'

                            elif int(id_own) == 3:
                                if own_helicopter == 0:
                                    if price_own_helicopter3 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter3
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸš Sikorsky UH-60 Ð·Ð° ' + str(price_own_helicopter3) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ Ð²ÐµÑ€Ñ‚Ð¾Ð»Ñ‘Ñ‚! ðŸ˜‰'
                            elif int(id_own) == 4:
                                if own_helicopter == 0:
                                    if price_own_helicopter4 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter4
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸš HAVOK â€” NAGASAKI Ð·Ð° ' + str(price_own_helicopter4) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ Ð²ÐµÑ€Ñ‚Ð¾Ð»Ñ‘Ñ‚! ðŸ˜‰'

                            elif int(id_own) == 5:
                                if own_helicopter == 0:
                                    if price_own_helicopter5 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter5
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸš Eurocopter EC145 Ð·Ð° ' + str(price_own_helicopter5) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ Ð²ÐµÑ€Ñ‚Ð¾Ð»Ñ‘Ñ‚! ðŸ˜‰'
                            elif int(id_own) == 6:
                                if own_helicopter == 0:
                                    if price_own_helicopter6 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter6
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸš Airbus H160 Ð·Ð° ' + str(price_own_helicopter6) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ Ð²ÐµÑ€Ñ‚Ð¾Ð»Ñ‘Ñ‚! ðŸ˜‰'
                            elif int(id_own) == 7:
                                if own_helicopter == 0:
                                    if price_own_helicopter7 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter7
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸš Mil Mi-24 Ð·Ð° ' + str(price_own_helicopter7) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ Ð²ÐµÑ€Ñ‚Ð¾Ð»Ñ‘Ñ‚! ðŸ˜‰'
                            elif int(id_own) == 8:
                                if own_helicopter == 0:
                                    if price_own_helicopter8 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter8
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸš POLICE MAVERICK Ð·Ð° ' + str(price_own_helicopter8) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ Ð²ÐµÑ€Ñ‚Ð¾Ð»Ñ‘Ñ‚! ðŸ˜‰'
                            elif int(id_own) == 9:
                                if own_helicopter == 0:
                                    if price_own_helicopter9 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter9
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸš MAVERICK Ð·Ð° ' + str(price_own_helicopter9) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ Ð²ÐµÑ€Ñ‚Ð¾Ð»Ñ‘Ñ‚! ðŸ˜‰'
                            else:
                                return ', Ð²ÐµÑ€Ñ‚Ð¾Ð»Ñ‘Ñ‚Ð° Ñ Ñ‚Ð°ÐºÐ¸Ð¼ ID Ð½Ðµ ÑÑƒÑ‰ÐµÑÑ‚Ð²ÑƒÐµÑ‚! ðŸ˜”'
                        else:
                            return ', ÑÐ¸Ð¼Ð²Ð¾Ð»Ñ‹ Ð¸ Ð±ÑƒÐºÐ²Ñ‹ Ð·Ð°Ð¿Ñ€ÐµÑ‰ÐµÐ½Ñ‹! ðŸ˜”'
                    else:
                        return ', Ð´Ð»Ñ Ð¿Ð¾ÐºÑƒÐ¿ÐºÐ¸ Ñ‚Ñ€Ð°Ð½ÑÐ¿Ð¾Ñ€Ñ‚Ð° Ð½ÐµÐ¾Ð±Ñ…Ð¾Ð´Ð¸Ð¼ Ð´Ð¾Ð¼! ðŸ˜‰'
                elif sourceText.split()[1].lower() in ['Ñ„ÐµÑ€Ð¼Ð°', 'Ñ„ÐµÑ€Ð¼Ñ‹']:
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
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸ”‹ Miner Ð·Ð° ' + str(price_own_farm1) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ Ñ„ÐµÑ€Ð¼Ð°! ðŸ˜‰'
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
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸ”‹ Miner S Ð·Ð° ' + str(price_own_farm2) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ Ñ„ÐµÑ€Ð¼Ð°! ðŸ˜‰'

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
                                        return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸ”‹ Miner X Ð·Ð° ' + str(price_own_farm3) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                    else:
                                        return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ Ñ„ÐµÑ€Ð¼Ð°! ðŸ˜‰'
                            else:
                                return ', Ñ„ÐµÑ€Ð¼Ñ‹ Ñ Ñ‚Ð°ÐºÐ¸Ð¼ ID Ð½Ðµ ÑÑƒÑ‰ÐµÑÑ‚Ð²ÑƒÐµÑ‚! ðŸ˜”'
                        else:
                            return ', ÑÐ¸Ð¼Ð²Ð¾Ð»Ñ‹ Ð¸ Ð±ÑƒÐºÐ²Ñ‹ Ð·Ð°Ð¿Ñ€ÐµÑ‰ÐµÐ½Ñ‹! ðŸ˜”'
                    else:
                        return ', Ð´Ð»Ñ Ð¿Ð¾ÐºÑƒÐ¿ÐºÐ¸ Ñ„ÐµÑ€Ð¼Ñ‹ Ð½ÐµÐ¾Ð±Ñ…Ð¾Ð´Ð¸Ð¼ Ð´Ð¾Ð¼! ðŸ˜‰'
                elif sourceText.split()[1].lower() in ['ÐºÐ¾Ð¼Ð¿', 'ÐºÐ¾Ð¼Ð¿ÑŒÑŽÑ‚ÐµÑ€', 'Ð½Ð¾ÑƒÑ‚', 'Ð½Ð¾ÑƒÑ‚Ð±ÑƒÐº', 'ÐºÐ¾Ð¼Ð¿Ñ‹','ÐºÐ¾Ð¼Ð¿ÑŒÑŽÑ‚ÐµÑ€Ñ‹', 'Ð½Ð¾ÑƒÑ‚Ñ‹', 'Ð½Ð¾ÑƒÑ‚Ð±ÑƒÐºÐ¸']:
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
                                    return ', Ð²Ñ‹ ÑƒÑÐ¿ÐµÑˆÐ½Ð¾ Ð¿Ñ€ÐµÐ¾Ð±Ñ€ÐµÐ»Ð¸ - ðŸ–¥ Book Ð·Ð° ' + str(price_own_comp1) + 'â‚¬!\nðŸ’° Ð’Ð°Ñˆ Ð±Ð°Ð»Ð°Ð½Ñ: ' + str(algo_buy_own) + 'â‚¬'
                                else:
                                    return ', Ñƒ Ð²Ð°Ñ Ð½ÐµÐ´Ð¾ÑÑ‚Ð°Ñ‚Ð¾Ñ‡Ð½Ð¾ Ð´ÐµÐ½ÐµÐ³! ðŸ˜”'
                            else:
                                return ', Ñƒ Ð²Ð°Ñ ÑƒÐ¶Ðµ ÐµÑÑ‚ÑŒ ÐºÐ¾Ð¼Ð¿ÑŒÑŽÑ‚ÐµÑ€! ðŸ˜‰'
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

    shopHelp = ', §á§à§Þ§à§ë§î §á§à §Þ§Ñ§Ô§Ñ§Ù§Ú§ß§å:\n\n7Õ4•0“6 §±§à§Ü§å§á§Ñ§Û§ä§Ö §â§Ñ§Ù§Ý§Ú§é§ß§à§Ö §Ú§Þ§å§ë§Ö§ã§ä§Ó§à §Ó §à§Õ§Ú§ß §Ü§Ý§Ú§Ü! §±§à§ã§Ý§Ö §á§à§Ü§å§á§Ü§Ú §Õ§à§Þ§Ñ, §Ó§í §ã§Þ§à§Ø§Ö§ä§Ö §á§â§Ö§à§Ò§â§Ö§ã§ä§Ú §ä§â§Ñ§ß§ã§á§à§â§ä §Ú §æ§Ö§â§Þ§å §Õ§Ý§ñ §Þ§Ñ§Û§ß§Ú§ß§Ô§Ñ §Ò§Ú§ä§Ü§à§Ú§ß§à§Ó.\n\n”9Ý8 §°§ã§ß§à§Ó§ß§à§Ö:\n7Õ47Õ4”9Æ2 §¥§à§Þ§Ñ\n7Õ47Õ4•07 §®§Ñ§ê§Ú§ß§í\n7Õ47Õ47¼6 §³§Ñ§Þ§à§Ý§×§ä§í\n7Õ47Õ4•0‹5 §£§Ö§â§ä§à§Ý§×§ä§í\n7Õ47Õ4•0•5 §Á§ç§ä§í\n\n”9Ù5 §°§ã§ä§Ñ§Ý§î§ß§à§Ö:\n7Õ47Õ4”9ó5 §¬§à§Þ§á§î§ð§ä§Ö§â§í\n7Õ47Õ4”9á5 §´§Ö§Ý§Ö§æ§à§ß§í\n7Õ47Õ4”9ä1 §¶§Ö§â§Þ§í\n\n7Ä1 §±§à§Þ§à§ë§î:\n7Õ47Õ4”9ä4 §®§Ñ§Ô§Ñ§Ù§Ú§ß [§Ü§Ñ§ä§Ö§Ô§à§â§Ú§ñ] - §ä§à§Ó§Ñ§â§í.\n7Õ47Õ4•0“6 §®§Ñ§Ô§Ñ§Ù§Ú§ß [§Ü§Ñ§ä§Ö§Ô§à§â§Ú§ñ] [§ß§à§Þ§Ö§â] - §Ü§å§á§Ú§ä§î §ä§à§Ó§Ñ§â.'

    if sourceText != '':
        if '§Þ§Ñ§Ô§Ñ§Ù§Ú§ß' == sourceText.split()[0].lower():
            if len(sourceText.split()) == 2:
                if sourceText.split()[1].lower() in ['§Õ§à§Þ', '§Õ§à§Þ§Ñ']:
                    return ', §ã§á§Ú§ã§à§Ü §Õ§à§ã§ä§å§á§ß§í§ç §Õ§à§Þ§à§Ó:\n\n7Õ4”9å0 §±§à§ã§Ý§Ö §á§à§Ü§å§á§Ü§Ú §Õ§à§Þ§Ñ, §Ó§í §ã§Þ§à§Ø§Ö§ä§Ö §Ü§å§á§Ú§ä§î §ä§â§Ñ§ß§ã§á§à§â§ä §Ú §æ§Ö§â§Þ§å!\n\n7Õ47Õ4”9Æ2 1. §¬§à§â§à§Ò§Ü§Ñ ¡ª 25.000¢ã\n7Õ47Õ4”9Æ2 2. §±§à§Õ§Ó§Ñ§Ý ¡ª 65.000¢ã\n7Õ47Õ4”9Æ2 3. §³§Ñ§â§Ñ§Û ¡ª 225.000¢ã\n7Õ47Õ4”9Æ2 4. §¤§Ñ§â§Ñ§Ø ¡ª 595.000¢ã\n7Õ47Õ4”9Æ2 5. §£§Ö§ä§ç§Ñ§ñ §ç§Ú§Ø§Ú§ß§Ñ ¡ª 655.000¢ã\n7Õ47Õ4”9Æ2 6. §¥§Ö§â§Ö§Ó§ñ§ß§ß§í§Û §Õ§à§Þ§Ú§Ü ¡ª 1.525.000¢ã\n7Õ47Õ4”9Æ2 7. §¬§Ú§â§á§Ú§é§ß§í§Û §Õ§à§Þ ¡ª 8.525.000¢ã\n7Õ47Õ4”9Æ2 8. §¬§à§ä§ä§Ö§Õ§Ø ¡ª 35.650.000¢ã\n7Õ47Õ4”9Æ2 9. §¥§à§Þ §ß§Ñ §±§å§Þ§Ñ§Ó§å§Õ§Ö ¡ª 68.250.000¢ã\n7Õ47Õ4”9Æ2 10. §£§Ú§Ý§Ý§Ñ §ß§Ñ §±§å§Þ§Ñ§Ó§å§Õ§Ö ¡ª 93.500.000¢ã\n7Õ47Õ4”9Æ2 11. §­§Ú§é§ß§í§Û §à§ã§ä§â§à§Ó ¡ª 999.999.999¢ã\n\n7Ä1 §¥§Ý§ñ §á§à§Ü§å§á§Ü§Ú §Õ§à§Þ§Ñ, §Ú§ã§á§à§Ý§î§Ù§å§Û§ä§Ö:\n7Õ47Õ4•0“6 §®§Ñ§Ô§Ñ§Ù§Ú§ß §Õ§à§Þ [§ß§à§Þ§Ö§â]'
                elif sourceText.split()[1].lower() in ['§Þ§Ñ§ê§Ú§ß§Ñ', '§Þ§Ñ§ê§Ú§ß§í']:
                    return ', §ã§á§Ú§ã§à§Ü §Õ§à§ã§ä§å§á§ß§í§ç §Þ§Ñ§ê§Ú§ß:\n\n7Õ4”9å0 §±§à§Ü§å§á§Ñ§Û§ä§Ö §ä§â§Ñ§ß§ã§á§à§â§ä §Ó §à§Õ§Ú§ß §Ü§Ý§Ú§Ü!\n\n7Õ47Õ4•07 1. §£§Ö§Ý§à§ã§Ú§á§Ö§Õ ¡ª 125.000¢ã\n7Õ47Õ4•07 2. §¤§Ú§â§à§ã§Ü§å§ä§Ö§â ¡ª 255.000¢ã\n7Õ47Õ4”9Ä3 3. Ducati Scrambler ¡ª 525.000¢ã\n7Õ47Õ4”9Ä3 4. Honda CTX1300 ¡ª 1.275.000¢ã\n7Õ47Õ4•07 5. Ferrari California front ¡ª 1.650.000¢ã\n7Õ47Õ4•07 6. Porsche 911 ¡ª 2.000.000¢ã\n7Õ47Õ4•07 7. Nissan GT-R ¡ª 4.350.000¢ã\n7Õ47Õ4•07 8. BMW X6 ¡ª 15.650.000¢ã\n7Õ47Õ4•07 9. Jaguar F-Type ¡ª 25.735.000¢ã\n7Õ47Õ4•07 10. Lamborghini Hurac¨¢n ¡ª 30.800.000¢ã\n7Õ47Õ4•07 11. Lamborghini Gallardo ¡ª 37.580.000¢ã\n7Õ47Õ4•07 12. Ferrari F80 Concept ¡ª 57.999.999¢ã\n7Õ47Õ4•07 13. Lamborghini Sesto ¡ª 108.555.000¢ã\n7Õ47Õ4•07 14. Various Ford-based trucks ¡ª 999.999.999¢ã\n7Õ47Õ4•07 15. Tesla Cybertruck ¡ª 1.500.000.000¢ã\n\n7Ä1 §¥§Ý§ñ §á§à§Ü§å§á§Ü§Ú §ä§â§Ñ§ß§ã§á§à§â§ä§Ñ, §Ú§ã§á§à§Ý§î§Ù§å§Û§ä§Ö:\n7Õ47Õ4•0“6 §®§Ñ§Ô§Ñ§Ù§Ú§ß §Þ§Ñ§ê§Ú§ß§Ñ [§ß§à§Þ§Ö§â]'
                elif sourceText.split()[1].lower() in ['§ñ§ç§ä§Ñ', '§ñ§ç§ä§í']:
                    return ', §ã§á§Ú§ã§à§Ü §Õ§à§ã§ä§å§á§ß§í§ç §ñ§ç§ä:\n\n7Õ47Õ4•0•5 1. RHIB ¡ª 575.000¢ã\n7Õ47Õ4•0•5 2. Kawasaki ¡ª 1.225.000¢ã\n7Õ47Õ4•0•5 3. Riva Aquarama ¡ª 2.500.000¢ã\n7Õ47Õ4•0•5 4. Various ¡ª 3.650.000¢ã\n7Õ47Õ4•0•5 5. §²rin§ã§Öss 60 ¡ª 8.355.000¢ã\n7Õ47Õ4•0•5 6. §¡zimut 70 ¡ª 12.850.000¢ã\n7Õ47Õ4•0•5 7. D§àmin§Ñt§àr 40M ¡ª 23.125.000¢ã\n7Õ47Õ4•0•5 8. M§à§àn§Ön 124 ¡ª 34.666.000¢ã\n7Õ47Õ4•0•5 9. Wid§Ör 150 ¡ª 66.225.000¢ã\n7Õ47Õ4•0•5 10. Palmer J§àhns§àn 42M Su§â§ÖrS§â§àrt ¡ª 96.000.000¢ã\n7Õ47Õ4•0•5 11. Wid§Ör 165 ¡ª 126.650.000¢ã\n7Õ47Õ4•0•5 12. §¦§ãli§âs§Ö ¡ª 527.777.777¢ã\n7Õ47Õ4•0•5 13. Dub§Ñi ¡ª 999.999.999¢ã\n7Õ47Õ4•0•5 14. Str§Ö§Öts §àf M§àn§Ñ§ã§à ¡ª 1.255.000.000¢ã\n\n7Ä1 §¥§Ý§ñ §á§à§Ü§å§á§Ü§Ú §ä§â§Ñ§ß§ã§á§à§â§ä§Ñ, §Ú§ã§á§à§Ý§î§Ù§å§Û§ä§Ö:\n7Õ47Õ4•0“6 §®§Ñ§Ô§Ñ§Ù§Ú§ß §ñ§ç§ä§Ñ [§ß§à§Þ§Ö§â]'
                elif sourceText.split()[1].lower() in ['§ã§Ñ§Þ§à§Ý§×§ä', '§ã§Ñ§Þ§à§Ý§Ö§ä', '§ã§Ñ§Þ§à§Ý§×§ä§í', '§ã§Ñ§Þ§à§Ý§Ö§ä§í']:
                    return ', §ã§á§Ú§ã§à§Ü §Õ§à§ã§ä§å§á§ß§í§ç §ã§Ñ§Þ§à§Ý§×§ä§à§Ó:\n\n7Õ4”9å0 §±§à§Ü§å§á§Ñ§Û§ä§Ö §ä§â§Ñ§ß§ã§á§à§â§ä §Ó §à§Õ§Ú§ß §Ü§Ý§Ú§Ü!\n\n7Õ47Õ47¼6 1. de Havilland Canada DHC-2 ¡ª 500.000¢ã\n7Õ47Õ47¼6 2. Piper PA-46 ¡ª 3.995.000¢ã\n7Õ47Õ47¼6 3. Cessna 310 ¡ª 6.350.000¢ã\n7Õ47Õ47¼6 4. Learjet 55 ¡ª 15.500.000¢ã\n7Õ47Õ47¼6 5. Bombardier Global Express ¡ª 17.800.000¢ã\n7Õ47Õ47¼6 6. Cessna Citation X ¡ª 22.250.000¢ã\n7Õ47Õ47¼6 7. C-130 ¡ª 43.000.000¢ã\n7Õ47Õ47¼6 8. VOLATOL ¡ª 65.505.000¢ã\n7Õ47Õ47¼6 9. RM-10 BOMBUSHKA ¡ª 75.985.000¢ã\n7Õ47Õ47¼6 10. AVENGER ¡ª HYV ¡ª 86.495.000¢ã\n7Õ47Õ47¼6 11. F-16 Fighting Falcon ¡ª 109.999.999¢ã\n7Õ47Õ47¼6 12. RM-10 BOMBUSHKA ¡ª 313.000.000¢ã\n7Õ47Õ47¼6 13. TULA ¡ª MAMMOTH ¡ª 617.555.000¢ã\n7Õ47Õ47¼6 14. V-65 MOLOTOK ¡ª 850.000.000¢ã\n7Õ47Õ47¼6 15. MOGUL ¡ª MAMMOTH ¡ª 2.000.000.000¢ã\n\n7Ä1 §¥§Ý§ñ §á§à§Ü§å§á§Ü§Ú §ä§â§Ñ§ß§ã§á§à§â§ä§Ñ, §Ú§ã§á§à§Ý§î§Ù§å§Û§ä§Ö:\n7Õ47Õ4•0“6 §®§Ñ§Ô§Ñ§Ù§Ú§ß §ã§Ñ§Þ§à§Ý§×§ä [§ß§à§Þ§Ö§â]'
                elif sourceText.split()[1].lower() in ['§Ó§Ö§â§ä§à§Ý§×§ä', '§Ó§Ö§â§ä§à§Ý§Ö§ä', '§Ó§Ö§â§ä§à§Ý§×§ä§í', '§Ó§Ö§â§ä§à§Ý§Ö§ä§í']:
                    return ', §ã§á§Ú§ã§à§Ü §Õ§à§ã§ä§å§á§ß§í§ç §Ó§Ö§â§ä§à§Ý§×§ä§à§Ó:\n\n7Õ4”9å0 §±§à§Ü§å§á§Ñ§Û§ä§Ö §ä§â§Ñ§ß§ã§á§à§â§ä §Ó §à§Õ§Ú§ß §Ü§Ý§Ú§Ü!\n\n7Õ47Õ4•0‹5 1. Eurocopter EC130/135/14 ¡ª 1.300.000¢ã\n7Õ47Õ4•0‹5 2. Boeing MH-6 ¡ª 1.750.000¢ã\n7Õ47Õ4•0‹5 3. Sikorsky UH-60 ¡ª 2.225.000¢ã\n7Õ47Õ4•0‹5 4. HAVOK ¡ª NAGASAKI ¡ª 3.500.000¢ã\n7Õ47Õ4•0‹5 5. Eurocopter EC145 ¡ª 8.850.000¢ã\n7Õ47Õ4•0‹5 6. Airbus H160 ¡ª 25.555.555¢ã\n7Õ47Õ4•0‹5 7. Mil Mi-24 ¡ª 58.000.000¢ã\n7Õ47Õ4•0‹5 8. POLICE MAVERICK ¡ª 215.000.000¢ã\n7Õ47Õ4•0‹5 9. MAVERICK ¡ª 525.000.000¢ã\n\n7Ä1 §¥§Ý§ñ §á§à§Ü§å§á§Ü§Ú §ä§â§Ñ§ß§ã§á§à§â§ä§Ñ, §Ú§ã§á§à§Ý§î§Ù§å§Û§ä§Ö:\n7Õ47Õ4•0“6 §®§Ñ§Ô§Ñ§Ù§Ú§ß §Ó§Ö§â§ä§à§Ý§×§ä [§ß§à§Þ§Ö§â]'
                elif sourceText.split()[1].lower() in ['§æ§Ö§â§Þ§Ñ', '§æ§Ö§â§Þ§í']:
                    return ', §ã§á§Ú§ã§à§Ü §Õ§à§ã§ä§å§á§ß§í§ç §æ§Ö§â§Þ:\n\n7Õ4”9å0 §±§à§ã§Ý§Ö §á§à§Ü§å§á§Ü§Ú §æ§Ö§â§Þ§í, §Ó§í §ã§Þ§à§Ø§Ö§ä§Ö §Þ§Ñ§Û§ß§Ú§ä§î §Ò§Ú§ä§Ü§à§Ú§ß§í!\n\n7Õ47Õ4”9ä1 1. Miner (52Õ1/§Õ§Ö§ß§î) ¡ª 500.000¢ã\n7Õ47Õ4”9ä1 2. Miner S (502Õ1/§Õ§Ö§ß§î) ¡ª 5.000.000¢ã\n7Õ47Õ4”9ä1 3. Miner X (1 0002Õ1/§Õ§Ö§ß§î) ¡ª 500.000.000¢ã\n\n7Ä1 §¥§Ý§ñ §á§à§Ü§å§á§Ü§Ú §æ§Ö§â§Þ§í, §Ú§ã§á§à§Ý§î§Ù§å§Û§ä§Ö:\n7Õ47Õ4•0“6 §®§Ñ§Ô§Ñ§Ù§Ú§ß §æ§Ö§â§Þ§Ñ [§ß§à§Þ§Ö§â]'
                elif sourceText.split()[1].lower() in ['§Ü§à§Þ§á', '§Ü§à§Þ§á§î§ð§ä§Ö§â', '§ß§à§å§ä', '§ß§à§å§ä§Ò§å§Ü', '§Ü§à§Þ§á§í', '§Ü§à§Þ§á§î§ð§ä§Ö§â§í', '§ß§à§å§ä§í', '§ß§à§å§ä§Ò§å§Ü§Ú']:
                    return ', §ã§á§Ú§ã§à§Ü §Õ§à§ã§ä§å§á§ß§í§ç §Ü§à§Þ§á§î§ð§ä§Ö§â§à§Ó:\n\n7Õ4”9å0 §±§à§ã§Ý§Ö §á§à§Ü§å§á§Ü§Ú §Ü§à§Þ§á§î§ð§ä§Ö§â§Ñ, §Ó§í §ã§Þ§à§Ø§Ö§ä§Ö §á§â§à§Ú§Ù§Ó§à§Õ§Ú§ä§î §Ó§Ù§Ý§à§Þ§í!\n\n7Õ47Õ4”9ó5 1. Book ¡ª 35.000.000¢ã\n7Õ47Õ4”9ó5 2. Book Air ¡ª 45.000.000¢ã\n7Õ47Õ4”9ó5 3. Book Pro ¡ª 150.000.000¢ã\n\n7Ä1 §¥§Ý§ñ §á§à§Ü§å§á§Ü§Ú §Ü§à§Þ§á§î§ð§ä§Ö§â§Ñ, §Ú§ã§á§à§Ý§î§Ù§å§Û§ä§Ö:\n7Õ47Õ4•0“6 §®§Ñ§Ô§Ñ§Ù§Ú§ß §Ü§à§Þ§á§î§ð§ä§Ö§â [§ß§à§Þ§Ö§â]'
                elif sourceText.split()[1].lower() in ['§ä§Ö§Ý§Ö§æ§à§ß', '§ã§Þ§Ñ§â§ä§æ§à§ß', '§ä§Ö§Ý§Ö§æ§à§ß§í', '§ã§Þ§Ñ§â§ä§æ§à§ß§í']:
                    return ', §ã§á§Ú§ã§à§Ü §Õ§à§ã§ä§å§á§ß§í§ç §ä§Ö§Ý§Ö§æ§à§ß§à§Ó:\n\n7Õ4”9å0 §±§à§Ü§å§á§Ñ§Û§ä§Ö §ä§Ö§Ý§Ö§æ§à§ß§í §Ó §à§Õ§Ú§ß §Ü§Ý§Ú§Ü!\n\n7Õ47Õ4”9á5 1. iPhone ¡ª 25.800.000¢ã\n7Õ47Õ4”9á5 2. iPhone Pro ¡ª 30.000.000¢ã\n7Õ47Õ4”9á5 3. iPhone Pro Max ¡ª 35.250.000¢ã\n\n7Ä1 §¥§Ý§ñ §á§à§Ü§å§á§Ü§Ú §ã§Þ§Ñ§â§ä§æ§à§ß§Ñ, §Ú§ã§á§à§Ý§î§Ù§å§Û§ä§Ö:\n7Õ47Õ4•0“6 §®§Ñ§Ô§Ñ§Ù§Ú§ß §ã§Þ§Ñ§â§ä§æ§à§ß [§ß§à§Þ§Ö§â]'
            elif len(sourceText.split()) == 3:
                id_own = str(sourceText.split()[2].lower())
                if sourceText.split()[1].lower() in ['§Õ§à§Þ', '§Õ§à§Þ§Ñ']:
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
                                    return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9Æ2 §¬§à§â§à§Ò§Ü§å §Ù§Ñ ' + str(price_own_housing1) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                else:
                                    return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                            else:
                                return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Õ§à§Þ! ”9ý5'
                        elif int(id_own) == 2:
                            if own_housing == 0:
                                if price_own_housing2 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing2
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9Æ2 §±§à§Õ§Ó§Ñ§Ý §Ù§Ñ ' + str(price_own_housing2) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                else:
                                    return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                            else:
                                return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Õ§à§Þ! ”9ý5'
                        elif int(id_own) == 3:
                            if own_housing == 0:
                                if price_own_housing3 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing3
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9Æ2 §³§Ñ§â§Ñ§Û §Ù§Ñ ' + str(price_own_housing3) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                else:
                                    return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                            else:
                                return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Õ§à§Þ! ”9ý5'
                        elif int(id_own) == 4:
                            if own_housing == 0:
                                if price_own_housing4 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing4
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9Æ2 §¤§Ñ§â§Ñ§Ø §Ù§Ñ ' + str(price_own_housing4) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                else:
                                    return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                            else:
                                return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Õ§à§Þ! ”9ý5'
                        elif int(id_own) == 5:
                            if own_housing == 0:
                                if price_own_housing5 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing5
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9Æ2 §£§Ö§ä§ç§å§ð §ç§Ú§Ø§Ú§ß§å §Ù§Ñ ' + str(price_own_housing5) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                else:
                                    return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                            else:
                                return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Õ§à§Þ! ”9ý5'
                        elif int(id_own) == 6:
                            if own_housing == 0:
                                if price_own_housing6 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing6
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9Æ2 §¥§Ö§â§Ö§Ó§ñ§ß§ß§í§Û §Õ§à§Þ§Ú§Ü §Ù§Ñ ' + str(price_own_housing6) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                else:
                                    return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                            else:
                                return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Õ§à§Þ! ”9ý5'
                        elif int(id_own) == 7:
                            if own_housing == 0:
                                if price_own_housing7 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing7
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9Æ2 §¬§Ú§â§á§Ú§é§ß§í§Û §Õ§à§Þ §Ù§Ñ ' + str(price_own_housing7) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                else:
                                    return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                            else:
                                return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Õ§à§Þ! ”9ý5'
                        elif int(id_own) == 8:
                            if own_housing == 0:
                                if price_own_housing8 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing8
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9Æ2 §¬§à§ä§ä§Ö§Õ§Ø §Ù§Ñ ' + str(price_own_housing8) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                else:
                                    return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                            else:
                                return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Õ§à§Þ! ”9ý5'
                        elif int(id_own) == 9:
                            if own_housing == 0:
                                if price_own_housing9 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing9
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9Æ2 §¥§à§Þ §ß§Ñ §±§å§Þ§Ñ§Ó§å§Õ§Ö §Ù§Ñ ' + str(price_own_housing9) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                else:
                                    return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                            else:
                                return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Õ§à§Þ! ”9ý5'
                        elif int(id_own) == 10:
                            if own_housing == 0:
                                if price_own_housing10 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing10
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9Æ2 §£§Ú§Ý§Ý§å §ß§Ñ §±§å§Þ§Ñ§Ó§å§Õ§Ö §Ù§Ñ ' + str(price_own_housing10) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                else:
                                    return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                            else:
                                return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Õ§à§Þ! ”9ý5'
                        elif int(id_own) == 11:
                            if own_housing == 0:
                                if price_own_housing11 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_housing11
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_housing": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9Æ2 §­§Ú§é§ß§í§Û §à§ã§ä§â§à§Ó §Ù§Ñ ' + str(price_own_housing11) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                else:
                                    return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                            else:
                                return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Õ§à§Þ! ”9ý5'
                        else:
                            return ', §Õ§à§Þ§Ñ §ã §ä§Ñ§Ü§Ú§Þ ID §ß§Ö §ã§å§ë§Ö§ã§ä§Ó§å§Ö§ä! ”9þ6'
                    else:
                        return ', §ã§Ú§Þ§Ó§à§Ý§í §Ú §Ò§å§Ü§Ó§í §Ù§Ñ§á§â§Ö§ë§Ö§ß§í! ”9þ6'

                elif sourceText.split()[1].lower() in ['§Þ§Ñ§ê§Ú§ß§Ñ', '§Þ§Ñ§ê§Ú§ß§í']:
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
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •07 §£§Ö§Ý§à§ã§Ú§á§Ö§Õ §Ù§Ñ ' + str(price_own_car1) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Þ§Ñ§ê§Ú§ß§Ñ! ”9ý5'
                            elif int(id_own) == 2:
                                if own_car == 0:
                                    if price_own_car2 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car2
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •07 §¤§Ú§â§à§ã§Ü§å§ä§Ö§â §Ù§Ñ ' + str(price_own_car2) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Þ§Ñ§ê§Ú§ß§Ñ! ”9ý5'

                            elif int(id_own) == 3:
                                if own_car == 0:
                                    if price_own_car3 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car3
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9Ä3 Ducati Scrambler §Ù§Ñ ' + str(price_own_car3) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Þ§Ñ§ê§Ú§ß§Ñ! ”9ý5'
                            elif int(id_own) == 4:
                                if own_car == 0:
                                    if price_own_car4 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car4
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9Ä3 Honda CTX1300 §Ù§Ñ ' + str(price_own_car4) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Þ§Ñ§ê§Ú§ß§Ñ! ”9ý5'

                            elif int(id_own) == 5:
                                if own_car == 0:
                                    if price_own_car5 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car5
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •07 Ferrari California front §Ù§Ñ ' + str(price_own_car5) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Þ§Ñ§ê§Ú§ß§Ñ! ”9ý5'
                            elif int(id_own) == 6:
                                if own_car == 0:
                                    if price_own_car6 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car6
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •07 Porsche 911 §Ù§Ñ ' + str(price_own_car6) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Þ§Ñ§ê§Ú§ß§Ñ! ”9ý5'
                            elif int(id_own) == 7:
                                if own_car == 0:
                                    if price_own_car7 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car7
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •07 Nissan GT-R §Ù§Ñ ' + str(price_own_car7) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Þ§Ñ§ê§Ú§ß§Ñ! ”9ý5'
                            elif int(id_own) == 8:
                                if own_car == 0:
                                    if price_own_car8 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car8
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •07 BMW X6 §Ù§Ñ ' + str(price_own_car8) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Þ§Ñ§ê§Ú§ß§Ñ! ”9ý5'
                            elif int(id_own) == 9:
                                if own_car == 0:
                                    if price_own_car9 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car9
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •07 Jaguar F-Type §Ù§Ñ ' + str(price_own_car9) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Þ§Ñ§ê§Ú§ß§Ñ! ”9ý5'
                            elif int(id_own) == 10:
                                if own_car == 0:
                                    if price_own_car10 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car10
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •07 Lamborghini Hurac¨¢n §Ù§Ñ ' + str(price_own_car10) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Þ§Ñ§ê§Ú§ß§Ñ! ”9ý5'
                            elif int(id_own) == 11:
                                if own_car == 0:
                                    if price_own_car11 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car11
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •07 Lamborghini Gallardo §Ù§Ñ ' + str(price_own_car11) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Þ§Ñ§ê§Ú§ß§Ñ! ”9ý5'
                            elif int(id_own) == 12:
                                if own_car == 0:
                                    if price_own_car12 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car12
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •07 Ferrari F80 Concept §Ù§Ñ ' + str(price_own_car12) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Þ§Ñ§ê§Ú§ß§Ñ! ”9ý5'
                            elif int(id_own) == 13:
                                if own_car == 0:
                                    if price_own_car13 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car13
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •07 Lamborghini Sesto §Ù§Ñ ' + str(price_own_car13) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Þ§Ñ§ê§Ú§ß§Ñ! ”9ý5'
                            elif int(id_own) == 14:
                                if own_car == 0:
                                    if price_own_car14 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car14
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •07 Various Ford-based trucks §Ù§Ñ ' + str(price_own_car14) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Þ§Ñ§ê§Ú§ß§Ñ! ”9ý5'
                            elif int(id_own) == 15:
                                if own_car == 0:
                                    if price_own_car15 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_car15
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_car": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •07 Tesla Cybertruck §Ù§Ñ ' + str(price_own_car15) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Þ§Ñ§ê§Ú§ß§Ñ! ”9ý5'
                            else:
                                return ', §Þ§Ñ§ê§Ú§ß§í §ã §ä§Ñ§Ü§Ú§Þ ID §ß§Ö §ã§å§ë§Ö§ã§ä§Ó§å§Ö§ä! ”9þ6'
                        else:
                            return ', §ã§Ú§Þ§Ó§à§Ý§í §Ú §Ò§å§Ü§Ó§í §Ù§Ñ§á§â§Ö§ë§Ö§ß§í! ”9þ6'
                    else:
                        return ', §Õ§Ý§ñ §á§à§Ü§å§á§Ü§Ú §ä§â§Ñ§ß§ã§á§à§â§ä§Ñ §ß§Ö§à§Ò§ç§à§Õ§Ú§Þ§à §Õ§à§Þ! ”9ý5'
                elif sourceText.split()[1].lower() in ['§ñ§ç§ä§Ñ', '§ñ§ç§ä§í']:
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
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •0•5 RHIB §Ù§Ñ ' + str(price_own_yacht1) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ñ§ç§ä§Ñ! ”9ý5'
                            elif int(id_own) == 2:
                                if own_yacht == 0:
                                    if price_own_yacht2 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht2
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •0•5 Kawasaki §Ù§Ñ ' + str(price_own_yacht2) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ñ§ç§ä§Ñ! ”9ý5'

                            elif int(id_own) == 3:
                                if own_yacht == 0:
                                    if price_own_yacht3 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht3
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •0•5 Riva Aquarama §Ù§Ñ ' + str(price_own_yacht3) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ñ§ç§ä§Ñ! ”9ý5'
                            elif int(id_own) == 4:
                                if own_yacht == 0:
                                    if price_own_yacht4 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht4
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •0•5 Various §Ù§Ñ ' + str(price_own_yacht4) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ñ§ç§ä§Ñ! ”9ý5'

                            elif int(id_own) == 5:
                                if own_yacht == 0:
                                    if price_own_yacht5 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht5
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •0•5 §²rin§ã§Öss 60 §Ù§Ñ ' + str(price_own_yacht5) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ñ§ç§ä§Ñ! ”9ý5'
                            elif int(id_own) == 6:
                                if own_yacht == 0:
                                    if price_own_yacht6 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht6
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •0•5 §¡zimut 70 §Ù§Ñ ' + str(price_own_yacht6) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ñ§ç§ä§Ñ! ”9ý5'
                            elif int(id_own) == 7:
                                if own_yacht == 0:
                                    if price_own_yacht7 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht7
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •0•5 D§àmin§Ñt§àr 40M §Ù§Ñ ' + str(price_own_yacht7) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ñ§ç§ä§Ñ! ”9ý5'
                            elif int(id_own) == 8:
                                if own_yacht == 0:
                                    if price_own_yacht8 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht8
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •0•5 M§à§àn§Ön 124 §Ù§Ñ ' + str(price_own_yacht8) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ñ§ç§ä§Ñ! ”9ý5'
                            elif int(id_own) == 9:
                                if own_yacht == 0:
                                    if price_own_yacht9 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht9
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •0•5 Wid§Ör 150 §Ù§Ñ ' + str(price_own_yacht9) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ñ§ç§ä§Ñ! ”9ý5'
                            elif int(id_own) == 10:
                                if own_yacht == 0:
                                    if price_own_yacht10 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht10
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •0•5 Palmer J§àhns§àn 42M Su§â§ÖrS§â§àrt §Ù§Ñ ' + str(
                                            price_own_yacht10) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ñ§ç§ä§Ñ! ”9ý5'
                            elif int(id_own) == 11:
                                if own_yacht == 0:
                                    if price_own_yacht11 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht11
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •0•5 Wid§Ör 165 §Ù§Ñ ' + str(price_own_yacht11) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ñ§ç§ä§Ñ! ”9ý5'
                            elif int(id_own) == 12:
                                if own_yacht == 0:
                                    if price_own_yacht12 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht12
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •0•5 §¦§ãli§âs§Ö §Ù§Ñ ' + str(price_own_yacht12) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ñ§ç§ä§Ñ! ”9ý5'
                            elif int(id_own) == 13:
                                if own_yacht == 0:
                                    if price_own_yacht13 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht13
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •0•5 Dub§Ñi §Ù§Ñ ' + str(price_own_yacht13) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ñ§ç§ä§Ñ! ”9ý5'
                            elif int(id_own) == 14:
                                if own_yacht == 0:
                                    if price_own_yacht14 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_yacht14
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_yacht": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •0•5 Str§Ö§Öts §àf M§àn§Ñ§ã§à §Ù§Ñ ' + str(price_own_yacht14) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ñ§ç§ä§Ñ! ”9ý5'
                            else:
                                return ', §ñ§ç§ä§í §ã §ä§Ñ§Ü§Ú§Þ ID §ß§Ö §ã§å§ë§Ö§ã§ä§Ó§å§Ö§ä! ”9þ6'
                        else:
                            return ', §ã§Ú§Þ§Ó§à§Ý§í §Ú §Ò§å§Ü§Ó§í §Ù§Ñ§á§â§Ö§ë§Ö§ß§í! ”9þ6'
                    else:
                        return ', §Õ§Ý§ñ §á§à§Ü§å§á§Ü§Ú §ä§â§Ñ§ß§ã§á§à§â§ä§Ñ §ß§Ö§à§Ò§ç§à§Õ§Ú§Þ §Õ§à§Þ! ”9ý5'
                elif sourceText.split()[1].lower() in ['§ã§Ñ§Þ§à§Ý§×§ä', '§ã§Ñ§Þ§à§Ý§Ö§ä', '§ã§Ñ§Þ§à§Ý§×§ä§í', '§ã§Ñ§Þ§à§Ý§Ö§ä§í']:
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
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - 7¼6 de Havilland Canada DHC-2 §Ù§Ñ ' + str(price_own_air1) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ã§Ñ§Þ§à§Ý§×§ä! ”9ý5'
                            elif int(id_own) == 2:
                                if own_air == 0:
                                    if price_own_air2 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air2
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - 7¼6 Piper PA-46 §Ù§Ñ ' + str(price_own_air2) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ã§Ñ§Þ§à§Ý§×§ä! ”9ý5'

                            elif int(id_own) == 3:
                                if own_air == 0:
                                    if price_own_air3 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air3
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - 7¼6 Cessna 310 §Ù§Ñ ' + str(price_own_air3) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ã§Ñ§Þ§à§Ý§×§ä! ”9ý5'
                            elif int(id_own) == 4:
                                if own_air == 0:
                                    if price_own_air4 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air4
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - 7¼6 Learjet 55 §Ù§Ñ ' + str(price_own_air4) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ã§Ñ§Þ§à§Ý§×§ä! ”9ý5'

                            elif int(id_own) == 5:
                                if own_air == 0:
                                    if price_own_air5 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air5
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - 7¼6 Bombardier Global Express §Ù§Ñ ' + str(price_own_air5) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ã§Ñ§Þ§à§Ý§×§ä! ”9ý5'
                            elif int(id_own) == 6:
                                if own_air == 0:
                                    if price_own_air6 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air6
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - 7¼6 Cessna Citation X §Ù§Ñ ' + str(price_own_air6) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ã§Ñ§Þ§à§Ý§×§ä! ”9ý5'
                            elif int(id_own) == 7:
                                if own_air == 0:
                                    if price_own_air7 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air7
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - 7¼6 C-130 §Ù§Ñ ' + str(price_own_air7) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ã§Ñ§Þ§à§Ý§×§ä! ”9ý5'
                            elif int(id_own) == 8:
                                if own_air == 0:
                                    if price_own_air8 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air8
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - 7¼6 VOLATOL §Ù§Ñ ' + str(price_own_air8) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ã§Ñ§Þ§à§Ý§×§ä! ”9ý5'
                            elif int(id_own) == 9:
                                if own_air == 0:
                                    if price_own_air9 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air9
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - 7¼6 RM-10 BOMBUSHKA §Ù§Ñ ' + str(
                                            price_own_air9) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ã§Ñ§Þ§à§Ý§×§ä! ”9ý5'
                            elif int(id_own) == 10:
                                if own_air == 0:
                                    if price_own_air10 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air10
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - 7¼6 AVENGER ¡ª HYV §Ù§Ñ ' + str(price_own_air10) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ã§Ñ§Þ§à§Ý§×§ä! ”9ý5'
                            elif int(id_own) == 11:
                                if own_air == 0:
                                    if price_own_air11 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air11
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - 7¼6 F-16 Fighting Falcon §Ù§Ñ ' + str(price_own_air11) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ã§Ñ§Þ§à§Ý§×§ä! ”9ý5'
                            elif int(id_own) == 12:
                                if own_air == 0:
                                    if price_own_air12 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air12
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - 7¼6 RM-10 BOMBUSHKA §Ù§Ñ ' + str(price_own_air12) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ã§Ñ§Þ§à§Ý§×§ä! ”9ý5'
                            elif int(id_own) == 13:
                                if own_air == 0:
                                    if price_own_air13 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air13
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - 7¼6 TULA ¡ª MAMMOTH §Ù§Ñ ' + str(price_own_air13) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ã§Ñ§Þ§à§Ý§×§ä! ”9ý5'
                            elif int(id_own) == 14:
                                if own_air == 0:
                                    if price_own_air14 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air14
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - 7¼6 V-65 MOLOTOK §Ù§Ñ ' + str(price_own_air14) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ã§Ñ§Þ§à§Ý§×§ä! ”9ý5'
                            elif int(id_own) == 15:
                                if own_air == 0:
                                    if price_own_air15 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_air15
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_air": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - 7¼6 MOGUL ¡ª MAMMOTH §Ù§Ñ ' + str(price_own_air15) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ã§Ñ§Þ§à§Ý§×§ä! ”9ý5'
                            else:
                                return ', §ã§Ñ§Þ§à§Ý§×§ä§Ñ §ã §ä§Ñ§Ü§Ú§Þ ID §ß§Ö §ã§å§ë§Ö§ã§ä§Ó§å§Ö§ä! ”9þ6'
                        else:
                            return ', §ã§Ú§Þ§Ó§à§Ý§í §Ú §Ò§å§Ü§Ó§í §Ù§Ñ§á§â§Ö§ë§Ö§ß§í! ”9þ6'
                    else:
                        return ', §Õ§Ý§ñ §á§à§Ü§å§á§Ü§Ú §ä§â§Ñ§ß§ã§á§à§â§ä§Ñ §ß§Ö§à§Ò§ç§à§Õ§Ú§Þ §Õ§à§Þ! ”9ý5'
                elif sourceText.split()[1].lower() in ['§Ó§Ö§â§ä§à§Ý§×§ä', '§Ó§Ö§â§ä§à§Ý§Ö§ä', '§Ó§Ö§â§ä§à§Ý§×§ä§í', '§Ó§Ö§â§ä§à§Ý§Ö§ä§í']:
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
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •0‹5 Eurocopter EC130/135/14 §Ù§Ñ ' + str(price_own_helicopter1) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Ó§Ö§â§ä§à§Ý§×§ä! ”9ý5'
                            elif int(id_own) == 2:
                                if own_helicopter == 0:
                                    if price_own_helicopter2 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter2
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •0‹5 Boeing MH-6 §Ù§Ñ ' + str(price_own_helicopter2) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Ó§Ö§â§ä§à§Ý§×§ä! ”9ý5'

                            elif int(id_own) == 3:
                                if own_helicopter == 0:
                                    if price_own_helicopter3 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter3
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •0‹5 Sikorsky UH-60 §Ù§Ñ ' + str(price_own_helicopter3) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Ó§Ö§â§ä§à§Ý§×§ä! ”9ý5'
                            elif int(id_own) == 4:
                                if own_helicopter == 0:
                                    if price_own_helicopter4 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter4
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •0‹5 HAVOK ¡ª NAGASAKI §Ù§Ñ ' + str(price_own_helicopter4) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Ó§Ö§â§ä§à§Ý§×§ä! ”9ý5'

                            elif int(id_own) == 5:
                                if own_helicopter == 0:
                                    if price_own_helicopter5 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter5
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •0‹5 Eurocopter EC145 §Ù§Ñ ' + str(price_own_helicopter5) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Ó§Ö§â§ä§à§Ý§×§ä! ”9ý5'
                            elif int(id_own) == 6:
                                if own_helicopter == 0:
                                    if price_own_helicopter6 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter6
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •0‹5 Airbus H160 §Ù§Ñ ' + str(price_own_helicopter6) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Ó§Ö§â§ä§à§Ý§×§ä! ”9ý5'
                            elif int(id_own) == 7:
                                if own_helicopter == 0:
                                    if price_own_helicopter7 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter7
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •0‹5 Mil Mi-24 §Ù§Ñ ' + str(price_own_helicopter7) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Ó§Ö§â§ä§à§Ý§×§ä! ”9ý5'
                            elif int(id_own) == 8:
                                if own_helicopter == 0:
                                    if price_own_helicopter8 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter8
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •0‹5 POLICE MAVERICK §Ù§Ñ ' + str(price_own_helicopter8) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Ó§Ö§â§ä§à§Ý§×§ä! ”9ý5'
                            elif int(id_own) == 9:
                                if own_helicopter == 0:
                                    if price_own_helicopter9 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_helicopter9
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_helicopter": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - •0‹5 MAVERICK §Ù§Ñ ' + str(price_own_helicopter9) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Ó§Ö§â§ä§à§Ý§×§ä! ”9ý5'
                            else:
                                return ', §Ó§Ö§â§ä§à§Ý§×§ä§Ñ §ã §ä§Ñ§Ü§Ú§Þ ID §ß§Ö §ã§å§ë§Ö§ã§ä§Ó§å§Ö§ä! ”9þ6'
                        else:
                            return ', §ã§Ú§Þ§Ó§à§Ý§í §Ú §Ò§å§Ü§Ó§í §Ù§Ñ§á§â§Ö§ë§Ö§ß§í! ”9þ6'
                    else:
                        return ', §Õ§Ý§ñ §á§à§Ü§å§á§Ü§Ú §ä§â§Ñ§ß§ã§á§à§â§ä§Ñ §ß§Ö§à§Ò§ç§à§Õ§Ú§Þ §Õ§à§Þ! ”9ý5'
                elif sourceText.split()[1].lower() in ['§æ§Ö§â§Þ§Ñ', '§æ§Ö§â§Þ§í']:
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
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9ä1 Miner §Ù§Ñ ' + str(price_own_farm1) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §æ§Ö§â§Þ§Ñ! ”9ý5'
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
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9ä1 Miner S §Ù§Ñ ' + str(price_own_farm2) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §æ§Ö§â§Þ§Ñ! ”9ý5'

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
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9ä1 Miner X §Ù§Ñ ' + str(price_own_farm3) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §æ§Ö§â§Þ§Ñ! ”9ý5'
                            else:
                                return ', §æ§Ö§â§Þ§í §ã §ä§Ñ§Ü§Ú§Þ ID §ß§Ö §ã§å§ë§Ö§ã§ä§Ó§å§Ö§ä! ”9þ6'
                        else:
                            return ', §ã§Ú§Þ§Ó§à§Ý§í §Ú §Ò§å§Ü§Ó§í §Ù§Ñ§á§â§Ö§ë§Ö§ß§í! ”9þ6'
                    else:
                        return ', §Õ§Ý§ñ §á§à§Ü§å§á§Ü§Ú §æ§Ö§â§Þ§í §ß§Ö§à§Ò§ç§à§Õ§Ú§Þ §Õ§à§Þ! ”9ý5'
                elif sourceText.split()[1].lower() in ['§Ü§à§Þ§á', '§Ü§à§Þ§á§î§ð§ä§Ö§â', '§ß§à§å§ä', '§ß§à§å§ä§Ò§å§Ü', '§Ü§à§Þ§á§í','§Ü§à§Þ§á§î§ð§ä§Ö§â§í', '§ß§à§å§ä§í', '§ß§à§å§ä§Ò§å§Ü§Ú']:
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
                                    return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9ó5 Book §Ù§Ñ ' + str(price_own_comp1) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                else:
                                    return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                            else:
                                return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Ü§à§Þ§á§î§ð§ä§Ö§â! ”9ý5'
                        elif int(id_own) == 2:
                            if own_comp == 0:
                                if price_own_comp2 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_comp2
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_comp": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9ó5 Book Air §Ù§Ñ ' + str(price_own_comp2) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                else:
                                    return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                            else:
                                return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Ü§à§Þ§á§î§ð§ä§Ö§â! ”9ý5'

                        elif int(id_own) == 3:
                            if own_comp == 0:
                                if price_own_comp3 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_comp3
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_comp": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9ó5 Book Pro §Ù§Ñ ' + str(price_own_comp3) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                else:
                                    return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                            else:
                                return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §Ü§à§Þ§á§î§ð§ä§Ö§â! ”9ý5'
                        else:
                            return ', §Ü§à§Þ§á§î§ð§ä§Ö§â§Ñ §ã §ä§Ñ§Ü§Ú§Þ ID §ß§Ö §ã§å§ë§Ö§ã§ä§Ó§å§Ö§ä! ”9þ6'
                    else:
                        return ', §ã§Ú§Þ§Ó§à§Ý§í §Ú §Ò§å§Ü§Ó§í §Ù§Ñ§á§â§Ö§ë§Ö§ß§í! ”9þ6'
                elif sourceText.split()[1].lower() in ['§ä§Ö§Ý§Ö§æ§à§ß', '§ã§Þ§Ñ§â§ä§æ§à§ß', '§ä§Ö§Ý§Ö§æ§à§ß§í', '§ã§Þ§Ñ§â§ä§æ§à§ß§í']:
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
                                    return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9á5 iPhone §Ù§Ñ ' + str(price_own_smart1) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                else:
                                    return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                            else:
                                return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ã§Þ§Ñ§â§ä§æ§à§ß! ”9ý5'
                        elif int(id_own) == 2:
                            if own_smart == 0:
                                if price_own_smart2 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_smart2
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_smart": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9á5 iPhone Pro §Ù§Ñ ' + str(price_own_smart2) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                else:
                                    return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                            else:
                                return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ã§Þ§Ñ§â§ä§æ§à§ß! ”9ý5'

                        elif int(id_own) == 3:
                            if own_smart == 0:
                                if price_own_smart3 <= user_balance:
                                    get_data = gf.loadjson(users_dir + str(id) + ".json")
                                    algo_buy_own = user_balance - price_own_smart3
                                    get_data.update({"balance": '{}'.format(algo_buy_own)})
                                    get_data.update({"own_smart": '{}'.format(id_own)})
                                    gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                    return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9á5 iPhone Pro Max §Ù§Ñ ' + str(price_own_smart3) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                else:
                                    return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                            else:
                                return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ã§Þ§Ñ§â§ä§æ§à§ß! ”9ý5'
                        else:
                            return ', §ã§Þ§Ñ§â§ä§æ§à§ß§Ñ §ã §ä§Ñ§Ü§Ú§Þ ID §ß§Ö §ã§å§ë§Ö§ã§ä§Ó§å§Ö§ä! ”9þ6'
                    elif sourceText.split()[1].lower() in ['§ä§Ö§Ý§Ö§æ§à§ß', '§ã§Þ§Ñ§â§ä§æ§à§ß', '§ä§Ö§Ý§Ö§æ§à§ß§í', '§ã§Þ§Ñ§â§ä§æ§à§ß§í']:
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
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9á5 iPhone §Ù§Ñ ' + str(
                                            price_own_smart1) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ã§Þ§Ñ§â§ä§æ§à§ß! ”9ý5'
                            elif int(id_own) == 2:
                                if own_smart == 0:
                                    if price_own_smart2 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_smart2
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_smart": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9á5 iPhone Pro §Ù§Ñ ' + str(
                                            price_own_smart2) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ã§Þ§Ñ§â§ä§æ§à§ß! ”9ý5'

                            elif int(id_own) == 3:
                                if own_smart == 0:
                                    if price_own_smart3 <= user_balance:
                                        get_data = gf.loadjson(users_dir + str(id) + ".json")
                                        algo_buy_own = user_balance - price_own_smart3
                                        get_data.update({"balance": '{}'.format(algo_buy_own)})
                                        get_data.update({"own_smart": '{}'.format(id_own)})
                                        gf.dumpjson(get_data, users_dir + str(id) + ".json")
                                        return ', §Ó§í §å§ã§á§Ö§ê§ß§à §á§â§Ö§à§Ò§â§Ö§Ý§Ú - ”9á5 iPhone Pro Max §Ù§Ñ ' + str(
                                            price_own_smart3) + '¢ã!\n”9Û0 §£§Ñ§ê §Ò§Ñ§Ý§Ñ§ß§ã: ' + str(algo_buy_own) + '¢ã'
                                    else:
                                        return ', §å §Ó§Ñ§ã §ß§Ö§Õ§à§ã§ä§Ñ§ä§à§é§ß§à §Õ§Ö§ß§Ö§Ô! ”9þ6'
                                else:
                                    return ', §å §Ó§Ñ§ã §å§Ø§Ö §Ö§ã§ä§î §ã§Þ§Ñ§â§ä§æ§à§ß! ”9ý5'
                            else:
                                return ', §ã§Þ§Ñ§â§ä§æ§à§ß§Ñ §ã §ä§Ñ§Ü§Ú§Þ ID §ß§Ö §ã§å§ë§Ö§ã§ä§Ó§å§Ö§ä! ”9þ6'
                    else:
                        return ', §ã§Ú§Þ§Ó§à§Ý§í §Ú §Ò§å§Ü§Ó§í §Ù§Ñ§á§â§Ö§ë§Ö§ß§í! ”9þ6'
                else:
                    return ', §ä§Ñ§Ü§à§Û §Ü§Ñ§ä§Ö§Ô§à§â§Ú§Ú §ß§Ö §ã§å§ë§Ö§ã§ä§Ó§å§Ö§ä! ”9þ6'
            else:
                return shopHelp
        else:
            return None
    pass