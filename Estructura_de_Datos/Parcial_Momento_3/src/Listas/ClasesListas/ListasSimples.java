package Listas.ClasesListas;

import Listas.ClasesListas.SubClasesListasCirculares.ImprimirListasDobles;
import Listas.ClasesListas.SubClasesListasSimples.AgregarListasSimples;
import Listas.ClasesListas.SubClasesListasSimples.EliminarListasSimples;
import Listas.ClasesListas.SubClasesListasSimples.ImprimirListasSimples;
import Listas.ClasesListas.SubClasesListasSimples.ReportesListasSimples;

public class ListasSimples {

    EliminarListasSimples eliminarListasSimples = new EliminarListasSimples();
    AgregarListasSimples agregarListasSimples = new AgregarListasSimples();
    ImprimirListasSimples imprimirListasSimples = new ImprimirListasSimples();
    ReportesListasSimples reportesListasSimples = new ReportesListasSimples();

    public void menuListasSimples()
    {
        int opc;
        System.out.println("MENU LISTAS SIMPLES");
        System.out.println("1. Adicionar listas simples.");
        System.out.println("2. Eliminar listas simples");
        System.out.println("3. Modificar listas simples");
        System.out.println("4. Imprimir listas simples");
        System.out.println("5. Imprimir artistas de forma impar.");
        System.out.println("6. Reportes");
        System.out.println("7. Volver.");

        System.out.println();
        System.out.println("Escoja una opcion");
        opc = leer.nextInt();

        switch (opc) {
            case 1:
                agregarListasSimples.menuAdicionarListasSimples();
                menuListasSimples();
                break;

            case 2:
                eliminarListasSimples.menuEliminarListasSimples();
                menuListasSimples();
                break;

            case 3:
                modificarListasSimples();
                menuListasSimples();
                break;

            case 4:
                imprimirListasSimples.imprimirListasSimples();
                menuListasSimples();
                break;

            case 5:
                imprimirNodosImparesArtista();
                menuListasSimples();
                break;

            case 6:
                reportesListasSimples.menuReportesListasSimples();
                menuListasSimples();
                break;

            case 7:
                menuPrincipal();
                break;

            default:
                menuListasSimples();
        }
    }
}
