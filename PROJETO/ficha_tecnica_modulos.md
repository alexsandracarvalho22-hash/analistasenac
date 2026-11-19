# Fichas Técnicas de Desenvolvimento — Pipoca.AI (UC1)

Consulte abaixo o card correspondente à função atribuída a você. Siga rigorosamente os nomes de arquivos, parâmetros, chaves de dicionário e tipos de retorno!

---

## F01 — Autenticação de Usuário (Função Curta)
* **Arquivo:** `modulos/f01_login_usuario.py`
* **Assinatura:** `def autenticar_usuario():`
* **Parâmetros:** Nenhum.
* **Retorno Esperado:** `tuple` contendo `(email, nickname)` — ambos `str`.
* **Passo a Passo da Lógica:**
  1. Exiba um cabeçalho criativo de boas-vindas ao **Pipoca.AI**.
  2. Inicie um laço `while True:` para solicitar o `email` e o `nickname` via `input()`.
  3. Remova espaços extras com `.strip()`.
  4. Verifique com `if` se o `email` contém `"@"` e `"."` e se o `nickname` não é uma string vazia (`len(nickname) > 0`).
  5. Se estiver tudo certo, retorne `(email, nickname)`. Caso contrário, exiba uma mensagem de erro amigável e repita o laço.

---

## F02 — Menu Interativo do Chatbot (Função Curta)
* **Arquivo:** `modulos/f02_menu_chatbot.py`
* **Assinatura:** `def exibir_menu_chatbot(nickname):`
* **Parâmetros:** `nickname` (`str`).
* **Retorno Esperado:** `int` (opção de `0` a `9`, ou `-1` em caso de erro).
* **Passo a Passo da Lógica:**
  1. Exiba uma saudação personalizada usando o `@nickname` recebido.
  2. Imprima as opções numeradas de `[1]` a `[9]` e `[0]` (conforme o painel do sistema).
  3. Utilize um bloco `try / except ValueError:` para ler a escolha do usuário com `int(input(...))`.
  4. Se o número estiver entre `0` e `9`, retorne o número inteiro. Se estiver fora do intervalo ou cair no `except`, exiba uma mensagem de aviso e retorne `-1`.

---

## F03 — Abertura de Carrinho Digital (Função Curta)
* **Arquivo:** `modulos/f03_abrir_pedido.py`
* **Assinatura:** `def abrir_carrinho_digital(banco_dados, email_usuario, nickname, assinante_anual):`
* **Parâmetros:** `banco_dados` (`dict`), `email_usuario` (`str`), `nickname` (`str`), `assinante_anual` (`bool`).
* **Retorno Esperado:** `int` (`id_pedido` gerado).
* **Passo a Passo da Lógica:**
  1. Calcule o `id_pedido` somando `len(banco_dados["assinaturas_transacoes"]) + 2026001`.
  2. Crie uma nova chave `banco_dados["assinaturas_transacoes"][id_pedido]` contendo o dicionário padrão da transação:
     * `"email_usuario": email_usuario`
     * `"nickname": nickname`
     * `"assinante_anual": assinante_anual`
     * `"carrinho": []`
     * `"valor_bruto": 0.0`, `"valor_desconto": 0.0`, `"valor_liquido": 0.0`
     * `"metodo_pagamento": "PENDENTE"`, `"status": "ABERTO"`
  3. Retorne o `id_pedido`.

---

## F04 — Validador de Cupom de Influencer (Função Curta)
* **Arquivo:** `modulos/f04_validar_influencer.py`
* **Assinatura:** `def validar_cupom_influencer(banco_dados, codigo_cupom):`
* **Parâmetros:** `banco_dados` (`dict`), `codigo_cupom` (`str`).
* **Retorno Esperado:** `bool` (`True` ou `False`).
* **Passo a Passo da Lógica:**
  1. Padronize a string recebida usando `codigo_cupom.strip().upper()`.
  2. Verifique se o código padronizado está contido na tupla `banco_dados["cupons_ativos"]`.
  3. Retorne `True` se existir na tupla ou `False` caso contrário.

---

