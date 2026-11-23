# virgula separa variaveis









# ana = 2
# alex = 3
# media = (ana + alex) / 2
# print("media:", media)
# nota = int(input("nota:"))
# print = (nota)



resultados = []

for i in range (1,6):
    print (f"aluno {i}" )
    nota1 = float (input("primeiro nota:"))
    nota2 = float (input("segunda nota:"))
    media = (nota1 + nota2) / 2

    if media >= 7:
        status = ("aprovado")
    elif media >= 5:
        status = ("recuperacao")

    else:
        status = ("reprovado")

    resultados.append (f"alunos {i} - {status}")

print ("\nresutados:")
for item in resultados:
    print (item)