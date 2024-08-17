class Libro:
    def _init_(self,titulo, autor,genero,año):
        self.titulo = titulo
        self.autor  = autor
        self.genero = genero
        self.año = año
        self.prestado = False

    def prestar (self):
     self.prestado = True

    def devolver (self):
      self.devolver = False

    def _str_(self):
        if self.prestado:
            estado = "prestado"
        else:
            estado = "Disponible"
        return f"{self.titulo}de {self.autor}({self.año})- genero:{self.genero} - estado:{estado}"
     
class Biblioteca:
    def _init_(self):
        self.libro = []

    def agregar_libros(self, libro):
        self.libros.append(libro)

    def eliminar_libro(self,titulo):
        nueva_lista_libros = []
        for libro in self.libros:
            if libro.titulo != titulo:
                nueva_lista_libros.append(libro)
                self.libros = nueva_lista_libros
        

    def buscar_por_titulo(self,titulo):
        libros_encontrados =[]
        for libro in self.libros:
            if titulo ==titulo:
                libros_encontrados.append(libro)
                return libros_encontrados
      
    def buscar_por_autor(self,autor):
        libros_encontrados =[]
        for libro in self.libros:
            if autor == libro.autor:
                libros_encontrados.append(libro)
            return libros_encontrados
      

    def buscar_por_genero(self,genero):
        libros_encontrados = []
        for libro in self.libros:
            if genero == libro.genero:
                libros_encontrados.append(libro)
            return libros_encontrados
      
class Biblioteca:
    def listar_libros(self):
        return self.libros

def mostrar_menu():
        print("1.agregar libro")
        print("2.eliminar libro")
        print("3.buscar libro por titulo")
        print("4.buscar libro por autor")
        print("5.buscar libro por genero")
        print("6.listar todos los libros")
        print("7.prestar libro")
        print("devolver libro")
        print("guardar y salir")

biblioteca = Biblioteca()

while True:
 
    mostrar_menu()
    opcion = input("ingrese una opcion:")

    if opcion == "1":
        titulo = input("titulo:")
        autor = input("auto:")
        genero = input("genero:")
        año = int(input("año:"))
        libro = Libro(titulo, autor, genero, año)
        biblioteca.agregar_libros(libro)


       
       




