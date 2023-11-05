import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.Scanner;


public class LISTAS {

    Scanner leer = new Scanner(System.in);
    Artista cabezaArtista, puntero, nodoNuevoArtista;
    PerrosCalientes cabezaPerrosCalientes,r,s;
    PaginasAmarillas cabezaPaginasAmarillas,t,u;
    Curso cabezaCurso,x,y;
    int opc;
    File archivo = new File("C:\\Users\\FelipeCastro\\Documents\\GitHub\\UCC\\Estructura_de_Datos\\Parcial_Momento_3\\src\\Archivo.txt");
    public LISTAS()
    {
        menuPrincipal();
    }

    private static class NodoArtista {
        public Artista artista;
        public NodoArtista siguiente = null;
        public NodoArtista(Artista artista) {
            this.artista = artista;
        }
    }

    public Artista recolectarInformacionArtista() {

        String nombre, nacionalidad, fechaNacimiento;

        System.out.println("Digite el nombre del artista: ");
        nombre = leer.next();

        System.out.println("Digite la nacionalidad del artista: ");
        nacionalidad = leer.next();

        System.out.println("Digite fecha de nacimiento del artista: ");
        fechaNacimiento = leer.next();

        return new Artista(nombre, nacionalidad, fechaNacimiento);
    }
   
    public void menuPrincipal()
    {
        int opcion;
        System.out.println("MENU PRINCIPAL");
        System.out.println("1. Listas simples");
        System.out.println("2. Listas circulares");
        System.out.println("3. Listas dobles");
        System.out.println("4. Listas circulares dobles");
        System.out.println("5. Terminar");
        
        System.out.println("");
        System.out.println("Escoja la opcion:");
        opcion = leer.nextInt();
        
        switch (opcion) {
            case 1:
                menuListasSimples();
                menuPrincipal();
                break;
                
            case 2:
                menuListasCirculares();
                menuPrincipal();
                break;
                
            case 3:
                menuListasDobles();
                menuPrincipal();
                break;
                
            case 4:
                menuListasCircularesDobles();
                menuPrincipal();
                break;
                
            case 5:
                System.exit(0);
                break;
                
            default:
                menuPrincipal();
        }
    }
    
    public void menuListasSimples()
    {
        int opc;
        System.out.println("MENU LISTAS SIMPLES");
        System.out.println("1. Crear listas simples");
        System.out.println("2. Adicionar listas simples.");
        System.out.println("3. Eliminar listas simples");
        System.out.println("4. Modificar listas simples");
        System.out.println("5. Imprimir listas simples");
        System.out.println("6. Imprimir artistas de forma impar.");
        System.out.println("7. Volver.");
        
        System.out.println();
        System.out.println("Escoja una opcion");
        opc = leer.nextInt();
        
        switch (opc) {
            case 1:
                cargarArtistasListasSimples();
                menuListasSimples();
                break;
                
            case 2:
                menuAdicionarListasSimples();
                menuListasSimples();
                break;
                
            case 3:
                menuEliminarListasSimples();
                menuListasSimples();
                break;
                
            case 4:
                modificarListasSimples();
                menuListasSimples();
                break;
            
            case 5:
                imprimirListasSimples();
                menuListasSimples();
                break;

            case 6:
                imprimirNodosImparesArtista();
                menuPrincipal();
                break;

            case 7:
                menuPrincipal();
                break;
                
            default:
                menuListasSimples();
        }
    }
    
    public void crearListasSimples()
    {
        nodoNuevoArtista = new Artista("Luis","peruano","12/08/1994");
        cabezaArtista = nodoNuevoArtista;
        puntero = nodoNuevoArtista;

        nodoNuevoArtista = new Artista("Elsa","japonesa","21/10/1980");
        puntero.siguiente = nodoNuevoArtista;
        puntero = nodoNuevoArtista;

        nodoNuevoArtista = new Artista("Gabriel","aleman","13/01/1910");
        puntero.siguiente = nodoNuevoArtista;
        puntero = nodoNuevoArtista;

        nodoNuevoArtista = new Artista("Estela","india","21/12/1991");
        puntero.siguiente = nodoNuevoArtista;
        puntero = nodoNuevoArtista;
    }
    
    public void menuAdicionarListasSimples()
    {
        int opc;
        System.out.println("MENU ADICIONAR LISTAS SIMPLES");
        System.out.println("1. Adicionar por el inicio listas simples.");
        System.out.println("2. Adicionar por el fin listas simples.");
        System.out.println("3. Adicionar antes de nodo listas simples");
        System.out.println("4. Adicionar despues de nodo listas simples");
        System.out.println("5. Volver.");
        
        System.out.println("\nEscoja una opcion;");
        opc = leer.nextInt();
        
        switch (opc) {
            case 1:
                adicionarInicioListasSimples();
                menuAdicionarListasSimples();
                break;
                
            case 2:
                adicionarFinListasSimples();
                menuAdicionarListasSimples();
                break;
                
            case 3:
                adicionarAntesListasSimples();
                menuAdicionarListasSimples();
                break;
                
            case 4:
                adicionarDespuesListasSimples();
                menuAdicionarListasSimples();
                break;
            
            case 5:
                menuListasSimples();
                break;
                
            default:
                menuAdicionarListasSimples();
                break;
        }
    }
    
    public void adicionarInicioListasSimples()
    {
        nodoNuevoArtista = recolectarInformacionArtista();
        nodoNuevoArtista.siguiente = cabezaArtista;
        cabezaArtista = nodoNuevoArtista;
    }
    
    public void adicionarFinListasSimples()
    {
        nodoNuevoArtista = recolectarInformacionArtista();
        puntero = cabezaArtista;

        while(puntero.siguiente != null) {
            puntero = puntero.siguiente;
            puntero.siguiente = nodoNuevoArtista;
        }
    }
    
    public void adicionarAntesListasSimples()
    {
        Artista nodoAnteriorArtista;
        String nombreABuscar;

        puntero = cabezaArtista;
        System.out.println("Digite el nombre a buscar: ");
        nombreABuscar = leer.next();

        if(cabezaArtista.getNombre().compareToIgnoreCase(nombreABuscar)==0)
        {
            adicionarInicioListasSimples();
        }
        else
        {
            // Se pone cabezaArtista.siguiente porque ya se verifico que el valor que se estaba buscando no era el
            // primero
            nodoNuevoArtista = recolectarInformacionArtista();
            puntero = cabezaArtista.siguiente; // Se quiere iniciar desde el segundo nodo de la lista
            nodoAnteriorArtista = cabezaArtista;

            // Se itera toda la lista, y cuando se encuentre el valor que se solicito, entonces el nodoAnteriorArtista
            // se queda con el nodoActualArtista
            while(puntero.getNombre().compareToIgnoreCase(nombreABuscar)!=0 && puntero.siguiente !=null)
            {
                nodoAnteriorArtista = puntero;
                puntero = puntero.siguiente;
            }

            if(puntero.getNombre().compareToIgnoreCase(nombreABuscar)==0)
            {
                nodoNuevoArtista.siguiente = puntero;
                nodoAnteriorArtista.siguiente = nodoNuevoArtista;
            }
            else
                System.out.println("El nombre buscado no se encuentra en la lista");
        }
                
    }

