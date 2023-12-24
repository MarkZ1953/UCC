package Listas.ClasesListas.SubClasesListasSimples;

import Entidades.Artista;

import java.util.Scanner;

public class AgregarListasSimples {

    public Artista cabezaArtista;
    public Artista punteroArtista;
    public Artista nodoNuevoArtista;
    public Scanner leer = new Scanner(System.in);

    public Artista recolectarInformacionArtista() {

        String nombre, nacionalidad, fechaNacimiento;

        System.out.println("Digite el nombre del artista: ");
        nombre = leer.next();

        System.out.println("Digite la nacionalidad del artista: ");
        nacionalidad = leer.next();

        System.out.println("Digite fecha de nacimiento del artista: ");
        fechaNacimiento = leer.next();

        return new Artista(nombre, nacionalidad, fechaNacimiento);
    }

    public void menuAdicionarListasSimples()
    {
        int opcion;
        System.out.println("MENU ADICIONAR LISTAS SIMPLES");
        System.out.println("1. Adicionar por el inicio listas simples.");
        System.out.println("2. Adicionar por el fin listas simples.");
        System.out.println("3. Adicionar antes de nodo listas simples");
        System.out.println("4. Adicionar despues de nodo listas simples");
        System.out.println("5. Volver.");

        System.out.println("\nEscoja una opcion;");
        opcion = leer.nextInt();

        switch (opcion) {
            case 1:
                adicionarInicioListasSimples();
                menuAdicionarListasSimples();
                break;

            case 2:
                adicionarFinListasSimples();
                menuAdicionarListasSimples();
                break;

            case 3:
                adicionarAntesListasSimples();
                menuAdicionarListasSimples();
                break;

            case 4:
                adicionarDespuesListasSimples();
                menuAdicionarListasSimples();
                break;

            case 5:
                break;

            default:
                menuAdicionarListasSimples();
                break;
        }
    }

    public void adicionarInicioListasSimples()
    {
        nodoNuevoArtista = recolectarInformacionArtista();
        nodoNuevoArtista.siguiente = cabezaArtista;
        cabezaArtista = nodoNuevoArtista;

        System.out.println("Se ha agregado correctamente el nuevo Artista");
    }

    public void adicionarFinListasSimples()
    {
        nodoNuevoArtista = recolectarInformacionArtista();
        punteroArtista = cabezaArtista;

        while(punteroArtista.siguiente != null) {
            punteroArtista = punteroArtista.siguiente;
            punteroArtista.siguiente = nodoNuevoArtista;
        }
    }

    public void adicionarDespuesListasSimples()
    {
        Artista nodoSiguienteArtista;
        String nombreABuscar;

        System.out.println("Ingrese el nombre a buscar: ");
        nombreABuscar = leer.next();

        punteroArtista = cabezaArtista;

        while (punteroArtista != null) {
            if (punteroArtista.getNombre().compareToIgnoreCase(nombreABuscar) == 0) {

                // Se obtiene el siguiente del nodo que se estaba buscando
                nodoSiguienteArtista = punteroArtista.siguiente;

                // Se crea un nuevo nodo
                nodoNuevoArtista = recolectarInformacionArtista();

                // El nuevo nodo hace que su siguiente ahora apunte a el nodo siguiente del nodo encontrado
                nodoNuevoArtista.siguiente = nodoSiguienteArtista;

                // El siguiente del puntero ahora apunta a el nuevo nodo que tiene la cola
                punteroArtista.siguiente = nodoNuevoArtista;

                break;
            }
            punteroArtista = punteroArtista.siguiente;
        }
    }

    public void adicionarAntesListasSimples()
    {
        Artista nodoAnteriorArtista;
        String nombreABuscar;

        punteroArtista = cabezaArtista;

        System.out.println("Digite el nombre a buscar: ");
        nombreABuscar = leer.next();

        if(cabezaArtista.getNombre().compareToIgnoreCase(nombreABuscar)==0)
        {
            adicionarInicioListasSimples();
        }
        else
        {
            // Se pone cabezaArtista.siguiente porque ya se verifico que el valor que se estaba buscando no era el
            // primero
            nodoNuevoArtista = recolectarInformacionArtista();
            punteroArtista = cabezaArtista.siguiente; // Se quiere iniciar desde el segundo nodo de la lista
            nodoAnteriorArtista = cabezaArtista;

            // Se itera toda la lista, y cuando se encuentre el valor que se solicito, entonces el nodoAnteriorArtista
            // se queda con el nodoActualArtista
            while(punteroArtista.getNombre().compareToIgnoreCase(nombreABuscar)!=0 && punteroArtista.siguiente !=null)
            {
                nodoAnteriorArtista = punteroArtista;
                punteroArtista = punteroArtista.siguiente;
            }

            if(punteroArtista.getNombre().compareToIgnoreCase(nombreABuscar)==0)
            {
                nodoNuevoArtista.siguiente = punteroArtista;
                nodoAnteriorArtista.siguiente = nodoNuevoArtista;
            }
            else
                System.out.println("El nombre buscado no se encuentra en la lista");
        }
                
    }

}
