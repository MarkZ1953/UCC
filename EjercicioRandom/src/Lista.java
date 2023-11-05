public class Lista {

    private Nodo cabeza = null;

    private static class Nodo {
        public Libro libro;
        public Nodo siguiente = null;
        public Nodo(Libro libro) {
            this.libro = libro;
        }
    }

    public Lista() {
        insertarPrincipio(recolectarValores());

        Nodo puntero = cabeza;

        while (puntero != null) {
            System.out.println();
            System.out.println("Titulo: " + puntero.libro.getTitulo());
            System.out.println("Autor: " + puntero.libro.getAutor());
            System.out.println("Isbn: " + puntero.libro.getIsbn());

            puntero = puntero.siguiente;
        }

    }

    public Libro recolectarValores() {

        return new Libro("Don quijote", "Nose", "1234");

    }

    public void insertarPrincipio(Libro libro) {

        Nodo nuevoNodo = new Nodo(libro);
        nuevoNodo.siguiente = cabeza;
        cabeza = nuevoNodo;

    }

    public void insertarFinal(Libro libro) {

        Nodo nodo = new Nodo(libro);
        Nodo puntero = cabeza;

        while (puntero.siguiente != null) {
            puntero = puntero.siguiente;
        }

        puntero.siguiente = nodo;

    }

    public void insertarDespues(int n, Libro libro) {
        Nodo nodo = new Nodo(libro);

        if (cabeza == null) {
            cabeza = nodo;
        } else {
            Nodo puntero = cabeza;
            int contador = 0;

            while (contador < n && puntero.siguiente != null) {
                puntero = puntero.siguiente;
                contador++;
            }

            nodo.siguiente = puntero.siguiente;
            puntero.siguiente = nodo;
        }
    }

    public static void main(String[] args) {
        Lista lista = new Lista();
    }
}
