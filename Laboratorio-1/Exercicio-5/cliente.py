import socket, pickle

HOST = '127.0.0.1'
PORT = 50000

class Nadador:
  categoria = ""
  
  def __init__(self, idade):
    self.idade = idade

# coletando informações do usuário
idade = int(input("Entre com a idade da pessoa: "))

# criando um objeto
nadador1 = Nadador(idade)
# serializando o objeto para ser passado como mensagem
data_string = pickle.dumps(nadador1)

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

print("\nMensagem Recebida:")

print("Categoria:", obj.categoria)

