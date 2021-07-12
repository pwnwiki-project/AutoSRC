#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import subprocess
import requests
import argparse
import base64
import sys
import json
import codecs


def dec_data(byte_data: bytes):
    try:
        return byte_data.decode('UTF-8')
    except UnicodeDecodeError:
        return byte_data.decode('GB18030')


def get_files(path):
    all_files = []
    for root, dirs, files in os.walk(path):
        all_files = files
    return all_files


def automation():
    get_payload_dir = get_files("./payload/")
    get_result_dir = get_files("./fofa_file/")
    for i in get_payload_dir:
        print("\033[1;32m ================================================================\033[0m")
        print("\033[1;32m 开始 %s 漏洞检查\033[0m" % (i))
        print("\033[1;32m 正在检查请稍等......\033[0m")
        print("\033[1;32m ================================================================\033[0m")
        for j in get_result_dir:
            if j == i + ".txt":
                p = subprocess.Popen('python3 "./payload/%s" -f "./fofa_file/%s"' % (i, j), shell=True,
                                     stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
                while p.poll() is None:
                    line = p.stdout.readline().strip()
                    if line:
                        line = dec_data(line)
                        x = line.find('不', 0, len(line))
                        if x == -1:
                            result = line.replace(
                                "\033[1;36m", "").replace("\033[0m", " ").replace("\033[1;32m", " ").replace(
                                "\033[0m", " ".replace("\033[36m[o] ", " ").replace("\033[0m", " "))
                            print(result)
                            f = open("./results/" + i + "_OK.txt", 'a', encoding='utf-8')
                            f.write(result + "\n")


def banner():
    print("""                                        
    \033[1;36m                              ___                                           \033[0m
    \033[1;36m                            ,--.'|_                                         \033[0m
    \033[1;36m                      ,--,  |  | :,'   ,---.                __  ,-.         \033[0m
    \033[1;36m                    ,'_ /|  :  : ' :  '   ,'\   .--.--.   ,' ,'/ /|         \033[0m
    \033[1;36m   ,--.--.     .--. |  | :.;__,'  /  /   /   | /  /    '  '  | |' | ,---.   \033[0m
    \033[1;36m  /       \  ,'_ /| :  . ||  |   |  .   ; ,. :|  :  /`./  |  |   ,'/     \  \033[0m
    \033[1;36m .--.  .-. | |  ' | |  . .:__,'| :  '   | |: :|  :  ;_    '  :  / /    / '  \033[0m
    \033[1;36m  \__\/: . . |  | ' |  | |  '  : |__'   | .; : \  \    `. |  | ' .    ' /   \033[0m
    \033[1;36m  ," .--.; | :  | : ;  ; |  |  | '.'|   :    |  `----.   \;  : | '   ; :__  \033[0m
    \033[1;36m /  /  ,.  | '  :  `--'   \ ;  :    ;\   \  /  /  /`--'  /|  , ; '   | '.'| \033[0m
    \033[1;36m;  :   .'   \:  ,      .-./ |  ,   /  `----'  '--'.     /  ---'  |   :    : \033[0m
    \033[1;36m|  ,     .-./ `--`----'      ---`-'             `--'---'          \   \  /  \033[0m
    \033[1;36m `--`---'                                                          `----'   \033[0m
    """)
    print('\033[1;36m   工具使用方法\033[0m')
    print('\033[1;36m           python3 autosrc.py -e/--email email -k/--key key\033[0m')
    print('\033[1;36m           python3 autosrc.py -h/--help\033[0m')


if len(sys.argv) == 1:
    banner()
    sys.exit()
parser = argparse.ArgumentParser(description='autosrcfofaapi help')
parser.add_argument('-e', '--email', help='Please Input a email!', default='')
parser.add_argument('-k', '--key', help='Please Input a key!', default='')
args = parser.parse_args()
email = args.email
key = args.key
url = "https://fofa.so/api/v1/info/my?email=" + email + "&key=" + key
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded"
}
response = requests.get(url, headers=header)
if 'errmsg' not in response.text:
    print("\033[1;32memail和key均正确\033[0m")

    get_payload_dir = get_files("./payload/")
    print(get_payload_dir)
    for i in get_payload_dir:
        f = codecs.open("./payload/" + i, mode='r', encoding='utf-8')
        line = f.readline()
        sentence = line.strip("#")
        print(sentence)
        print("\033[1;36mfofa语句 >>>\033[0m" + sentence)
        sentence = base64.b64encode(sentence.encode('utf-8')).decode("utf-8")
        url = "https://fofa.so/api/v1/search/all?email=" + email + "&key=" + key + "&qbase64=" + sentence
        response = requests.get(url, headers=header)
        if 'errmsg' not in response.text:
            print("\033[1;36m已保存到\033[0m\033[1;32mfofa_file目录下\033[0m")
            r1 = json.loads(response.text)
            for k in r1['results']:
                s = k[0]
                print(s)
                f = open("./fofa_file/" + i + ".txt", 'a', encoding='utf-8')
                f.write(s + "\n")
        else:
            print("\033[1;31mfofa语句不正确\033[0m")
else:
    print("\033[1;31memail或key不正确\033[0m")

print("\033[1;34m[INFO]\033[0m Success")
print("\033[1;32m ================================================================\033[0m")
print("\033[1;32m FOFA采集完成 开始漏洞检查\033[0m")
print("\033[1;32m ================================================================\033[0m")

automation()
