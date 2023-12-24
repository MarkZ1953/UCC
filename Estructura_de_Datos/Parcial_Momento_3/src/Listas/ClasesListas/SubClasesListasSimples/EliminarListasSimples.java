package Listas.ClasesListas.SubClasesListasSimples;

import Entidades.Artista;

import java.util.Scanner;

public class EliminarListasSimples {

    private Artista cabezaArtista;
    private Artista punteroArtista;
    private Artista nodoNuevoArtista;
    public Scanner leer = new Scanner(System.in);

    public void menuEliminarListasSimples()
    {
        int opcion;
        System.out.println("MENU ELIMINAR LISTAS SIMPLES");
        System.out.println("1. Eliminar por el inicio listas simples.");
        System.out.println("2. Eliminar por el fin listas simples.");
        System.out.println("3. Eliminar antes de nodo listas simples");
        System.out.println("4. Eliminar despues de nodo listas simples");
        System.out.println("5. Eliminar nodo dado listas simples.");
        System.out.println("6. Volver.");

        System.out.println("\nEscoja una opcion;");
        opcion = leer.nextInt();

        switch (opcion) {
            case 1:
                eliminarInicioListasSimples();
                menuEliminarListasSimples();
                break;

            case 2:
                eliminarFinListasSimples();
                menuEliminarListasSimples();
                break;

            case 3:
                eliminarAntesListasSimples();
                menuEliminarListasSimples();
                break;

            case 4:
                eliminarDespuesListasSimples();
                menuEliminarListasSimples();
                break;

            case 5:
                eliminarNodoDadoListasSimples();
                menuEliminarListasSimples();
                break;

            case 6:
                break;

            default:
                menuEliminarListasSimples();
                break;
        }
    }

    public boolean verificarExistenciaNodoListasSimples(String nombre) {
        boolean nodoEncontrado = false;

        punteroArtista = cabezaArtista;

        while (punteroArtista != null) {
            punteroArtista = punteroArtista.siguiente;
            nodoEncontrado = true;
            break;
        }

        return nodoEncontrado;
    }

    public void eliminarAntesListasSimples()
    {
        // Se declaran las variables necesarias
        String nombreABuscar;
        Artista nodoArtistaAnteriorTemp = null;
        Artista nodoArtistaAnteriorAnterior = null;

        // Se pide el artista el cual se desea buscar
        System.out.println("Ingrese el nombre a buscar: ");
        nombreABuscar = leer.next();

        if (verificarExistenciaNodoListasSimples(nombreABuscar)) {
            // Hacemos que el puntero inicie desde la cabeza
            punteroArtista = cabezaArtista;

            // Se pregunta si el valor que esta buscando es el anterior a la cabeza
            if (cabezaArtista.getNombre().compareToIgnoreCase(nombreABuscar) == 0) {
                System.out.println("Se encontro el Entidades.Artista, pero no se puede eliminar el anterior ya que no existe");
            } else if (punteroArtista.siguiente == null) {
                System.out.println("No se puede eliminar ya que la lista solo posee un elemento");

            } else if (punteroArtista.siguiente.getNombre().compareToIgnoreCase(nombreABuscar) == 0) {
                eliminarInicioListasSimples();
            } else {
                // Se busca el valor que se esta solicitando, iterando toda la lista
                while (punteroArtista != null) {
                    // Se pregunta que si en el caso de que el siguiente del puntero sea el que se esta buscando, guarde
                    // el nodo anterior al que se esta buscando
                    if (punteroArtista.siguiente.siguiente.getNombre().compareToIgnoreCase(nombreABuscar) == 0 && punteroArtista.siguiente != null) {

                        nodoArtistaAnteriorAnterior = punteroArtista;
                        nodoArtistaAnteriorTemp = punteroArtista.siguiente;
                        nodoArtistaAnteriorAnterior.siguiente = nodoArtistaAnteriorAnterior.siguiente.siguiente;

                        // Se elimina el nodo anterior al que se estaba buscando
                        nodoArtistaAnteriorTemp = null;

                        System.out.println("Se ha eliminado correctamente");
                        break;
                    }

                    punteroArtista = punteroArtista.siguiente;
                }
            }
        } else {
            System.out.println("No se ha encontrado el Entidades.Artista que se estaba buscando");
        }
    }