    public void imprimirNodosImparesArtista() {
        int contador = 1;
        puntero = cabezaArtista;

        while (true)
        {
            System.out.println("Id: " + contador);
            System.out.println("Nombre: "+ puntero.nombre);
            System.out.println("Nacionalidad: "+ puntero.nacionalidad);
            System.out.println("Fecha: "+ puntero.fechaNacimiento);
            System.out.println("Direccion de memoria del Nodo: "+ puntero);

            if (puntero.siguiente != null) {
                puntero = puntero.siguiente.siguiente;
                contador = contador + 2;
            } else {
                break;
            }
        }
    }

    public void cargarArtistasListasSimples()
    {
        int cont;
        String nombre;
        String nacionalidad;
        String fecha;
        String linea = " ";
        int contadorListas = 1;

        try
        {
            FileReader reader= new FileReader(archivo) ;
            BufferedReader bufer= new BufferedReader(reader);

            linea=bufer.readLine();
            System.out.println(linea);
            cont=Integer.parseInt(linea);

            for(int i=0;i<cont;i++)
            {

                nombre=bufer.readLine();
                nacionalidad=bufer.readLine();
                fecha=bufer.readLine();

                nodoNuevoArtista = new Artista(nombre, nacionalidad, fecha);

                if (contadorListas == 1) {
                    cabezaArtista = nodoNuevoArtista;
                    puntero = nodoNuevoArtista;
                    contadorListas = 2;
                } else {
                    puntero.siguiente = nodoNuevoArtista;
                    puntero = nodoNuevoArtista;
                }

            }

            bufer.close();
            reader.close();

        }
        catch(Exception e)
        {
            System.out.println("error al leer informacion del archivo");
        }
    }


    public void adicionarDespuesListasSimples()
    {
        Artista m;
        String nombre, nacionalidad, fechaNacimiento, nombreABuscar;

        System.out.println("Ingrese el nombre a buscar: ");
        nombreABuscar = leer.next();

        // 1. Despues de quien tenemos que agregar?
        // 2. A quien tenemos que agregar?

        puntero = cabezaArtista;

        if(puntero.getNombre().compareToIgnoreCase(nombreABuscar)==0)
        {
            adicionarInicioListasSimples();
        }
        else
        {
            System.out.println("Digite el nombre del artista ");
            nombre=leer.next();
            System.out.println("Digite la nacionalidad del artista ");
            nacionalidad=leer.next();
            System.out.println("Digite fecha nacimiento del artista ");
            fechaNacimiento=leer.next();

            nodoNuevoArtista =new Artista(nombre,nacionalidad,fechaNacimiento);

            puntero = cabezaArtista.siguiente;
            m= cabezaArtista;

            while(puntero.getNombre().compareToIgnoreCase(nombreABuscar)!=0 && puntero.siguiente !=null)
            {
                m= puntero;
                puntero = puntero.siguiente;
            }

            if(puntero.getNombre().compareToIgnoreCase(nombreABuscar)==0)
            {
                nodoNuevoArtista.siguiente = puntero;
                m.siguiente = nodoNuevoArtista;
            }
            else
                System.out.println("El nombre buscado no se encuentra en la lista");
        }

    }
    
    public void menuEliminarListasSimples()
    {
        int opc;
        System.out.println("MENU ELIMINAR LISTAS SIMPLES");
        System.out.println("1. Eliminar por el inicio listas simples.");
        System.out.println("2. Eliminar por el fin listas simples.");
        System.out.println("3. Eliminar antes de nodo listas simples");
        System.out.println("4. Eliminar despues de nodo listas simples");
        System.out.println("5. Eliminar nodo dado listas simples.");
        System.out.println("6. Volver.");
        
        System.out.println("\nEscoja una opcion;");
        opc = leer.nextInt();
        
        switch (opc) {
            case 1:
                eliminarInicioListasSimples();
                menuEliminarListasSimples();
                break;
                
            case 2:
                eliminarFinListasSimples();
                menuEliminarListasSimples();
                break;
                
            case 3:
                eliminarAntesListasSimples();
                menuEliminarListasSimples();
                break;
                
            case 4:
                eliminarDespuesListasSimples();
                menuEliminarListasSimples();
                break;
                
            case 5:
                eliminarNodoDadoListasSimples();
                menuEliminarListasSimples();
                break;
                
            case 6:
                menuListasSimples();
                break;
                
            default:
                menuEliminarListasSimples();
                break;
        }
    }
    
    public void eliminarInicioListasSimples()
    {

    }
    
    public void eliminarFinListasSimples()
    {
        
    }
    
    public void eliminarAntesListasSimples()
    {
        
    }

    public void eliminarDespuesListasSimples()
    {
        
    }
    
    public void eliminarNodoDadoListasSimples()
    {
        
    }
    
    public void modificarListasSimples()
    {
        
    }
    
    public void imprimirListasSimples()
    {
        puntero = cabezaArtista;

        while (puntero != null)
        {
            System.out.println("nombre : "+ puntero.nombre);
            System.out.println("nacionalidad : "+ puntero.nacionalidad);
            System.out.println("fecha : "+ puntero.fechaNacimiento);
            System.out.println("p : "+ puntero);
            puntero = puntero.siguiente;
        }
    }
    
    public void menuListasCirculares()
    {
        int opc;
        String valor;
        System.out.println("MENU LISTAS SIMPLES");
        System.out.println("1. Crear listas circulares");
        System.out.println("2. Adicionar listas circulares");
        System.out.println("3. Eliminar listas circulares");
        System.out.println("4. Modificar listas circulares");
        System.out.println("5. Imprimir listas circulares");
        System.out.println("6. Volver.");
        
        System.out.println("");
        System.out.println("Escoja una opcion");
        valor= leer.next();
        //opc = leer.nextInt();
        opc=Integer.parseInt(valor);
        switch (opc) {
            case 1:
                crearListasCirculares();
                menuListasCirculares();
                break;
                
            case 2:
                menuAdicionarListasCirculares();
                menuListasCirculares();
                break;
                
            case 3:
                menuEliminarListasCirculares();
                menuListasCirculares();
                break;
                
            case 4:
                modificarListasCirculares();
                menuListasCirculares();
                break;
            
            case 5:
                imprimirListasCirculares();
                menuListasCirculares();
                break;
                
            case 6:
                menuPrincipal();
                break;
                
            default:
                menuListasCirculares();
        }
    }
    
