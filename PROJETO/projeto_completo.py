"""
Orquestrador Principal - Pipoca.AI (BingeBot)
Curso: Analista de Dados - Big Data Science (UC1)
Gerenciado pelo Instrutor: Douglas Klem
"""

import pandas as pd

# =====================================================================
# 1. BANCO DE DADOS GLOBAL EM MEMÓRIA (CONTRATO DE DADOS)
# =====================================================================
banco_dados = {
    "planos_streaming": {
        1: {
            "nome": "Plano Pipoca Solo (Full HD)",
            "mensalidade": 29.90,
            "telas_simultaneas": 1,
        },
        2: {
            "nome": "Plano Sofá Compartilhado (4K + IA)",
            "mensalidade": 54.90,
            "telas_simultaneas": 4,
        },
        3: {
            "nome": "Plano Omniverso (8K + Cloud Gaming)",
            "mensalidade": 89.90,
            "telas_simultaneas": 6,
        },
    },
    "eventos_live": {
        101: {
            "evento": "Final Mundial Valorant 2026 (POV Pro)",
            "preco": 39.90,
            "slots_servidor": 500,
        },
        102: {
            "evento": "Show Holográfico Daft Punk Experience",
            "preco": 69.90,
            "slots_servidor": 200,
        },
        103: {
            "evento": "Estreia Global: Matrix 5 (Acesso Antecipado)",
            "preco": 49.90,
            "slots_servidor": 300,
        },
    },
    "loja_digital": {
        501: {
            "item": "Pacote 1000 PipocaCoins (Moeda Virtual)",
            "preco": 19.90,
            "licencas_estoque": 100,
            "alerta_minimo": 15,
        },
        502: {
            "item": "Passe de Batalha: Temporada Cyber 2026",
            "preco": 44.90,
            "licencas_estoque": 50,
            "alerta_minimo": 10,
        },
        503: {
            "item": "Aluguel 48h: Trilogia O Senhor dos Anéis (8K Remaster)",
            "preco": 24.90,
            "licencas_estoque": 30,
            "alerta_minimo": 5,
        },
    },
    "cupons_ativos": ("SOFA10", "PIPOCA2026", "BUGZERO"),
    "assinaturas_transacoes": {},
    "faturamento_total": 0.0,
}

# =====================================================================
# 2. IMPORTAÇÃO DOS MÓDULOS
# =====================================================================
status_modulos = {}

# F01: Login
try:
    from modulos.f01_login_usuario import autenticar_usuario

    status_modulos["F01"] = "OK"
except Exception as e:
    status_modulos["F01"] = f"FALLBACK ({e})"

    def autenticar_usuario():
        print("\n=== BEM-VINDO AO PIPOCA.AI (MODO FALLBACK) ===")
        while True:
            email = input("Digite seu e-mail: ").strip()
            nick = input("Digite seu @nickname: ").strip()
            if "@" in email and "." in email and len(nick) > 0:
                return (email, nick)
            print("E-mail ou nickname inválido! Tente novamente.")


# F02: Menu
try:
    from modulos.f02_menu_chatbot import exibir_menu_chatbot

    status_modulos["F02"] = "OK"
except Exception as e:
    status_modulos["F02"] = f"FALLBACK ({e})"

    def exibir_menu_chatbot(nickname):
        print(f"\n--- PAINEL PIPOCA.AI | Olá, @{nickname}! ---")
        print("[1] Assinar Plano de Streaming (SaaS)")
        print("[2] Comprar Acesso Live Event (Pay-Per-View)")
        print("[3] Comprar na Loja Digital (Coins, Passes, 8K)")
        print("[4] Ver Resumo do Carrinho Digital")
        print("[5] Remover Último Item do Carrinho")
        print("[6] Aplicar Descontos e Finalizar Checkout")
        print("[7] Solicitar Reembolso (Anti-Churn)")
        print("[8] Operações de Servidor / Auditoria de Licenças")
        print("[9] Gerar Relatório Analytics (Pandas + CSV)")
        print("[0] Trocar Usuário / Sair")
        try:
            op = int(input("Escolha uma opção (0-9): "))
            return op if 0 <= op <= 9 else -1
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")
            return -1


# F03: Abrir Pedido
try:
    from modulos.f03_abrir_pedido import abrir_carrinho_digital

    status_modulos["F03"] = "OK"