    public void eliminarDespuesListasSimples()
    {
        // Se declaran las variables necesarias
        String nombreABuscar;
        Artista nodoSiguienteArtista = null;

        // Se pide el artista el cual se desea buscar
        System.out.println("Ingrese el nombre a buscar: ");
        nombreABuscar = leer.next();

        if (verificarExistenciaNodoListasSimples(nombreABuscar)) {

            punteroArtista = cabezaArtista;

            while (punteroArtista != null) {
                if (punteroArtista.siguiente == null) {
                    eliminarFinListasSimples();
                    break;
                } else if (punteroArtista.getNombre().compareToIgnoreCase(nombreABuscar) == 0) {

                    // Obtiene el nodo actual
                    nodoSiguienteArtista = punteroArtista;

                    // Se conecta el siguiente del siguiente del valor encontrado
                    nodoSiguienteArtista.siguiente = nodoSiguienteArtista.siguiente.siguiente;

                    // Eliminar el nodo siguiente al nodo solicitado
                    nodoSiguienteArtista = null;

                    System.out.println("Se ha eliminado correctamente");

                    break;
                }

                punteroArtista = punteroArtista.siguiente;
            }

        } else {
            System.out.println("No se ha encontrado el Artista que se estaba buscando");
        }
    }

    public void eliminarNodoDadoListasSimples() {
        String nombreABuscar;
        Artista nodoArtista;

        // Se pide el artista el cual se desea buscar
        System.out.println("Ingrese el nombre del artista a eliminar: ");
        nombreABuscar = leer.next();

        if (verificarExistenciaNodoListasSimples(nombreABuscar)) {

            punteroArtista = cabezaArtista;

            if (nombreABuscar.compareToIgnoreCase(cabezaArtista.getNombre()) == 0) {
                eliminarInicioListasSimples();
                System.out.println("Se ha eliminado correctamente");
            } else {
                while (punteroArtista != null && punteroArtista.siguiente != null) {
                    if (nombreABuscar.compareToIgnoreCase(punteroArtista.siguiente.getNombre()) == 0) {
                        nodoArtista = punteroArtista.siguiente;
                        punteroArtista.siguiente = punteroArtista.siguiente.siguiente;
                        nodoArtista = null; // Eliminando la referencia al nodo eliminado
                        System.out.println("Se ha eliminado correctamente");
                        break;
                    }

                    punteroArtista = punteroArtista.getSiguiente();
                }
            }
        } else {
            System.out.println("No se ha encontrado el Entidades.Artista que se estaba buscando");
        }
    }

    public void eliminarInicioListasSimples()
    {
        System.out.println("Referencia cabeza: " + cabezaArtista);

        // Preguntamos si hay valores que se puedan eliminar
        if (cabezaArtista != null) {

            // Hacemos que el puntero inicie desde la cabeza
            punteroArtista = cabezaArtista;

            // Luis = Luis.siguiente = elsa
            punteroArtista = punteroArtista.siguiente;

            cabezaArtista = punteroArtista;

            System.out.println("Se ha eliminado correctamente");
//
//            return cabezaArtista;
        } else {
            System.out.println("No hay elementos que se puedan eliminar");
        }


    }

    public void eliminarFinListasSimples()
    {
        // Pregunta si hay por lo menos dos elementos, sino hay se elimina la cabeza
        if (cabezaArtista.siguiente == null) {
            cabezaArtista = null;
        } else {
            // Hacemos que el puntero inicie desde la cabeza
            punteroArtista = cabezaArtista;

            // Recorremos la lista para hallar el ultimo valor, preguntando si el siguiente del ultimo valor es
            // diferente de null
            while (punteroArtista.siguiente.siguiente != null) {
                punteroArtista = punteroArtista.siguiente;
            }

            // Eliminamos el ultimo nodo de la lista
            punteroArtista.siguiente = null;
        }
    }
}
