
#Noob Editors
#Posy you mother Editor
from colorama import init, Fore
init()
from random import choice, randint
print("AMI-NOT")
print(Fore.RED+'                   ●○●○●○●○●○●○●○●○●○●○●○●')
print(Fore.RED+'                   ○                     ●')
print(Fore.RED+'                   ●                     ○')
print(Fore.RED+'                   ○                     ●')
print(Fore.RED+'                   ●                     ○')
print(Fore.GREEN+'                   》      AMI-NOT      《')
print(Fore.RED+'                   ○                     ●')
print(Fore.RED+'                   ●                     ○')
print(Fore.RED+'                   ○                     ●')
print(Fore.RED+'                   ●○●○●○●○●○●○●○●○●○●○●○●')
print(Fore.BLUE+'■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
print(Fore.YELLOW+'         telegram : Mr_AMI_NOT ')
print(Fore.GREEN+'         instagram : me_AMI.NOT')
print(Fore.RED+'         GITHUB : https://github.com/AMI-NOT')
print(Fore.BLUE+'■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
print(Fore.WHITE+'           bazi in                                                  AMI-NOT   ')
print("                                                                                                                                                                                     ")



password = input("enter youre pass : ")
while password != ("AMI-NOT-79"):
	print(Fore.RED+'password ×')
	password = input("enter youre pass : ")
print(Fore.GREEN+'pasword☆')

print(Fore.YELLOW+'   for example : rubika.ir')

import random
#امتیاز بازیکن ها
your1 = 0
bot1 = 0
q =int(input('بازی تا چند؟ '))
#تاثیرگذار در انتخاب ربات
bot = random.randint(1,4)
#شروع حلقه
while your1 < q and bot1 < q:
    print('کدام سنگ یا کاغذ یا قیچی؟ ')
    #دریافت از کاربر
    your = input('شما:  ')
    if your =='سنگ'  or your =='قیچی'  or your =='کاغذ':
    #انتخاب ربات    
        if bot == 1:
            bot ='سنگ'
            print('ربات: ', bot)
        elif bot == 2:
            bot ='کاغذ'
            print('ربات: ', bot)
        else: bot ='قیچی'; print('ربات: ', bot)
    else:
        print(Forer.GRREN+'سنگ یا کاغذ یا قیچی')
    #مشخص کردن نتیجه
    if your == bot:
        print('مساوی')
        print('شما',your1,'ربات',bot1)
    elif your =='سنگ' and bot =='قیچی':
        your1 +=1
        print('شما',your1,'ربات',bot1)
    elif your =='کاغذ' and bot =='سنگ':
        your1 +=1
        print('شما',your1,'ربات',bot1)
    elif your =='قیچی' and bot =='کاغذ':
        your1 +=1
        print('شما',your1,'ربات',bot1)
    elif your =='سنگ' and bot =='کاغذ':
        bot1 +=1
        print('شما',your1,'ربات',bot1) 
    elif your =='کاغذ' and bot =='قیچی':
        bot1 +=1
        print('شما',your1,'ربات',bot1)
    elif your =='قیچی' and bot =='سنگ':
        bot1 +=1
        print('شما',your1,'ربات',bot1)
    #پایان هر دور
    print('\n_-_-_-_-_- \n')
    #مشخص کردن برنده
    if your1 == q:
        print('برنده شما')
    elif bot1 == q:
        print('برنده ربات')