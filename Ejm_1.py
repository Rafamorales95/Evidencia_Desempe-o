# Definir la clase Libro
class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    # Método __str__: para mostrar una descripción amigable del objeto
    def __str__(self):
        return f"'{self.titulo}' de {self.autor}"

    # Método __repr__: para mostrar una representación formal del objeto
    def __repr__(self):
        return f"Libro(titulo='{self.titulo}', autor='{self.autor}', paginas={self.paginas})"

# Crear dos instancias de la clase Libro
libro1 = Libro("Como cambia la vida", "Rafa Morales", 471)
libro2 = Libro("Una vida Sin Son risas", " Liceth Marin", 1072)


print("Usando str:")
print(libro1)
print(libro2)

print("\nUsando repr:")
print(repr(libro1))
print(repr(libro2))