except Exception as e:
    status_modulos["F03"] = f"FALLBACK ({e})"

    def abrir_carrinho_digital(bd, email_usuario, nickname, assinante_anual):
        novo_id = len(bd["assinaturas_transacoes"]) + 2026001
        bd["assinaturas_transacoes"][novo_id] = {
            "email_usuario": email_usuario,
            "nickname": nickname,
            "assinante_anual": assinante_anual,
            "carrinho": [],
            "valor_bruto": 0.0,
            "valor_desconto": 0.0,
            "valor_liquido": 0.0,
            "metodo_pagamento": "PENDENTE",
            "status": "ABERTO",
        }
        return novo_id


# F04: Validar Cupom Influencer
try:
    from modulos.f04_validar_influencer import validar_cupom_influencer

    status_modulos["F04"] = "OK"
except Exception as e:
    status_modulos["F04"] = f"FALLBACK ({e})"

    def validar_cupom_influencer(bd, codigo_cupom):
        return codigo_cupom.strip().upper() in bd["cupons_ativos"]


# F05: Catálogo de Planos
try:
    from modulos.f05_catalogo_planos import listar_planos_streaming

    status_modulos["F05"] = "OK"
except Exception as e:
    status_modulos["F05"] = f"FALLBACK ({e})"

    def listar_planos_streaming(bd):
        print("\nPLANOS DE STREAMING DISPONÍVEIS:")
        for id_p, dados in bd["planos_streaming"].items():
            print(
                f"ID [{id_p}] {dados['nome']} | R$ {dados['mensalidade']:.2f}/mês | Telas: {dados['telas_simultaneas']}"
            )


# F06: Contratar Plano
try:
    from modulos.f06_assinar_plano import contratar_plano_streaming

    status_modulos["F06"] = "OK"
except Exception as e:
    status_modulos["F06"] = f"FALLBACK ({e})"

    def contratar_plano_streaming(bd, id_pedido, id_plano, meses_fidelidade):
        if id_plano not in bd["planos_streaming"] or meses_fidelidade < 1:
            return False
        plano = bd["planos_streaming"][id_plano]
        subtotal = plano["mensalidade"] * meses_fidelidade
        if meses_fidelidade >= 12:
            subtotal *= 0.85
        subtotal = round(subtotal, 2)
        pedido = bd["assinaturas_transacoes"][id_pedido]
        pedido["carrinho"].append(
            {
                "categoria": "STREAMING",
                "descricao": f"{plano['nome']} ({meses_fidelidade}m)",
                "qtd": meses_fidelidade,
                "subtotal": subtotal,
            }
        )
        pedido["valor_bruto"] = round(pedido["valor_bruto"] + subtotal, 2)
        pedido["valor_liquido"] = round(
            pedido["valor_bruto"] - pedido["valor_desconto"], 2
        )
        return True


# F07: Catálogo de Lives
try:
    from modulos.f07_catalogo_lives import listar_eventos_live

    status_modulos["F07"] = "OK"
except Exception as e:
    status_modulos["F07"] = f"FALLBACK ({e})"

    def listar_eventos_live(bd):
        print("\nEVENTOS LIVE PAY-PER-VIEW:")
        for id_ev, dados in bd["eventos_live"].items():
            print(
                f"ID [{id_ev}] {dados['evento']} | R$ {dados['preco']:.2f} | Slots Livres: {dados['slots_servidor']}"
            )


# F08: Comprar PPV
try:
    from modulos.f08_comprar_ppv import reservar_acesso_live

    status_modulos["F08"] = "OK"
except Exception as e:
    status_modulos["F08"] = f"FALLBACK ({e})"

    def reservar_acesso_live(bd, id_pedido, id_evento, qtd_acessos):
        if id_evento not in bd["eventos_live"] or qtd_acessos < 1:
            return False
        ev = bd["eventos_live"][id_evento]
        if ev["slots_servidor"] < qtd_acessos:
            return False
        ev["slots_servidor"] -= qtd_acessos
        subtotal = round(ev["preco"] * qtd_acessos, 2)
        pedido = bd["assinaturas_transacoes"][id_pedido]
        pedido["carrinho"].append(
            {
                "categoria": "LIVE_PPV",
                "descricao": ev["evento"],
                "qtd": qtd_acessos,
                "subtotal": subtotal,
            }
        )
        pedido["valor_bruto"] = round(pedido["valor_bruto"] + subtotal, 2)
        pedido["valor_liquido"] = round(
            pedido["valor_bruto"] - pedido["valor_desconto"], 2
        )
        return True


# F09: Liberar Servidor
try:
    from modulos.f09_liberar_servidor import liberar_slots_servidor

    status_modulos["F09"] = "OK"
