txt = "arquivo.txt"

while True:
    print("\nMenu:")
    print("1 - Criar arquivo")
    print("2 - Escrever no arquivo")
    print("3 - Mostrar conteúdo do arquivo")
    print("0 - Sair")

    try:
        opcao = int(input("Digite sua escolha: "))  # Converte para inteiro
    except ValueError:
        print("Erro: Digite um número válido!")
        continue  # Volta ao início do loop

    if opcao == 1:
        txt = input( "Digite o nome do arquivo que deseja criar: ")
        with open(txt, 'a') as arquivo:
            arquivo.write('')
            continue


    elif opcao == 2:
        print("Escrever no Arquivo.")
        with open(txt, 'a') as arquivo:
            linha= input("Novo conteúdo: ")
            arquivo.write('\n'+linha)
            continue

    elif opcao == 3:
        print("\nMostrando dados do arquivo:")
        with open(txt, 'r') as arquivo:
            dados = arquivo.read()
        
        # Tratamento do texto:
        # 1. Converte tudo para minúsculas
        # 2. Capitaliza a primeira letra de cada frase (separada por ponto)
        dados_formatados = ". ".join(
            frase.strip().capitalize() 
            for frase in dados.lower().split(".")
        ).strip()
        
        print("-" * 40)  # Linha separadora
        print(dados_formatados)
        print("-" * 40)  # Linha separadora
        continue
    
    elif opcao == 0:
        print("Até mais!")
        break

    else:
        print("Opção inválida!")
