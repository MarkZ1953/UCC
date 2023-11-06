package Listas.ClasesListas.SubClasesListasSimples;

import Entidades.Artista;
import Listas.ListasSC;

public class AgregarListasSimples extends ListasSC {

    public void adicionarInicioListasSimples()
    {
        nodoNuevoArtista = recolectarInformacionArtista();
        nodoNuevoArtista.siguiente = cabezaArtista;
        cabezaArtista = nodoNuevoArtista;
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
