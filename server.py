import socket, cv2, pickle, struct

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_name = socket.gethostname()
host_ip = '127.0.0.1'
print('HOST IP:',host_ip)
port = 9999
socket_address = (host_ip,port)

#socket Bind
server_socket.bind(socket_address)
server_socket.listen(5)
print('LISTENING AT:', socket_address)
while True:
    client_socket,addr = server_socket.accept()
    print('GOT CONNECTION FROM:', addr)
    if client_socket:
        vid = cv2.VideoCapture('./video/a.mp4')
        while(vid.isOpened()):
            img,frame = vid.read()
            a = pickle.dumps(frame)
            message = struct.pack("Q",len(a))+a
            client_socket.sendall(message)
            cv2.imshow('Setver',frame)
            cv2.waitKey(1)