except Exception as e:
    status_modulos["F09"] = f"FALLBACK ({e})"

    def liberar_slots_servidor(bd, id_evento, qtd_liberada):
        if id_evento in bd["eventos_live"] and qtd_liberada > 0:
            bd["eventos_live"][id_evento]["slots_servidor"] += qtd_liberada
            return bd["eventos_live"][id_evento]["slots_servidor"]
        return -1


# F10: Catálogo Loja Digital
try:
    from modulos.f10_catalogo_loja import listar_loja_digital

    status_modulos["F10"] = "OK"
except Exception as e:
    status_modulos["F10"] = f"FALLBACK ({e})"

    def listar_loja_digital(bd):
        print("\n🎮 LOJA DE ATIVOS DIGITAIS:")
        for id_it, dados in bd["loja_digital"].items():
            print(
                f"ID [{id_it}] {dados['item']} | R$ {dados['preco']:.2f} | Licenças: {dados['licencas_estoque']}"
            )


# F11: Comprar Item Digital
try:
    from modulos.f11_comprar_item_digital import comprar_item_digital

    status_modulos["F11"] = "OK"
except Exception as e:
    status_modulos["F11"] = f"FALLBACK ({e})"

    def comprar_item_digital(bd, id_pedido, id_item, qtd):
        if id_item not in bd["loja_digital"] or qtd < 1:
            return False
        item = bd["loja_digital"][id_item]
        if item["licencas_estoque"] < qtd:
            return False
        item["licencas_estoque"] -= qtd
        subtotal = round(item["preco"] * qtd, 2)
        pedido = bd["assinaturas_transacoes"][id_pedido]
        pedido["carrinho"].append(
            {
                "categoria": "LOJA_DIGITAL",
                "descricao": item["item"],
                "qtd": qtd,
                "subtotal": subtotal,
            }
        )
        pedido["valor_bruto"] = round(pedido["valor_bruto"] + subtotal, 2)
        pedido["valor_liquido"] = round(
            pedido["valor_bruto"] - pedido["valor_desconto"], 2
        )
        return True


# F12: Auditoria de Licenças
try:
    from modulos.f12_auditoria_licencas import verificar_esgotamento_licencas

    status_modulos["F12"] = "OK"
except Exception as e:
    status_modulos["F12"] = f"FALLBACK ({e})"

    def verificar_esgotamento_licencas(bd):
        criticos = []
        for dados in bd["loja_digital"].values():
            if dados["licencas_estoque"] <= dados["alerta_minimo"]:
                criticos.append(dados["item"])
        return criticos


# F13: Resumo do Carrinho
try:
    from modulos.f13_resumo_carrinho import exibir_resumo_pedido

    status_modulos["F13"] = "OK"
except Exception as e:
    status_modulos["F13"] = f"FALLBACK ({e})"

    def exibir_resumo_pedido(bd, id_pedido):
        if id_pedido not in bd["assinaturas_transacoes"]:
            print("Pedido não encontrado.")
            return
        p = bd["assinaturas_transacoes"][id_pedido]
        print(
            f"\nEXTRATO DO PEDIDO #{id_pedido} | @{p['nickname']} ({p['email_usuario']})"
        )
        print(f"Status: {p['status']} | Pagamento: {p['metodo_pagamento']}")
        for idx, it in enumerate(p["carrinho"], 1):
            print(
                f"  {idx}. [{it['categoria']}] {it['descricao']} (x{it['qtd']}) -> R$ {it['subtotal']:.2f}"
            )
        print(
            f"Bruto: R$ {p['valor_bruto']:.2f} | Desconto: R$ {p['valor_desconto']:.2f} | Líquido: R$ {p['valor_liquido']:.2f}"
        )


# F14: Remover Último Item
try:
    from modulos.f14_remover_item import remover_ultimo_item_carrinho

    status_modulos["F14"] = "OK"
except Exception as e:
    status_modulos["F14"] = f"FALLBACK ({e})"

    def remover_ultimo_item_carrinho(bd, id_pedido):
        p = bd["assinaturas_transacoes"].get(id_pedido)
        if not p or len(p["carrinho"]) == 0 or p["status"] != "ABERTO":
            return False
        removido = p["carrinho"].pop()
        p["valor_bruto"] = round(max(0.0, p["valor_bruto"] - removido["subtotal"]), 2)
        p["valor_liquido"] = round(max(0.0, p["valor_bruto"] - p["valor_desconto"]), 2)
        return True


# F15: Cálculo de Descontos Digitais
try:
    from modulos.f15_calculo_cashback_desconto import aplicar_descontos_digitais

    status_modulos["F15"] = "OK"
