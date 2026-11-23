banco_dados =  {
"loja_digital" :{
        501: {"item": "Pacote 1000 PipocaCoins (Moeda Virtual)", "preco": 19.90, "licencas_estoque": 100, "alerta_minimo": 15},
        502: {"item": "Passe de Batalha: Temporada Cyber 2026", "preco": 44.90, "licencas_estoque": 50, "alerta_minimo": 10},
        503: {"item": "Aluguel 48h: Trilogia O Senhor dos Anéis (8K Remaster)", "preco": 24.90, "licencas_estoque": 30, "alerta_minimo": 5}
    }}



def verificar_esgotamento_licencas(banco_dados):
    itens_criticos = []
    for dados in banco_dados["loja_digital"].values():
        if dados ["licencas_estoque"] <= dados ["alerta_minimo"]:
            itens_criticos.append(dados["item"])

    return itens_criticos

print (verificar_esgotamento_licencas(banco_dados))
