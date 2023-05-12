import socket
SERVER_IP_ADDRESS = 'localhost'
DOMAIN_NAME = 'www.yahoo.com'


client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.sendto(DOMAIN_NAME.encode(), (SERVER_IP_ADDRESS, 53))

# -> untuk mengembalikan data dalam format byte dan alamat ip sumber yang mengirim data
response, _ = client_socket.recvfrom(1024)
# -> mengubah data response DNS yang diterima menjadi string menggunakan decode
ip_address = response.decode()

# -> untuk mencetak hasil yang di request
print(F"Alamat IP dari {DOMAIN_NAME} adalah {ip_address}")
