origem = int(input("qual o codigo?"))


if origem == 1:
    print ("sul")
elif origem == 2:
    print ("norte")
elif origem == 3:
    print ("leste")
elif origem == 4:
    print ("oeste")
elif origem == 5 or origem == 6:
    print("nordeste")
elif origem == 7 or origem == 8 or origem == 9:
    print ("sudeste")
elif origem == 10:
    print ("centro oeste")
elif origem == 11:
    print ("noroeste")
else:
    print ("importado")
