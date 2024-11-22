#!/usr/bin/env python3

import requests


# # 隧道域名:端口号
# tunnel = "xxxxxxxxxxxxcom:端口"

# # 用户名密码方式
# username = "xxxxxxxxxx"
# password = "xxxxxxxxxx"
# proxies = {
#     "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel},
#     "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel}
# }

def domain_scan(domain_name,sub_names):
    for sub in sub_names:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"
        }
        url = f"https://{sub}.{domain_name}"
        try:
            requests.head = headers
            requests.get(url)
            # requests.get(url,proxies=proxies)
            print(f"[*]{url}")
        except requests.ConnectionError:
            # print("error")
            pass    


if __name__ == '__main__':
    dom_name = input("enter the domain name :")


    with open("F:\python_arsenal\python-arsenal\python-tools\Subdomain_explosion\Subdomain_info.txt") as file:
        sub_name = file.read()
        sub_dom = sub_name.splitlines()
        print("文件中存在的子域名数量：{}".format(len(sub_dom)))
        print("文件子域名列表")
        print(sub_dom)
    domain_scan(dom_name,sub_dom)    

# 由于本人大学生没有钱买代理，所以代理模块直接注销掉了