from componentes import Menu,Valida
from helpers import borrarPantalla,gotoxy
from crudArhivos import Archivo
from entidadesUnemi import *
from datetime import date
import time

# Procesos de las Opciones del Menu Mantenimiento
def carreras():
   borrarPantalla()
   validar = Valida()     
   gotoxy(20,2);print("MANTENIMIENTO DE CARRERAS")
   gotoxy(15,4);print("Codigo: ")
   gotoxy(15,5);print("Descripcion Carrera: ")
   descarrera = validar.solo_letras("Error: Solo Letras;",38,5)
   archiCarrera = Archivo("carrera.txt",";")
   carreras = archiCarrera.leer()
   if carreras : idSig = int(carreras[-1][0])+1
   else: idSig=1
   carrera = Carrera(idSig,descarrera)
   datos = carrera.getCarrera()
   datos = ';'.join(datos)
   archiCarrera.escribir([datos],"a")

def materias():
   borrarPantalla()
   validar = Valida()   
   gotoxy(20,2);print("MANTENIMIENTO DE MATERIAS")
   gotoxy(15,4);print("Codigo: ")
   gotoxy(15,5);print("Descripcion Materias: ")
   desmateria = validar.solo_letras("Error: Solo Letras;",38,5)
   archiMateria = Archivo("materias.txt",";")
   materias = archiMateria.leer()
   if materias : idSig = int(materias[-1][0])+1
   else: idSig=1
   materia = Materia(idSig,desmateria)
   datos = materia.getMateria()
   datos = ';'.join(datos)
   archiMateria.escribir([datos],"a")

def periodos():
   borrarPantalla()
   validar = Valida()  
   gotoxy(20,2);print("MANTENIMIENTO DE PERIODOS")
   gotoxy(15,4);print("Año Periodo: AAAAMM")
   gotoxy(15,5);print("Descripcion: ")
   pedaño = validar.solo_numeros("Error: Solo Numeros;",28,4)
   gotoxy(28,5);desperiodo = input()
   archiPeriodo = Archivo("periodos.txt",";")
   perd = Periodo(pedaño,desperiodo)
   datos = perd.getPeriodo()
   datos = ';'.join(datos)
   archiPeriodo.escribir([datos],"a")


def profesores():
   borrarPantalla()
   validar = Valida()     
   gotoxy(20,2);print("INGRESO DE PROFESORES")
   gotoxy(15,4);print("Nombre: ")
   gotoxy(15,5);print("Cedula:  ")
   gotoxy(15,6);print("Titulo:  ")
   gotoxy(15,7);print("Telefono: ")
   gotoxy(15,8);print("Carrera ID[    ]: ")
   nom = validar.solo_letras("Error: Solo Letras;",25,4)
   ced = validar.solo_diez("Error: Digitar Bien su Cedula",25,5)
   tit = validar.solo_letras("Error: Solo letras,",25,6)
   tel=validar.solo_diez("Error: Digitar Bien su Telefono",25,7)
   lisCarrera,entCarrera = [],None
   while not lisCarrera:
      gotoxy(27,8);id = input().upper()
      archiCarrera = Archivo("carrera.txt")
      lisCarrera = archiCarrera.buscar(id)
      if lisCarrera:
          entCarrera = Carrera(lisCarrera[0],lisCarrera[1]) 
          gotoxy(33,8);print(entCarrera.descripcion)
      else: 
         gotoxy(33,8);print("No existe Carrera con ese codigo[{}]:".format(id))
         time.sleep(1);gotoxy(33,8);print(" "*70)
   gotoxy(15,10);print("Esta seguro de Grabar El registro(s/n):")
   gotoxy(54,10);grabar = input().lower()
   if grabar == "s":
        archiProfesor = Archivo("profesores.txt")
        lisProfesores = archiProfesor.leer()
        if lisProfesores : idSig = int(lisProfesores[-1][0])+1
        else: idSig=1
        entProfesor = Profesor(idSig,nom,ced,entCarrera,tit,tel)
        datos = entProfesor.getProfesor()
        datos = ';'.join(datos)
        archiProfesor.escribir([datos],"a")                 
        gotoxy(15,11);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
   else:
       gotoxy(15,11);input("Registro No fue Grabado\n presione una tecla para continuar...")     

