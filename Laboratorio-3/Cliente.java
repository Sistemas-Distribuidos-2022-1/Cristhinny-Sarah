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
      
      try{
        dataOut.writeUTF(String.valueOf(problema)); 
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