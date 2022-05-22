from random import Random
from beverages import *

class CoffeeMachine:
	def __init__(self, usage=0) -> None:
		self.usage=usage
		pass
	class EmptyCup(HotBeverage):
		def __init__(self, name="empty cup", price=0.9, des="An emptycup?! Gimme my money back!"):
			super().__init__(name, price, des)
	class BrokenMachineException(Exception):
		def __init__(self,args= "This coffee machine has to be repaired.") -> None:
			super().__init__(args)
	def serve(self, drink):
		if self.usage > 10:
			return self.BrokenMachineException()
		else:
			y = Random()
			x = y.randint(0,1)
			if x == 0:
				self.usage += 1
				return self.EmptyCup()
			else:
				self.usage+=1
				return drink
	def repair(self):
		self.usage = 0


m=CoffeeMachine()
i =0
while i <=12:
	i+=1
	print(m.serve(Tea()), end="\n\n")

m.repair()

i = 0

while i <=12:
	i+=1
	print(m.serve(Coffe()), end="\n\n")