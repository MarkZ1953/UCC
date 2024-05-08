/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author lab.inf1
 */
public class Artista {
    
    String nombre;
    String nacionalidad;
    String fecha;
    Artista sig;
    
    public Artista(String nom, String nac, String fec)
    {
        nombre=nom;
        nacionalidad=nac;
        fecha=fec;
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

    public String getFecha() {
        return fecha;
    }

    public void setFecha(String fecha) {
        this.fecha = fecha;
    }

    public Artista getSig() {
        return sig;
    }

    public void setSig(Artista sig) {
        this.sig = sig;
    }
    
    
}
