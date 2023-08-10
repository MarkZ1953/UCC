package Clase_09_08_2023.Ejemplo;

public class Libro {
    private String nombre;
    private String isbn;
    private double precio;

    public Libro(String nombre, String isbn, double precio) {
        this.nombre = nombre;
        this.isbn = isbn;
        this.precio = precio;
    }

    public double getPrecio() {
        return precio;
    }

    public void setPrecio(double precio) {
        this.precio = precio;
    }

    public String getIsbn() {
        return isbn;
    }

    public void setIsbn(String isbn) {
        this.isbn = isbn;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public static void main(String[] args) {
        Libro libro = new Libro("Harry Potter", "0011", 20_000);
        System.out.println(libro.getNombre());
    }

}
