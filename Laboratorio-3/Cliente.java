// import statements
import java.net.*;
import java.io.*;
import java.util.Scanner;

public class Cliente{
  // inicializando os sockets e os canais de input e output 
  private DataOutputStream dataOut = null;
  private BufferedReader dataIn = null;
  
  private Socket S = null;
  private Scanner teclado = new Scanner(System.in);
  
  private int problema = -1;
  private String mensagem = null;
  private String mensagemRecebida;
  private String buffer;

  private String dadoS1;
  private String dadoS2;

  private float dadoF1;
  private float dadoF2;
  private float dadoF3;

  private int dadoI1;
  private int dadoI2;
  
  // construtor de um socket dado um IP e uma porta
  public Cliente(String address, int port){
    // vamos pegar os dados do usuário
    while (problema != 0){
      mensagem = null;
      
      System.out.println("\nEscolha um problema:");
      System.out.println("1: Reajuste de Salario");
      System.out.println("2: Maioridade");
      System.out.println("3: Media de Notas");
      System.out.println("4: Peso Ideal");
      System.out.println("5: Classificar Nadadores");
      System.out.println("6: Salario Liquido");
      System.out.println("7: Aposentadoria");
      System.out.println("8: Credito Especial");
      System.out.println("0: Sair");
      
      problema = teclado.nextInt();
      
      if(problema == 0){
        System.out.println(" Conexao finalizada!! ");
        // finalizando a conexao
        try{
          dataIn.close();
          dataOut.close();
          S.close();
        }
        catch(IOException io){
          System.out.println(io);
        }
        break;
      }

      // fazendo a conexão com o servidor
      try{
        // criando um socket
        S = new Socket(address, port);
        System.out.println("\nConectado ao Servidor!");
        System.out.println("Para finalizar a conexao, digite \"0\" ");
        
        // Abrindo o canal de output e input do socket
        dataOut = new DataOutputStream(S.getOutputStream());
        dataIn = new BufferedReader(new InputStreamReader(S.getInputStream()));
      }
      catch(UnknownHostException uh){
        System.out.println(uh);
      }
      catch(IOException io){
        System.out.println(io);
      }

      if(problema == 1){
        System.out.println("\nEntre com o nome: ");
        buffer = teclado.nextLine();
        dadoS1 = teclado.nextLine();
        System.out.println("Entre com o cargo: ");
        dadoS2 = teclado.nextLine();
        System.out.println("Entre com o salario: ");
        dadoF1 = teclado.nextFloat();
        
        mensagem = problema + "$" + dadoS1 + "$" + dadoS2 + "$" + dadoF1;
      }
      if(problema == 2){
        System.out.println("\nEntre com o nome: ");
        buffer = teclado.nextLine();
        dadoS1 = teclado.nextLine();
        System.out.println("Entre com o sexo: ");
        dadoS2 = teclado.nextLine();
        System.out.println("Entre com o idade: ");
        dadoI1 = teclado.nextInt();

        mensagem = "2$" + dadoS1 + "$" + dadoS2 + "$" + dadoI1;
      }
      if(problema == 3){
        System.out.println("\nEntre com a nota N1: ");
        buffer = teclado.nextLine();
        dadoF1 = teclado.nextFloat();
        System.out.println("Entre com a nota N2: ");
        dadoF2 = teclado.nextFloat();
        System.out.println("Entre com a nota N3: ");
        dadoF3 = teclado.nextFloat();

        mensagem = "3$" + dadoF1 + "$" + dadoF2 + "$" + dadoF3;
      }
      if(problema == 4){
        System.out.println("\nEntre com a altura: ");
        dadoF1 = teclado.nextFloat();
        System.out.println("Entre com o sexo: ");
        buffer = teclado.nextLine();
        dadoS1 = teclado.nextLine();

        mensagem = "4$" + dadoF1 + "$" + dadoS1;
      }
      if(problema == 5){
        System.out.println("\nEntre com o idade: ");
        buffer = teclado.nextLine();
        dadoI1 = teclado.nextInt();

        mensagem = "5$" + dadoI1;
      }
      if(problema == 6){
        System.out.println("\nEntre com o nome: ");
        buffer = teclado.nextLine();
        dadoS1 = teclado.nextLine();
        System.out.println("Entre com o nivel: ");
        dadoS2 = teclado.nextLine();
        System.out.println("Entre com o salario bruto: ");
        dadoF1 = teclado.nextFloat();
        System.out.println("Entre com o numero de dependentes do funcionario: ");
        dadoI1 = teclado.nextInt();

        mensagem = "6$" + dadoS1 + "$" + dadoS2 + "$" + dadoF1 + "$" + dadoI1;
      }
      if(problema == 7){
        System.out.println("\nEntre com a idade do funcionario: ");
        buffer = teclado.nextLine();
        dadoI1 = teclado.nextInt();
        System.out.println("Entre com o tempo de servico em anos: ");
        dadoI2 = teclado.nextInt();

        mensagem = "7$" + dadoI1 + "$" + dadoI2;
      }
      if(problema == 8){
        System.out.println("\nEntre com o salario medio do cliente: ");
        buffer = teclado.nextLine();
        dadoF1 = teclado.nextFloat();

        mensagem = "8$" + dadoF1;
      }
      
      try{
        dataOut.writeUTF(mensagem); 
      }
      catch(IOException io){
        System.out.println(io);
      }
    
      try{
        mensagemRecebida = dataIn.readLine();
        System.out.println(mensagemRecebida);
      }
      catch(IOException e) {
        e.printStackTrace();
      }
    } 
  }
  
  public static void main(String argvs[]){
      Cliente client = new Cliente("localhost", 50000);
  }
}