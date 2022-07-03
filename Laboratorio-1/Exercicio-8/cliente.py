import socket, pickle

HOST = '127.0.0.1'
PORT = 50000

class Cliente:
  credito = 0.00
  
  def __init__(self, saldoMedio):
    self.saldoMedio = saldoMedio

# coletando informações do usuário
saldoMedio = float(input("Entre com o saldo medio do cliente: "))

# criando um objeto
cliente1 = Cliente(saldoMedio)
# serializando o objeto para ser passado como mensagem
data_string = pickle.dumps(cliente1)

#Para conectar ao socket precisamos passar a família de protocolos
# AF_INET = IPV4
#sock_STREAM = TCP
S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
S.connect((HOST, PORT))

# envio dos dados para o servidor
S.sendall(data_string)

# recebendo resposta do servidor
data = S.recv(1024)

# precisamos de-serializar o dado recebido
obj = pickle.loads(data)

print("Mensagem Recebida:", )
print("Saldo medio:", obj.saldoMedio)
print("Crédito aprovado pelo banco:", obj.credito)