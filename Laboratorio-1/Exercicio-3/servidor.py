import socket, pickle

HOST = 'localhost'
PORT = 50000

class Aluno:
  aprovado = -1
  N1 = ""
  N2 = ""
  N3 = 0 

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
print("\nDados recebidos:")
print("N1:", data_object.N1)
print("N2:", data_object.N2)
print("N3:", data_object.N3)

print("\nAnalisando os dados...")

mediaN1N2 = (data_object.N1 + data_object.N2)/2 

# Analisando se o aluno foi aprovado
if mediaN1N2 >= 7.0:
  data_object.aprovado = 0
else:
  if mediaN1N2 > 3.0 and mediaN1N2 < 7.0:
    if (mediaN1N2 + data_object.N3)/2 >= 5.0:
      data_object.aprovado = 0
    else:
      data_object.aprovado = 1
  else:
    data_object.aprovado = 1

print("\nEnviando a análise dos dados...")

# agora vamos serializar nosso objeto e enviar para o cliente 
data = pickle.dumps(data_object)
conexao.sendall(data)

print("\nFechando a conexao")
conexao.close()