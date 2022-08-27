# -*- coding: utf-8 -*-
from re import I
import vk_api
import json
import random
import time
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

sms = [
"""
подготовка...
""",
"""
подключение к хостингу القاعدة ...
""",
"""
инициализация...
""",
"""
ответ от VK_API...
""",
"""
успешно!запуск...
"""
]
newk = 0
for q in range(5):
    print(sms[newk])
    newk +=1
    if newk == 5:
        newk = 0
    time.sleep(0.5)

print ('𝚁𝙰𝙸𝙳𝙴𝚁 𝙶𝙻𝙰 3.0.1 вы молодец!  ₳Ʉ₮ⱧØⱤ: ₳Ⱡł ₳Ⱨ₥ɎĐ,V₭: ₴ⱧɆłⱧ_₳Ⱡł_₳Ⱨ₥ɎĐ,пригласи HOIC в чат')
print ('𝔸𝕝𝕝𝕒𝕩𝕦 𝔸𝕜𝕓𝕒𝕣')
vk = vk_api.VkApi(token='vk1.a.JAZkpmfCOvMvTYMnpnNfYyfYXStYMJwVRMfyAYnyfIPeaZY3bmgDqO2rn1Bk1v2fBLdNn5Mwe7TIYAkakPzp6NkXdjva4aKPjQmgMiOyHkMgin2N97TZF9NucpTD-ahvyxFw-REtUODUpUThwBnAsYPOOwomM97hHHjjJU0762jKSb9yyvxEx6qZO4Y4AkBB') 
vk._auth_token()
vk.get_api()
def get_random_id():
    return random.randint(0, 100000000000)

group_id = '214432926' 

longpoll = VkBotLongPoll(vk, group_id)
bot_help = '''

'''

print(bot_help)
for event in longpoll.listen():
   if event.type == VkBotEventType.MESSAGE_NEW:
            d1 = event.object.message
            s1 = json.dumps(d1)
            d2 = json.loads(s1)

            json_object = d2
            message = json_object['text']

            message = message.split("alkaida")
            msg_text = event.object.message['text']
            str1 = message[0].split("|")[0]


            str1 = str1.replace("club", "alkaida")
            if group_id == str1:
                message.pop(0)

            message = 'AL-KAIDA'.join(message).lower()

            id = json_object['peer_id']
            try:
                dey = event.message.action['type']
            except:
                dey = ''
            
            print(message)
            print ('выполнено!пушка в чате!')
            g = input ('чтобы взорвать жопу всем в чате нажми enter: ')
            print ('орудие активировано!я буду также частично уведомлять о том что происходит в чате! ')
            print ('》》》★《《《')
            geir = 'wall-196632179_3'
            
            if dey == 'chat_invite_user':
                while True:    
                    sleep = random.uniform(1.001, 0.999)
                    keyboard = VkKeyboard(one_time=True )
                    keyboard.add_button('дeльше vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('стõп vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('пiдр vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('нəт vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('нет vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_line() 
                    keyboard.add_button('да vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('Акбар @all vto.pe', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('АлКаида vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('АлКаида vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('лох vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_line()
                    keyboard.add_button('nostop vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('sþop vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('stop vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('ещё vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('ещё vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_line()
                    keyboard.add_button('ещё vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('стапе vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('стоп vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('стòп vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('start vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_line()
                    keyboard.add_button('on vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('on vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('on vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('off vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('off vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_line()
                    keyboard.add_button('off vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('Привет vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('АлКаида vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('сильно vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('слабо vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_line()
                    keyboard.add_button('Привет vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('пока vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('Привет vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('Привеt vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('ягени vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_line()
                    keyboard.add_button('Пээ vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('мощь vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('мощь vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('хуйня vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('бля vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.get_keyboard()
                    vk.method("messages.send", {"peer_id": id, 'random_id':get_random_id(), "message": f"Аль-Каида!", "attachment": geir,"keyboard": keyboard.get_keyboard()}) 
                    
                    keyboard = VkKeyboard(one_time=True )
                    keyboard.add_button('дальше vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('стøп vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('пидр vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('нет vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('нет vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_line() 
                    keyboard.add_button('да vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('Акбар @all vto.pe', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('АлКаида vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('АлКаида vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('лöх vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_line()
                    keyboard.add_button('nttop vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('stop vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('stip vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('iщё vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('ещё vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_line()
                    keyboard.add_button('ещё vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('стапе vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('стоп vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('стоп vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('start vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_line()
                    keyboard.add_button('øn vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('on vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('on vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('off vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('off vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_line()
                    keyboard.add_button('off vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('Привет vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('АлКаида vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('сильно vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('слабо vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_line()
                    keyboard.add_button('Привет vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('пока vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('Привет vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('Привеt vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('ягени vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_line()
                    keyboard.add_button('Пээ vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('мощь vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('мощь vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('хуйня vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('бля vto.pe https://vk.cc/cg2ATB', color=VkKeyboardColor.NEGATIVE)
                    keyboard.get_keyboard()
                    vk.method("messages.send", {"peer_id": id, 'random_id':get_random_id(), "message": f"", "attachment": geir,"keyboard": keyboard.get_keyboard()})        
                    time.sleep(sleep)
            
                    
  
 
