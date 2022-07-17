from Pessoa import Pessoa

class Juridica(Pessoa):

	def __init__(self, nome, cnpj ,fone, nFuncionarios):
		super().__init__(nome, fone )
		self.cnpj = cnpj
		self.nFuncionarios = nFuncionarios

	def alteracnpj(self,cnpj):
		self.cnpj = cnpj

	def alteranumeroFunc(self,nFuncionarios):
		self.nFuncionarios = nFuncionarios

	def info(self):
		super().info()
		print("CNPJ: " + self.cnpj + "\nFuncionários: " + str(self.nFuncionarios))