def estudiantes():
   borrarPantalla()
   validar = Valida()     
   gotoxy(20,2);print("INGRESO DE ESTUDIANTES")
   gotoxy(15,4);print("Nombre: ")
   gotoxy(15,5);print("Cedula:  ")
   gotoxy(15,6);print("Direccion: ")
   gotoxy(15,7);print("Telefono: ")
   nom = validar.solo_letras("Error: Solo Letras;",26,4)
   ced = validar.solo_diez("Error: Digitar Bien su Cedula",26,5)
   gotoxy(26,6);dir = input()
   tel=validar.solo_diez("Error: Digitar Bien su Telefono",26,7)
   archiEstudiantes = Archivo("estudiantes.txt",";")
   lisEstudiantes = archiEstudiantes.leer()
   if lisEstudiantes : idSig = int(lisEstudiantes[-1][0])+1
   else: idSig=1
   gotoxy(15,10);print("Esta seguro de Grabar El registro(s/n):")
   gotoxy(54,10);grabar = input().lower()
   if grabar == "s":
        entEstudiante = Estudiante(idSig,nom,ced,dir,tel)
        datos = entEstudiante.getEstudiante()
        datos = ';'.join(datos)
        archiEstudiantes.escribir([datos],"a")                 
        gotoxy(15,11);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
   else:
       gotoxy(15,11);input("Registro No fue Grabado\n presione una tecla para continuar...")   



# Procesos de las Opciones del Menu Matricula

def matriculacion():
   borrarPantalla()
   validar = Valida()     
   gotoxy(20,2);print("INGRESO DE PROFESORES")
   gotoxy(15,4);print("Id Perido: [ AAAAMM ] : ")
   gotoxy(15,5);print("Id Estudiantes [   ] : ")
   gotoxy(15,6);print("Id Carrera [   ] : ")
   gotoxy(15,7);print("Matricula Precio: ")
   
   lisPerido, entPeriodo = [],None
   while not lisPerido:
        gotoxy(28,4);idpe = input().upper()
        ArchiPeriodo= Archivo("periodos.txt")
        lisPerido = ArchiPeriodo.buscar(idpe)
        if lisPerido:
            entPeriodo = Periodo(lisPerido[0],lisPerido[1]) 
            gotoxy(41,4);print(entPeriodo.descripcion)
        else: 
            gotoxy(41,4);print("No existe Periodo con ese codigo[{}]:".format(idpe))
            time.sleep(1);gotoxy(41,4);print(" "*41)
            
   lisEstudiantes, entEstudiante = [],None
   while not lisEstudiantes:
        gotoxy(32,5);ided = input().upper()
        ArchiEstudiantes= Archivo("estudiantes.txt")
        lisEstudiantes= ArchiEstudiantes.buscar(ided)
        if lisEstudiantes:
            entEstudiante = Estudiante(lisEstudiantes[0],lisEstudiantes[1],lisEstudiantes[2],lisEstudiantes[3],lisEstudiantes[4]) 
            gotoxy(40,5);print(entEstudiante.nombre)
        else: 
            gotoxy(40,5);print("No existe Estudiantes con ese codigo[{}]:".format(ided))
            time.sleep(1);gotoxy(40,5);print(" "*40)   
               
   lisCarrera, entCarrera = [],None
   while not lisCarrera:
        gotoxy(28,6);idca = input().upper()
        ArchiCarrera= Archivo("carrera.txt")
        lisCarrera = ArchiCarrera.buscar(idca)
        if lisCarrera:
            entCarrera = Carrera(lisCarrera[0],lisCarrera[1]) 
            gotoxy(41,6);print(entCarrera.descripcion)
        else: 
            gotoxy(41,6);print("No existe Carrera con ese codigo[{}]:".format(idca))
            time.sleep(1);gotoxy(41,4);print(" "*41) 

   valorP = validar.solo_numeros("Error: Solo ingresar numeros", 34,7)
   
   gotoxy(15,9);print("Esta seguro de Grabar El registro(s/n):")
   gotoxy(54,9);grabar = input().lower()
   if grabar == "s":
        archiMatricula = Archivo("matricula.txt")
        lisMatricula = archiMatricula.leer()
        if lisMatricula : idSig = int(lisMatricula[-1][0])+1
        else: idSig=1
        entMatricula = Matricula(idSig,ided,idca,idpe,valorP)
        datos = entMatricula.getEstudiantemat()
        datos = ';'.join(datos)
        archiMatricula.escribir([datos],"a")                 
        gotoxy(15,11);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
   else:
       gotoxy(15,11);input("Registro No fue Grabado\n presione una tecla para continuar...")     
   
