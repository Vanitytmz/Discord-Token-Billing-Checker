import requests
import colorama
from colorama import Fore
from colorama import init as colorama_init
import ctypes
import os
colorama_init(autoreset=True)


def main():
    while True:
        try:
            with open('proxy.txt', 'r') as f:
                http_proxy = f.read().splitlines()[0]
            proxyDict = {
            "http": http_proxy,
            "https": http_proxy,
            }
            ctypes.windll.kernel32.SetConsoleTitleW(f'Vanity Xbox Code Claimer')
            with open('tokens.txt', 'r') as f:
                global token
                token = f.read().splitlines()[0]
                f.close()
            with open('tokens.txt', 'r') as fin:
                data = fin.read().splitlines(True)
            with open('tokens.txt', 'w') as fout:
                fout.writelines(data[1:])
            fout.close()
            url = 'https://discord.com/api/v9/users/@me/billing/payment-sources'
            headers = {
                'authorization': token,
            }
            response = requests.get(url, headers=headers, proxies=proxyDict).json()
            invalid = response[0]['invalid']
            brand = response[0]['brand']
            last4 = response[0]['last_4']
            expm = response[0]['expires_month']
            if expm < 10:
                expm = '0' + str(expm)
            expy = response[0]['expires_year']
            print(Fore.CYAN+"Checking -> "+Fore.YELLOW+token+'\n'+Fore.BLUE+"Invalid? -> "+Fore.YELLOW+str(invalid)+'\n'+Fore.BLUE+"Brand -> " +Fore.YELLOW+brand+'\n'+Fore.BLUE+"Last 4 -> "+Fore.YELLOW+last4+'\n'+Fore.BLUE+"Expires -> "+Fore.YELLOW+str(expm)+"/"+str(expy))
            with open('billing.txt', 'a') as the_file:
                the_file.write(token + '\n')
                the_file.close()
        except KeyError:
            print(Fore.RED+"No Billing ->"+Fore.YELLOW+token)
            pass
        if os.stat('tokens.txt').st_size == 0:
            print(Fore.RED+"No Tokens Left")
            os.system('pause')
            break