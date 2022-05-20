
class Intern:
	def __init__(self, name="My name? I’m nobody, an intern, I have no name."):
		self.name = name
	def __str__(self) -> str:
		return self.name
	class Coffe:
		def __str__(self) -> str:
			return "This is the worst coffee you ever tasted"
	def make_coffe(self) -> str:
		return self.Coffe()
	def work(self):
		raise Exception("'I,’m just an intern, I can’t do that...")



persona = Intern()
schiavo = Intern("Mark")

print(persona)
print(schiavo)
print(schiavo.make_coffe())
try:
	persona.work()
except Exception as x:
	print(x)