    public void crearListasCirculares(){
        cabezaPerrosCalientes = new PerrosCalientes("juan delgadillo", "peruano", 78.3, 3.2,16, "adulto");
        cabezaPerrosCalientes.sig = cabezaPerrosCalientes;
        r = new PerrosCalientes("luang xion", "chino", 65.4, 4.6,23, "junior");
        s = cabezaPerrosCalientes;
        s.sig = r;
        r.sig = cabezaPerrosCalientes;
        s = r;
        r = new PerrosCalientes("robert conti", "italiano",67.8 ,3.6 ,18, "junior");
        s.sig = r;
        r.sig = cabezaPerrosCalientes;
    
    }
    public void menuAdicionarListasCirculares(){
        //int opc;
        String valor;
        System.out.println("MENU ADICIONAR LISTAS CIRCULARES");
        System.out.println("1. Adicionar por el inicio listas circulares.");
        System.out.println("2. Adicionar por el fin listas circulares.");
        System.out.println("3. Adicionar antes de nodo listas circulares");
        System.out.println("4. Adicionar despues de nodo listas circulares");
        System.out.println("5. Volver.");
        System.out.println("7");
        System.out.println("\nEscoja una opcion;");
       valor= leer.next();
        //opc = leer.nextInt();
        opc=Integer.parseInt(valor);
       // opc = leer.nextInt();
       // opc = leer.nextInt();
        System.out.println(opc+"8");
        
        switch (opc) {
            case 1:
                adicionarInicioListasDobles();
                menuAdicionarListasCirculares();
                break;
                
            case 2:
                adicionarFinListasCirculares();
                menuAdicionarListasCirculares();
                break;
                
            case 3:
                adicionarAntesListasCirculares();
                menuAdicionarListasCirculares();
                break;
                
            case 4:
                adicionarDespuesListasCirculares();
                imprimirListasCirculares();
                menuAdicionarListasCirculares();
               //  menuListasCirculares();
                break;
            
            case 5:
                menuListasCirculares();
                break;
                
            default:
                menuAdicionarListasCirculares();
                break;
        }
    }
    public void adicionarInicioListasCirculares()
    {
        
        s = cabezaPerrosCalientes;
        r = new PerrosCalientes("sofia reina", "mexicana",63.0 ,5.2 ,31, "infantil");
         while(s.sig!= cabezaPerrosCalientes)
                s=s.sig;
         r.sig= cabezaPerrosCalientes;
         s.sig=r;
         cabezaPerrosCalientes =r;
    }
    public void adicionarFinListasCirculares()
    {
        s = cabezaPerrosCalientes;
        r = new PerrosCalientes("sofia reina", "mexicana",63.0 ,5.2 ,31, "infantil");
         while(s.sig!= cabezaPerrosCalientes)
                s=s.sig;
         r.sig= cabezaPerrosCalientes;
         s.sig=r;
    }
    
    public void adicionarAntesListasCirculares()
    {
        PerrosCalientes opc;
        String valor;
        System.out.println("Digite el nombre a buscar");
        valor = leer.nextLine();
        valor = leer.nextLine();
        
        s = cabezaPerrosCalientes;
        r = new PerrosCalientes("sofia reina", "mexicana",63.0 ,5.2 ,31, "infantil");
        
        if(s.getNombre().compareToIgnoreCase(valor)==0 )
        {
            r.sig= cabezaPerrosCalientes;
            while(s.sig!= cabezaPerrosCalientes)
                s=s.sig;
            s.sig=r;
            cabezaPerrosCalientes =r;
        }
        else
        {
            s=s.sig;
            opc= cabezaPerrosCalientes;
            while (s.getNombre().compareToIgnoreCase(valor)!=0 && s.sig!= cabezaPerrosCalientes)
            {
                opc=s;
                s = s.sig;
            }
            if(s.getNombre().compareToIgnoreCase(valor)==0 )
            {
             r.sig = s;
            opc.sig = r;
            }
            else{
                System.out.println("El participante no se encuentra en la lista");
               }
        }
          
    }
    public void adicionarDespuesListasCirculares(){
        String valor;
        System.out.println("Digite el nombre a buscar");
        valor = leer.nextLine();
        valor = leer.nextLine();
        
        s = cabezaPerrosCalientes;
        
        while (s.getNombre().compareToIgnoreCase(valor)!=0 && s.sig!= cabezaPerrosCalientes){
            s = s.sig;
        }
        
        if(s.getNombre().compareToIgnoreCase(valor)==0 && s.sig== cabezaPerrosCalientes){
            r = new PerrosCalientes("sofia reina", "mexicana",63.0 ,5.2 ,31, "infantil");
            s.sig = r;
            r.sig = cabezaPerrosCalientes;
             
        }else {
            if(s.getNombre().compareToIgnoreCase(valor)==0 && s.sig != cabezaPerrosCalientes){
            r = new PerrosCalientes("sofia reina", "mexicana",63.0 ,5.2 ,31, "infantil");
            r.sig = s.sig;
            s.sig = r;
            
            }else{
                System.out.println("El participante no se encuentra en la lista");
            }
        }
       
         
        
    }
    public void menuEliminarListasCirculares(){
         int opc;
        System.out.println("MENU ELIMINAR LISTAS CIRCULARES");
        System.out.println("1. Eliminar por el inicio listas circulares.");
        System.out.println("2. Eliminar por el fin listas circulares.");
        System.out.println("3. Eliminar antes de nodo listas circulares");
        System.out.println("4. Eliminar despues de nodo listas circulares");
        System.out.println("5. Eliminar nodo dado listas circulares.");
        System.out.println("6. Volver.");
        
        System.out.println("\nEscoja una opcion;");
        opc = leer.nextInt();
        
        switch (opc) {
            case 1:
                eliminarInicioListasCirculares();
                menuEliminarListasCirculares();
                break;
                
            case 2:
                eliminarFinListasCirculares();
                menuEliminarListasCirculares();
                break;
                
            case 3:
                eliminarAntesListasCirculares();
                menuEliminarListasCirculares();
                break;
                
            case 4:
                eliminarDespuesListasCirculares();
                menuEliminarListasCirculares();
                break;
                
            case 5:
                eliminarNodoDadoListasCirculares();
                menuEliminarListasCirculares();
                break;
                
            case 6:
                menuListasCirculares();
                break;
                
            default:
                menuEliminarListasCirculares();
                break;
        }
        
    }
    
     public void eliminarInicioListasCirculares()
    {
        s = cabezaPerrosCalientes;
        while (s.sig != cabezaPerrosCalientes)
            s = s.sig;
        s.sig = cabezaPerrosCalientes.sig;
        cabezaPerrosCalientes = cabezaPerrosCalientes.sig;
    }
    
