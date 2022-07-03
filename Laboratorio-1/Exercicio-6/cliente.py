import socket, pickle

HOST = '127.0.0.1'
PORT = 50000

class Funcionario:
  salarioLiquido = 0.00
  
  def __init__(self, nome, nivel, salarioBruto, numeroDeDependentes):
    self.nome = nome
    # "A", "B", "C" ou "D"
    self.nivel = nivel
    self.salarioBruto = salarioBruto
    self.numeroDeDependentes = numeroDeDependentes

# coletando informações do usuário
nome = input("Entre com o nome: ")
nivel = input("Entre com o nivel: ")
salarioBruto = float(input("Entre com o salario bruto: "))
numeroDeDependentes = int(input("Entre com o números de dependentes do funcionário: "))

# criando um objeto
funcionario1 = Funcionario(nome, nivel, salarioBruto, numeroDeDependentes)
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

print("Mensagem Recebida:")
print("Nome:", obj.nome)
print("Nivel:", obj.nivel)
print("Salario bruto:", obj.salarioBruto)
print("Salario liquido:", obj.salarioLiquido)
