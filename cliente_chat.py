import socket
from cryptography.fernet import Fernet

CHAVE = b'gL62w732p_V3q-xY_85n6bH4v8Wb389u82YtZ1Ak6Fs=' 
cipher = Fernet(CHAVE)

HOST = '127.0.0.1'
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("=== Chat Criptografado Simétrico ===")
print("Digite suas mensagens (ou 'EXIT' para sair):\n")

while True:
    mensagem = input("Você: ")
    if not mensagem:
        continue

    mensagem_bytes = mensagem.encode('utf-8')
    
    mensagem_criptografada = cipher.encrypt(mensagem_bytes)
    
    client.send(mensagem_criptografada)
    
    if mensagem.upper() == 'EXIT':
        break

client.close()