    public void eliminarFinListasCirculares()
    {
        s = cabezaPerrosCalientes;
        while (s.sig.sig != cabezaPerrosCalientes)
            s = s.sig;
        s.sig = cabezaPerrosCalientes;
    }
    
    public void eliminarAntesListasCirculares()
    {
        String dato;
        System.out.println("Digite el dato a eliminar");
        dato = leer.nextLine();
        dato = leer.nextLine();
        s = cabezaPerrosCalientes;
        if(dato.compareToIgnoreCase(s.getNombre() )== 0)
            
            System.out.println("NO EXISTE NODO ANTES PARA ELIMINAR");
                
        else {
         s = s.sig;
         if(dato.compareToIgnoreCase(s.getNombre() )== 0){
         
          eliminarInicioListasCirculares();
          
         }
         else{
             
             PerrosCalientes opc = cabezaPerrosCalientes;
               s = s.sig;
               
              while (dato.compareToIgnoreCase(s.getNombre() ) != 0 && s.sig != cabezaPerrosCalientes)
              {
                s = s.sig;
                opc = opc.sig;
              }
              
              if (dato.compareToIgnoreCase(s.getNombre()) ==0)
                  
                  opc.sig = s;
              else{
              
                  System.out.println("EL DATO NO EXISTE");
              }
              
         }
        }
    }
    
    public void eliminarDespuesListasCirculares()
    {
        String valor;
        System.out.println("digite el nombre a buscar");
        valor = leer.nextLine();
        valor = leer.nextLine();
        s= cabezaPerrosCalientes;
        while (s.getNombre().compareToIgnoreCase(valor)!=0 && s.getSig()!= cabezaPerrosCalientes)
            s= s.sig;
        if(s.getNombre().compareToIgnoreCase(valor)==0 && s.sig.sig == cabezaPerrosCalientes)
            s.sig= cabezaPerrosCalientes;
        else
            if(s.getNombre().compareToIgnoreCase(valor)==0 && s.sig== cabezaPerrosCalientes)
               eliminarInicioListasCirculares();
           else
                if(s.getNombre().compareToIgnoreCase(valor)==0)
                    s.sig=s.sig.sig;
                else
                    System.out.println("el valor no existe");
        
    }
    
    public void eliminarNodoDadoListasCirculares()
    {
        String valor;
        PerrosCalientes t;
        System.out.println("digite el nombre a eliminar");
        valor = leer.nextLine();
        valor = leer.nextLine();
        s= cabezaPerrosCalientes;
                while (s.getNombre().compareToIgnoreCase(valor)!=0 && s.sig != cabezaPerrosCalientes)
                    s= s.sig;
                if(s.getNombre().compareToIgnoreCase(cabezaPerrosCalientes.getNombre())==0)
                    eliminarInicioListasCirculares();
                else
                    if(s.getNombre().compareToIgnoreCase(valor)==0 && s.sig== cabezaPerrosCalientes)
                        eliminarFinListasCirculares();
                else
                        if(s.getNombre().compareToIgnoreCase(valor)==0)
                        {
                          t= cabezaPerrosCalientes;
                          while(t.sig.getNombre().compareToIgnoreCase(valor)!=0)
                              t= t.sig;
                          t.sig=s.sig;
                          
                        }
                else
                            System.out.println("el valor no existe");
    }
    
    public void modificarListasCirculares()
    {
        
    }
    
   
   
    public void imprimirListasCirculares(){
         r= cabezaPerrosCalientes;
        while (r.sig!= cabezaPerrosCalientes)
        {
            System.out.println("nombre : "+ r.nombre);
            System.out.println("nacionalidad : "+ r.nacionalidad);
            System.out.println("peso : "+ r.peso);
            System.out.println("velocidad de ingestion : "+ r.velocidadIngestion);
            System.out.println("perros consumidos : "+ r.perrosConsumidos);
            System.out.println("categoria : "+ r.categoria);
            r=r.sig;
        }
        
            System.out.println("nombre : "+ r.nombre);
            System.out.println("nacionalidad : "+ r.nacionalidad);
            System.out.println("peso : "+ r.peso);
            System.out.println("velocidad de ingestion : "+ r.velocidadIngestion);
            System.out.println("perros consumidos : "+ r.perrosConsumidos);
            System.out.println("categoria : "+ r.categoria);
            r=r.sig;
    }
    
   
    
    
    
     public void menuListasDobles()
    {
        int opc;
        System.out.println("MENU LISTAS DOBLES");
        System.out.println("1. Crear listas Dobles");
        System.out.println("2. Adicionar listas Dobles.");
        System.out.println("3. Eliminar listas Dobles");
        System.out.println("4. Modificar listas Dobles");
        System.out.println("5. Imprimir listas Dobles");
        System.out.println("6. Volver.");
        
        System.out.println("");
        System.out.println("Escoja una opcion");
        opc = leer.nextInt();
        
        switch (opc) {
            case 1:
                crearListasDobles();
                menuListasDobles();
                break;
                
            case 2:
                menuAdicionarListasDobles();
                menuListasDobles();
                break;
                
            case 3:
                menuEliminarListasDobles();
                menuListasDobles();
                break;
                
            case 4:
                modificarListasDobles();
                menuListasDobles();
                break;
            
            case 5:
                imprimirListasDobles();
                menuListasDobles();
                break;
                
            case 6:
                menuPrincipal();
                break;
                
            default:
                menuListasDobles();
        }
    }
    
    public void crearListasDobles()
    {
        t = new PaginasAmarillas("construcciones beta sas","cll 12 n° 20-14","3103332211");
        cabezaPaginasAmarillas =t;
        u=t;
        t = new PaginasAmarillas("inversiones electronicas","crr 21 n° 4-11","3117776655");
        u.sig=t;
        t.ant=u;
        u=t;
        t = new PaginasAmarillas("comercializadora mayor ltda","tv 34 n° 37-40","3122221817");
        u.sig=t;
        t.ant=u;
        u=t;
        t = new PaginasAmarillas("cacharreria urbana","dg 72 n° 104-2","3003143218");
        u.sig=t;
        t.ant=u;
        u=t;
    }
    
    public void menuAdicionarListasDobles()
    {
        int opc;
        System.out.println("MENU ADICIONAR LISTAS DOBLES");
        System.out.println("1. Adicionar por el inicio listas Dobles.");
        System.out.println("2. Adicionar por el fin listas Dobles.");
        System.out.println("3. Adicionar antes de nodo listas Dobles");
        System.out.println("4. Adicionar despues de nodo listas Dobles");
        System.out.println("5. Volver.");
        
        System.out.println("\nEscoja una opcion;");
        opc = leer.nextInt();
        
        switch (opc) {
            case 1:
                adicionarInicioListasDobles();
                menuAdicionarListasDobles();
                break;
                
            case 2:
                adicionarFinListasDobles();
                menuAdicionarListasDobles();
                break;
                
            case 3:
                adicionarAntesListasDobles();
                menuAdicionarListasDobles();
                break;
                
            case 4:
                adicionarDespuesListasDobles();
                menuAdicionarListasDobles();
                break;
            
            case 5:
                menuListasDobles();
                break;
                
            default:
                menuAdicionarListasDobles();
                break;
        }
    }
    
