#entrada de dados

km_inicial = float (input("digite o km do começo do dia:"))
km_final = float (input('digite a marcação do km do final do dia:'))
gasolina_gasta = float (input("digite o total de gasolina gasta:"))
valor_recebido = float (input("numero total de passageiros no dia:"))

km_rodados = km_final - km_inicial
media_de_consumo = km_rodados/gasolina_gasta
custo_gasolina = valor_recebido * 6.15
lucro = valor_recebido - custo_gasolina

print ()
print ("resutados do dia")
print()

print (f"total de km rodados: {km_rodados}")
print (f"total da media por consumo:{media_de_consumo}")
print (f"total gasto com gasolina:{custo_gasolina}")
print (f"lucro final:{lucro}")