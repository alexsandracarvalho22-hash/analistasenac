"""
Sorteador de Módulos - Projeto Final UC1: Pipoca.AI
Associa o nome do aluno a uma das 18 funções disponíveis (1 a 18),
salvando o histórico local para não repetir números já sorteados em execuções diferentes.
"""

import random
import json
import os

ARQUIVO_MEMORIA = "historico_sorteio_pipoca.json"

CATALOGO_FUNCOES = {
    1: "F01 - Login de Usuário (modulos/f01_login_usuario.py)",
    2: "F02 - Menu do Chatbot (modulos/f02_menu_chatbot.py)",
    3: "F03 - Abrir Pedido (modulos/f03_abrir_pedido.py)",
    4: "F04 - Validar Influencer (modulos/f04_validar_influencer.py)",
    5: "F05 - Catálogo de Planos (modulos/f05_catalogo_planos.py)",
    6: "F06 - Assinar Plano (modulos/f06_assinar_plano.py)",
    7: "F07 - Catálogo de Lives (modulos/f07_catalogo_lives.py)",
    8: "F08 - Comprar PPV (modulos/f08_comprar_ppv.py)",
    9: "F09 - Liberar Servidor (modulos/f09_liberar_servidor.py)",
    10: "F10 - Catálogo da Loja (modulos/f10_catalogo_loja.py)",
    11: "F11 - Comprar Item Digital (modulos/f11_comprar_item_digital.py)",
    12: "F12 - Auditoria de Licenças (modulos/f12_auditoria_licencas.py)",
    13: "F13 - Resumo do Carrinho (modulos/f13_resumo_carrinho.py)",
    14: "F14 - Remover Último Item (modulos/f14_remover_item.py)",
    15: "F15 - Motor de Descontos (modulos/f15_calculo_cashback_desconto.py)",
    16: "F16 - Gateway de Pagamento (modulos/f16_gateway_pagamento.py)",
    17: "F17 - Reembolso / Anti-Churn (modulos/f17_reembolso_churn.py)",
    18: "F18 - Analytics Pandas (modulos/f18_analytics_pandas.py)"
}


def carregar_sorteios():
    if os.path.exists(ARQUIVO_MEMORIA):
        try:
            with open(ARQUIVO_MEMORIA, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


def salvar_sorteios(dados):
    with open(ARQUIVO_MEMORIA, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)


def realizar_sorteio():
    sorteados = carregar_sorteios()
    numeros_ocupados = [int(k) for k in sorteados.keys()]
    numeros_disponiveis = [n for n in range(1, 19) if n not in numeros_ocupados]

    print("=" * 65)
    print("SORTEADOR DE MÓDULOS - PROJETO PIPOCA.AI 🍿")
    print("=" * 65)
    print(f"Status: {len(numeros_ocupados)}/18 funções sorteadas | {len(numeros_disponiveis)} disponíveis.")
    print("Comandos especiais: digite 'LISTA' para ver o quadro ou 'RESET' para zerar.")
    print("-" * 65)

    entrada = input("Digite o nome do(a) aluno(a): ").strip()

    if not entrada:
        print("Nenhum nome foi inserido. Execute novamente.")
        return

    if entrada.upper() == "RESET":
        if os.path.exists(ARQUIVO_MEMORIA):
            os.remove(ARQUIVO_MEMORIA)
        print("Histórico de sorteio zerado com sucesso! Todas as 18 funções estão livres.")
        return

    if entrada.upper() == "LISTA":
        if not sorteados:
            print("Nenhuma função foi sorteada até o momento.")
        else:
            print("\nRELAÇÃO DE ALUNOS E FUNÇÕES SORTEADAS:")
            for num_str in sorted(sorteados.keys(), key=lambda x: int(x)):
                num = int(num_str)
                print(f"  Nº {num:02d} | {sorteados[num_str]} ➔ {CATALOGO_FUNCOES[num]}")
        return

    if not numeros_disponiveis:
        print("Todas as 18 funções já foram sorteadas!")
        return

    # Sorteia aleatoriamente entre os números ainda disponíveis (de 1 a 18)
    numero_sorteado = random.choice(numeros_disponiveis)
    sorteados[str(numero_sorteado)] = entrada
    salvar_sorteios(sorteados)

    print("\n" + "" * 22)
    print(f"ALUNO(A): {entrada}")
    print(f"NÚMERO SORTEADO: {numero_sorteado:02d}")
    print(f"MÓDULO DESIGNADO: {CATALOGO_FUNCOES[numero_sorteado]}")
    print("" * 22 + "\n")


if __name__ == "__main__":
    realizar_sorteio()
