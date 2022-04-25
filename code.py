import vk_api
import time
token = '258c12ad88c272c97e3dfcbbe8ee1585ebeb54ece71a4d4dfc9ecd6bd5ab407dad6da82dcf6ceb89b0994'
session = vk_api.VkApi(token = token)
def scum():
    count = 0
    arg = 0
    while True:
        if arg <= 5:
            try:
                while True:
                    time.sleep(count)
                    print('hello')
                    session.method('messages.send', {'random_id':0, 'user_id':543120045, 'message':'...'})
            except vk_api.exceptions.Captcha:
                print('я заснул')
                time.sleep(30)
                print('я проснулся')
                count+=0.5
                arg+=1
                print(count)
                print(arg)
        else:
            arg = 0
            count = 0

scum()
