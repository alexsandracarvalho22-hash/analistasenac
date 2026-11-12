# login = "admin"
# senha = "admin123"

# dado1 = input("qual seu login?:")
# dado2 = input ("qual sua senha?:")

# print ("login correto")
# print ("qual sua senha? {senha}")

print("--- SIMULAÇÃO DE LOGIN ---")

# Credenciais cadastradas no sistema
usuario_correto = "ale"
senha_correta = "ale123"

contador = 0
limite_tentativas = 3

while contador < limite_tentativas:
    print(f"\ntentativa {contador + 1} de {limite_tentativas}")
    
    # Capturando a entrada do usuário dentro do loop
    usuario_digitado = input("digite o usuário: ")
    senha_digitada = input("digite a senha: ")

    # Verificando se os dados conferem
    if usuario_digitado == usuario_correto and senha_digitada == senha_correta:
        print("\nlogin bem-sucedido! bem-vinda a simulacão, ale!")
        break  # Sai do loop imediatamente se acertar
    else:
        print("usuário ou senha incorretos. tente novamente.")
        contador += 1  # Incrementa o contador apenas se errar

# Se o contador atingir o limite e o loop acabar sem um 'break' bem-sucedido
if contador == limite_tentativas:
    print("\n[AVISO] número máximo de tentativas atingido. acesso bloqueado!")