from scapy.all import *
import os
import time
def JNtool():
    hosts ="0.0.0.0"
    #装饰器
    def logo(jn):
        def JN(*args,**kwargs):
            print("--JN--")
            rethings = jn(*args,**kwargs)
            return rethings
        return JN

    # 功能函数
    @logo
    def nowhost():
        hosts = input("目标的IP>>> ")
        if "quit"==hosts or "q"==hosts:
            exit()
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
        #端口嗅探
        nowports(hosts)
    def nowports(hosts):
        i = 20
        while i <= 4000:
            seport = RandShort()
            packet = IP(dst=hosts) / TCP(sport=seport, dport=i, flags="S")
            repkt = sr1(packet, timeout=1, verbose=0)
            if repkt and repkt.haslayer(TCP) and repkt.getlayer(TCP).flags == 0x12:
                print(f"Port {i} is open ")
            i += 1

    @logo
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
        "A": nowhost,
        "B": nowhosts
    }

    # 处理输入
    def users_input(users): 
        if users in Function:
            Function[users]()
        else:
            print("WARNING!!! NO THING ...")
    def userwelcome():
        while True:
            a=os.system("cls" if os.name == 'nt' else 'clear')
            print("""

    ===============================
    ===<< Welcome JN nmap-plus>>===
    ===============================
    A.    ----(单个)Host存活+Port扫描
    B.    ----(多个)Hosts存活
    ...
    if you will quit "q" or "(Ctrl+Z)"
          """)
            users = input("JN>>> ")
            if users in ["A", "B"]:
                users_input(users)
            elif users == "q"or users =="quit"or users=="Q":
                print("GoodBye ...!")
                time.sleep(1)
                break
            else:
                print("WARNING!!! Please try again.")
                time.sleep(2)
    userwelcome()
JNtool()
