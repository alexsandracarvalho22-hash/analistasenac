## LISTAS:
# índices:   0        1      2       3       4             
# compras = ["arroz","sabão","pão","açúcar","feijão"]
# print(compras)
# print(compras[-1])


# compras2 = ["amaciante", "papel toalha", "farinha", "maçã", "pão de forma" ]

# compras_final = compras + compras2
# print (compras_final)



# compras3 = ["laranja","maçã","hamburguer", "sal"]
            
#compras_final = compras_final = compras3
#print (compras_final)


#compras_final += compras3
#print = (compras_final)

# compras_final += ["café"]
# print = (compras_final)




## LISTAS:
# índices:   0        1      2       3       4             
compras = ["arroz","sabão","pão","açúcar","feijão"]
print(compras)
print(compras[-1])

#############################

13-11-2026

compras2 = [
    "amaciante", "papel toalha", "farinha", "maçã","pão de forma"
]

compras_final = compras + compras2
print(compras_final)

compras3 = [
    "laranja",
    "maçã",
    "hamburguer",
    "sal"
]
 
compras_final += compras3
print(compras_final)

# compras_final += ["café"]
# compras_final.append("café")
compras_final.insert(2,"café")
# print(compras_final)
compras_final.pop(3)
compras_final.remove("maçã")
compras_final.pop()
compras_dezembro=compras_final.copy()
print(compras_dezembro)

compras_final.count("maçã")
compras_final.clear()

print(compras_final)
print(compras_dezembro)