    public void adicionarInicioListasDobles()
    {
        String nom, dir, tel;
        System.out.println("Digite el nombre de la empres ");
        nom=leer.nextLine();
        nom=leer.nextLine();
        System.out.println("Digite la direccion de la empresa ");
        dir=leer.nextLine();
        
        System.out.println("Digite el telefono de la empresa ");
        tel=leer.nextLine();
                
        t=new PaginasAmarillas(nom,dir,tel);
        u= cabezaPaginasAmarillas;
        t.sig=u;
        u.ant=t;
        cabezaPaginasAmarillas =t;
    }
    
    public void adicionarFinListasDobles()
    {
        String nom, dir, tel;
        System.out.println("Digite el nombre de la empres ");
        nom=leer.nextLine();
        nom=leer.nextLine();
        System.out.println("Digite la direccion de la empresa ");
        dir=leer.nextLine();
        
        System.out.println("Digite el telefono de la empresa ");
        tel=leer.nextLine();
                
        t=new PaginasAmarillas(nom,dir,tel);
        
        u= cabezaPaginasAmarillas;
        while(u.sig!=null)
            u=u.sig;
        t.ant=u;
        u.sig=t;
    }
    
    public void adicionarAntesListasDobles()
    {        
        String nom, dir, tel;
        String dato;
        u= cabezaPaginasAmarillas;
        System.out.println("Digite el nombre a buscar ");
        dato=leer.nextLine();
        dato=leer.nextLine();
        if(u.getNombre().compareToIgnoreCase(dato)==0)
        {
            adicionarInicioListasDobles();
        }
        else
        {  
            while(u.getNombre().compareToIgnoreCase(dato)!=0 && u.sig!=null)
            {                
                u=u.sig;
            }
            if(u.getNombre().compareToIgnoreCase(dato)==0)
              {
                  System.out.println("Digite el nombre de la empres ");
                nom=leer.nextLine();
                nom=leer.nextLine();
                System.out.println("Digite la direccion de la empresa ");
                dir=leer.nextLine();        
                System.out.println("Digite el telefono de la empresa ");
                tel=leer.nextLine();        
                t=new PaginasAmarillas(nom,dir,tel);
                t.sig=u;
                t.ant=u.ant;
                u.ant.sig=t;
                  u.ant=t;               
              }
            else
                System.out.println("el nombre buscado no se encuentra en la lista");            
        }                
    }
    
    public void adicionarDespuesListasDobles()
    {
        
    }
    
    public void menuEliminarListasDobles()
    {
        int opc;
        System.out.println("MENU ELIMINAR LISTAS DOBLES");
        System.out.println("1. Eliminar por el inicio listas Dobles.");
        System.out.println("2. Eliminar por el fin listas Dobles.");
        System.out.println("3. Eliminar antes de nodo listas Dobles");
        System.out.println("4. Eliminar despues de nodo listas Dobles");
        System.out.println("5. Eliminar nodo dado listas Dobles.");
        System.out.println("6. Volver.");
        
        System.out.println("\nEscoja una opcion;");
        opc = leer.nextInt();
        
        switch (opc) {
            case 1:
                eliminarInicioListasDobles();
                menuEliminarListasDobles();
                break;
                
            case 2:
                eliminarFinListasDobles();
                menuEliminarListasDobles();
                break;
                
            case 3:
                eliminarAntesListasDobles();
                menuEliminarListasDobles();
                break;
                
            case 4:
                eliminarDespuesListasDobles();
                menuEliminarListasDobles();
                break;
                
            case 5:
                eliminarNodoDadoListasDobles();
                menuEliminarListasDobles();
                break;
                
            case 6:
                menuListasDobles();
                break;
                
            default:
                menuEliminarListasDobles();
                break;
        }
    }
    
    public void eliminarInicioListasDobles()
    {
        cabezaPaginasAmarillas = cabezaPaginasAmarillas.sig;
        cabezaPaginasAmarillas.ant=null;
        
    }
    
    public void eliminarFinListasDobles()
    {
       t= cabezaPaginasAmarillas;
        while(t.sig!=null)
        {
            t=t.sig;
           
        }
        t.ant.sig=null;
    }
    
    public void eliminarAntesListasDobles()
    {
        
    }
    
    public void eliminarDespuesListasDobles()
    {
        
    }
    
    public void eliminarNodoDadoListasDobles()
    {
        
    }
    
    public void modificarListasDobles()
    {
        String dato;
        System.out.println("digite el nombre de a empresa a modificar ");
        dato=leer.nextLine();
        dato=leer.nextLine();
        u= cabezaPaginasAmarillas;
        while(u.getNombre().compareToIgnoreCase(dato)!=0 && u.sig!=null)
            u=u.sig;
        if(u.getNombre().compareToIgnoreCase(dato)==0)
        {
            int opc;
            String nom, dir, tel;
            System.out.println("1. cambiar nombre");
            System.out.println("2.cambiar direccion");
            System.out.println("3.cambiar telefono");
            System.out.println("4.cambiar todos los datos");
            System.out.println("escoja la opcion");
            opc=leer.nextInt();
            switch(opc)
            {
                case 1: 
                    System.out.println("digite el nuevo nombre de la empresa ");
                    nom=leer.nextLine();
                    nom=leer.nextLine();
                    u.setNombre(nom);
                    break;
                case 2: 
                    System.out.println("digite la nueva direccion de la empresa ");
                    dir=leer.nextLine();
                    dir=leer.nextLine();
                    u.setDireccion(dir);
                    break;
                case 3: 
                    System.out.println("digite el nuevo telefono de la empresa ");
                    tel=leer.nextLine();
                     tel=leer.nextLine();
                    u.setTelefono(tel);
                    break;
                case 4: 
                    System.out.println("digite el nuevo nombre de la empresa ");
                    nom=leer.nextLine();
                    nom=leer.nextLine();
                    u.setNombre(nom);
                    System.out.println("digite la nueva direccion de la empresa ");
                    dir=leer.nextLine();
                    u.setDireccion(dir);
                    System.out.println("digite el nuevo telefono de la empresa ");
                    tel=leer.nextLine();
                    u.setTelefono(tel);
                    break;
                default:    
                    System.out.println("error al escoger la opcion");
                    modificarListasDobles();
            }
        }
               
    }
    
