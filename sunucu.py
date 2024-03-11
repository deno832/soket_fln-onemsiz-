import socket
import time

# Sunucunun IP adresi ve port numarası
HOST = '127.0.0.1'  # localhost
PORT = 65432        # Önerilen port numarası 1024 ile 65535 arasında seçilmelidir.

# TCP soketi oluşturma
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Soketi belirtilen IP adresine ve port numarasına bağlama
server_socket.bind((HOST, PORT))

# Sunucuyu dinleme moduna geçirme, en fazla 1 istemci kabul edilecek
server_socket.listen(1)

print('Sunucu başlatıldı. İstemci bekleniyor...')

# İstemci bağlantısını kabul etme
connection, address = server_socket.accept()

print('İstemci bağlandı:', address)


while True:
    # İstemciden veri alınması
    # data = connection.recv(1024)
    # if not data:
    #     break  # Eğer istemciden veri gelmiyorsa döngüden çık
    # İstemciye veri gönderme
    connection.sendall("SLM".encode())
    time.sleep(1)

# Soketleri kapatma
connection.close()
server_socket.close()