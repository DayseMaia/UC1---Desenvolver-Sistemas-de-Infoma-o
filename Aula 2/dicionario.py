dic = {"Nome":'Larissa', "UltimoNome":'Maria', "Idade":'25', "Curso":'Administração', "Endereço":'Rua xxxxxxxxx'}
print(dic.items())
print(dic.values())

del dic["Curso"]
print(dic.items())

dic["UltimoNome"] = 'Lopes'
print(dic.items())
print(dic["Endereço"])

dic2 = dic.copy()
dic2["Nome"] = 'Paula'
dic2["Idade"] = '30'
print(dic2.items())