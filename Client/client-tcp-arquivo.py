import socket

# HOST = '192.168.126.125'  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor esta

HOST = input("Informe o endereço de IP do servidor: ")

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

file = input("Informe o nome do arquivo que deseja enviar: ")

with open(file, 'rb') as arquivo:
    dados = arquivo.read()
    tcp.sendall(dados)

tcp.close()
