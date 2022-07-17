from Pessoa import Pessoa

"""
OBS: parametros começam com a letra p
	 Tudo que termina com PES vem da classe Pessoa e o que termina com FIS da classe Fisica
"""

class PessoaFisica(Pessoa):

	def __init__(self, pNomePes , pFonePes, pIdadeFis):
		super().__init__(pNomePes, pFonePes)
		self.idade = pIdadeFis

	def setIdadeFisica(self,pIdadeFis):
		self.idade = pIdadeFis

	def getInformacoesFisica(self):
		super().getInformacoesPessoa()
		print("Idade: " +  str(self.idade))




