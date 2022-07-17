from Pessoa import Pessoa

"""
OBS: parametros começam com a letra p
	 Tudo que termina com PES vem da classe Pessoa e o que termina com JUR da classe Juridica
"""

class PessoaJuridica(Pessoa):

	def __init__(self, pNomePes,pFonePes,pCnpjJur,pNumFuncionariosJur):
		super().__init__(pNomePes, pFonePes)
		self.cnpjJur = pCnpjJur
		self.numFuncionariosJur = pNumFuncionariosJur

	def setCnpjJur(self,pCnpjJur):
		self.cnpjJur = pCnpjJur

	def setNumFuncionariosJur(self,pNumFuncionariosJur):
		self.numFuncionariosJur = pNumFuncionariosJur

	def getInformacoesJuridica(self):
		super().getInformacoesPessoa()
		print("CNPJ: " + self.cnpjJur + "\nFuncionários: " + str(self.numFuncionariosJur))





