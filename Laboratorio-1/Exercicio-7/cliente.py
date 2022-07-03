import socket, pickle

HOST = '127.0.0.1'
PORT = 50000

class Funcionario:
  aposentar = ""
  
  def __init__(self, idade, tempoDeServico):
    self.idade = idade
    self.tempoDeServico = tempoDeServico

# coletando informações do usuário
idade = int(input("Entre com a idade do funcionario: "))
tempoDeServico = int(input("Entre com o tempo de serviço em anos: "))

# criando um objeto
funcionario1 = Funcionario(idade, tempoDeServico)
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
print("Idade:", obj.idade)
print("Tempo de Servico:", obj.tempoDeServico)
print(obj.aposentar)

