def criar_arquivo():
    nome_arquivo = input("Informe o nome do arquivo: [arquivo.txt] ") or "arquivo.txt"
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write('')
    print(f"Arquivo '{nome_arquivo}' criado com sucesso!")
    return nome_arquivo

def acrescentar_linhas(nome_arquivo):
    print("Digite as linhas a serem acrescentadas (0 para sair):")
    with open(nome_arquivo, 'a') as arquivo:
        while True:
            linha = input("> ")
            if linha == '0':
                break
            # Formatar a linha: primeira letra maiúscula, resto minúsculo
            linha_formatada = linha.capitalize()
            arquivo.write(linha_formatada + '\n')

def mostrar_conteudo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            if conteudo:
                print(conteudo)
            else:
                print("O arquivo está vazio.")
    except FileNotFoundError:
        print("Arquivo não encontrado. Crie um arquivo primeiro.")

def main():
    nome_arquivo = "arquivo.txt"  # nome padrão
    while True:
        print("\nMenu:")
        print("1. Criar um arquivo")
        print("2. Acrescentar linhas ao arquivo")
        print("3. Mostrar o conteudo do arquivo")
        print("0. Sair")
        
        opcao = input("Opcao: ")
        
        if opcao == '1':
            nome_arquivo = criar_arquivo()
        elif opcao == '2':
            acrescentar_linhas(nome_arquivo)
        elif opcao == '3':
            mostrar_conteudo(nome_arquivo)
        elif opcao == '0':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