## F05 — Catálogo de Planos de Streaming (Função Completa)
* **Arquivo:** `modulos/f05_catalogo_planos.py`
* **Assinatura:** `def listar_planos_streaming(banco_dados):`
* **Parâmetros:** `banco_dados` (`dict`).
* **Retorno Esperado:** `None`.
* **Passo a Passo da Lógica:**
  1. Imprima um título formatado para a seção de Planos SaaS.
  2. Percorra `banco_dados["planos_streaming"].items()` utilizando um laço `for id_plano, info in ...:`.
  3. Exiba na tela o ID do plano, o `"nome"`, a `"mensalidade"` formatada com duas casas decimais (`R$ XX.XX`) e a quantidade de `"telas_simultaneas"`.
  4. Informe no rodapé que contratações de 12 meses ou mais recebem 15% de desconto direto no plano.

---

## F06 — Contratação de Plano de Streaming (Função Completa)
* **Arquivo:** `modulos/f06_assinar_plano.py`
* **Assinatura:** `def contratar_plano_streaming(banco_dados, id_pedido, id_plano, meses_fidelidade):`
* **Parâmetros:** `banco_dados` (`dict`), `id_pedido` (`int`), `id_plano` (`int`), `meses_fidelidade` (`int`).
* **Retorno Esperado:** `bool`.
* **Passo a Passo da Lógica:**
  1. Verifique se `id_plano` existe em `banco_dados["planos_streaming"]` e se `meses_fidelidade >= 1`. Se não, retorne `False`.
  2. Calcule o `subtotal = mensalidade * meses_fidelidade`.
  3. Se `meses_fidelidade >= 12`, aplique 15% de desconto multiplicando o `subtotal` por `0.85`. Arredonde com `round(subtotal, 2)`.
  4. Adicione ao array `carrinho` do pedido um dicionário com `"categoria": "STREAMING"`, `"descricao": nome_do_plano`, `"qtd": meses_fidelidade` e `"subtotal": subtotal`.
  5. Some o `subtotal` ao `"valor_bruto"` do pedido, atualize o `"valor_liquido"` e retorne `True`.

---

## F07 — Catálogo de Eventos Live PPV (Função Curta)
* **Arquivo:** `modulos/f07_catalogo_lives.py`
* **Assinatura:** `def listar_eventos_live(banco_dados):`
* **Parâmetros:** `banco_dados` (`dict`).
* **Retorno Esperado:** `None`.
* **Passo a Passo da Lógica:**
  1. Percorra `banco_dados["eventos_live"].items()` com um laço `for`.
  2. Imprima o ID do evento, o nome em `"evento"`, o `"preco"` e o número de `"slots_servidor"` disponíveis (se for `0`, exiba `"SERVIDOR LOTADO"`).

---

## F08 — Reserva de Acesso Live Pay-Per-View (Função Completa)
* **Arquivo:** `modulos/f08_comprar_ppv.py`
* **Assinatura:** `def reservar_acesso_live(banco_dados, id_pedido, id_evento, qtd_acessos):`
* **Parâmetros:** `banco_dados` (`dict`), `id_pedido` (`int`), `id_evento` (`int`), `qtd_acessos` (`int`).
* **Retorno Esperado:** `bool`.
* **Passo a Passo da Lógica:**
  1. Verifique se `id_evento` existe em `banco_dados["eventos_live"]` e se `qtd_acessos > 0`.
  2. Verifique se `slots_servidor >= qtd_acessos`. Caso não haja vagas suficientes no servidor, exiba um alerta e retorne `False`.
  3. Subtraia `qtd_acessos` de `slots_servidor`.
  4. Calcule `subtotal = round(preco * qtd_acessos, 2)`.
  5. Insira o item na lista `carrinho` do pedido com `"categoria": "LIVE_PPV"`, atualize `"valor_bruto"` e `"valor_liquido"`, e retorne `True`.

---

## F09 — Liberação de Slots de Servidor Cloud (Função Curta)
* **Arquivo:** `modulos/f09_liberar_servidor.py`
* **Assinatura:** `def liberar_slots_servidor(banco_dados, id_evento, qtd_liberada):`
* **Parâmetros:** `banco_dados` (`dict`), `id_evento` (`int`), `qtd_liberada` (`int`).
* **Retorno Esperado:** `int` (total atualizado de slots ou `-1` se erro).
* **Passo a Passo da Lógica:**
  1. Valide se `id_evento` está em `banco_dados["eventos_live"]` e se `qtd_liberada > 0`. Se for inválido, retorne `-1`.
  2. Some `qtd_liberada` ao campo `"slots_servidor"` do evento.
  3. Retorne o novo valor inteiro de `"slots_servidor"`.

