import socket, pickle

HOST = 'localhost'
PORT = 50000

class Funcionario:
  aposentar = ""
  idade = 0
  tempoDeServico = 0

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
print("Idade:", data_object.idade)
print("Tempo de serviço:", data_object.tempoDeServico)

print("Analisando os dados...")

# Analisando se o Funcionario pode aposentar
if data_object.idade >= 60 and data_object.tempoDeServico >= 25:
  data_object.aposentar = "O funcinário pode se aposentar!"
else:
  if data_object.idade >= 65 and data_object.tempoDeServico >= 30:
    data_object.aposentar = "O funcinário pode se aposentar!"
  else:
    data_object.aposentar = "O funcinário não pode se aposentar ainda!"

print("Enviando os dados atualizados...")

# agora vamos serializar nosso objeto e enviar para o cliente 
data = pickle.dumps(data_object)
conexao.sendall(data)

print("Fechando a conexao")
conexao.close()