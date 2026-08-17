#Aranza Aguilar, Ariana Chinchilla, Erwin Torres Matriz de 3x3

class Matriz:
   def __init__(self, filas, columnas):
       self.filas = filas
       self.columnas = columnas
       self.elementos = [[0] * columnas for _ in range(filas)]
 
   def llenar(self, valores):
       self.elementos = valores
 
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
 
 
m1 = Matriz(3, 3)
m1.llenar([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
 
m2 = Matriz(3, 3)
m2.llenar([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
 
m1.suma(m2).mostrar()
m1.resta(m2).mostrar()
m1.multiplicarEscalar(3).mostrar()
