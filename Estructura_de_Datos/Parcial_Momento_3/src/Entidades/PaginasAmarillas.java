package Entidades;/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author lab.inf1
 */
public class PaginasAmarillas {
    
    public PaginasAmarillas ant;
    private String nombre;
    private String direccion;
    private String telefono;
    public PaginasAmarillas sig;
    
    public PaginasAmarillas(String nom,String direc,String tel)
    {
        ant=null;
        nombre=nom;
        direccion=direc;
        telefono=tel;
        sig=null;
    }

    public PaginasAmarillas getAnt() {
        return ant;
    }

    public void setAnt(PaginasAmarillas ant) {
        this.ant = ant;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getDireccion() {
        return direccion;
    }

    public void setDireccion(String direccion) {
        this.direccion = direccion;
    }

    public String getTelefono() {
        return telefono;
    }

    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }

    public PaginasAmarillas getSig() {
        return sig;
    }

    public void setSig(PaginasAmarillas sig) {
        this.sig = sig;
    }

    @Override
    public String toString() {
        return  "Nombre: " + nombre +
                "Direccion: " + direccion +
                "Telefono: " + telefono;
    }
}
