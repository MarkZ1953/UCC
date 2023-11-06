import Listas.ClasesListas.ListasCirculares;
import Listas.ClasesListas.ListasCircularesDobles;
import Listas.ClasesListas.ListasDobles;
import Listas.ClasesListas.ListasSimples;

public class Listas {
    
    ListasSimples listasSimples = new ListasSimples();
    ListasCirculares listasCirculares = new ListasCirculares();
    ListasDobles listasDobles = new ListasDobles();
    ListasCircularesDobles listasCircularesDobles = new ListasCircularesDobles();
    
    public Listas() {
        menuPrincipal();
    }

    public void menuPrincipal()
    {
        int opcion;
        System.out.println("MENU PRINCIPAL");
        System.out.println("1. Listas simples");
        System.out.println("2. Listas circulares");
        System.out.println("3. Listas dobles");
        System.out.println("4. Listas circulares dobles");
        System.out.println("5. Terminar");
        
        System.out.println();
        System.out.println("Escoja la opcion:");

        opcion = leer.nextInt();
        
        switch (opcion) {
            case 1:
                listasSimples.menuListasSimples();
                menuPrincipal();
                break;
                
            case 2:
                listasCirculares.menuListasCirculares();
                menuPrincipal();
                break;
                
            case 3:
                listasDobles.menuListasDobles();
                menuPrincipal();
                break;
                
            case 4:
                listasCircularesDobles.menuListasCircularesDobles();
                menuPrincipal();
                break;
                
            case 5:
                System.exit(0);
                break;
                
            default:
                menuPrincipal();
        }
    }

    public static void main(String[] args) {
        Listas listas = new Listas();
    }

}
