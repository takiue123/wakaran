import getpass  
import socket   

SERVER_IP = "192.168.0.3" 
PORT = 8000 

# スタート
user_name = getpass.getuser()
user_name_bytes = user_name.encode("utf-8")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER_IP, PORT))
s.send(user_name_bytes)

receive_data = s.recv(4)

x = receive_data[0]
y = receive_data[1]

map_size_x = receive_data[2]
map_size_y = receive_data[3]

print("x = %d, y = %d\n" %(x, y))
print("mapsize %d * %d\n" %(map_size_x, map_size_y))


# エンド
receive_data = s.recv(2048)

ranking = receive_data.decode("utf-8")

print(ranking)

