import socket, pickle

HOST = 'localhost'
PORT = 50000

class Pessoa:
  maioridade = -1
  nome = ""
  sexo = ""
  idade = 0

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
print("Nome:", data_object.nome)
print("Sexo:", data_object.sexo)
print("Idade:", data_object.idade)

print("\nAtualizando os dados...")

# Analisando a maioridade
if data_object.sexo == "feminino":
  if data_object.idade >= 21:
    data_object.maioridade = 0
  else:
    data_object.maioridade = 1
else:
  if data_object.idade >= 18:
    data_object.maioridade = 0
  else:
    data_object.maioridade = 1

print("\nEnviando os dados atualizados...")

# agora vamos serializar nosso objeto e enviar para o cliente 
data = pickle.dumps(data_object)
conexao.sendall(data)

print("\nFechando a conexao")
conexao.close()