import socket
import ssl

CERT_FILE = "cert_server/cert.pem"  # Certificado do servidor para validação

def main():
    # Cria socket normal
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Cria contexto TLS
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.load_verify_locations(CERT_FILE)
    context.check_hostname = False
    context.verify_mode = ssl.CERT_REQUIRED

    # Conecta primeiro via TCP
    tls_client = context.wrap_socket(client, server_hostname='localhost')
    tls_client.connect(('localhost', 9999))

    # Envia arquivo
    with open("send.txt", "rb") as f:
        data = f.read()
        tls_client.sendall(data)

    # 🚀 IMPORTANTE → avisa ao servidor que terminou de enviar
    tls_client.shutdown(socket.SHUT_WR)

    tls_client.close()

if __name__ == "__main__":
    main()
