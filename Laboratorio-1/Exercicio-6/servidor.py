import socket, pickle

HOST = 'localhost'
PORT = 50000

class Funcionario:
  salarioLiquido = 0.00
  nome = ""
  nivel = ""
  salarioBruto = 0.00
  numeroDeDependentes = 0

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
print("Nivel:", data_object.nivel)
print("Salario bruto:", data_object.salarioBruto)
print("Numero de dependentes:", data_object.numeroDeDependentes)

print("Calculando o salario liquido...")

# Fazendo o reajuste do salario
if data_object.nivel == "A":
  if data_object.numeroDeDependentes != 0:
    data_object.salarioLiquido = data_object.salarioBruto - (data_object.salarioBruto*8)/100
  else:
    data_object.salarioLiquido = data_object.salarioBruto - (data_object.salarioBruto*3)/100

if data_object.nivel == "B":
  if data_object.numeroDeDependentes != 0:
    data_object.salarioLiquido = data_object.salarioBruto - (data_object.salarioBruto*10)/100
  else:
    data_object.salarioLiquido = data_object.salarioBruto - (data_object.salarioBruto*5)/100

if data_object.nivel == "C":
  if data_object.numeroDeDependentes != 0:
    data_object.salarioLiquido = data_object.salarioBruto - (data_object.salarioBruto*15)/100
  else:
    data_object.salarioLiquido = data_object.salarioBruto - (data_object.salarioBruto*8)/100

if data_object.nivel == "D":
  if data_object.numeroDeDependentes != 0:
    data_object.salarioLiquido = data_object.salarioBruto - (data_object.salarioBruto*17)/100
  else:
    data_object.salarioLiquido = data_object.salarioBruto - (data_object.salarioBruto*10)/100

print("Enviando os dados atualizados...")

# agora vamos serializar nosso objeto e enviar para o cliente 
data = pickle.dumps(data_object)
conexao.sendall(data)

print("Fechando a conexao")
conexao.close()