curriculos = []

while True:
    print("\nMENU".center(15))
    print("1 - Cadastrar currículo")
    print("2 - Listar todos os currículos")
    print("3 - Buscar currículo por nome")  
    print("4 - Atualizar currículo")
    print("5 - Excluir currículo")
    print("6 - Sair")

    opcao = int(input("Digite a opção desejada:"))

    if opcao == 1:
        print("\nCadastrar currículo")
        while True:
            Nome = input("Digite seu nome completo:").strip().upper()
            if Nome:
                Nome = Nome.title()  
                break
            else:
                print("O nome não pode ser vazio. Tente novamente.")
        
        entrada_idade =input("Digite sua idade: ")
        if entrada_idade.isdigit():
            Idade = int(entrada_idade)
        else:
            print("Idade inválida. Currículo não será cadastrado.")
            continue
            
        Formação_academica = input("Digite sua formação acadêmica:").upper().strip()
    
        Experiencia_profissional = []
        num_exp = int(input("Digite quantas expêriencias deseja cadastrar(cargo e empresa):"))
        for i in range(num_exp):
            cargo = input("Digite seu cargo:").upper().strip()
            empresa = input("Digite sua empresa:").upper().strip()
            experiencia = f" Cargo: {cargo}, Empresa: {empresa}"
            Experiencia_profissional.append(experiencia)
        print("Experiências cadastradas:")
        print(Experiencia_profissional)
    
        Habilidades = []
        num_hab = int(input("Digite quantas habilidades deseja cadastrar:"))
        for i in range(num_hab):
            habilidade = input("Digite sua habilidade:").upper().strip()
            Habilidades.append(habilidade)
        print("Habilidades cadastradas:")
        print(Habilidades)
    
        curriculo = [Nome, Idade, Formação_academica, Experiencia_profissional, Habilidades]
        if curriculo not in curriculos:
            curriculos.append(curriculo)
            print("Seu currículo foi cadastrado com sucesso!")
    
    elif opcao == 2:
        print("\nListar todos os currículos")
        if not curriculos:
            print("Nenhum currículo cadastrado!")
        else:
            for i, curriculo in enumerate(curriculos):
                print(f"\nCurrículo {i+1}:")
                print(f"  Nome: {curriculo[0]}")
                print(f"  Idade: {curriculo[1]}")
                print(f"  Formação Acadêmica: {curriculo[2]}")
                print("  Experiência Profissional:")
                for Experiencia_profissional in curriculo[3]:
                    print(f"    - {Experiencia_profissional}")
                print("  Habilidades:")
                for Habilidades in curriculo[4]:
                    print(f"    - {Habilidades}")
    
    elif opcao == 3:
        print("\nBuscar currículo por nome")
        nome_procurar = input("Digite o nome da pessoa que deseja visualizar o currículo:").upper().title()
        for curriculo in curriculos:
            if curriculo[0] == nome_procurar:
                print("\nCurrículo encontrado!")
                print(f"  Nome: {curriculo[0]}")
                print(f"  Idade: {curriculo[1]}")
                print(f"  Formação Acadêmica: {curriculo[2]}")
                print("  Experiência Profissional:")
                for experiencia in curriculo[3]:
                    print(f"    - {experiencia}")
                print("  Habilidades:")
                for habilidade in curriculo[4]:
                    print(f"    - {habilidade}")
                break
            else:
                print("Nome não encontrado.Tente Novamente.")
    
    elif opcao == 4:
        print("\nAtualizar currículo")
        nome_atualizar = input("Digite o nome da pessoa que deseja atualizar o currículo:").upper().title()
        for curriculo in curriculos:
            if curriculo[0] == nome_atualizar:
                print("Currículo encontrado!")
                print(f"  Nome: {curriculo[0]}")
                print(f"  Idade: {curriculo[1]}")
                print(f"  Formação Acadêmica: {curriculo[2]}")
                print("  Experiência Profissional:")
                for experiencia in curriculo[3]:
                    print(f"    - {experiencia}")
                print("  Habilidades:")
                for habilidade in curriculo[4]:
                    print(f"    - {habilidade}")
                
                nova_idade = input("Digite a nova idade(ou pressione Enter para manter): ")
                if nova_idade.strip():
                    curriculo[1] = nova_idade
                
                nova_formacao= input("Digite a nova formação acadêmica(ou presione Enter para manter): ").upper()
                if nova_formacao.strip():
                    curriculo[2] = nova_formacao

                if input("Deseja atualizar as experiências? (s/n): ").lower() == "s":
                    curriculo[3].clear()
                    num_exp = int(input("Digite quantas expêriencias deseja cadastrar(cargo e empresa): "))
                    for i in range(num_exp):
                        cargo = input("Digite seu cargo:").upper().strip()
                        empresa = input("Digite sua empresa:").upper().strip()
                        experiencia = f" Cargo: {cargo}, Empresa: {empresa}"
                        curriculo[3].append(experiencia)
                
                if input("Deseja atualizar as habilidades? (s/n): ").lower() == "s":
                    curriculo[4].clear()
                    num_hab = int(input("Digite quantas habilidades deseja cadastrar:"))
                    for i in range(num_hab):
                        habilidade = input("Digite sua habilidade:").upper().strip()
                        curriculo[4].append(habilidade)
                print("Currículo atualizado com sucesso!")
                break
                
            else:
                print("Nome não encontrado.Tente Novamente.")
    
    elif opcao == 5:
        print("\nExcluir currículo")
        for i, curriculo in enumerate(curriculos):
            print(f"{i + 1} - {curriculo[0]}")
        indice = int(input("Digite o NÚMERO do currículo que deseja excluir: ")) - 1
        if 0 <= indice < len(curriculos):
            nome_removido = curriculos[indice][0]
            del curriculos[indice]
            print(f"Currículo de {nome_removido} foi removido com sucesso!")
        else:
            print("Índice inválido.")


        
    elif opcao == 6:
        print("\nSair")
        break

    else:
        print("\nEscolha uma opção de 1 a 6.")

        