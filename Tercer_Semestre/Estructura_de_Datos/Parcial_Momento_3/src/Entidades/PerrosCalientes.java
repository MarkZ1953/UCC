package Entidades;/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */


public class PerrosCalientes {
    
    private String nombre;
    private String nacionalidad;
    private double peso;
    private double velocidadIngestion;
    private int perrosConsumidos;
    private String categoria;
    public PerrosCalientes siguiente;
    
    public PerrosCalientes(String nombre, String nacionalidad, double peso, double velocidadIngestion,
                           int perrosConsumidos, String categoria)
    {
        this.nombre = nombre;
        this.nacionalidad = nacionalidad;
        this.peso = peso;
        this.velocidadIngestion = velocidadIngestion;
        this.perrosConsumidos = perrosConsumidos;
        this.categoria = categoria;
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

    public double getPeso() {
        return peso;
    }

    public void setPeso(double peso) {
        this.peso = peso;
    }

    public double getVelocidadIngestion() {
        return velocidadIngestion;
    }

    public void setVelocidadIngestion(double velocidadIngestion) {
        this.velocidadIngestion = velocidadIngestion;
    }

    public int getPerrosConsumidos() {
        return perrosConsumidos;
    }

    public void setPerrosConsumidos(int perrosConsumidos) {
        this.perrosConsumidos = perrosConsumidos;
    }

    public String getCategoria() {
        return categoria;
    }

    public void setCategoria(String categoria) {
        this.categoria = categoria;
    }

    public PerrosCalientes getSiguiente() {
        return siguiente;
    }

    public void setSiguiente(PerrosCalientes siguiente) {
        this.siguiente = siguiente;
    }

    @Override
    public String toString() {
        return  "Nombre: " + nombre +
                "\nNacionalidad: " + nacionalidad +
                "\nPeso: " + peso +
                "\nVelocidad Ingestion: " + velocidadIngestion +
                "\nPerros Consumidos: " + perrosConsumidos +
                "\nCategoria: " + categoria;
    }
}
