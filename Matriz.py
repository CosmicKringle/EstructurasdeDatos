#Aranza Aguilar, Ariana Chinchilla, Erwin Torres Matriz de 3x3

class Matriz:
   def __init__(self, filas, columnas):
       self.filas = filas
       self.columnas = columnas
       self.elementos = [[0] * columnas for _ in range(filas)]
 
   def llenar(self):
       print(f"\nIngrese los valores de una matriz de {self.filas}x{self.columnas}:")
       for f in range(self.filas):
           for c in range(self.columnas):
            self.elementos[f][c] = int(input(f"Elemento [{f}][{c}]: "))
 
   def suma(self, otra):
       resultado = Matriz(self.filas, self.columnas)
       for f in range(self.filas):
           for c in range(self.columnas):
               resultado.elementos[f][c] = self.elementos[f][c] + otra.elementos[f][c]
       return resultado
 
   def resta(self, otra):
       resultado = Matriz(self.filas, self.columnas)
       for f in range(self.filas):
           for c in range(self.columnas):
               resultado.elementos[f][c] = self.elementos[f][c] - otra.elementos[f][c]
       return resultado
 
   def multiplicarEscalar(self, escalar):
       resultado = Matriz(self.filas, self.columnas)
       for f in range(self.filas):
           for c in range(self.columnas):
               resultado.elementos[f][c] = self.elementos[f][c] * escalar
       return resultado
 
   def mostrar(self):
       for fila in self.elementos:
           print(fila)
 
filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

m1 = Matriz(filas, columnas)
m1.llenar()
 
m2 = Matriz(filas, columnas)
m2.llenar()
 
print("\nSuma:")
m1.suma(m2).mostrar()

print("\nResta:")
m1.resta(m2).mostrar()

escalar = int(input("\nIngrese un escalar para multiplicar la primera matriz: "))
print("\nProducto de escalar:")
m1.multiplicarEscalar(3).mostrar()
