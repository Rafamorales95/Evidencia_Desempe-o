from abc import ABC, abstractmethod

# Clase abstracta Publicacion
class Publicacion(ABC):
    def __init__(self, titulo, autor_o_editor, paginas):
        self.titulo = titulo
        self.autor_o_editor = autor_o_editor
        self.paginas = paginas

    @abstractmethod
    def informacion(self):
        pass

    @abstractmethod
    def resumen(self):
        pass

    # Método mágico __str__ para mostrar el tipo de publicación
    def __str__(self):
        return f"Tipo de publicación: {self.__class__.__name__}"

# Clase derivada Libro
class Libro(Publicacion):
    def __init__(self, titulo, autor, paginas):
        super().__init__(titulo, autor, paginas)

    def informacion(self):
        return f"Libro: '{self.titulo}' escrito por {self.autor_o_editor} con {self.paginas} páginas."

    def resumen(self):
        return f"Este libro, '{self.titulo}', es una obra famosa de {self.autor_o_editor}."

    # Sobrescribir el método __str__ para incluir el título del libro
    def __str__(self):
        return f"Libro: '{self.titulo}'"

# Clase derivada Revista
class Revista(Publicacion):
    def __init__(self, titulo, editor, paginas):
        super().__init__(titulo, editor, paginas)

    def informacion(self):
        return f"Revista: '{self.titulo}' editada por {self.autor_o_editor} con {self.paginas} páginas."

    def resumen(self):
        return f"La revista '{self.titulo}' contiene artículos interesantes bajo la dirección de {self.autor_o_editor}."

    # Sobrescribir el método __str__ para incluir el título de la revista
    def __str__(self):
        return f"Revista: '{self.titulo}'"

# Crear instancias de Libro y Revista
libro = Libro("El Más Trabajador", "Rafa Morales", 1232)
revista = Revista("El Chismógrafo", "Álvaro Ruiz", 120)

# Mostrar la información y el resumen de cada publicación
print(libro.informacion())
print(libro.resumen())

print(revista.informacion())
print(revista.resumen())

# Comprobar la funcionalidad del método __str__
print(libro)    # Salida esperada: Libro: 'El Más Trabajador'
print(revista)  # Salida esperada: Revista: 'El Chismógrafo'
