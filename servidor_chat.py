import socket
from cryptography.fernet import Fernet

CHAVE = b'gL62w732p_V3q-xY_85n6bH4v8Wb389u82YtZ1Ak6Fs=' 
cipher = Fernet(CHAVE)

HOST = '127.0.0.1' 
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"[*] Servidor de Chat iniciado em {HOST}:{PORT}")
print("[*] Aguardando conexão do cliente...")

conexao, cliente = server.accept()
print(f"[+] Cliente conectado: {cliente}")

try:
    while True:
        dados_criptografados = conexao.recv(1024)
        if not dados_criptografados:
            break
        
        print(f"\n[Wireshark View - Cifrado]: {dados_criptografados}")
        
        dados_descriptografados = cipher.decrypt(dados_criptografados)
        mensagem = dados_descriptografados.decode('utf-8')
        print(f"[Mensagem Original - Decifrada]: {mensagem}")
        
        if mensagem.upper() == 'EXIT':
            break
            
except Exception as e:
    print(f"Erro: {e}")
finally:
    print("[-] Finalizando conexão.")
    conexao.close()
    server.close()