
banco_dados =  {
"loja_digital" :{
        501: {"item": "Pacote 1000 PipocaCoins (Moeda Virtual)", "preco": 19.90, "licencas_estoque": 100, "alerta_minimo": 15},
        502: {"item": "Passe de Batalha: Temporada Cyber 2026", "preco": 44.90, "licencas_estoque": 50, "alerta_minimo": 10},
        503: {"item": "Aluguel 48h: Trilogia O Senhor dos Anéis (8K Remaster)", "preco": 24.90, "licencas_estoque": 30, "alerta_minimo": 5}
    }}

def listar_loja_digital(banco_dados):
    for id_item, dados in banco_dados["loja_digital"].items():
        print (f"id:{id_item} | item: {dados['item']} | preço R$ {dados['preco']:.2f} | estoque {dados['licencas_estoque']}")

listar_loja_digital(banco_dados)
