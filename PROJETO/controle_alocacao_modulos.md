# Controle de Alocação e Entregas — Projeto Pipoca.AI (UC1)

**Curso:** Analista de Dados - Big Data Science (Código: 13455)  
**Unidade Curricular:** UC1 — Desenvolver algoritmos, versionamentos e linguagem de consulta estruturada  
**Instrutor:** Douglas Klem  
**Repositório Oficial:** `PipocaAI-Platform` (breve)

---

## Instruções de Controle
* **Porte Curto:** Funções mais enxutas (ideais para alunos que ficarão responsáveis por **2 módulos**).
* **Porte Completo:** Funções com maior densidade de regras de negócio (ideais para alunos com **1 módulo**).
* **Padrão de Branch:** `feature-fXX-nomealuno` (ex: `feature-f01-maria`).

---

## Tabela Oficial de Distribuição (Módulos F01 a F18)

| ID | Arquivo (`modulos/`) | Função (`def`) | Porte | Aluno(a) Responsável | Usuário GitHub (`@`) | Branch Criada | Status PR / Merge |
| :-: | :--- | :--- | :-: | :--- | :--- | :--- | :-: |
| **F01** | `f01_login_usuario.py` | `autenticar_usuario()` | Curta | *A definir* | `@` | `feature-f01-` | Pendente |
| **F02** | `f02_menu_chatbot.py` | `exibir_menu_chatbot()` | Curta | *A definir* | `@` | `feature-f02-` | Pendente |
| **F03** | `f03_abrir_pedido.py` | `abrir_carrinho_digital()` | Curta | *A definir* | `@` | `feature-f03-` | Pendente |
| **F04** | `f04_validar_influencer.py` | `validar_cupom_influencer()` | Curta | *A definir* | `@` | `feature-f04-` | Pendente |
| **F05** | `f05_catalogo_planos.py` | `listar_planos_streaming()` | Completa | *A definir* | `@` | `feature-f05-` | Pendente |
| **F06** | `f06_assinar_plano.py` | `contratar_plano_streaming()` | Completa | *A definir* | `@` | `feature-f06-` | Pendente |
| **F07** | `f07_catalogo_lives.py` | `listar_eventos_live()` | Curta | *A definir* | `@` | `feature-f07-` | Pendente |
| **F08** | `f08_comprar_ppv.py` | `reservar_acesso_live()` | Completa | *A definir* | `@` | `feature-f08-` | Pendente |
| **F09** | `f09_liberar_servidor.py` | `liberar_slots_servidor()` | Curta | *A definir* | `@` | `feature-f09-` | Pendente |
| **F10** | `f10_catalogo_loja.py` | `listar_loja_digital()` | Curta | *A definir* | `@` | `feature-f10-` | Pendente |
| **F11** | `f11_comprar_item_digital.py` | `comprar_item_digital()` | Completa | *A definir* | `@` | `feature-f11-` | Pendente |
| **F12** | `f12_auditoria_licencas.py` | `verificar_esgotamento_licencas()` | Curta | *A definir* | `@` | `feature-f12-` | Pendente |
| **F13** | `f13_resumo_carrinho.py` | `exibir_resumo_pedido()` | Curta | *A definir* | `@` | `feature-f13-` | Pendente |
| **F14** | `f14_remover_item.py` | `remover_ultimo_item_carrinho()` | Completa | *A definir* | `@` | `feature-f14-` | Pendente |
| **F15** | `f15_calculo_cashback_desconto.py` | `aplicar_descontos_digitais()` | Curta | *A definir* | `@` | `feature-f15-` | Pendente |
| **F16** | `f16_gateway_pagamento.py` | `finalizar_checkout_digital()` | Completa | *A definir* | `@` | `feature-f16-` | Pendente |
| **F17** | `f17_reembolso_churn.py` | `solicitar_reembolso()` | Curta | *A definir* | `@` | `feature-f17-` | Pendente |
| **F18** | `f18_analytics_pandas.py` | `gerar_relatorio_pandas_csv()` | Completa | *A definir* | `@` | `feature-f18-` | Pendente |

---

## Combinações

1. **Par Onboarding & Menu:** `F01` (Login de Usuário) + `F02` (Menu do Chatbot)
2. **Par Sessão & Marketing:** `F03` (Abrir Pedido) + `F04` (Validar Cupom Influencer)
3. **Par Infraestrutura Live:** `F07` (Catálogo de Lives) + `F09` (Liberar Slots do Servidor)
4. **Par Loja Digital & Supply:** `F10` (Catálogo da Loja) + `F12` (Auditoria de Licenças)
5. **Par Carrinho & Benefícios:** `F13` (Resumo do Carrinho) + `F15` (Motor de Descontos)

---

## Checklist de Validação de Pull Request

Antes de aprovar o *Merge* da branch de cada módulo para a `main`, verificaremos:
- [ ] O aluno modificou **apenas** o(s) arquivo(s) `modulos/fXX_...py` sob sua responsabilidade?
- [ ] A assinatura `def nome_funcao(...):` e a quantidade de parâmetros permanecem idênticas ao Contrato de Dados?
- [ ] O tipo de retorno (`bool`, `int`, `float`, `tuple`, `list` ou `None`) respeita a especificação?
- [ ] Os testes locais do aluno estão isolados dentro do bloco `if __name__ == "__main__":`?