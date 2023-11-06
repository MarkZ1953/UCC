package Listas.ClasesListas.SubClasesListasSimples;

import Listas.ListasSC;

public class ImprimirListasSimples extends ListasSC {
    public void imprimirListasSimples()
    {
        punteroArtista = cabezaArtista;

        while (punteroArtista != null)
        {
            System.out.println();
            System.out.println(punteroArtista.toString());
            punteroArtista = punteroArtista.siguiente;
        }

        System.out.println();
    }
}