---

## F10 — Catálogo da Loja Digital (Função Curta)
* **Arquivo:** `modulos/f10_catalogo_loja.py`
* **Assinatura:** `def listar_loja_digital(banco_dados):`
* **Parâmetros:** `banco_dados` (`dict`).
* **Retorno Esperado:** `None`.
* **Passo a Passo da Lógica:**
  1. Percorra `banco_dados["loja_digital"].items()` com um laço `for`.
  2. Imprima o ID, o nome do `"item"`, o `"preco"` formatado e a quantidade em `"licencas_estoque"`.

---

## F11 — Compra de Ativo na Loja Digital (Função Completa)
* **Arquivo:** `modulos/f11_comprar_item_digital.py`
* **Assinatura:** `def comprar_item_digital(banco_dados, id_pedido, id_item, qtd):`
* **Parâmetros:** `banco_dados` (`dict`), `id_pedido` (`int`), `id_item` (`int`), `qtd` (`int`).
* **Retorno Esperado:** `bool`.
* **Passo a Passo da Lógica:**
  1. Verifique se `id_item` existe em `banco_dados["loja_digital"]` e se `qtd > 0`.
  2. Valide se `licencas_estoque >= qtd`. Se não houver chaves digitais suficientes, retorne `False`.
  3. Desconte `qtd` de `"licencas_estoque"`.
  4. Calcule `subtotal = round(preco * qtd, 2)` e adicione ao `carrinho` do pedido com `"categoria": "LOJA_DIGITAL"`.
  5. Atualize `"valor_bruto"` e `"valor_liquido"` do pedido e retorne `True`.

---

## F12 — Auditoria Automática de Licenças (Função Curta)
* **Arquivo:** `modulos/f12_auditoria_licencas.py`
* **Assinatura:** `def verificar_esgotamento_licencas(banco_dados):`
* **Parâmetros:** `banco_dados` (`dict`).
* **Retorno Esperado:** `list` (lista de strings com os nomes dos itens em alerta).
* **Passo a Passo da Lógica:**
  1. Crie uma lista vazia `itens_criticos = []`.
  2. Percorra os itens de `banco_dados["loja_digital"]`.
  3. Sempre que `licencas_estoque <= alerta_minimo`, adicione o nome do `"item"` na lista `itens_criticos`.
  4. Retorne a lista `itens_criticos`.

---

## F13 — Extrato Detalhado do Carrinho Digital (Função Curta)
* **Arquivo:** `modulos/f13_resumo_carrinho.py`
* **Assinatura:** `def exibir_resumo_pedido(banco_dados, id_pedido):`
* **Parâmetros:** `banco_dados` (`dict`), `id_pedido` (`int`).
* **Retorno Esperado:** `None`.
* **Passo a Passo da Lógica:**
  1. Verifique se `id_pedido` existe em `banco_dados["assinaturas_transacoes"]`.
  2. Exiba os dados de cabeçalho: ID do pedido, `@nickname`, `email_usuario`, se é `assinante_anual`, `status` e `metodo_pagamento`.
  3. Percorra a lista `carrinho` imprimindo cada item (categoria, descrição, quantidade e subtotal).
  4. No rodapé, mostre `valor_bruto`, `valor_desconto` e `valor_liquido`.

---

## F14 — Remoção do Último Item do Carrinho (Função Completa)
* **Arquivo:** `modulos/f14_remover_item.py`
* **Assinatura:** `def remover_ultimo_item_carrinho(banco_dados, id_pedido):`
* **Parâmetros:** `banco_dados` (`dict`), `id_pedido` (`int`).
* **Retorno Esperado:** `bool`.
* **Passo a Passo da Lógica:**
  1. Verifique se o pedido existe, se `status == "ABERTO"` e se a lista `carrinho` possui pelo menos 1 item (`len > 0`). Caso contrário, retorne `False`.
  2. Remova o último elemento da lista `carrinho` usando o método `.pop()` e guarde em uma variável `item_removido`.
  3. Subtraia `item_removido["subtotal"]` do `"valor_bruto"` do pedido (garantindo que não fique menor que `0.0`).
  4. Atualize o `"valor_liquido"` (`valor_bruto - valor_desconto`) e retorne `True`.

