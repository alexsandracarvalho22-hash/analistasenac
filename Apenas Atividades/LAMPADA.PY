#ENTRADA DE DADOS

potencia_lampada = float(input("digite a potecia da lampada(em watts):"))
largura = float (input("digite a largura do local(em metros):"))
comprimento = float (input("digite o comprimento do local:"))

# calculo da area

area = largura * comprimento

# calculo da portecia da lampada

potencia_total = area * 3

quantidade_de_lampadas = round (potencia_total / potencia_lampada)


print(f"Área do cômodo: {area:.2f} m²")
print(f"Potência total necessária: {potencia_total:.2f} W")
print(f"Número de lâmpadas necessárias: {quantidade_de_lampadas}")

