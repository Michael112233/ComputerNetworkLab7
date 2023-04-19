from socket import *
import threading

def thread_func(connectionSocket):
    message = connectionSocket.recv(1024).decode()
    modified = message.upper()
    connectionSocket.send(modified.encode())

def multithreading_server_BIO(ip: str, port: int):
    # 创建服务器套接字，使用IPv4协议，TCP协议
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # 绑定端口号和套接字
    serverSocket.bind((ip, port))
    # 开启监听，设置1024个连接缓冲，暂时将连接挂起
    serverSocket.listen(1024)
    print('The server is ready to receive')
    while True:
        # 等待接受客户端的连接
        conn, addr = serverSocket.accept()
        # 创建线程
        serve_thread = threading.Thread(target=thread_func, args=(conn,))
        serve_thread.start()
        serve_thread.join()
    serverSocket.close()


if __name__ == '__main__':
    # 服务器端口号
    serverPort = 12000
    multithreading_server_BIO('', serverPort)
