from Pessoa import Pessoa

class Fisica(Pessoa):

	def __init__(self, nome , fone, idade):
		super().__init__(nome, fone)
		self.idade = idade

	def alterar(self,pIdadeFis):
		self.idade = pIdadeFis

	def info(self):
		super().info()
		print("Idade: " +  str(self.idade))





