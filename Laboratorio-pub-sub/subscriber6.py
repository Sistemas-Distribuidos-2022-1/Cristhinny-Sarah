import zmq

HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor está

contexto = zmq.Context()
socket = contexto.socket(zmq.SUB)
conexao = "tcp://" + HOST + ":" + str(PORT)

socket.connect(conexao)
socket.setsockopt_string(zmq.SUBSCRIBE, "SALARIOBRUTO")

while(True):
  dados = socket.recv(4096).decode()
  
  if dados == None:
    continue
  
  print("Mensagem recebida no sub 6!")

  tipo, nome, nivel, salarioBruto, numeroDeDependentes = dados.split(' ')
  salarioBruto = float(salarioBruto)
  numeroDeDependentes = int(numeroDeDependentes)
  salarioLiquido = 0.00

  # Fazendo o reajuste do salario
  if nivel == "A":
    if numeroDeDependentes != 0:
      salarioLiquido = salarioBruto - (salarioBruto*8)/100
    else:
      salarioLiquido = salarioBruto - (salarioBruto*3)/100

  if nivel == "B":
    if numeroDeDependentes != 0:
      salarioLiquido = salarioBruto - (salarioBruto*10)/100
    else:
      salarioLiquido = salarioBruto - (salarioBruto*5)/100

  if nivel == "C":
    if numeroDeDependentes != 0:
      salarioLiquido = salarioBruto - (salarioBruto*15)/100
    else:
      salarioLiquido = salarioBruto - (salarioBruto*8)/100

  if nivel == "D":
    if numeroDeDependentes != 0:
      salarioLiquido = salarioBruto - (salarioBruto*17)/100
    else:
      salarioLiquido = salarioBruto - (salarioBruto*10)/100         
  
  mensagem = "Salario Liquido: " + str(salarioLiquido)

  print(mensagem)