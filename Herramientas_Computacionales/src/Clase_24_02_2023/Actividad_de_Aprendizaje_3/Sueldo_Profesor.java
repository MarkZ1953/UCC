package UCC.Momento_1.Actividad_de_Aprendizaje_3;
import javax.swing.JOptionPane;
import java.text.DecimalFormat;

public class Sueldo_Profesor {
    public static void main(String[] args) {

        DecimalFormat df = new DecimalFormat("#,###.00");

        float salario = Float.parseFloat(JOptionPane.showInputDialog(null, "Ingrese su salario en bruto: "));

    }   
}
