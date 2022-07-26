import zmq

HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor está

contexto = zmq.Context()
socket = contexto.socket(zmq.SUB)
conexao = "tcp://" + HOST + ":" + str(PORT)

socket.connect(conexao)
socket.setsockopt_string(zmq.SUBSCRIBE, "PESOIDEAL")

while(True):
  dados = socket.recv(4096).decode()
  
  if dados == None:
    continue
  
  print("Mensagem recebida no sub 4!")

  tipo, altura, sexo = dados.split(' ')
  pesoIdeal = 0.00

  # Analisando o peso ideal
  if sexo == "feminino":
    pesoIdeal = (62.1*float(altura)) - 44.7
  else:
    pesoIdeal = (72.7*float(altura)) - 58

  mensagem = "Peso ideal para o sexo " + sexo + " e altura " + altura + ": " + str(pesoIdeal)

  print(mensagem)