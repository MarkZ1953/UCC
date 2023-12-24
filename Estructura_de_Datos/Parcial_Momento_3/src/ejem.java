import java.util.Scanner;

// Superclase que contiene la cabeza principal y métodos de lista
class SuperClase {
    Artista cabeza;

    public SuperClase() {
        this.cabeza = null;
    }

    public void agregarPorInicio(Artista nuevoArtista) {
        if (cabeza == null) {
            cabeza = nuevoArtista;
        } else {
            nuevoArtista.siguiente = cabeza;
            cabeza = nuevoArtista;
        }
    }

    public void eliminarPorInicio() {
        if (cabeza != null) {
            cabeza = cabeza.siguiente;
        }
    }
}

// Subclase que contiene el menú y maneja referencias
class SubClase extends SuperClase {

    public void mostrarMenu() {
        Scanner scanner = new Scanner(System.in);
        int opcion = 0;

        while (opcion != 4) {
            System.out.println("\n1. Agregar por inicio");
            System.out.println("2. Eliminar por inicio");
            System.out.println("3. Mostrar lista");
            System.out.println("4. Salir");
            System.out.print("Elija una opción: ");

            opcion = scanner.nextInt();

            switch (opcion) {
                case 1:
                    System.out.print("Ingrese el nombre del artista a agregar: ");
                    String nombre = scanner.next();
                    Artista nuevoArtista = new Artista(nombre);
                    agregarPorInicio(nuevoArtista);
                    break;
                case 2:
                    eliminarPorInicio();
                    break;
                case 3:
                    mostrarLista();
                    break;
                case 4:
                    System.out.println("Saliendo del programa...");
                    break;
                default:
                    System.out.println("Opción no válida. Intente de nuevo.");
            }
        }
    }

    public void mostrarLista() {
        System.out.println("\nLista actual:");
        Artista artistaActual = cabeza;
        while (artistaActual != null) {
            System.out.println(artistaActual.nombre);
            artistaActual = artistaActual.siguiente;
        }
    }
}

// Clase Artista para representar los nodos
class Artista {
    String nombre;
    Artista siguiente;

    public Artista(String nombre) {
        this.nombre = nombre;
        this.siguiente = null;
    }
}

// Clase principal
public class ejem {
    public static void main(String[] args) {
        SubClase subClase = new SubClase();
        subClase.mostrarMenu();
    }
}
