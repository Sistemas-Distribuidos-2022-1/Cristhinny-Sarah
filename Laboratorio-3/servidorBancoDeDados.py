import psycopg2
import socket

HOST = 'localhost'
PORT = 8000

while True:
  # Para criar o socket precisamos passar a família de protocolos
  # AF_INET = IPV4
  # sock_STREAM = TCP
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  # o servidor estará linkado com a respectiva porta e HOST definidas anteriormente
  server.bind((HOST, PORT))
  # vamos ouvir o endereço uma unica vez
  server.listen(1)
  print("\nAguardando a conexao de um cliente")

  conexao, endereco = server.accept()
  print("Conectado em ", endereco)

  data = conexao.recv(1024).decode()

  con = psycopg2.connect(host='localhost', database='SistemasDistribuidos', user='postgres', password='timosa123')
  cur = con.cursor()

  cur.execute("SELECT * FROM ex" + data)
  recset = cur.fetchall()

  for rec in recset:
    #print(rec)
    mensagem = '$'.join(str(i) for i in rec)

  print("Dados recebidos do banco de dados: ", mensagem)
  print("Enviando os dados do banco de dados...\n")

  conexao.sendall(mensagem.encode())

  con.close()
  conexao.close()