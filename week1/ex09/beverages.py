class HotBeverage:
	def	__init__(self, name = "hot beverage", price = 0.30, des= "Just some hot water in a cup"):
		self.name = name
		self.price = price
		self.descriptio=des
	def __str__(self) -> str:
		return f"Name: {self.name}\nPrice: {self.price:.2f}\nDescription: {self.descriptio}"
	def description(self):
		return self.descriptio

class Coffe(HotBeverage):
	def __init__(self, name="coffee", price=0.40, des="A coffee, to stay awake."):
		super().__init__(name, price, des)

class Tea(HotBeverage):
	def __init__(self, name="tea"):
		super().__init__(name)

class Chocolate(HotBeverage):
	def __init__(self, name="chocolate", price=0.50, des="Chocolate, sweet chocolate..."):
		super().__init__(name, price, des)


class Cappuccino(HotBeverage):
	def __init__(self, name="cappuccino", price=0.45, des="Un po' di Italia nella sua tazza!"):
		super().__init__(name, price, des)