---

## F15 — Motor de Descontos (Fidelidade + Influencer) (Função Curta)
* **Arquivo:** `modulos/f15_calculo_cashback_desconto.py`
* **Assinatura:** `def aplicar_descontos_digitais(banco_dados, id_pedido, cupom_influencer_valido):`
* **Parâmetros:** `banco_dados` (`dict`), `id_pedido` (`int`), `cupom_influencer_valido` (`bool`).
* **Retorno Esperado:** `float` (`valor_liquido` atualizado).
* **Passo a Passo da Lógica:**
  1. Acesse o pedido em `banco_dados["assinaturas_transacoes"][id_pedido]`.
  2. Crie um acumulador `percentual = 0.0`.
  3. Se `pedido["assinante_anual"] == True`, some `0.10` (10%).
  4. Se `cupom_influencer_valido == True`, some mais `0.10` (10%).
  5. Calcule `valor_desconto = round(valor_bruto * percentual, 2)` e `valor_liquido = round(valor_bruto - valor_desconto, 2)`.
  6. Atualize ambas as chaves no pedido e retorne `valor_liquido`.

---

## F16 — Gateway de Pagamento Digital (Função Completa)
* **Arquivo:** `modulos/f16_gateway_pagamento.py`
* **Assinatura:** `def finalizar_checkout_digital(banco_dados, id_pedido, opcao_pagamento):`
* **Parâmetros:** `banco_dados` (`dict`), `id_pedido` (`int`), `opcao_pagamento` (`int`).
* **Retorno Esperado:** `bool`.
* **Passo a Passo da Lógica:**
  1. Verifique se o pedido existe, se `status == "ABERTO"` e se o `carrinho` não está vazio. Se falhar, retorne `False`.
  2. Utilize `match opcao_pagamento:` (ou `if/elif/else`) para definir `"metodo_pagamento"`:
     * `1` -> `"PIX"`
     * `2` -> `"CARTAO_VIRTUAL"`
     * `3` -> `"CRIPTO_REAL"`
     * Outro valor -> retorne `False`.
  3. Altere o `"status"` do pedido para `"PAGO"`.
  4. Some o `"valor_liquido"` do pedido em `banco_dados["faturamento_total"]` e retorne `True`.

---

## F17 — Gestão de Reembolso / Anti-Churn (Função Curta)
* **Arquivo:** `modulos/f17_reembolso_churn.py`
* **Assinatura:** `def solicitar_reembolso(banco_dados, id_pedido):`
* **Parâmetros:** `banco_dados` (`dict`), `id_pedido` (`int`).
* **Retorno Esperado:** `bool`.
* **Passo a Passo da Lógica:**
  1. Verifique se o pedido existe e se o `status` atual é diferente de `"REEMBOLSADO"`. Caso contrário, retorne `False`.
  2. Se o `status` era `"PAGO"`, deduza o `"valor_liquido"` de `banco_dados["faturamento_total"]`.
  3. Limpe a lista `carrinho` (`.clear()`), mude o `"status"` para `"REEMBOLSADO"` e retorne `True`.

---

## F18 — Pipeline Analytics com Pandas e Exportação CSV (Função Completa)
* **Arquivo:** `modulos/f18_analytics_pandas.py`
* **Assinatura:** `def gerar_relatorio_pandas_csv(banco_dados, nome_arquivo="telemetria_vendas_pipoca.csv"):`
* **Parâmetros:** `banco_dados` (`dict`), `nome_arquivo` (`str`).
* **Retorno Esperado:** `bool`.
* **Passo a Passo da Lógica:**
  1. Importe a biblioteca `import pandas as pd`.
  2. Verifique se `banco_dados["assinaturas_transacoes"]` possui dados. Se estiver vazio, avise na tela e retorne `False`.
  3. Envolva o processamento em um bloco `try / except Exception as erro:`.
  4. Crie o DataFrame: `df = pd.DataFrame.from_dict(banco_dados["assinaturas_transacoes"], orient="index")`.
  5. Imprima o DataFrame completo no terminal com `print(df.to_string())` e mostre também o `banco_dados["faturamento_total"]`.
  6. Exporte o DataFrame para CSV usando `df.to_csv(nome_arquivo, index_label="id_pedido")` e retorne `True` (ou `False` se cair no `except`).