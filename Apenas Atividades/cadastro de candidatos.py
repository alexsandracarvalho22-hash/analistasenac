


for i in range(1, 13):
    print(f"\n--- candidato {i} ---")
    
    
    ano_nascimento = int(input("digite o seu ano de nascimento: "))
    

    idade = 2026 - ano_nascimento
    
    
    if idade < 18:
        print("você não pode participar por ser menor de 18 anos.")
        
    
        
   
    print("cadastro permitido! Vamos continuar...")
    telefone = input("digite seu telefone: ")
    email = input("digite seu e-mail: ")
    
    print(f"candidato {i} cadastrado com sucesso!")