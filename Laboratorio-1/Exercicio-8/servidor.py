import socket, pickle

HOST = 'localhost'
PORT = 50000

class Cliente:
  credito = 0.00
  saldoMedio = 0.00

# Para criar o socket precisamos passar a família de protocolos
# AF_INET = IPV4
# sock_STREAM = TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# o servidor estará linkado com a respectiva porta e HOST definidas anteriormente
server.bind((HOST, PORT))

# vamos ouvir o endereço uma unica vez
server.listen(1)
print("Aguardando a conexao de um cliente")

conexao, endereco = server.accept()
print("Conectado em ", endereco)

# da conexao nós recebemos dados do cliente
data = conexao.recv(4096)
# precisamos de-serializar o dado recebido
data_object = pickle.loads(data)
print("Dados recebidos:")
print("Saldo medio:", data_object.saldoMedio)

print("Calculando o crédito especial...")

# Analisando se o cliente receberá crédito
if data_object.saldoMedio >= 0 and data_object.saldoMedio <= 200:
  data_object.credito = 0.00
else:
  if data_object.saldoMedio >= 201 and data_object.saldoMedio <= 400:
    data_object.credito = (data_object.saldoMedio*20)/100
  else:
    if data_object.saldoMedio >= 401 and data_object.saldoMedio <= 600:
      data_object.credito = (data_object.saldoMedio*30)/100
    else:
      data_object.credito = (data_object.saldoMedio*40)/100

print("Enviando os dados atualizados...")

# agora vamos serializar nosso objeto e enviar para o cliente 
data = pickle.dumps(data_object)
conexao.sendall(data)

print("Fechando a conexao")
conexao.close()