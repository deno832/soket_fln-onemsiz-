import socket
import threading
import time

# Sunucunun IP adresi ve port numarası
HOST = '127.0.0.1'  # localhost
PORT = 65432        # Önerilen port numarası 1024 ile 65535 arasında seçilmelidir.

def handle_client(connection, address):
    print('Yeni istemci bağlandı:', address)
    while True:
        try:
            # İstemciden veri alınması
            data = connection.recv(1024)
            if not data:
                break  # Eğer istemciden veri gelmiyorsa döngüden çık
            print('İstemciden gelen veri:', data.decode())
            
            # İstemciye veri gönderme
            connection.sendall("SLM".encode())
            time.sleep(1)
        except Exception as e:
            print('Hata:', e)
            break

    # Bağlantıyı kapatma
    connection.close()
    print('İstemci bağlantısı kapatıldı:', address)

# TCP soketi oluşturma
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Soketi belirtilen IP adresine ve port numarasına bağlama
server_socket.bind((HOST, PORT))

# Sunucuyu dinleme moduna geçirme
server_socket.listen()

print('Sunucu başlatıldı. İstemci bekleniyor...')

while True:
    # Yeni istemci bağlantısını kabul etme
    connection, address = server_socket.accept()
    
    # Yeni bir iş parçacığı oluşturma ve istemci bağlantısını işlemek için başlatma
    client_thread = threading.Thread(target=handle_client, args=(connection, address))
    client_thread.start()