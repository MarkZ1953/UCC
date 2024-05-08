package Listas.ClasesListas.SubClasesListasSimples;
import Entidades.Artista;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Scanner;


public class ReportesListasSimples {

    private Artista cabezaArtista;
    private Artista punteroArtista;
    private Artista nodoNuevoArtista;

    public Scanner leer = new Scanner(System.in);

    public void menuReportesListasSimples() {
        int opcion;

        System.out.println("REPORTES LISTAS SIMPLES");
        System.out.println("1. Imprimir artistas por caracter alfabetico");
        System.out.println("2. Imprimir cantidad de artistas");
        System.out.println("3. Imprimir el artista mas joven y mas viejo");
        System.out.println("4. Imprimir artistas por nacionalidad");
        System.out.println("5. Volver a menu listas simples");

        System.out.println();
        System.out.println("Escoja una opcion: ");
        opcion = leer.nextInt();

        switch (opcion) {
            case 1:
                imprimirNodosPorLetraListasSimples();
                menuReportesListasSimples();
                break;
            case 2:
                imprimirCantidadNodosListasSimples();
                menuReportesListasSimples();
                break;
            case 3:
                imprimirNodoMasViejoYJoven();
                menuReportesListasSimples();
                break;
            case 4:
                imprimirNodosPorNacionalidadListasSimples();
                menuReportesListasSimples();
                break;
            case 5:
                break;
            default:
                menuReportesListasSimples();
        }
    }

    public void imprimirNodoMasViejoYJoven() {

        DateTimeFormatter formato = DateTimeFormatter.ofPattern("dd/MM/yyyy");
        LocalDate fechaNacimientoMayor, fechaNacimientoMenor, fechaNacimiento;
        Artista nodoArtistaMayor = null, nodoArtistaMenor = null;

        fechaNacimientoMayor = LocalDate.parse(cabezaArtista.getFechaNacimiento(), formato);
        fechaNacimientoMenor = LocalDate.parse(cabezaArtista.getFechaNacimiento(), formato);

        punteroArtista = cabezaArtista.siguiente;

        while (punteroArtista != null) {

            fechaNacimiento = LocalDate.parse(punteroArtista.getFechaNacimiento(), formato);

            if (fechaNacimiento.isBefore(fechaNacimientoMayor)) {
                fechaNacimientoMayor = fechaNacimiento;
                nodoArtistaMayor = punteroArtista;
            } else if (fechaNacimiento.isAfter(fechaNacimientoMenor)) {
                fechaNacimientoMenor = fechaNacimiento;
                nodoArtistaMenor = punteroArtista;
            }

            punteroArtista = punteroArtista.siguiente;
        }

        System.out.println();
        System.out.println("El Entidades.Artista mas joven es: " + nodoArtistaMenor.getNombre());
        System.out.println("El Entidades.Artista mas viejo es: " + nodoArtistaMayor.getNombre());
        System.out.println();

    }

    public void imprimirNodosPorNacionalidadListasSimples() {

        String nacionalidadAFiltrar;

        System.out.println("Ingrese la nacionalidad por la que desea filtrar la lista: ");
        nacionalidadAFiltrar = leer.next();
        
        punteroArtista = cabezaArtista;

        while (punteroArtista != null) {
            if (nacionalidadAFiltrar.compareToIgnoreCase(punteroArtista.getNacionalidad()) == 0) {
                System.out.println();
                System.out.println(punteroArtista.toString());
            }
            punteroArtista = punteroArtista.siguiente;
        }

        System.out.println();
    }

    public void imprimirNodosPorLetraListasSimples() {
        String caracterAlfabetico;

        punteroArtista = cabezaArtista;
        
        System.out.println("Ingrese la letra por la que desea buscar los nombres: ");
        caracterAlfabetico = leer.next();

        while (punteroArtista != null) {
            if (Character.toUpperCase(caracterAlfabetico.charAt(0)) == Character.toUpperCase(punteroArtista.getNombre().charAt(0))) {
                System.out.println();
                System.out.println(punteroArtista.toString());
            }
            punteroArtista = punteroArtista.siguiente;
        }

        System.out.println();
    }

    public void imprimirCantidadNodosListasSimples() {
        int contador = 0;
    
        punteroArtista = cabezaArtista;

        while (punteroArtista != null) {
            contador++;
            punteroArtista = punteroArtista.siguiente;
        }

        if (contador == 0) {
            System.out.println("No hay artistas en la lista");
        } else {
            System.out.println("Hay " + contador + " Artistas en la lista");
        }
        
    }
}