    public void imprimirListasDobles()
    {
        t= cabezaPaginasAmarillas;
        while (t.sig!=null)
        {
            
            System.out.println("nombre : "+ t.nombre + "   " + "direccion : "+ t.getDireccion()+ "    " + "telefono : "+ t.getTelefono());
     
            t=t.sig;
          
        }
        System.out.println("nombre : "+ t.nombre + "   " + "direccion : "+ t.getDireccion()+ "    " + "telefono : "+ t.getTelefono());
        System.out.println(" ");
        System.out.println("lista inversa ");
        System.out.println(" ");
           
             while (t.ant!=null)
             {
               System.out.println("nombre : "+ t.nombre + "   " + "direccion : "+ t.getDireccion()+ "    " + "telefono : "+ t.getTelefono());    
                t=t.ant;
           
             }
           System.out.println("nombre : "+ t.nombre + "   " + "direccion : "+ t.getDireccion()+ "    " + "telefono : "+ t.getTelefono()); 
    }
    
    public void menuListasCircularesDobles()
    {
     int opc;
        System.out.println("MENU LISTAS CIRCULARES DOBLES");
        System.out.println("1. Crear listas Circulares Dobles");
        System.out.println("2. Adicionar listas Circulares Dobles.");
        System.out.println("3. Eliminar listas Circulares Dobles");
        System.out.println("4. Modificar listas Circulares Dobles");
        System.out.println("5. Imprimir listas Circulares Dobles");
        System.out.println("6. Volver.");
        
        System.out.println("");
        System.out.println("Escoja una opcion");
        opc = leer.nextInt();
        
        switch (opc) {
            case 1:
                crearListasCircularesDobles();
                menuListasCircularesDobles();
                break;
                
            case 2:
                menuAdicionarListasCircularesDobles();
                menuListasCircularesDobles();
                break;
                
            case 3:
                menuEliminarListasCircularesDobles();
                menuListasCircularesDobles();
                break;
                
            case 4:
                modificarListasCircularesDobles();
                menuListasCircularesDobles();
                break;
            
            case 5:
                imprimirListasCircularesDobles();
                menuListasCircularesDobles();
                break;
                
            case 6:
                menuPrincipal();
                break;
                
            default:
                menuListasCircularesDobles();
        }
    }
    
    public void crearListasCircularesDobles()
    {
        x = new Curso(34010,"algoritmia",4.3);
        cabezaCurso =x;
        y=x;
        x.sig= cabezaCurso;
        cabezaCurso.ant=x;
        x = new Curso(34011,"herramientas computacionales",3.5);
        x.ant=y;
        x.sig= cabezaCurso;
        y.sig=x;
        cabezaCurso.ant=x;
        y=x;
        x = new Curso(34012,"estructuras de datos",4.7);
        x.ant=y;
        x.sig= cabezaCurso;
        y.sig=x;
        cabezaCurso.ant=x;
        y=x;
        x = new Curso(34012,"ingenieria del software",3.8);
        x.ant=y;
        x.sig= cabezaCurso;
        y.sig=x;
        cabezaCurso.ant=x;
        y=x;
    }
    
    public void menuAdicionarListasCircularesDobles()
    {
        int opc;
        System.out.println("MENU ADICIONAR LISTAS CIRCULARES DOBLES");
        System.out.println("1. Adicionar por el inicio listas Circulares Dobles.");
        System.out.println("2. Adicionar por el fin listas Circulares Dobles.");
        System.out.println("3. Adicionar antes de nodo listas Circulares Dobles");
        System.out.println("4. Adicionar despues de nodo listas Circulares Dobles");
        System.out.println("5. Volver.");
        
        System.out.println("\nEscoja una opcion;");
        opc = leer.nextInt();
        
        switch (opc) {
            case 1:
                adicionarInicioListasCircularesDobles();
                menuAdicionarListasCircularesDobles();
                break;
                
            case 2:
                adicionarFinListasCircularesDobles();
                menuAdicionarListasCircularesDobles();
                break;
                
            case 3:
                adicionarAntesListasCircularesDobles();
                menuAdicionarListasCircularesDobles();
                break;
                
            case 4:
                adicionarDespuesListasCircularesDobles();
                menuAdicionarListasCircularesDobles();
                break;
            
            case 5:
                menuListasCircularesDobles();
                break;
                
            default:
                menuAdicionarListasCircularesDobles();
                break;
        }
    }
    
    public void adicionarInicioListasCircularesDobles()
    {
        String  nom;
        int cod;
        Double not;
        System.out.println("Digite el codigo del estudiante ");
        cod=leer.nextInt();
        System.out.println("Digite nombre de la asignatura ");
        nom=leer.nextLine();
        nom=leer.nextLine();
        System.out.println("Digite nota del estudiante ");
        not=leer.nextDouble();
                
        y=new Curso(cod,nom,not);
        x= cabezaCurso;
        y.sig=x;
        y.ant=x.ant;
        x.ant.sig=y;
        x.ant=y;
        cabezaCurso =y;
    }
    
    public void adicionarFinListasCircularesDobles()
    {
        String  nom;
        int cod;
        Double not;
        System.out.println("Digite el codigo del estudiante ");
        cod=leer.nextInt();
        System.out.println("Digite nombre de la asignatura ");
        nom=leer.nextLine();
        nom=leer.nextLine();
        System.out.println("Digite nota del estudiante ");
        not=leer.nextDouble();
                
        y=new Curso(cod,nom,not);
        x= cabezaCurso;
        y.ant=x.ant;
        y.sig=x;
        x.ant.sig=y;
        x.ant=y;
    }
    
    public void adicionarAntesListasCircularesDobles()
    {        
        int cod;
        String nom;
        Double not;
        String dato;
        x= cabezaCurso;
        System.out.println("Digite la asignatura a buscar ");
        dato=leer.nextLine();
        dato=leer.nextLine();
        
            while(x.getAsignatura().compareToIgnoreCase(dato)!=0 && x.sig!= cabezaCurso)
            {                
                x=x.sig;
            }
            if(x== cabezaCurso)
            {
                System.out.println("entre por el ultimo ");
                System.out.println("Digite el codigo del estudiante ");
                cod=leer.nextInt();
                System.out.println("Digite nombre de la asignatura ");
                nom=leer.nextLine();
                nom=leer.nextLine();
                System.out.println("Digite nota del estudiante ");
                not=leer.nextDouble();
                
                y=new Curso(cod,nom,not);
                
                y.sig=x;
                y.ant=x.ant;
                x.ant.sig=y;
                x.ant=y;
                cabezaCurso =y;
                
            }
            else
            { System.out.println("no era el ultimo ");
                if(x.getAsignatura().compareToIgnoreCase(dato)==0)
                {
                    System.out.println("entre por uno cualquiera ");
                    System.out.println("Digite el codigo del estudiante ");
                cod=leer.nextInt();
                System.out.println("Digite nombre de la asignatura ");
                nom=leer.nextLine();
                nom=leer.nextLine();
                System.out.println("Digite nota del estudiante ");
                not=leer.nextDouble();
                
                y=new Curso(cod,nom,not);
                    y.sig=x;
                    y.ant=x.ant;
                    x.ant.sig=y;
                    x.ant=y;
                }
                else
                    System.out.println("la asignatura no se encuentra en la lista");
                
            }
    }
    
