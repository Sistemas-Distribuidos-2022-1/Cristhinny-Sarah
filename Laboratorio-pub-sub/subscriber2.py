import zmq

HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor está

contexto = zmq.Context()
socket = contexto.socket(zmq.SUB)
conexao = "tcp://" + HOST + ":" + str(PORT)

socket.connect(conexao)
socket.setsockopt_string(zmq.SUBSCRIBE, "MAIORIDADE")

while(True):
  dados = socket.recv(4096).decode()
  
  if dados == None:
    continue

  print("Mensagem recebida no sub 2!")
  
  tipo, nome, sexo, idade = dados.split()
  
  # Analisando a maioridade
  if sexo == "feminino":
    if int(idade) >= 21:
      mensagem = "Maioridade atingida!"
    else:
      mensagem = "Maioridade nao atingida ainda!"
  else:
    if int(idade) >= 18:
      mensagem = "Maioridade atingida!"
    else:
      mensagem = "Maioridade não atingida ainda!"

  print(mensagem)