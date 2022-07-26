import zmq

HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor está

contexto = zmq.Context()
socket = contexto.socket(zmq.SUB)
conexao = "tcp://" + HOST + ":" + str(PORT)

socket.connect(conexao)
socket.setsockopt_string(zmq.SUBSCRIBE, "SALARIOS")

while(True):
  dados = socket.recv(4096).decode()
  
  if dados == None:
    continue
  
  print("Mensagem recebida no sub 1!")

  tipo, nome, cargo, salario = dados.split()
  salario = float(salario)
  
  # Fazendo o reajuste do salario
  if cargo == "operador":
    salario += (salario*20)/100
  if cargo == "programador":
    salario += (salario*18)/100
  mensagem = "Salario atualizado de " + nome + ": " + str(salario)

  print(mensagem)