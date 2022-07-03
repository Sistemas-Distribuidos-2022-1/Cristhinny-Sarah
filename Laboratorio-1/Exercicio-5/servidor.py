import socket, pickle

HOST = 'localhost'
PORT = 50000

class Nadador:
  categoria = ""
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
print("Idade:", data_object.idade)

print("\nAnalisando os dados...")

# Analisando a categoria da pessoa
if data_object.idade >= 0 and data_object.idade <= 4:
  data_object.categoria = "Sem categoria!"
else:
  if data_object.idade >= 5 and data_object.idade <= 7:
    data_object.categoria = "infantil A"
  else:
    if data_object.idade >= 8 and data_object.idade <= 10:
      data_object.categoria = "infantil B"
    else:
      if data_object.idade >= 11 and data_object.idade <= 13:
        data_object.categoria = "juvenil A"
      else:
        if data_object.idade >= 14 and data_object.idade <= 17:
          data_object.categoria = "juvenil B"
        else:
          data_object.categoria = "adulto"

print("\nEnviando a análise dos dados...")

# agora vamos serializar nosso objeto e enviar para o cliente 
data = pickle.dumps(data_object)
conexao.sendall(data)

print("\nFechando a conexao")
conexao.close()