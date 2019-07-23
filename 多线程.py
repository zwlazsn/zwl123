# 导入创建线程的包
import threading
import time
import random

def download(filename):
    print("==={}下载开始===".format(filename))

    # 阻塞当前函数
    time.sleep(random.random() * 10)

    print("==={}下载结束===".format(filename))


# 这里是主线程的代码
if __name__ == '__main__':
    # 创建5个线程
    for i in range(1, 6):
        # 主线程中的代码
        # 创建一个线程 target表示线程执行的函数，args表示传递给函数的参数
        # t 表示线程对象
        t = threading.Thread(target=download, args=(i,))
        # 启动线程 才会执行download函数
        t.start()

'''
===1下载开始===  执行完1线程 进入阻塞
===2下载开始===  执行完2线程 进入阻塞
===3下载开始===  执行完3线程 进入阻塞
===4下载开始===  执行完4线程 进入阻塞
===5下载开始===  执行完5线程 进入阻塞

===5下载结束===  每个线程的阻塞时间不定 所以导致 谁先结束无法判断（随机）
===3下载结束===
===2下载结束===
===1下载结束===
===4下载结束===
'''