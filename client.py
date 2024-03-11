import socket

# Sunucunun IP adresi ve port numarası
HOST = '127.0.0.1'  # localhost
PORT = 65432        # Sunucunun kullandığı port numarası

# TCP soketi oluşturma
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Sunucuya bağlanma
client_socket.connect((HOST, PORT))

# Sunucuya mesaj gönderme
# message = 'Merhaba, sunucu!'
# client_socket.sendall(message.encode())

# Sunucudan yanıtın alınması
while True:
    data = client_socket.recv(1024)
    print('Sunucudan gelen yanıt:', data.decode())

# Soketi kapatma
# client_socket.close()