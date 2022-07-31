import xmlrpc.client

problema = -1

with xmlrpc.client.ServerProxy("http://localhost:8000/") as conexao:
  while True:
    print("\nEscolha um problema: ")
    print("1: Reajuste de Salario")
    print("2: Maioridade")
    print("3: Media de Notas")
    print("4: Peso Ideal")
    print("5: Classificar Nadadores")
    print("6: Salario Liquido")
    print("7: Aposentadoria")
    print("8: Credito Especial")
    problema = input("0: Sair\n")
    problema = int(problema)

    if problema == 0:
      break
    
    if problema == 1:
      # coletando informações do usuário
      nome = input("Entre com o nome: ")
      cargo = input("Entre com o cargo: ")
      salario = int(input("Entre com o salario: "))
      
      mensagem = conexao.salarios(nome, cargo, salario)
      print(mensagem)
    
    if problema == 2:
      # coletando informações do usuário
      nome = input("Entre com o nome: ")
      sexo = input("Entre com o sexo: ")
      idade = int(input("Entre com a idade: "))

      mensagem = conexao.maioridade(nome, sexo, idade)
      print(mensagem)

    if problema == 3:
      # coletando informações do usuário
      N1 = float(input("Entre com a N1: "))
      N2 = float(input("Entre com a N2: "))
      N3 = float(input("Entre com a N3: "))

      mensagem = conexao.media(N1, N2, N3)
      print(mensagem)

    if problema == 4:
      # coletando informações do usuário
      altura = input("Entre com a altura da pessoa: ")
      sexo = input("Entre com o sexo da pessoa: ")

      mensagem = conexao.pesoIdeal(altura, sexo)
      print(mensagem)
    
    if problema == 5:
      # coletando informações do usuário
      idade = int(input("Entre com a idade da pessoa: "))
      
      mensagem = conexao.categoria(idade)
      print(mensagem)
    
    if problema == 6:
      # coletando informações do usuário
      nome = input("Entre com o nome: ")
      nivel = input("Entre com o nivel: ")
      salarioBruto = float(input("Entre com o salario bruto: "))
      numeroDeDependentes = int(input("Entre com o números de dependentes do funcionário: "))
      
      mensagem = conexao.salarioLiquido(nome, nivel, salarioBruto, numeroDeDependentes)
      print(mensagem)

    if problema == 7:
      # coletando informações do usuário
      idade = int(input("Entre com a idade do funcionario: "))
      tempoDeServico = int(input("Entre com o tempo de serviço em anos: "))
      
      mensagem = conexao.aposentadoria(idade, tempoDeServico)
      print(mensagem)

    if problema == 8:
      # coletando informações do usuário
      saldoMedio = float(input("Entre com o saldo medio do cliente: "))
      
      mensagem = conexao.saldoMedio(saldoMedio)
      print(mensagem)