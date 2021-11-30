# https://docs.python.org/3/howto/sockets.html
# https://stackoverflow.com/questions/8627986/how-to-keep-a-socket-open-until-client-closes-it
# https://stackoverflow.com/questions/10091271/how-can-i-implement-a-simple-web-server-using-python-without-using-any-libraries


from socket import *


def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM)
    try:
        # serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        serversocket.bind(("192.168.0.219", 23455))
        # serversocket.bind(("192.168.0.219", 23456))
        print("Access http://192.168.0.219:23455")
        serversocket.listen(5)
        while 1:
            (clientsocket, address) = serversocket.accept()

            rd = clientsocket.recv(5000).decode()
            pieces = rd.split("\n")
            if len(pieces) > 0:
                print(pieces[0])
                print(rd)
                print(address)

            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            # data += "<html><body>Hello World " + address + "</body></html>\r\n\r\n"
            data += "<html><body>Hello World " + "</body></html>\r\n\r\n"

            clientsocket.sendall(data.encode())
            clientsocket.shutdown(SHUT_WR)

    except KeyboardInterrupt:
        print("\nShutting down...\n")
    except Exception as exc:
        print("Error:\n")
        print(exc)

    serversocket.close()


createServer()
