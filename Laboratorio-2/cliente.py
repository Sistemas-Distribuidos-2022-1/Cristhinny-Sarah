import socket

HOST = 'localhost'     # Endereço IP do Servidor
PORT = 50000            # Porta que o Servidor está

def ReajusteSalario():
  nome = input("Entre com o nome: ")
  cargo = input("Entre com o cargo: ")
  salario = int(input("Entre com o salario: "))
  mensagem = str(1) + "$" + nome + "$" + cargo + "$" + str(salario)
  EnviaMensagem(mensagem)

def Maioridade():
  nome = input("Entre com o nome: ")
  sexo = input("Entre com o sexo: ")
  idade = int(input("Entre com a idade: "))
  mensagem = str(2) + "$" + nome + "$" + sexo + "$" + str(idade)
  EnviaMensagem(mensagem)

def MediaNotas():
  N1 = float(input("Entre com a N1: "))
  N2 = float(input("Entre com a N2: "))
  N3 = float(input("Entre com a N3: "))
  mensagem = str(3) + "$" + str(N1) + "$" + str(N2) + "$" + str(N3)
  EnviaMensagem(mensagem)

def PesoIdeal():
  altura = float(input("Entre com a altura da pessoa: "))
  sexo = input("Entre com o sexo da pessoa: ")
  mensagem = str(4) + "$" + str(altura) + "$" + sexo
  EnviaMensagem(mensagem)

def ClassificacaoNadador():
  idade = int(input("Entre com a idade da pessoa: "))
  mensagem = str(5) + "$" + str(idade)
  EnviaMensagem(mensagem)

def SalarioLiquido():
  nome = input("Entre com o nome: ")
  nivel = input("Entre com o nivel: ")
  salarioBruto = float(input("Entre com o salario bruto: "))
  numeroDeDependentes = int(input("Entre com o números de dependentes do funcionário: "))
  mensagem = str(6) + "$" + nome + "$" + nivel + "$" + str(salarioBruto) + "$" + str(numeroDeDependentes)
  EnviaMensagem(mensagem)

def Aposentadoria():
  idade = int(input("Entre com a idade do funcionario: "))
  tempoDeServico = int(input("Entre com o tempo de serviço em anos: "))
  mensagem = str(7) + "$" + str(idade) + "$" + str(tempoDeServico)
  EnviaMensagem(mensagem)

def CreditoEspecial():
  saldoMedio = float(input("Entre com o saldo medio do cliente: "))
  mensagem = str(8) + "$" + str(saldoMedio)
  EnviaMensagem(mensagem)

def EscolhendoProblema(problema):
  if problema == 1:
    ReajusteSalario()
  if problema == 2:
    Maioridade()
  if problema == 3:
    MediaNotas()
  if problema == 4:
    PesoIdeal()     
  if problema == 5:
    ClassificacaoNadador()          
  if problema == 6:
    SalarioLiquido()           
  if problema == 7:
    Aposentadoria()                 
  if problema == 8:
    CreditoEspecial()

def EnviaMensagem(mensagem):
  # Para conectar ao socket precisamos passar a família de protocolos
  # AF_INET = IPV4
  # sock_STREAM = TCP
  S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  S.connect((HOST, PORT))

  # envio dos dados para o servidor
  S.send(str(mensagem).encode())

  # dados do servidor
  resposta = S.recv(4096).decode()
  print("Resposta do servidor: ", resposta)

  # fechando o Socket
  S.close()

while True:
  print("\n\nEscolha um problema:")
  print("1: Reajuste de Salario")
  print("2: Maioridade")
  print("3: Media de Notas")
  print("4: Peso Ideal")
  print("5: Classificar Nadadores")
  print("6: Salario Liquido")
  print("7: Aposentadoria")
  print("8: Credito Especial")
  print("0: Sair")
  problema = int(input())
  if problema == 0:
    break
  EscolhendoProblema(problema)