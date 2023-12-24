package Listas.ClasesListas;

import Entidades.Artista;
import Listas.ClasesListas.SubClasesListasSimples.*;

import java.util.Scanner;

public class ListasSimples {
    EliminarListasSimples eliminarListasSimples;
    AgregarListasSimples agregarListasSimples;
    ImprimirListasSimples imprimirListasSimples;
    ReportesListasSimples reportesListasSimples;
    ModificarListasSimples modificarListasSimples = new ModificarListasSimples();
    Artista cabezaListasSimples;
    public Scanner leer = new Scanner(System.in);

    public ListasSimples(Artista cabezaArtista, Artista punteroArtista, Artista nodoNuevoArtista) {
        cabezaListasSimples = cabezaArtista;

        agregarListasSimples = new AgregarListasSimples();
        reportesListasSimples = new ReportesListasSimples();
        eliminarListasSimples = new EliminarListasSimples();
        imprimirListasSimples = new ImprimirListasSimples();
    }

    public Artista cambiarReferenciaCabezaListasSimples(Artista cabezaActual, Artista nodoCabezaNueva) {
        Artista cabezaNueva;

        cabezaNueva = nodoCabezaNueva;
        cabezaNueva.siguiente = cabezaActual;

        return cabezaNueva;
    }

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
//                modificarListasSimples.modificarListasSimples();
                menuListasSimples();
                break;

            case 4:
                imprimirListasSimples.imprimirListasSimples(cabezaListasSimples);
                menuListasSimples();
                break;

            case 5:
                imprimirListasSimples.imprimirNodosImparesArtista();
                menuListasSimples();
                break;

            case 6:
                reportesListasSimples.menuReportesListasSimples();
                menuListasSimples();
                break;

            case 7:
                break;

            default:
                menuListasSimples();
        }
    }
}
