package Listas.ClasesListas.SubClasesListasSimples;

import Entidades.Artista;

import java.util.Scanner;

public class ImprimirListasSimples {
    public Artista cabezaArtista;
    public Artista punteroArtista;
    public Artista nodoNuevoArtista;
    public Scanner leer = new Scanner(System.in);

    public void imprimirListasSimples(Artista cabezaArtista)
    {
        punteroArtista = cabezaArtista;
        System.out.println("Referencia cabeza: " + cabezaArtista);

        while (punteroArtista != null)
        {
            System.out.println();
            System.out.println(punteroArtista.obtenerInformacion());
            punteroArtista = punteroArtista.siguiente;
        }

        System.out.println();
    }

    public void imprimirNodosImparesArtista() {
        int contador = 1;
        punteroArtista = cabezaArtista;

        while (true)
        {
            System.out.println();
            System.out.println("Id: " + contador);
            System.out.println(punteroArtista.toString());
            System.out.println("Direccion de memoria del Nodo: "+ punteroArtista);

            if (punteroArtista.siguiente != null) {
                punteroArtista = punteroArtista.siguiente.siguiente;
                contador = contador + 2;
            } else {
                break;
            }
        }

        System.out.println();
    }
}
