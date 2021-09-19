class Carrera:
    def __init__(self,id,descripcion):
        self.__id = id
        self.descripcion = descripcion
       
    @property
    def id(self):
        return self.__id

    def getCarrera(self):
        return  [str(self.id),self.descripcion]

class Materia:
    def __init__(self,id, descripcion):
        self.__id = id
        self.descripcion = descripcion
       
    @property
    def id(self):
        return self.__id

    def getMateria(self):
        return  [str(self.id),self.descripcion]
     
class Periodo:
    def __init__(self,periodo,descripcion):
        self.periodo =periodo     # 202111
        self.descripcion = descripcion # Segundo semestre 2021
       
   
    def getPeriodo(self):
        return  [str(self.periodo),self.descripcion]
     
class Profesor: 
    def __init__(self,id,nombre,cedula,carrera,titulo,telefono):
        self.__id = id
        self.nombre = nombre
        self.cedula = cedula
        self.titulo = titulo
        self.telefono = telefono
        self.carrera=carrera
       
    @property
    def id(self):
        return self.__id

    def getProfesor(self):
        return  [str(self.id),self.nombre,self.cedula,self.titulo,self.telefono,self.carrera.id]
   
class Estudiante: 
    def __init__(self,id,nombre,cedula,direccion,telefono):
        self.__id = id
        self.nombre = nombre
        self.cedula = cedula
        self.direccion=direccion
        self.telefono = telefono
       
    @property
    def id(self):
        return self.__id

    def getEstudiante(self):
        return  [str(self.id),self.nombre,self.cedula,self.direccion,self.telefono]
   
class Matricula: 
    def __init__(self,id,estudiante,carrera,periodo,valor):
        self.__id = id
        self.periodo= periodo
        self.estudiante = estudiante
        self.carrera = carrera
        self.valor = valor
       
    @property
    def id(self):
        return self.__id

    def getEstudiantemat(self):
        return  [str(self.id),self.periodo,str(self.estudiante),str(self.carrera),str(self.valor)]
   
class Notas: 
    def __init__(self,id,periodo,estudiante,materia,profesor,nota1,nota2):
        self.__id = id
        self.periodo = periodo
        self.estudiante = estudiante
        self.materia = materia
        self.profesor= profesor
        self.nota1 = nota1
        self.nota2 = nota2

    @property
    def id(self):
        return self.__id

    def getEstudiantenot(self):
        return  [str(self.id),str(self.estudiante),str(self.materia),str(self.profesor),str(self.nota1),str(self.nota2)]
   