    public void adicionarDespuesListasCircularesDobles()
    {
        int cod;
        String nom;
        Double not;
        String dato;
        x= cabezaCurso;
        System.out.println("Digite la asignatura a buscar ");
        dato=leer.nextLine();
        dato=leer.nextLine();
        
            while(x.getAsignatura().compareToIgnoreCase(dato)!=0 && x.sig!= cabezaCurso)
            {                
                x=x.sig;
            }
            if(x.getAsignatura().compareToIgnoreCase(dato)==0 && x.sig== cabezaCurso)
            {
                System.out.println("entre por el ultimo ");
                System.out.println("Digite el codigo del estudiante ");
                cod=leer.nextInt();
                System.out.println("Digite nombre de la asignatura ");
                nom=leer.nextLine();
                nom=leer.nextLine();
                System.out.println("Digite nota del estudiante ");
                not=leer.nextDouble();
                
                y=new Curso(cod,nom,not);
                
                y.ant= cabezaCurso.ant;
                y.sig= cabezaCurso;
                cabezaCurso.ant.sig=y;
                cabezaCurso.ant=y;
            }
            else
            { System.out.println("no era el ultimo ");
                if(x.getAsignatura().compareToIgnoreCase(dato)==0)
                {
                    System.out.println("entre por uno cualquiera ");
                    System.out.println("Digite el codigo del estudiante ");
                cod=leer.nextInt();
                System.out.println("Digite nombre de la asignatura ");
                nom=leer.nextLine();
                nom=leer.nextLine();
                System.out.println("Digite nota del estudiante ");
                not=leer.nextDouble();
                
                y=new Curso(cod,nom,not);
                    y.sig=x.sig;
                    y.ant=x;
                    x.sig.ant=y;
                    x.sig=y;
                }
                else
                    System.out.println("la asignatura no se encuentra en la lista");
                
            }
    }
    
    public void menuEliminarListasCircularesDobles()
    {
        int opc;
        System.out.println("MENU ELIMINAR LISTAS CIRCULARES DOBLES");
        System.out.println("1. Eliminar por el inicio listas Circulares Dobles.");
        System.out.println("2. Eliminar por el fin listas Circulares Dobles.");
        System.out.println("3. Eliminar antes de nodo listas Circulares Dobles");
        System.out.println("4. Eliminar despues de nodo listas Circulares Dobles");
        System.out.println("5. Eliminar nodo dado listas Circulares Dobles.");
        System.out.println("6. Volver.");
        
        System.out.println("\nEscoja una opcion;");
        opc = leer.nextInt();
        
        switch (opc) {
            case 1:
                eliminarInicioListasCircularesDobles();
                menuEliminarListasCircularesDobles();
                break;
                
            case 2:
                eliminarFinListasCircularesDobles();
                menuEliminarListasCircularesDobles();
                break;
                
            case 3:
                eliminarAntesListasCircularesDobles();
                menuEliminarListasCircularesDobles();
                break;
                
            case 4:
                eliminarDespuesListasCircularesDobles();
                menuEliminarListasCircularesDobles();
                break;
                
            case 5:
                eliminarNodoDadoListasCircularesDobles();
                menuEliminarListasCircularesDobles();
                break;
                
            case 6:
                menuListasCircularesDobles();
                break;
                
            default:
                menuEliminarListasCircularesDobles();
                break;
        }
    }
    
    public void eliminarInicioListasCircularesDobles()
    {
        x= cabezaCurso;
        x.ant.sig=x.sig;
        x.sig.ant=x.ant;
        cabezaCurso =x.sig;
        
    }
    
    public void eliminarFinListasCircularesDobles()
    {
      x= cabezaCurso;
      x.ant.ant.sig=x;
      x.ant=x.ant.sig;
    }
    
    public void eliminarAntesListasCircularesDobles()
    {
        String dato;
        
        System.out.println("Digite la asignatura a buscar");
        dato=leer.nextLine();
        dato=leer.nextLine();
        
        x= cabezaCurso;
        y=x.sig;
        
        if (dato.compareToIgnoreCase(x.getAsignatura())==0) 
        {
            eliminarFinListasCircularesDobles();
        }else{
            if (dato.compareToIgnoreCase(y.getAsignatura())==0) 
            {
              eliminarInicioListasCircularesDobles();
            }else{
                x=y.sig;
                
                while(dato.compareToIgnoreCase(x.getAsignatura())!=0 && x.sig!= cabezaCurso)
                {
                   x=x.sig; 
                }
                if (dato.compareToIgnoreCase(x.getAsignatura())==0) 
                {
                  x.ant.ant.sig=x;
                  x.ant=x.ant.ant;
                }else{
                    System.out.println("El dato no se encuentra");
                }
            }
        }
    }
    
    public void eliminarDespuesListasCircularesDobles()
    {
        String dato;
        
        System.out.println("Digite la asignatura a buscar");
        dato=leer.nextLine();
        dato=leer.nextLine();
        x= cabezaCurso;
        
        while(dato.compareToIgnoreCase(x.getAsignatura())!=0 && x.sig!= cabezaCurso)
        {
            x=x.sig;
        }
        if (x.sig.sig== cabezaCurso)
        {
            eliminarFinListasCircularesDobles();
        }else{
            if (x.sig== cabezaCurso)
            {
                eliminarInicioListasCircularesDobles();
            }else{
                if (dato.compareToIgnoreCase(x.getAsignatura())==0) 
                {
                  x.sig=x.sig.sig;
                  x.sig.ant=x;
                }else{
                    System.out.println("El dato no se encontra");
                }
            }
        }
    }
    
    public void eliminarNodoDadoListasCircularesDobles()
    {
        String dato;
        
        System.out.println("Digite la asignatura a eliminar");
        dato=leer.nextLine();
        dato=leer.nextLine();
        x= cabezaCurso;
        
        
        while(dato.compareToIgnoreCase(x.getAsignatura())!=0 && x.sig!= cabezaCurso)
        {
            x=x.sig;
        }
        if (x== cabezaCurso)
        {
            eliminarInicioListasCircularesDobles();
        }else{
            if (x.sig== cabezaCurso && dato.compareToIgnoreCase(x.getAsignatura())==0)
            {
               eliminarFinListasCircularesDobles();
            }else{
                if (dato.compareToIgnoreCase(x.getAsignatura())==0) 
                {
                   x.ant.sig=x.sig;
                   x.sig.ant=x.ant;
                }else{
                    if (dato.compareToIgnoreCase(x.getAsignatura())!=0 && x.sig== cabezaCurso)
                    {
                      System.out.println("El dato no se encuentra");   
                    }
                   
                }
            }
        
        } 
    }
    
