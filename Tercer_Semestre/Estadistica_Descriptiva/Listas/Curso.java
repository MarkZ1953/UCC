/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author lab.inf1
 */
public class Curso {
    
    Curso ant;
    int codigo;
    String asignatura;
    double nota;
    Curso sig;
    
    public Curso(int cod,String asig,double not)
    {
        ant=null;
        codigo=cod;
        asignatura=asig;
        nota=not;
        sig=null;
    }

    public Curso getAnt() {
        return ant;
    }

    public void setAnt(Curso ant) {
        this.ant = ant;
    }

    public int getCodigo() {
        return codigo;
    }

    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }

    public String getAsignatura() {
        return asignatura;
    }

    public void setAsignatura(String asignatura) {
        this.asignatura = asignatura;
    }

    public double getNota() {
        return nota;
    }

    public void setNota(double nota) {
        this.nota = nota;
    }

    public Curso getSig() {
        return sig;
    }

    public void setSig(Curso sig) {
        this.sig = sig;
    }
    
    
}