except Exception as e:
    status_modulos["F15"] = f"FALLBACK ({e})"

    def aplicar_descontos_digitais(bd, id_pedido, cupom_influencer_valido):
        p = bd["assinaturas_transacoes"][id_pedido]
        perc = 0.0
        if p["assinante_anual"]:
            perc += 0.10
        if cupom_influencer_valido:
            perc += 0.10
        p["valor_desconto"] = round(p["valor_bruto"] * perc, 2)
        p["valor_liquido"] = round(p["valor_bruto"] - p["valor_desconto"], 2)
        return p["valor_liquido"]


# F16: Gateway de Pagamento
try:
    from modulos.f16_gateway_pagamento import finalizar_checkout_digital

    status_modulos["F16"] = "OK"
except Exception as e:
    status_modulos["F16"] = f"FALLBACK ({e})"

    def finalizar_checkout_digital(bd, id_pedido, opcao_pagamento):
        p = bd["assinaturas_transacoes"].get(id_pedido)
        if not p or p["status"] != "ABERTO" or len(p["carrinho"]) == 0:
            return False
        match opcao_pagamento:
            case 1:
                p["metodo_pagamento"] = "PIX"
            case 2:
                p["metodo_pagamento"] = "CARTAO_VIRTUAL"
            case 3:
                p["metodo_pagamento"] = "CRIPTO_REAL"
            case _:
                return False
        p["status"] = "PAGO"
        bd["faturamento_total"] = round(bd["faturamento_total"] + p["valor_liquido"], 2)
        return True


# F17: Reembolso / Anti-Churn
try:
    from modulos.f17_reembolso_churn import solicitar_reembolso

    status_modulos["F17"] = "OK"
except Exception as e:
    status_modulos["F17"] = f"FALLBACK ({e})"

    def solicitar_reembolso(bd, id_pedido):
        p = bd["assinaturas_transacoes"].get(id_pedido)
        if not p or p["status"] == "REEMBOLSADO":
            return False
        if p["status"] == "PAGO":
            bd["faturamento_total"] = round(
                max(0.0, bd["faturamento_total"] - p["valor_liquido"]), 2
            )
        p["carrinho"].clear()
        p["status"] = "REEMBOLSADO"
        return True


# F18: Analytics com Pandas e Exportação CSV
try:
    from modulos.f18_analytics_pandas import gerar_relatorio_pandas_csv

    status_modulos["F18"] = "OK"
except Exception as e:
    status_modulos["F18"] = f"FALLBACK ({e})"

    def gerar_relatorio_pandas_csv(bd, nome_arquivo="telemetria_vendas_pipoca.csv"):
        try:
            if not bd["assinaturas_transacoes"]:
                print("⚠️ Nenhuma transação registrada para gerar relatório.")
                return False
            df = pd.DataFrame.from_dict(bd["assinaturas_transacoes"], orient="index")
            print("\nTELEMETRIA DE VENDAS (PANDAS DATAFRAME):")
            print(df.to_string())
            print(f"\n💰 FATURAMENTO TOTAL ACUMULADO: R$ {bd['faturamento_total']:.2f}")
            df.to_csv(nome_arquivo, index_label="id_pedido")
            print(f"Arquivo '{nome_arquivo}' exportado com sucesso!")
            return True
        except Exception as erro:
            print(f"Erro ao processar Pandas/CSV: {erro}")
            return False


# =====================================================================
# 3. LOOP PRINCIPAL DE EXECUÇÃO DO SISTEMA
# =====================================================================


