package Entidades;

public class Artista {
    
    private String nombre;
    private String nacionalidad;
    private String fechaNacimiento;
    public Artista siguiente;
    
    public Artista(String nombre, String nacionalidad, String fechaNacimiento)
    {
        this.nombre = nombre;
        this.nacionalidad = nacionalidad;
        this.fechaNacimiento = fechaNacimiento;
        siguiente = null;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getNacionalidad() {
        return nacionalidad;
    }

    public void setNacionalidad(String nacionalidad) {
        this.nacionalidad = nacionalidad;
    }

    public String getFechaNacimiento() {
        return fechaNacimiento;
    }

    public void setFechaNacimiento(String fechaNacimiento) {
        this.fechaNacimiento = fechaNacimiento;
    }

    public Artista getSiguiente() {
        return siguiente;
    }

    public void setSiguiente(Artista siguiente) {
        this.siguiente = siguiente;
    }

    @Override
    public String toString() {
        return "Nombre: " + nombre +
        "\nNacionalidad: " + nacionalidad +
        "\nFecha De Nacimiento: " + fechaNacimiento;
    }
    
    
}
