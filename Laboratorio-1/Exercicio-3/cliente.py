import socket, pickle

HOST = '127.0.0.1'
PORT = 50000

class Aluno:
  # 1 para não, 0 para sim
  aprovado = -1
  
  def __init__(self, N1, N2, N3):
    self.N1 = N1
    self.N2 = N2
    self.N3 = N3

# coletando informações do usuário
N1 = float(input("Entre com a N1: "))
N2 = float(input("Entre com a N2: "))
N3 = float(input("Entre com a N3: "))

# criando um objeto
aluno1 = Aluno(N1, N2, N3)
# serializando o objeto para ser passado como mensagem
data_string = pickle.dumps(aluno1)

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

if obj.aprovado == 0:
  print("O aluno foi aprovado!")
if obj.aprovado == 1:
  print("O aluno foi reprovado!")
