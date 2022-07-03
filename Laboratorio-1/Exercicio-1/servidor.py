import socket, pickle

HOST = 'localhost'
PORT = 50000

class Funcionario:
  nome = ""
  cargo = ""
  salario = 0

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
print("Nome:", data_object.nome)
print("Cargo:", data_object.cargo)
print("Salario:", data_object.salario)

print("Atualizando os dados...")

# Fazendo o reajuste do salario
if data_object.cargo == "operador":
  data_object.salario += (data_object.salario*20)/100

if data_object.cargo == "programador":
  data_object.salario += (data_object.salario*18)/100

print("Enviando os dados atualizados...")

# agora vamos serializar nosso objeto e enviar para o cliente 
data = pickle.dumps(data_object)
conexao.sendall(data)

print("Fechando a conexao")
conexao.close()