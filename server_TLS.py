import socket
import ssl

# Caminhos do certificado e chave geradas pelo openSSL
CERT_FILE = "cert_client/cert.pem"
KEY_FILE = "cert_client/key.pem"

def main():
    #Criando o socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 9999))
    server.listen(1)

    print("Aguardando conexão TLS...")

    #Criando camada TLS
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)

    conn, addr = server.accept()
    print(f"Conexão recebida de {addr}")

    #Aplica o TLS
    tls_conn = context.wrap_socket(conn, server_side=True)

    #Recebe arquivo
    with open("received.txt", "wb") as f:
        while True:
            data = tls_conn.recv(1024)
            if not data:
                break
            f.write(data)

    tls_conn.close()
    server.close()

if __name__ == "__main__":
    main()
