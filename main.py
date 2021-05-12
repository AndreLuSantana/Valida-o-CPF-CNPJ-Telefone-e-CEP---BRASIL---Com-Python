from cep import Cep
import requests

cep = Cep(38380000)

bairro, cidade, uf = cep.acessa_via_cep()
print(bairro)
print(cidade)
print(uf)

