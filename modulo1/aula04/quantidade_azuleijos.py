# ENTRADA DE DADOS

altura = float(input("digite a altura da cozinha:"))
comprimento = float (input("digite o comprimento da cozinha:"))
largura = float (input("digite  largurada cozinha:"))

#calculo

perimetro = 2 * (comprimento + largura)

area = perimetro * altura

area_por_caixa = 1.5

divisão_exata = area / area_por_caixa

caixas_necessarias = int(divisão_exata)
if divisão_exata>caixas_necessarias:
    caixas_necessarias = caixas_necessarias + 1

print(f"/narea_total: {area:.2f} m²")
print(f"numero de caixas de azuleijos necessarios: {caixas_necessarias}")




