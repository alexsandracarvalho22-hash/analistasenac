# (and) só é verdadeiro quando TUDO é verdeiro, caso ao contrario é falso!!!

# contexto (uso do operador AND)

#'''
#para q eu possa dirigir, eu preciso ter:
#- documento
#- maioridade
#- não estar alcoolizado
#'''

#pergunta1 = input("você tem os documentos em mãos?")
#pergunta2 = int(input("qual a sua idade?"))
#pergunta3 = input("você consumiu bebida alcoolica antes de dirigr?")

#if pergunta1 =="sim" and pergunta2 >= 18:
   # print ("pode dirigir.")

#elif pergunta1 == "sim" and pergunta3 == "sim":
 #   print ("não pode dirigir.")
    




## CONTEXTO 2: (uso do operador OR)

'''
para eu me deslocar até o senac de nova iguaçu:
- trem
- ônibus
- metrô
'''

trem = input("você veio de trem?")
ônibus = input ("você veio de ônibus?")
metrô = input ("você veio de metrô?")


if "trem" == "sim" or "ônibus" =="sim" or "metrô":
    print ("bem vindo ao senac!")
else:
    print ("tarifa dinâmica,né?")
