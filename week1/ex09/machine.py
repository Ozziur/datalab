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
	def serve(self):
		if self.usage > 10:
			return self.BrokenMachineException()
		else:
			if self.usage %2 ==1:
				self.usage += 1
				return self.EmptyCup()
			else:
				self.usage+=1
				y = Random()
				x = y.randint(1,4)
				if x == 1:
					return Coffe()
				if x == 2:
					return Tea()
				if x == 3:
					return Chocolate()
				if x == 4:
					return Cappuccino()
	def repair(self):
		self.usage = 0


m=CoffeeMachine()
i =0
while i <=12:
	i+=1
	print(m.serve(), end="\n\n")

m.repair()

i = 0

while i <=12:
	i+=1
	print(m.serve(), end="\n\n")