    public void modificarListasCircularesDobles()
    {
        String dato;
        System.out.println("digite el nombre de a empresa a modificar ");
        dato=leer.nextLine();
        dato=leer.nextLine();
        u= cabezaPaginasAmarillas;
        while(u.getNombre().compareToIgnoreCase(dato)!=0 && u.sig!=null)
            u=u.sig;
        if(u.getNombre().compareToIgnoreCase(dato)==0)
        {
            int opc;
            String nom, dir, tel;
            System.out.println("1. cambiar nombre");
            System.out.println("2.cambiar direccion");
            System.out.println("3.cambiar telefono");
            System.out.println("4.cambiar todos los datos");
            System.out.println("escoja la opcion");
            opc=leer.nextInt();
            switch(opc)
            {
                case 1: 
                    System.out.println("digite el nuevo nombre de la empresa ");
                    nom=leer.nextLine();
                    nom=leer.nextLine();
                    u.setNombre(nom);
                    break;
                case 2: 
                    System.out.println("digite la nueva direccion de la empresa ");
                    dir=leer.nextLine();
                    dir=leer.nextLine();
                    u.setDireccion(dir);
                    break;
                case 3: 
                    System.out.println("digite el nuevo telefono de la empresa ");
                    tel=leer.nextLine();
                     tel=leer.nextLine();
                    u.setTelefono(tel);
                    break;
                case 4: 
                    System.out.println("digite el nuevo nombre de la empresa ");
                    nom=leer.nextLine();
                    nom=leer.nextLine();
                    u.setNombre(nom);
                    System.out.println("digite la nueva direccion de la empresa ");
                    dir=leer.nextLine();
                    u.setDireccion(dir);
                    System.out.println("digite el nuevo telefono de la empresa ");
                    tel=leer.nextLine();
                    u.setTelefono(tel);
                    break;
                default:    
                    System.out.println("error al escoger la opcion");
                    modificarListasDobles();
            }
        }
               
    }
    
    public void imprimirListasCircularesDobles()
    {
        x= cabezaCurso;
        while (x.sig!= cabezaCurso)
        {
            
            System.out.println("codigo : "+ x.codigo + "   " + "asignatura : "+ x.asignatura + "    " + "nota : "+ x.nota);
     
            x=x.sig;
          
        }
         System.out.println("codigo : "+ x.codigo + "   " + "asignatura : "+ x.asignatura + "    " + "nota : "+ x.nota); 
    }
    
    
    public static void main(String[] args) 
    {
        LISTAS obj = new LISTAS ();
    }  
    
    /*
    public void menuListasSimples()
    {
        int opc;
        System.out.println("MENU LISTAS SIMPLES");
        System.out.println("1. Crear listas simples");
        System.out.println("2. Adicionar listas simples.");
        System.out.println("3. Eliminar listas simples");
        System.out.println("4. Modificar listas simples");
        System.out.println("5. Imprimir listas simples");
        System.out.println("6. Volver.");
        
        System.out.println("");
        System.out.println("Escoga una opcion");
        opc = leer.nextInt();
        
        switch (opc) {
            case 1:
                crearListasSimples();
                menuListasSimples();
                break;
                
            case 2:
                menuAdicionarListasSimples();
                menuListasSimples();
                break;
                
            case 3:
                menuEliminarListasSimples();
                menuListasSimples();
                break;
                
            case 4:
                modificarListasSimples();
                menuListasSimples();
                break;
            
            case 5:
                imprimirListasSimples();
                menuListasSimples();
                break;
                
            case 6:
                menuPrincipal();
                break;
                
            default:
                menuListasSimples();
        }
    }
    
    public void crearListasSimples()
    {
        
    }
    
    public void menuAdicionarListasSimples()
    {
        int opc;
        System.out.println("MENU ADICIONAR LISTAS SIMPLES");
        System.out.println("1. Adicionar por el inicio listas simples.");
        System.out.println("2. Adicionar por el fin listas simples.");
        System.out.println("3. Adicionar antes de nodo listas simples");
        System.out.println("4. Adicionar despues de nodo listas simples");
        System.out.println("5. Volver.");
        
        System.out.println("\nEscoja una opcion;");
        opc = leer.nextInt();
        
        switch (opc) {
            case 1:
                adicionarInicioListasSimples();
                menuAdicionarListasSimples();
                break;
                
            case 2:
                adicionarFinListasSimples();
                menuAdicionarListasSimples();
                break;
                
            case 3:
                adicionarAntesListasSimples();
                menuAdicionarListasSimples();
                break;
                
            case 4:
                adicionarDespuesListasSimples();
                menuAdicionarListasSimples();
                break;
            
            case 5:
                menuListasSimples();
                break;
                
            default:
                menuAdicionarListasSimples();
                break;
        }
    }
    
    public void adicionarInicioListasSimples()
    {
        
    }
    
    public void adicionarFinListasSimples()
    {
        
    }
    
    public void adicionarAntesListasSimples()
    {
        
    }
    
    public void adicionarDespuesListasSimples()
    {
        
    }
    
    public void menuEliminarListasSimples()
    {
        int opc;
        System.out.println("MENU ELIMINAR LISTAS SIMPLES");
        System.out.println("1. Eliminar por el inicio listas simples.");
        System.out.println("2. Eliminar por el fin listas simples.");
        System.out.println("3. Eliminar antes de nodo listas simples");
        System.out.println("4. Eliminar despues de nodo listas simples");
        System.out.println("5. Eliminar nodo dado listas simples.");
        System.out.println("6. Volver.");
        
        System.out.println("\nEscoja una opcion;");
        opc = leer.nextInt();
        
        switch (opc) {
            case 1:
                eliminarInicioListasSimples();
                menuEliminarListasSimples();
                break;
                
            case 2:
                eliminarFinListasSimples();
                menuEliminarListasSimples();
                break;
                
            case 3:
                eliminarAntesListasSimples();
                menuEliminarListasSimples();
                break;
                
            case 4:
                eliminarDespuesListasSimples();
                menuEliminarListasSimples();
                break;
                
            case 5:
                eliminarNodoDadoListasSimples();
                menuEliminarListasSimples();
                break;
                
            case 6:
                menuListasSimples();
                break;
                
            default:
                menuEliminarListasSimples();
                break;
        }
    }
    
    public void eliminarInicioListasSimples()
    {
        
    }
    
    public void eliminarFinListasSimples()
    {
        
    }
    
    public void eliminarAntesListasSimples()
    {
        
    }
    
    public void eliminarDespuesListasSimples()
    {
        
    }
    
    public void eliminarNodoDadoListasSimples()
    {
        
    }
    
    public void modificarListasSimples()
    {
        
    }
    */
    
}
