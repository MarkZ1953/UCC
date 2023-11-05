/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */


public class PerrosCalientes {
    
    String nombre;
    String nacionalidad;
    double peso;
    double velocidadIngestion;
    int perrosConsumidos;
    String categoria;
    PerrosCalientes sig;
    
    public PerrosCalientes(String nom, String nac,double pes,double vel,int per,String cat  )
    {
        nombre=nom;
        nacionalidad=nac;
        peso=pes;
        velocidadIngestion=vel;
        perrosConsumidos=per;
        categoria=cat;
        sig = null;
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

    public PerrosCalientes getSig() {
        return sig;
    }

    public void setSig(PerrosCalientes sig) {
        this.sig = sig;
    }
    
}
