def calcular_media(prova1,prova2,optativa = -1):

   media = (prova1 + prova2) / 2
    
   print (f"a media das notas é {media}:")

   if media >= 6.0:
         print ("aprovado")
   elif media >= 3.0:
        print ("recuperação")
   else:
        print ("reprovado")


calcular_media(10,2.6)


