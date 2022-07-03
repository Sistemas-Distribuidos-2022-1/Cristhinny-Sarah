import socket, pickle

HOST = '127.0.0.1'
PORT = 50000

class Pessoa:
  # 1 para não, 0 para sim
  maioridade = -1
  
  def __init__(self, nome, sexo, idade):
    self.nome = nome
    # "feminino" ou "masculino"
    self.sexo = sexo
    self.idade = idade

# coletando informações do usuário
nome = input("Entre com o nome: ")
sexo = input("Entre com o sexo: ")
idade = int(input("Entre com a idade: "))

# criando um objeto
pessoa1 = Pessoa(nome, sexo, idade)
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

print("\nMensagem Recebida:", )
print("Nome:", obj.nome)
print("Sexo:", obj.sexo)
print("Idade:", obj.idade)
if obj.maioridade == 0:
  print("Já atingiu a maioridade!")
if obj.maioridade == 1:
  print("Não atingiu a maioridade ainda!")
