class Pila:
	
	def __init__(self):
		self.pila = []

	def apilar(self, x):
		self.pila.append(x)

	def vacia(self):
		return len(self.pila) == 0

	def tope(self):
		return self.pila[len(self.pila)-1]

	def desapilar(self):
		self.pila.pop()