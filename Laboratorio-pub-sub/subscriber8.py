import zmq

HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor está

contexto = zmq.Context()
socket = contexto.socket(zmq.SUB)
conexao = "tcp://" + HOST + ":" + str(PORT)

socket.connect(conexao)
socket.setsockopt_string(zmq.SUBSCRIBE, "SALDOMEDIO")

while(True):
  dados = socket.recv(4096).decode()
  
  if dados == None:
    continue
  
  print("Mensagem recebida no sub 8!")

  tipo, saldoMedio = dados.split()
  saldoMedio = float(saldoMedio)
  credito = 0.00

  # Analisando se o cliente receberá crédito
  if saldoMedio >= 0 and saldoMedio <= 200:
    credito = 0.00
  else:
    if saldoMedio >= 201 and saldoMedio <= 400:
      credito = (saldoMedio*20)/100
    else:
      if saldoMedio >= 401 and saldoMedio <= 600:
        credito = (saldoMedio*30)/100
      else:
        credito = (saldoMedio*40)/100
  
  mensagem = "O Banco aprovou um credito especial de " + str(credito) + "!"

  print(mensagem)