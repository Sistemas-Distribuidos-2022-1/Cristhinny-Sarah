import zmq

HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor está

contexto = zmq.Context()
socket = contexto.socket(zmq.SUB)
conexao = "tcp://" + HOST + ":" + str(PORT)

socket.connect(conexao)
socket.setsockopt_string(zmq.SUBSCRIBE, "CATEGORIA")

while(True):
  dados = socket.recv(4096).decode()
  
  if dados == None:
    continue
  
  print("Mensagem recebida no sub 5!")

  tipo, idade = dados.split(' ')
  idade = int(idade)
  
  # Analisando a categoria da pessoa
  if idade >= 0 and idade <= 4:
    mensagem = "Sem categoria!"
  else:
    if idade >= 5 and idade <= 7:
      mensagem = "Categoria: Infantil A"
    else:
      if idade >= 8 and idade <= 10:
        mensagem = "Categoria: Infantil B"
      else:
        if idade >= 11 and idade <= 13:
          mensagem = "Categoria: Juvenil A"
        else:
          if idade >= 14 and idade <= 17:
            mensagem = "Categoria: Juvenil B"
          else:
            mensagem = "Categoria: Adulto"

  print(mensagem)