# Procesos de las Opciones del Menu Notas   
def notas():
 
   borrarPantalla()
   validar = Valida()     
   gotoxy(20,2);print("INGRESO DE NOTAS")
   gotoxy(15,4);print("Id Perido: [ AAAAMM ] : ")
   gotoxy(15,5);print("Id Estudiantes [   ] : ")
   gotoxy(15,6);print("Id Materia [   ] : ")
   gotoxy(15,7);print("Id Profesor [   ] : ")
   gotoxy(15,8);print("Primera Nota: ")
   gotoxy(15,9);print("Segunda Nota: ")
   
   lisPerido, entPeriodo = [],None
   while not lisPerido:
        gotoxy(28,4);idpe = input().upper()
        ArchiPeriodo= Archivo("periodos.txt")
        lisPerido = ArchiPeriodo.buscar(idpe)
        if lisPerido:
            entPeriodo = Periodo(lisPerido[0],lisPerido[1]) 
            gotoxy(41,4);print(entPeriodo.descripcion)
        else: 
            gotoxy(41,4);print("No existe Periodo con ese codigo[{}]:".format(idpe))
            time.sleep(1);gotoxy(41,4);print(" "*40)
            
   lisEstudiantes, entEstudiante = [],None
   while not lisEstudiantes:
        gotoxy(32,5);ided = input().upper()
        ArchiEstudiantes= Archivo("estudiantes.txt")
        lisEstudiantes= ArchiEstudiantes.buscar(ided)
        if lisEstudiantes:
            entEstudiante = Estudiante(lisEstudiantes[0],lisEstudiantes[1],lisEstudiantes[2],lisEstudiantes[3],lisEstudiantes[4]) 
            gotoxy(40,5);print(entEstudiante.nombre)
        else: 
            gotoxy(40,5);print("No existe Estudiantes con ese codigo[{}]:".format(ided))
            time.sleep(1);gotoxy(40,5);print(" "*40)   
               
   lisMateria, entMateria = [],None
   while not lisMateria:
        gotoxy(28,6);idma = input().upper()
        ArchiMateria= Archivo("materias.txt")
        lisMateria = ArchiMateria.buscar(idma)
        if lisMateria:
            entMateria = Materia(lisMateria[0],lisMateria[1]) 
            gotoxy(40,6);print(entMateria.descripcion)
        else: 
            gotoxy(40,6);print("No existe Materia con ese codigo[{}]:".format(idma))
            time.sleep(1);gotoxy(41,4);print(" "*41) 

   lisProfesores, entProfesores = [],None
   while not lisProfesores:
        gotoxy(29,7);idpo = input().upper()
        ArchiProfesores= Archivo("profesores.txt")
        lisProfesores = ArchiProfesores.buscar(idpo)
        if lisProfesores:
            entProfesores = Profesor(lisProfesores[0],lisProfesores[1],lisProfesores[2],lisProfesores[3],lisProfesores[4],lisProfesores[5]) 
            gotoxy(40,7);print(entProfesores.nombre)
        else: 
            gotoxy(40,7);print("No existe Profesores con ese codigo[{}]:".format(idpo))
            time.sleep(1);gotoxy(41,4);print(" "*41) 


   valorN1 = validar.solo_numeros("Error: Solo ingresar numeros", 30,8)
   valorN2 = validar.solo_numeros("Error: Solo ingresar numeros", 30,9)
   
   gotoxy(15,10);print("Esta seguro de Grabar El registro(s/n):")
   gotoxy(54,10);grabar = input().lower()
   if grabar == "s":
        archiNotas = Archivo("notas.txt")
        lisNotas = archiNotas.leer()
        if lisNotas : idSig = int(lisNotas[-1][0])+1
        else: idSig=1
        entNotas = Notas(idSig,idpe,ided,idma,idpo,valorN1,valorN2)
        datos = entNotas.getEstudiantenot()
        datos = ';'.join(datos)
        archiNotas.escribir([datos],"a")                 
        gotoxy(15,11);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
   else:
       gotoxy(15,11);input("Registro No fue Grabado\n presione una tecla para continuar...")        
            
            
     
# Menu Principal
opc=''
while opc !='4':  
    borrarPantalla()      
    menu = Menu("MENU PRINCIPAL",["1) Mantenimiento","2) Matriculacion","3) Notas","4) Salir"],20,10)
    opc = menu.menu()
    if opc == "1":
        opc1 = ''
        while opc1 !='6':
            borrarPantalla()    
            menu1 = Menu("Menu Mantenimiento",["1) Carrera","2) Materias","3) Periodos","4) Profesores","5) Estudiantes","6) Salir"],20,10)
            opc1 = menu1.menu()
            if opc1 == "1":
                carreras()
            
            elif opc1 == "2":
                materias()

            elif opc1 == "3":
                periodos()
                
            elif opc1 == "4":
                profesores()
                
            elif opc1 == "5":
                estudiantes()

            elif opc1 == "6":
                input("Esta por Salir al Menu Principal"  )
                        
    elif opc == "2":
            borrarPantalla()
            menu2 = Menu("Menu Matriculacion",["1) Matricula","2) Salir"],20,10)
            opc2 = menu2.menu()
            if opc2 == "1":
                matriculacion()
            elif opc2 == "2":
                input("Esta por Salir al Menu Principal"  )
                
    elif opc == "3":
            borrarPantalla()
            menu3 = Menu("Menu Notas",["1) Notas","2) Salir"],20,10)
            opc3 = menu3.menu()
            if opc3 == "1":
                notas()
                
            elif opc3 =="2":
                input("Esta por Salir al Menu Principal"  )
            
    elif opc == "4":
           borrarPantalla()
           print("Gracias por su visita....")
    else:
          print("Opcion no valida") 

input("Presione una tecla para salir")
borrarPantalla()

