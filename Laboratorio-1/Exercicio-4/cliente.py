import socket, pickle

HOST = '127.0.0.1'
PORT = 50000

class Pessoa:
  pesoIdeal = 0
  
  def __init__(self, altura, sexo):
    self.altura = altura
    # "feminino" ou "masculino"
    self.sexo = sexo

# coletando informações do usuário
altura = float(input("Entre com a altura da pessoa: "))
sexo = input("Entre com o sexo da pessoa: ")

# criando um objeto
pessoa1 = Pessoa(altura, sexo)
# serializando o objeto para ser passado como mensagem
data_string = pickle.dumps(pessoa1)

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

print("O peso ideal para você é: {:.2f} KG".format(obj.pesoIdeal))

