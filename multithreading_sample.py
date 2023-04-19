import threading

# 发送函数
def fun(name, data):
    print("I am {}, I got {}".format(name, data))

if __name__ == '__main__':
    name = 'Thread-1'
    data = '我有一只小毛驴，我从来也不骑'
    t = threading.Thread(target=fun, args=(name, data,))
    t.start()
    t.join()
