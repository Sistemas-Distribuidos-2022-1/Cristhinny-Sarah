import socket, pickle

HOST = 'localhost'
PORT = 50000

class Pessoa:
  pesoIdeal = 0
  altura = 0.0
  sexo = ""

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
print("Altura:", data_object.altura)
print("Sexo:", data_object.sexo)

print("\nCalculando o peso ideal...")

# Analisando o peso ideal
if data_object.sexo == "feminino":
  data_object.pesoIdeal = (62.1*data_object.altura) - 44.7
else:
  data_object.pesoIdeal = (72.7*data_object.altura) - 58

print("\nEnviando a análise dos dados...")

# agora vamos serializar nosso objeto e enviar para o cliente 
data = pickle.dumps(data_object)
conexao.sendall(data)

print("\nFechando a conexao")
conexao.close()