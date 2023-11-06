package Listas.ClasesListas.SubClasesListasSimples;

import Entidades.Artista;
import Listas.ListasSC;

public class EliminarListasSimples extends ListasSC {

    public void menuEliminarListasSimples()
    {
        int opc;
        System.out.println("MENU ELIMINAR LISTAS SIMPLES");
        System.out.println("1. Eliminar por el inicio listas simples.");
        System.out.println("2. Eliminar por el fin listas simples.");
        System.out.println("3. Eliminar antes de nodo listas simples");
        System.out.println("4. Eliminar despues de nodo listas simples");
        System.out.println("5. Eliminar nodo dado listas simples.");
        System.out.println("6. Volver.");

        System.out.println("\nEscoja una opcion;");
        opc = leer.nextInt();

        switch (opc) {
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
            System.out.println("No se ha encontrado el Entidades.Artista que se estaba buscando");
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
}
