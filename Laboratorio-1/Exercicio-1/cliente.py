import socket, pickle

HOST = '127.0.0.1'
PORT = 50000

class Funcionario:
  def __init__(self, nome, cargo, salario):
    self.nome = nome
    self.cargo = cargo
    self.salario = salario

# coletando informações do usuário
nome = input("Entre com o nome: ")
cargo = input("Entre com o cargo: ")
salario = int(input("Entre com o salario: "))

# criando um objeto
funcionario1 = Funcionario(nome, cargo, salario)
# serializando o objeto para ser passado como mensagem
data_string = pickle.dumps(funcionario1)

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

print("Mensagem Recebida:", )
print("Nome:", obj.nome)
print("Cargo:", obj.cargo)
print("Salario:", obj.salario)
