# Envio de arquivos utlizando o Docker
Este repositório contém os arquivos utlizados no desenvolvimento de uma aplicação que possibilita que uma máquina (cliente) seja capaz de enviar um arquivo para uma outra máquina (servidor) utilizando o protocolo TCP.  

Para utilizar a aplicação é necessário possuir previamente instalado em suas máquinas o Docker e a versão 3.X do Python. Segue o passo a passo:

1. Clone o repositório para suas máquinas utilizando o seguinte comando:
   ```bash
   git clone https://github.com/jhonegratieri/Laboratorio-Docker.git
   ```
2. Na máquina que será utilizada como servidor acesse o diretório "Server" e digite o seguinte comando para criar a imagem do Docker:
   ```bash
   sudo docker build . -t server
   ```
3. Após criar a imagem digite o seguinte comando para rodar o Docker:
   ```bash
   sudo docker run -it --network host server:latest /bin/bash
   ```
OBS: Os passos 2 e 3 podem ser substituídos pelo seguinte comando caso deseje baixar a imagem pronta do Dockerhub:
   ```bash
   docker run -it --rm --network=host jhone18/server:latest /bin/bash
   ```
4. Após isso você possuirá acesso ao container, então digite o seguinte comando para inicar o servidor:
   ```bash
   python3 server-tcp-arquivo.py
   ```
   A partir de então o servidor estará pronto aguardando novas conexões.
   
5. Agora na máquina que será utilizada como cliente acesse o diretório "Client" e adicione a esse diretório o arquivo no qual deseja enviar.

6. Altere o nome do arquivo que deseja enviar no Dockerfile:
   ```Docker
    FROM python:3.7-slim

    WORKDIR /app

    COPY client-tcp-arquivo.py /app
    COPY arquivo-teste.txt /app

    CMD [ "python", "client-tcp-arquivo.py" ]
   ```
   No lugar de ```arquivo-teste.txt``` digite o nome do arquivo que deseja enviar e salve as alterações.
   
7. Agora digite o seguinte comando para criar a imagem do Docker:
   ```bash
   sudo docker build . -t client
   ```
8. Após criar a imagem digite o seguinte comando para rodar o Docker:
   ```bash
   sudo docker run -it --network host client:latest /bin/bash
   ```
9. Após isso você possuirá acesso ao container, então digite o seguinte comando para inicar o cliente:
   ```bash
   python3 client-tcp-arquivo.py
   ```
10. Insira o endereço de IP do servidor quando solicitado.
    
OBS: Caso você deseje apenas testar o programa sem realizar alteração em qual arquivo será enviado, você pode substituir os comandos 7 e 8 pelo comando a seguir:
   ```bash
   docker run -it --rm --network=host jhone18/client:latest /bin/bash
   ```

Após seguir todos os passos descritos acima o servidor retornará uma mensagem indicando que o arquivo foi recebido e salvo com sucesso caso assim tenha acontecido.
   