def iniciar_plataforma():

    while True:
        email, nickname = autenticar_usuario()
        resp_anual = (
            input("Possui fidelidade de Assinante Anual Pipoca.AI? (S/N): ")
            .strip()
            .upper()
            == "S"
        )
        id_pedido_atual = abrir_carrinho_digital(
            banco_dados, email, nickname, resp_anual
        )
        print(f"Sessão iniciada! Pedido #{id_pedido_atual} vinculado a @{nickname}.")

        sessao_ativa = True
        while sessao_ativa:
            opcao = exibir_menu_chatbot(nickname)

            match opcao:
                case 1:
                    listar_planos_streaming(banco_dados)
                    try:
                        id_p = int(input("Digite o ID do Plano: "))
                        meses = int(
                            input(
                                "Quantos meses deseja contratar? (12+ ganha 15% off): "
                            )
                        )
                        if contratar_plano_streaming(
                            banco_dados, id_pedido_atual, id_p, meses
                        ):
                            print("Plano adicionado ao seu carrinho digital!")
                        else:
                            print(
                                "Não foi possível contratar o plano. Verifique o ID ou meses."
                            )
                    except ValueError:
                        print("Digite apenas números inteiros!")

                case 2:
                    listar_eventos_live(banco_dados)
                    try:
                        id_ev = int(input("Digite o ID do Evento Live: "))
                        qtd = int(input("Quantidade de acessos simultâneos: "))
                        if reservar_acesso_live(
                            banco_dados, id_pedido_atual, id_ev, qtd
                        ):
                            print("Acesso(s) reservado(s) no servidor Live!")
                        else:
                            print(
                                "Falha na reserva (verifique ID ou slots disponíveis)."
                            )
                    except ValueError:
                        print("Digite apenas números inteiros!")

                case 3:
                    listar_loja_digital(banco_dados)
                    try:
                        id_it = int(input("Digite o ID do Item Digital: "))
                        qtd = int(input("Quantidade desejada: "))
                        if comprar_item_digital(
                            banco_dados, id_pedido_atual, id_it, qtd
                        ):
                            print("Ativo digital adicionado ao carrinho!")
                        else:
                            print("Estoque de licenças insuficiente ou ID inválido.")
                    except ValueError:
                        print("Digite apenas números inteiros!")

                case 4:
                    exibir_resumo_pedido(banco_dados, id_pedido_atual)

                case 5:
                    if remover_ultimo_item_carrinho(banco_dados, id_pedido_atual):
                        print("Último item removido do carrinho com sucesso!")
                    else:
                        print(
                            "Não foi possível remover (carrinho vazio ou pedido já fechado)."
                        )

                case 6:
                    exibir_resumo_pedido(banco_dados, id_pedido_atual)
                    cupom = input(
                        "Possui cupom de Influencer? Digite o código (ou Enter p/ pular): "
                    ).strip()
                    cupom_ok = (
                        validar_cupom_influencer(banco_dados, cupom) if cupom else False
                    )
                    if cupom and cupom_ok:
                        print("Cupom de Influencer validado com sucesso!")
                    elif cupom:
                        print("Cupom inválido ou expirado.")

                    novo_liquido = aplicar_descontos_digitais(
                        banco_dados, id_pedido_atual, cupom_ok
                    )
                    print(f"Valor final a pagar: R$ {novo_liquido:.2f}")

                    try:
                        forma = int(
                            input(
                                "Forma de Pagamento [1-PIX | 2-CARTAO_VIRTUAL | 3-CRIPTO_REAL]: "
                            )
                        )
                        if finalizar_checkout_digital(
                            banco_dados, id_pedido_atual, forma
                        ):
                            print(
                                "Pagamento APROVADO! Aproveite sua maratona no Pipoca.AI!"
                            )
                        else:
                            print(
                                "Pagamento recusado. Verifique se o carrinho possui itens ou opção válida."
                            )
                    except ValueError:
                        print("Opção de pagamento inválida!")

                case 7:
                    if solicitar_reembolso(banco_dados, id_pedido_atual):
                        print("Pedido reembolsado/cancelado com sucesso.")
                    else:
                        print("Não foi possível reembolsar este pedido.")

                case 8:
                    print("\n--- PAINEL DE INFRAESTRUTURA & LICENÇAS ---")
                    alertas = verificar_esgotamento_licencas(banco_dados)
                    print(
                        f"Licenças em nível crítico: {alertas if alertas else 'Nenhum item crítico'}"
                    )
                    try:
                        ev_lib = int(
                            input(
                                "ID do Evento Live para liberar slots (ou 0 p/ voltar): "
                            )
                        )
                        if ev_lib != 0:
                            qtd_lib = int(
                                input("Quantidade de slots desconectados a liberar: ")
                            )
                            novo_total = liberar_slots_servidor(
                                banco_dados, ev_lib, qtd_lib
                            )
                            print(
                                f"Servidor atualizado! Total de slots livres: {novo_total}"
                            )
                    except ValueError:
                        print("Entrada inválida.")

                case 9:
                    gerar_relatorio_pandas_csv(banco_dados)

                case 0:
                    sessao_ativa = False
                    encerrar = (
                        input(
                            "\nDeseja encerrar o servidor Pipoca.AI completamente? (S/N): "
                        )
                        .strip()
                        .upper()
                    )
                    if encerrar == "S":
                        print("Servidor Pipoca.AI finalizado. Até a próxima!")
                        return


if __name__ == "__main__":
    iniciar_plataforma()