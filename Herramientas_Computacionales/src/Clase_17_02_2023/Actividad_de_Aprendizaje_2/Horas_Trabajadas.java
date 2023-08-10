package UCC.Momento_1.Actividad_de_Aprendizaje_2;
import java.util.Scanner;

public class Horas_Trabajadas {
    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);
        
        System.out.println("Ingrese la cantidad de horas trabajadas : ");
        int nHoras = entrada.nextInt();
        final int vHora = 50000;
        
        entrada.close();
        
        System.out.println("-----------COLILLA DE PAGO-----------" + 
            "\nSueldo Bruto : $" + (nHoras*50000) + "\nDescuento en Salud : $" + ((nHoras * vHora) * 0.05) +  "\nDescuento en Pension : $" + ((nHoras * vHora) * 0.06) + "\nTotal Descuentos : $" + (nHoras *  vHora) * 0.11 + "\nSueldo Neto : $" + (nHoras*vHora - (nHoras *  vHora) * 0.11) );
    }
}