class Pessoa:

	def __init__(self, nome, fone):
		self.nome = nome
		self.telefone = fone

	def definePessoa(self, nome):
		self.nome = nome

	def defineTelefone(self, telefone):
		self.telefone = telefone

	def info(self):
		print("Nome: " + self.nome + "\nPhone: " + self.telefone)



