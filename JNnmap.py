from scapy.all import *
import os
import time

# 功能函数
def nowhost():
    hosts = input("目标的IP>>> ")
    try:
        # 创建 ICMP 请求包
        pkt = IP(dst=hosts) / ICMP()
        # 发送请求并等待响应
        resp = sr1(pkt, timeout=2, verbose=0)
        
        if resp:
            print(f"IP {hosts} 可达，存活")
        else:
            print(f"IP {hosts} 不可达，遗失")
        time.sleep(2)
    except Exception as e:
        print(f"发生错误: {e}")
        time.sleep(2)

def nowhosts():
    hosts = input("目标的多个IP(以空格分隔)>>> ").split()
    for host in hosts:
        try:
            # 创建 ICMP 请求包
            pkt = IP(dst=host) / ICMP()
            # 发送请求并等待响应
            resp = sr1(pkt, timeout=2, verbose=0)
            
            if resp:
                print(f"IP {host} 可达，存活")
            else:
                print(f"IP {host} 不可达，遗失")
        except Exception as e:
            print(f"对 {host} 执行时发生错误: {e}")
        time.sleep(1)

# 功能表
Function = {
    "Host": nowhost,
    "Hosts": nowhosts
}

# 处理输入
def users_input(users):
    if users in Function:
        Function[users]()
    else:
        print("WARNING!!! NO THING ...")

while True:
    os.system("cls" if os.name == 'nt' else 'clear')
    print("""
===============================
===<< Welcome JN nmap-plus>>===
===============================
Host  ----(单个)Host存活+Port扫描
Hosts ----(多个)Host存活
...
if you will quit "q" or "(Ctrl+Z)"
      """)
    users = input("JN>>> ")
    if users in ["Host", "Hosts"]:
        users_input(users)
    elif users == "q":
        print("GoodBye ...!")
        time.sleep(1)
        break
    else:
        print("WARNING!!! Please try again.")
        time.sleep(2)
