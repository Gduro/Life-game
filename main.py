import os
from colorama import Fore
from colorama import Style
import keyboard
import time
import random


amount_of_set_thing = 0
amount = 0
shop_things = ['bagietka', 'mleko', 'majonez kielecki', 'sos czosnkowy', 'zupka chińska', 'marmolada', 'dżem', 'sok jabłkowy', 'sok pomarańczowy']
user_name = []
user_secondname = []
user_age = []
user_balance = 0
bank_balance = 100000000000000
clear = "\n" * 100

def menu():
    abc = True
    print(f'''{Fore.LIGHTMAGENTA_EX}$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Witamy w grze$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$''')
    print(f'''Celem gry jest wyposażenie swojego domu w meble i ustawienia się dobrze finansowo''')
    print(f'''Wybierz 1 jeśli chcesz rozpocząć''')
    print(f'''$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Powodzenia!!!$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$''')
    while abc:
        if keyboard.is_pressed('1'):
            print("\n")
            user_start()
            abc = False
            exit()

def user_start():
    abc = True
    print("Wszedłeś do okna personalizacji postaci!")
    set_nickname = str(input("Podaj Imię postaci:"))
    set_secondname = str(input("Podaj nazwisko postaci:"))
    set_age = int(input("Podaj wiek postaci:"))
    user_name.append(set_nickname)
    user_secondname.append(set_secondname)
    user_age.append(set_age)
    print(f'''{Fore.BLUE}############################################################''')
    print(f"{Fore.MAGENTA}Imię i nazwisko: " + user_name[0] , user_secondname[0])
    print(f"{Fore.LIGHTYELLOW_EX}Wiek: ", user_age[0])
    print(f'''{Fore.BLUE}############################################################''')
    print(f"{Fore.GREEN}Czy wszystko się zgadza?")
    print(f'''{Fore.LIGHTRED_EX}t - tak n - nie(zostaniesz odesłany do ponownej personalizacji)''')
    while abc:
        if keyboard.is_pressed('t'):
            print("\n")
            city()
            abc = False
            exit()
        elif keyboard.is_pressed('n'):
            print("\n")
            user_name.clear()
            user_secondname.clear()
            user_age.clear()
            user_start()
            abc = False
            exit()

def city():
    abc = True
    print(f'''{Fore.LIGHTYELLOW_EX}#################################Witamy w Ciasteczkowie###################################''')
    print('''2. Wejdź do domu
3. Wejdź do Banku
4. Zacznij zarabiać
5. Wyjdź z gry
E. ekwipunek''')
    print('''##########################################################################################''')
    while abc:
        if keyboard.is_pressed('2'):
            print("\n")
            house()
            abc = False
            exit()
        elif keyboard.is_pressed('3'):
            print("\n")
            bank()
            abc = False
            exit()
        elif keyboard.is_pressed('4'):
            print("\n")
            work()
            abc = False
            exit()
        elif keyboard.is_pressed('5'):
            print("\n")
            exit_warning()
            abc = False
            exit()
        elif keyboard.is_pressed('E'):
            print("\n")
            exit_warning()
            abc = False
            exit()


def eq():
    print("eq")
def exit_warning():
    abc = True

    print(f"{Fore.RED}Czy na pewno chcesz wyjść z gry?")
    print(f'''{Fore.BLUE}Kliknij ,,{Fore.GREEN}s{Fore.BLUE}'' jeśli chcesz zostac, a ,,{Fore.RED}l{Fore.BLUE}'' jeśli chcesz wyjść{Fore.RED}(Postępy w grze nie zostaną zapisane!!)''')
    while abc:
        if keyboard.is_pressed('s'):
            print("\n")
            city()
            abc = False

        elif keyboard.is_pressed('l'):
            print("\n")
            menu()
            abc = False

def work():
    while 10:
        abc = True
        print("#####################################Sklep pod żuczkiem#############################################")
        print("Zarabiaj poprzez rozkładanie towaru na półkach")
        print("Aby rozkładać towar naciskaj ,,t'' aby zakończyć naciśnij ,,m''")
        print("#####################################################################################################")
        print("Towar do rozłożenia: " + random.choice(shop_things))
        print('')
        print('')
        keyboard.wait('t' or 'm')
        amount = amount_of_set_thing + 1
        print(amount)


def summary():
    get_money = amount_of_set_thing * 10
    print("########################################Podsumowanie#################################################")
    print("Ilość rozłożonych produktów:" , amount)
    print("Ilość zdobytych pieniędzy:" , get_money)
    print("######################################################################################################")
    user_balance + get_money
def house():
    print("dom")

def bank():
    abc = True
    print(f'''{Fore.LIGHTRED_EX}#############################Pancake Bank##################################''')
    print('''6.Kredyt 
7.Sprawdź konto
8. Wyjdź z banku''')
    print('''###########################################################################''')
    while abc:
        if keyboard.is_pressed('6'):
            print("\n")
            credits()
            abc = False

        elif keyboard.is_pressed('7'):
            print("\n")
            account()
            abc = False
        elif keyboard.is_pressed('8'):
            print("\n")
            city()
            abc = False


def account():
    abc = True
    print(f"{Fore.CYAN}#####################################Witamy na koncie prywatnym################################################")
    print(f"{Fore.GREEN}Imię i nazwisko:" , user_name[0] , user_secondname[0])
    print(f"{Fore.LIGHTGREEN_EX}Wiek:" , user_age[0])
    print(f"{Fore.LIGHTRED_EX}Stan konta:", user_balance)
    print(f'''{Fore.CYAN}#############################################################################################################''')
    print(f"{Fore.MAGENTA}Kliknij ,,l'' aby wyjść z konta")
    while abc:
        if keyboard.is_pressed('l'):
            print("\n")
            bank()
            abc = False
menu()