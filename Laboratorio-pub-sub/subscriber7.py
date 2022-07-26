import zmq

HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor está

contexto = zmq.Context()
socket = contexto.socket(zmq.SUB)
conexao = "tcp://" + HOST + ":" + str(PORT)

socket.connect(conexao)
socket.setsockopt_string(zmq.SUBSCRIBE, "APOSENTADORIA")

while(True):
  dados = socket.recv(4096).decode()
  
  if dados == None:
    continue
  
  print("Mensagem recebida no sub 7!")

  tipo, idade, tempoDeServico = dados.split()
  idade = int(idade)
  tempoDeServico = int(tempoDeServico)

  # Analisando se o Funcionario pode aposentar
  if idade >= 60 and tempoDeServico >= 25:
    mensagem = "O funcinario pode se aposentar!"
  else:
    if idade >= 65 and tempoDeServico >= 30:
      mensagem = "O funcinario pode se aposentar!"
    else:
      mensagem = "O funcinario nao pode se aposentar ainda!"

  print(mensagem)