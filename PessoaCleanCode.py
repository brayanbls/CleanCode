"""
OBS: parametros começam com a letra p
"""

class Pessoa:

	def __init__(self, pNomePessoa, pFonePessoa):
		self.nomePessoa = pNomePessoa
		self.telefonePessoa = pFonePessoa

	def setNomePessoa(self, pNomePessoa):
		self.nomePessoa = pNomePessoa

	def setTelefonePessoa(self, pTelefonePessoa):
		self.telefonePessoa = pTelefonePessoa

	def getInformacoesPessoa(self):
		print("Nome: " + self.nomePessoa + "\nPhone: " + str(self.telefonePessoa))