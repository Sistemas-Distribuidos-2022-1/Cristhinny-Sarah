import zmq

HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor está

contexto = zmq.Context()
socket = contexto.socket(zmq.SUB)
conexao = "tcp://" + HOST + ":" + str(PORT)

socket.connect(conexao)
socket.setsockopt_string(zmq.SUBSCRIBE, "MEDIA")

while(True):
  dados = socket.recv(4096).decode()
  
  if dados == None:
    continue
  
  print("Mensagem recebida no sub 3!")  

  tipo, N1, N2, N3 = dados.split()
  mediaN1N2 = (float(N1) + float(N2))/2 

  # Analisando se o aluno foi aprovado
  if mediaN1N2 >= 7.0:
    mensagem = "O aluno foi aprovado!"
  else:
    if mediaN1N2 > 3.0 and mediaN1N2 < 7.0:
      if (mediaN1N2 + float(N3))/2 >= 5.0:
        mensagem = "O aluno foi aprovado!"
      else:
        mensagem = "O aluno foi reprovado!"
    else:
      mensagem = "O aluno foi reprovado!"

  print(mensagem)