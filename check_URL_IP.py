#!/usr/bin/env python3

import socket
import time

ip_addr = {}
ip_addr_prev = {}
dict_init = True
url_list = ("drive.google.com", "mail.google.com", "google.com")
while True:
    for url in url_list:
        ip_addr[url] = socket.gethostbyname(url)
        print(url + " - " + ip_addr[url])
        if (dict_init):
            ip_addr_prev[url] = ip_addr[url]
        if (ip_addr[url] != ip_addr_prev[url]):
            print("[ERROR] " + url + " IP mismatch: " + ip_addr_prev[url] + " " + ip_addr[url])
        ip_addr_prev[url] = ip_addr[url]
    time.sleep(10)
    dict_init = False
