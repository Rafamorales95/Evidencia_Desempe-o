from abc import ABC, abstractmethod

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
class Libro(Publicacion):
    def __init__(self, titulo, autor, paginas):
        super().__init__(titulo, autor, paginas)
    def informacion(self):
        return f"Libro: '{self.titulo}' escrito por {self.autor_o_editor} con {self.paginas} páginas."

    # Implementación del método resumen
    def resumen(self):
        return f"Este libro, '{self.titulo}', es una obra famosa de {self.autor_o_editor}."

# Clase derivada Revista
class Revista(Publicacion):
    def __init__(self, titulo, editor, paginas):
        super().__init__(titulo, editor, paginas)

    def informacion(self):
        return f"Revista: '{self.titulo}' editada por {self.autor_o_editor} con {self.paginas} páginas."

    def resumen(self):
        return f"La revista '{self.titulo}' Los Mejores Chisme De Medellin de {self.autor_o_editor}."
    
libro = Libro("El Mas trabajador", "Rafa morales", 1232)
revista = Revista("El Chismografo", "Alvaro Ruiz", 120)

# Mostrar la información y el resumen de cada publicación
print(libro.informacion())
print(libro.resumen())

print(revista.informacion())
print(revista.resumen())
