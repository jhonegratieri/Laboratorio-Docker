import socket

HOST = ''  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor esta

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

i = 1

while True:
    con, cliente = tcp.accept()
    print('Concetado por', cliente)
    file_name = "arquivo-" + str(i) + "-recebido"
    with open(file_name, 'wb') as arquivo:
        while True:
            dados = con.recv(1024)
            if not dados:
                break
            arquivo.write(dados)
    print('Salvo com sucesso!')
    i += 1
    con.close()
