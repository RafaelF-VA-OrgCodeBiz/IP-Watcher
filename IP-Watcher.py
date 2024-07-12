import datetime
import time
from time import sleep
import requests
import configparser
from telegram import Bot
import asyncio

Script = 'IP-Watcher'

configini = configparser.ConfigParser()
#configini.read('C:/Pythondata/config.ini')
configini.read('config.ini')
DynUpdateURL = configini['Configuration'].get('DynUpdateURL', '')
# time in sec between ip checks
ipchecksec = int(configini.get('Configuration', 'ipchecksec'))
Device = configini.get('Configuration', 'Device')
bot_token = configini.get('Configuration', 'bot_token')
chat_id = configini.get('Configuration', 'chat_id')
telegram_info = eval(configini.get('Configuration','telegram_info'))

print("# Script:",Script,"# ip check every", ipchecksec, "seconds", "# telegram_info:", telegram_info, "# time:", time.strftime("%Y-%m-%d %H:%M:%S"))



#MSG _ Telegram if action needed
async def SendMessageToTelegram(message):
    #sleep(2)
    ##
    try:
        
        messagestring = f'{message},{Script}, {Device}'
        await Bot(token=bot_token).send_message(chat_id=chat_id, text=messagestring)
        timenow = datetime.datetime.now()
        print("SendMessageToTelegram:", {message}, {Script}, {Device}, timenow)
        #sleep(1)
        pass
    except Exception as e:
        print("SendMessageToTelegram exception:", e)
        


def get_current_ip():
    response = requests.get('https://api.ipify.org?format=json')
    ip_address = response.json()['ip']
    return ip_address

def check_ip_change():
    print("check_ip_change", time.strftime("%Y-%m-%d %H:%M:%S"))
    try:
        with open('previous_ip.txt', 'r') as f:
            previous_ip = f.read().strip()
    except FileNotFoundError:
        previous_ip = ''
    
    current_ip = get_current_ip()
    
    if current_ip != previous_ip:
        print(f"IP address has changed from {previous_ip} to {current_ip}")
        if telegram_info == True:
            asyncio.run(SendMessageToTelegram("IP changed"))
        
        with open('previous_ip.txt', 'w') as f:
            f.write(current_ip)
        if DynUpdateURL:
            response = requests.get(DynUpdateURL)
            print("DynUpdateURL response: ",response.text)
        else:
            print("No request address specified in config.ini")


### Program exeption handling / restart after exeption###
run = 1
while run == 1:
    try:
        check_ip_change()
        sleep(ipchecksec)
    except Exception as ex:
            print("Exeption", ex)
            sleep(2)
            if telegram_info == True:
                asyncio.run(SendMessageToTelegram("ActionNeeded"))
            print("Sleep to continue sec 600")
            sleep(600)
            continue


